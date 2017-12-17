#/bin/sh

javac ctree/test/subgraph_iso.java

# java ctree/test/subgraph_iso data/aids.txt data/ca_copy/significantGraphs.txt sig_ca.txt
# java ctree/test/subgraph_iso data/aids.txt data/ci_copy/significantGraphs.txt sig_ci.txt

# java ctree/test/subgraph_iso data/aids.txt data/ca_copy/significantGraphs.txt sig_ca_test.txt
# java ctree/test/subgraph_iso data/aids.txt data/ci_copy/significantGraphs.txt sig_ci_test.txt

java ctree/test/subgraph_iso $1 $2 sig_ca.txt
java ctree/test/subgraph_iso $1 $3 sig_ci.txt

java ctree/test/subgraph_iso $4 $2 sig_ca_test.txt
java ctree/test/subgraph_iso $4 $3 sig_ci_test.txt
