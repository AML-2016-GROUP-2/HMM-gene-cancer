import json
import os
import sys
import scipy.cluster.vq as sp
import numpy as np
import os, pickle
import math
from myhmm_scaled import MyHmmScaled as HMM

from utils import *

def trainer(data):
	disease=data.keys()
	observation=data.values()
	hmm_trainer=[]
	model_file = "initial.json" # this is the model file name - you can create one yourself and set it in this variable
        hmm_trainer.append(HMM(os.path.join(".", model_file)))
	hmm_trainer.append(HMM(os.path.join(".", model_file)))
        hmm_trainer.append(HMM(os.path.join(".", model_file)))
        hmm_trainer.append(HMM(os.path.join(".", model_file)))
	j=0
        #print "Using the model from file: ", model_file, " - You can modify the parameters A, B and pi in this file to build different HMM models"
	for i in disease:
		print i
		total1=total2=0
		hmm_trainer[j].forward_backward_multi_scaled([data[i]])
     		print "The new model parameters after 1 iteration are: "
    		print "A = ", hmm_trainer[j].A
    		print "B = ", hmm_trainer[j].B
    		print "pi = ", hmm_trainer[j].pi
		
		#observations = ['1','0','1','2','3']
		pickle.dump([hmm_trainer[j].A,hmm_trainer[j].B,hmm_trainer[j].pi],open(i,"wb"))
		#print math.exp(hmm_trainer[j].forward_scaled(observations))
		j=j+1	
		#hmm_trainer.append(zzz)
        		
		#print hmm_trainer
	

if __name__=="__main__":
	bins = 16
	trng, vec_sizes = obtain_training_data()
	vq_data = vector_quantize(trng, vec_sizes, bins)
	#print "vq_data ",vq_data
	trainer(vq_data)
	
	

