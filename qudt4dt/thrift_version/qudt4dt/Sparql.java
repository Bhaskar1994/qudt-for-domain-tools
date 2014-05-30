package qudt4dt;
import com.hp.hpl.jena.query.QueryExecution;
import com.hp.hpl.jena.query.QueryExecutionFactory;
import com.hp.hpl.jena.query.ResultSet;
/**
 * Created by yli on 5/8/14.
 */

public class Sparql {
    private String ontology_server_address;

    public Sparql(String _ontology_server_address){
        this.ontology_server_address = _ontology_server_address;
    }



    public ResultSet query(String query){
//        String ontology =
//                "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n" +
//                        "                    SELECT\n" +
//                        "                    ?class\n" +
//                        "                    WHERE\n" +
//                        "                    { <http://qudt.org/schema/qudt#Unit> ^rdfs:subClassOf+ ?class\n" +
//                        "                    }\n";

        QueryExecution x = QueryExecutionFactory.sparqlService(ontology_server_address, query);
        ResultSet result = x.execSelect();
        return result;
        //ResultSetFormatter.out(System.out, result);

    }


}
