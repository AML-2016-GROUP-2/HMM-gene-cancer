import math
import numpy as np
import scipy.cluster.vq as sp
import pickle
mu = []
sup = []
dud = []
lam = []
val = []
o=0
num=0
codebooks = pickle.load(open("all_codebooks.pkl","rb"))
#op = open("testing_data.txt","r")
for line in open("testing_data.txt","r"):
	line = line.replace("\n","")
	line = line.replace("null","0")
	mu.append(line)
	sup = map(float,line.split(",")[1:])
	dud = line.split(",")[0]
	print "sup",sup
	print "dud",dud
	#loading from pickle files 
	hmm1 = pickle.load(open("Prostate Cancer","rb"))
	hmm2 = pickle.load(open("Breast Cancer","rb"))
	hmm3 = pickle.load(open("Lung Cancer","rb"))
	hmm4 = pickle.load(open("Colorectal Cancer","rb"))
	quant = []
	#maping
	try:
		quant[0]=map(str,sp.vq(np.reshape(sup,(len(sup)/8,8)),codebooks[8])[0])
	except:
		pass
	try:
		quant[1]=map(str,sp.vq(np.reshape(sup,(len(sup)/57,57)),codebooks[57])[0])
	except:
		pass
	try:
		quant[2]=map(str,sp.vq(np.reshape(sup,(len(sup)/18,18)),codebooks[18])[0])
	except:
		pass
	#print quant
	try:
		quant[3]=map(str,sp.vq(np.reshape(sup,(len(sup)/18,18)),codebooks[18])[0])
	except:
		pass		
	#print quant
	hmmo  = [hmm1,hmm2,hmm3,hmm4]
	#print hmm
	while(o!=4 and o>=0):
		try:
			#print "here==========================================================="
			val.append(math.exp(hmmo[o].forward_scaled(quant[o])))
		except:
			val.append(0)
		print o
		o+=1

	if(val.index(max(val))==0 and dud=="Prostrate Cancer"):
		print "Prostate found"
		num+=1
	elif(val.index(max(val))==1 and dud=="Breast Cancer"):
		print "Breast found"
		num+=1
	elif(val.index(max(val))==2 and dud=="Lung Cancer"):
		print "Lung found"
		num+=1
	elif(val.index(max(val))==3 and dud=="Colorectal Cancer"):
		print "Colorectal found"
		num+=1
print num
#print mu
		
