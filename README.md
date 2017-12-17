# subgraph-embedding-generation

## Following is the problem statement:

Consider the same AIDS graph dataset. We now provide you a label for a subset of the graphs: the active molecules against HIV virus and the inactive molecules. Molecules that do not have a class label should be ignored. Design a technique to classify graphs by using frequent subgraphs as features. More specifically, convert each graph into a binary feature vector where each dimension corresponds to the presence or absence of the corresponding subgraph. Ideally, you should not use all frequent subgraphs as features. Rather, you should only use the “discriminative” frequent subgraphs. We will classify the graphs (in the feature space) using the linear kernel of libsvm. While training, we will also ensure that the trainset has an equal number of active and inactive molecules.

For automated testing, you must submit a shell script titled classify.sh. It should support the following operation.

“sh classify.sh <trainset filename containing graphs> <active graph IDs filename> <inactive graph IDs filename> <testset filename containing graphs>”

The output should be two files titled “train.txt” and “test.txt”. In train.txt, the ith line contains the class label of graph i followed by the feature vector representation of the ith graph in the trainset. The label of an active graph is “1” and an inactive graph is “-1”. Each line must be of the following format:

label index1:value1 index2:value2 ...

.

.

.

The test.txt file should of the same format as above, with the only exception being that you do not need to include the class label. That is, it should be of the form

index1:value1 index2:value2 ...

.

.

.

If test set contains 100 graphs, test.txt should contain 100 lines (same for train.txt as well). We will run libsvm on your files. If you do not adhere to the above format, you will receive 0 points. More specifically, you should run libsvm on train.txt and ensure that libsvm is able to train on your data format.

Your shell script must complete within 20 minutes. This includes both the training and testing time.
