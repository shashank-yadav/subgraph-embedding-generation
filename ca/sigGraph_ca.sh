cd ca
java -Xmx7000m -cp graphSig.jar grank.mine.MotifHistSet $*
rm prepareForSubgraphMining.sh
bash subgraphMining_ca.sh
