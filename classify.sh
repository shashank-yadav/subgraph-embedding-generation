#!/usr/bin/sh

wget www.cse.iitd.ac.in/~cs5130702/graphSig.jar

cp graphSig.jar ca/graphSig.jar

cp graphSig.jar ci/graphSig.jar

python convert_all.py $1 gaston.txt $2 $3 $4

rm gaston.txt

rm labels.txt

time sh ca/sigGraph_ca.sh -pvalue=0.1 -minSup=0.1 ../data/aids.txt ../data/ca.txt &

time sh ci/sigGraph_ci.sh -pvalue=0.1 -minSup=0.1 ../data/aids.txt ../data/ci.txt

python correctFormat.py data/ca/significantGraphs.txt

python correctFormat.py data/ci/significantGraphs.txt

sh run.sh data/aids.txt data/ca/significantGraphs.txt.corrected data/ci/significantGraphs.txt.corrected data/test.txt

python ml.py data/ca.txt data/ci.txt data/test.txt

rm -rf data/ca

rm -rf data/ci

rm -rf ca/pafi-1.0.1/Linux/cg/*

rm -rf ci/pafi-1.0.1/Linux/cg/*

rm sig_ca.txt

rm sig_ci.txt

rm sig_ca_test.txt

rm sig_ci_test.txt

rm graphSig.jar

rm ca/graphSig.jar

rm ci/graphSig.jar

