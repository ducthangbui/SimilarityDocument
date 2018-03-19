import math
import numpy

def read_file(path):
	file = open(path, "r")
	results = []
	tmp = []
	list = file.readlines()
	for line in list:
		for li in line.replace('\n','').split():
			results.append(li)
	return results

def cos_sim(vector_a, vector_b):
	dot_product = numpy.dot(vector_a,vector_b)
	norm_a = numpy.linalg.norm(vector_a)
	norm_b = numpy.linalg.norm(vector_b)
	return dot_product / (norm_a * norm_b)
	
def number_of_term(word, document):
	#words = document.split()
	counter = 0
	for w in document:
		if word == w:
			counter = counter + 1
	return counter

def tf(word, document):
	times_term = number_of_term(word, document)
	return (times_term/float(len(document)))

def idf(word, list_document):
	counter = 0
	for document in list_document:
		if word in document:
			counter = counter + 1
	return math.log10(1 + float(len(list_document)/counter))
	
def tfidf(tf,idf):
	return tf * idf

if __name__ == "__main__":
	document_a = read_file("./test.txt")
	document_b = read_file("./test2.txt")
	print document_a
	print document_b
	list_document = [document_a, document_b]
	#word = 'bui'
	#document = 'bui duc thang'
	#list_document = [document]
	#tf = tf(word,document)
	#idf = idf(word, list_document)
	#print tf
	#print idf
	#print "tf-idf:", tfidf(tf,idf)
	#print "cosine:", cos_sim([1,2,3],[4,5,6])
	vector_a = []
	vector_b = []
	
	for word in document_a:
		tf_value = tf(word, document_a)
		idf_value = idf(word, list_document)
		tfidf_value = tfidf(tf_value,idf_value)
		vector_a.append(tfidf_value)
		print word, " ", tf_value, " ", idf_value, " ", tfidf_value
		
	print "**************************"
	
	for word in document_b:
		tf_value = tf(word, document_b)
		idf_value = idf(word, list_document)
		tfidf_value = tfidf(tf_value,idf_value)
		vector_b.append(tfidf_value)
		print word, " ", tf_value, " ", idf_value, " ", tfidf_value
	
	print "**************************"
	print "vector_a:", vector_a
	print "vector_b:", vector_b
	print "cosine(vector_a,vector_b):", cos_sim(vector_a,vector_b)
	print "cosine(vector_a,vector_a):", cos_sim(vector_a,vector_a)