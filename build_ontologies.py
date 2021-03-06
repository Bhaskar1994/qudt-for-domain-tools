#!/usr/bin/env python
import re
import sys
import os
import shlex
import urllib
import shutil
import glob
import fusekiutils
import qudt4dt

### Import stuff that's in our repo (in various places)
### SO UGLY
import inspect
pathOfThisFile = inspect.getfile(inspect.currentframe())
dirOfThisFile = os.path.split(pathOfThisFile)[0]

sys.path.append(os.path.join(dirOfThisFile, 'modelica'))
import MSL2OWL

sys.path.append(os.path.join(dirOfThisFile, 'openMDAO'))
import export_qudt_symbol
import export_openMDAO_units

sys.path.append(os.path.join(dirOfThisFile, 'requests'))
import requests
### End imports (and ugliness)


p_ScriptPathRoot = os.path.dirname(__file__)
### Generate OpenMDAO Unit Ontology
print "Generating OpenMDAO Unit ontology"
openMDAOUnit_path = os.path.join(p_ScriptPathRoot,'openMDAO/unitLibdefault.ini')
openMDAOOntology_path = os.path.join(p_ScriptPathRoot,'openMDAO/openMDAO-individuals.xml')
export_openMDAO_units.xml_generator(openMDAOUnit_path,openMDAOOntology_path)

print 'complete'


### Generate Modelica Unit Ontology
p_SIUnits = os.path.join(p_ScriptPathRoot,'modelica/modelica_units.json')
p_ModelicaUnitOntology = os.path.join(p_ScriptPathRoot,'modelica/modelica-individuals.xml')

if not os.path.exists(p_SIUnits):
    print "Generating Modelica ast json file"
    os.system('cd modelica&&python export_modelica_units.py')
    print "done"
    
print "Generating Modelica Unit ontology"
MSL2OWL.GenerateOWLIndividualFile(p_SIUnits,p_ModelicaUnitOntology)
print "complete"

print ""

### start jena-fuseki and seed database ###
fuseki_data_path = os.getcwd() + '/fuseki-data'
if os.path.exists(fuseki_data_path):
    print "Cleaning fuseki database"
    shutil.rmtree(fuseki_data_path)
    print "done"
    print ""

### Create fresh database folder
os.makedirs(fuseki_data_path)

fuseki_url = "http://localhost:3030"
fuseki_upload_url = fuseki_url + '/qudt4dt/upload'

print "Launching fuseki..."
fuseki = fusekiutils.LaunchFuseki()
print "done"

print ""

def LoadDirectoryOfOWLFiles(path):
    # Load QUDT data
    ap_XMLFiles = glob.glob(path + '/*.xml')
    for filename in ap_XMLFiles:
        # Skip Protege's "catalog" files
        if filename.find('catalog-') != -1:
            continue

        print 'Loading', filename
        files = {'file': open(filename, 'rb')}
        r = requests.post(fuseki_upload_url, files=files)

        if r.status_code != 200:
            print "EXCEPTION loading DB: ", r.status_code

def CreateOWLFilesFromCSV(sourceFilePath, objFilePath):
    s_file = re.search('[^/]+?\.csv',sourceFilePath).group()
    o_file = re.search('[^/]+?\.xml',objFilePath).group()
    print 'coverting %s to %s' %(s_file, o_file)
    qudt4dt.unit_mapping.createMapping(sourceFilePath, objFilePath)
            
try:
    print "Creating ontologies from CSV file..."
    LoadDirectoryOfOWLFiles('qudt-owl')
    export_qudt_symbol.xml_generator('openMDAO/openMDAO-dynamic-individuals.xml','openMDAO/openMDAO-dynamic-mapping.csv')
    CreateOWLFilesFromCSV('modelica/mapping-to-qudt.csv','modelica/modelica-qudt.xml')
    CreateOWLFilesFromCSV('openMDAO/mapping-to-qudt.csv','openMDAO/openMDAO-qudt.xml')
    CreateOWLFilesFromCSV('openMDAO/openMDAO-dynamic-mapping.csv','openMDAO-dynamic-mapping.xml')
    print "Loading ontologies into Fuseki..."
    LoadDirectoryOfOWLFiles('modelica')
    LoadDirectoryOfOWLFiles('ontologies')
    LoadDirectoryOfOWLFiles('openMDAO')
    print "done"

finally:
    print ""
    print "Terminating fuseki..."
    if fuseki is not None:
        fuseki.terminate()
    else:
        print "WARNING: Fuseki service pointer was None; Fuseki may not have launched properly, and the loaded ontology may not be correct."
    print "done"
    print ""

print "finished"
