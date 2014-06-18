/**
 * Created by yli on 5/8/14.
 */
package qudt4dt;

import org.apache.thrift.TProcessor;
import org.apache.thrift.server.*;
import org.apache.thrift.transport.TServerSocket;
import org.apache.thrift.transport.TServerTransport;
import org.apache.thrift.protocol.TJSONProtocol;

import qudt4dt.thrift.Qudt4dt_base;

public class Server {

    public static ServerHandler handler;
    public static TProcessor processor;
    public static void main(String[] args){
      //  try{
            handler = new ServerHandler("http://localhost:3030/qudt4dt/query?");
            processor = new Qudt4dt_base.Processor<ServerHandler>(handler);
            //System.out.print(handler.query("http://qudt.org/vocab/unit#DegreeCelsius").qudt_u);
            simple(processor);
//            Runnable t1 = new Runnable(){
//                public void run(){
//                    simple(processor);
//                }
//            };
//            new Thread(t1).start();
       // } catch (org.apache.thrift.transport.TTransportException x) {
         //   x.printStackTrace();
       // }
    }

    public static void simple(TProcessor processor) {
        try {
            TServerTransport serverTransport = new TServerSocket(9090);
            
            TServer server = new TSimpleServer(new TServer.Args(serverTransport).processor(processor).protocolFactory(new TJSONProtocol.Factory()));


            // Use this for a multithreaded server
            //TServer server = new TThreadPoolServer(new TThreadPoolServer.Args(serverTransport).processor(processor));

            System.out.println("Starting the simple server...");
            server.serve();
        } catch (org.apache.thrift.transport.TTransportException e) {
            e.printStackTrace();
        }
    }
}
