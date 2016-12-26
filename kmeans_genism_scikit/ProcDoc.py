import codecs
import io
import os
import fileinput
import collections


CNA_path = "Corpus"
Cluster_path = "clusters"
# read document
def read_doc():
	CNATraingSet = []
	title = "Doc "
	numOfDoc = 0
	# CNA_only_utf8
	for doc_item in os.listdir(CNA_path):
		# join dir path and file name
		doc_item_path = os.path.join(CNA_path, doc_item)
		# check whether a file exists before read
		if os.path.isfile(doc_item_path):
			with io.open(doc_item_path, 'r', encoding = 'utf8') as f:
				# read content of query document (doc, content)
				for line in f.readlines():
					numOfDoc += 1
					CNATraingSet.append(line)
	# CNATraingSet(list)
	return CNATraingSet

# read cluster
def read_clusters():
	clusters = []
	numOfClusters = 0
	# cluster_only_utf8
	for cluster_item in os.listdir(Cluster_path):
		# join dir path and file name
		cluster_item_path = os.path.join(Cluster_path, cluster_item)
		# check whether a file exists before read
		if os.path.isfile(cluster_item_path):
			with io.open(cluster_item_path, 'r', encoding = 'utf8') as f:
				# read content of query document (doc, content)
				for line in f.readlines():
					[cluster_name, documents] = line.split(", ")
					numOfClusters += 1
					clusters.append([cluster_name, documents])
	# clusters(list)
	return clusters	
	
# read document
def read_doc_dict():
	CNATraingSetDict = {}
	title = "Doc "
	numOfDoc = 0
	# CNA_only_utf8
	for doc_item in os.listdir(CNA_path):
		# join dir path and file name
		doc_item_path = os.path.join(CNA_path, doc_item)
		# check whether a file exists before read
		if os.path.isfile(doc_item_path):
			with io.open(doc_item_path, 'r', encoding = 'utf8') as f:
				# read content of query document (doc, content)
				for line in f.readlines():
					CNATraingSetDict[str(numOfDoc)] = line
					numOfDoc += 1
	# CNATraingSetDict(No., content)
	return CNATraingSetDict
	
# word count
def word_count(content, bg_word):
	for part in content.split():
		if part in bg_word:
			bg_word[part] += 1
		else:
			bg_word[part] = 1
	# return word count dictionary		
	return bg_word

# input dict
# output sum of word
def word_sum(data):
	num = 0
	for key, value in data.items():
		num += int(value)
	return num	