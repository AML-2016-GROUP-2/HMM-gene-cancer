# HMM-gene-cancer
HMM Classifer to detect Cancer from Gene Expressions

Problem statement:

     Build a classifier using HMMs to detect Cancer from Gene Expressions


Steps implemented:

Training:

     The initial Hmm was trained with initial.jason, which had 3 states initially which also constituted emission matrix, initial probability and transition probability matrix. Utils.py gave vector quantized data which was fed to train.py. The vector quantization function was used to map each vector given in the training data to a particular integer ranging from 0 to 15 Since bins = 16, and this vector quantization was achieved by k-Means clustering. 4 hmms were created as there were 4 types of cancer in dataset, trained them respectively with observable list which was created from mapped observables through forward-backward algorithm and made a pickle file for each trained HMM.

Testing:

    we first defined vector lengths of different type of cancers. And these vectors were passed to forward algorithm in order to classify input symbols and gain maximum possible probability.


Correctly tested 3/15 test data.
