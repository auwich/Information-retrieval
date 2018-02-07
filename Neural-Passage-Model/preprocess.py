import sys
sys.path.append("../Tools")

import operator
import numpy as np
import ProcDoc
from collections import defaultdict
from math import log
import os

data = {}                # content of document (doc, content)
background_model = {}    # word count of 2265 document (word, number of words)
query = {}                # query

corpus = "TDT2"
document_path = "../Corpus/" + corpus + "/SPLIT_DOC_WDID_NEW"    
query_path = "../Corpus/" + corpus + "/Train/XinTrainQryTDT2/QUERY_WDID_NEW"
test_query_path = "../Corpus/"+ corpus + "/Train/XinTestQryTDT2/QUERY_WDID_NEW"
resPos = True

# read document, reverse position
doc = ProcDoc.read_file(document_path)
doc = ProcDoc.doc_preprocess(doc, resPos)

# read query, reserve position
query = ProcDoc.read_file(query_path)
query = ProcDoc.query_preprocess(query, resPos)

# read test lone query model, reserve postion
test_query = ProcDoc.read_file(query_path)
test_query = ProcDoc.query_preprocess(test_query, resPos)

# HMMTrainingSet
HMMTraingSetDict = ProcDoc.read_relevance_dict()
query_relevance = {}
max_q = 0
max_d = 0
# create passage matrix
query_model = []
qry_list = query.keys()
doc_list = doc.keys()
rel_qd_list = []
patMatAll = []
# passage model (q_length X d_length)
for q, q_cont in query.items():
	if q in HMMTraingSetDict:
		q_terms = q_cont.split()
		height = len(q_terms)
		if height > max_q:
			max_q = height
		for d, d_cont in doc.items():
			d_terms = d_cont.split()
			width = len(d_terms)
			print width
			if width > max_d:
				max_d = width
			psgMat = np.zeros((height, width))
			print psgMat.shape
			for q_idx in xrange(len(q_terms)):
				q_term = q_terms[q_idx]
				for d_idx in xrange(len(d_terms)):
					d_term = d_terms[d_idx]
					if q_term == d_term:
						psgMat[q_idx][d_idx] = 1
					else:	
						psgMat[q_idx][d_idx] = 0
			if d in HMMTraingSetDict[q]:
				rel_qd_list.append(1)
			else:
				rel_qd_list.append(-1)
		patMatAll.append(psgMat)
	else:
		qry_list.remove(q)

print (max_q, max_d)
# list to numpy
qry_list = np.array(qry_list)
doc_list = np.array(doc_list)
rel_qd_list	= np.array(rel_qd_list)
# zero padding 
#from keras.layers import ZeroPadding2D
#patMatAll = ZeroPadding2D(padding=(1, 1), np.array(patMatAll).astype(np.float32))
# save

'''
np.save("exp/passageModel.np", patMatAll)
np.save("exp/rel_list.np", rel_qd_list)
np.save("exp/qry_list.np", qry_list)
np.save("exp/doc_list.np", doc_list)
'''