cd ci
java -Xmx7000m -cp graphSig.jar grank.mine.MotifHistSet $*
rm prepareForSubgraphMining.sh
bash subgraphMining_ci.sh
