package ctree.test;

import ctree.index.*;
import ctree.graph.*;

import ctree.util.*;

import ctree.lgraph.LGraphFile;

import java.io.*;
import java.util.Locale;

import java.lang.*;

/**
 *
 * @author Huahai He
 * @version 1.0
 */

public class subgraph_iso {
  public static void main(String[] args) throws Exception {
    if (args.length < 2) {
      System.err.println("Usage: ... graph_file query_file");
      System.exit(1);
    }
    
    Graph[] graphs = LGraphFile.loadLGraphs(args[0]);
    Graph[] queries = LGraphFile.loadLGraphs(args[1]);
    DataSum stat = new DataSum();
    PrintWriter writer = new PrintWriter(args[2], "UTF-8");
      
    for (int i = 0; i < Math.min(queries.length,100); i++) {
      if(i%10==0) {
        System.err.println(i);
      }
      int T2 = 0, F2 = 0;

      for (int j = 0; j < graphs.length; j++) {
        boolean flag2 = Util.subIsomorphic(queries[i], graphs[j]);
        if (flag2 == true) {
          T2++;
          writer.print(j);
          writer.print(" ");
        }
        else {
          F2++;
        }
      }
      writer.println("");
    }

    writer.close();
  }

}