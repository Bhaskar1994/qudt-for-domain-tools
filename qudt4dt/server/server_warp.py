import sys 
sys.path.append("../..")
sys.path.append("./")
import socket
import qudt4dt
import struct


def create_message(url):
    url_base = 'http://localhost:3030'
    q = qudt4dt.unit.qudt.QudtUnit(url_base, url)
    mdao = qudt4dt.unit.mdao.MdaoUnit(url_base, url)
    mode = qudt4dt.unit.modelica.ModelicaUnit(url_base, url)
    instance = qudt4dt.qudt_pb2.Unit()
    tmp = qudt4dt.qudt_pb2.Unit()
    q.createInstance(tmp.qudt_unit)
    mode.createInstance(tmp.modelica_unit)
    mdao.createInstance(tmp.mdao_unit)
    return tmp

def daemon():
    
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind(('', 3031))  
    sock.listen(5)  
    while True:  
        connection,address = sock.accept()  
        try:  
            connection.settimeout(5)  
            buf_len = connection.recv(struct.calcsize('!i'))        
            buf_len = struct.unpack('!i', buf_len)[0]
            print buf_len
            count = 0
            buf = ''
            while count < buf_len:
                _buf = connection.recv(1024)
                count += len(_buf)
                buf += _buf
            print buf
            ins = create_message(buf)
            data = ins.SerializeToString()
            length = len(data)
            connection.send(struct.pack('!i', length) + data)
        except socket.timeout:  
            print 'time out'  
        connection.close()   

if __name__ == '__main__':  
    daemon()
    #create_message(u'http://qudt.org/vocab/unit#Meter')