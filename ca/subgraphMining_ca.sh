rm pafi-1.0.1/Linux/cg/*.*
cp ../data/ca/subHist/*.cg pafi-1.0.1/Linux/cg/
cp ../data/ca/subHist/*.sh pafi-1.0.1/Linux/cg/
cd pafi-1.0.1/Linux/cg/
( cmdpid=$BASHPID; (sleep 500; kill $cmdpid) & exec time sh findFreqGraphs.sh )
if [ ! -d fp ]; then
  mkdir fp
  mv *.fp fp
fi
if [ -z "$(ls -A fp)" ]; then
   mv *.fp fp
fi
cp -rf fp ../../../../data/ca/subHist/
cd ../../../
java -Xmx7000m -cp graphSig.jar tool.GraphViz ../data/aids.txt ../data/ca.txt -nta=5
