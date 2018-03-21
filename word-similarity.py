import math

def read_file(path):
	file = open(path, "r")
	results = []
	tmp = []
	list = file.readlines()
	for line in list:
		for li in line.replace('\n','').split():
			results.append(li)
	return results

def length_vecto(vector):
	power = 0
	for dic in vector.values():
		power = power + math.pow(dic,2)
	return math.sqrt(power)
	
def cos_sim(vector_a, vector_b):
	length_vecto_a = length_vecto(vector_a)
	length_vecto_b = length_vecto(vector_b)
	
	total = 0
	keys_a = vector_a.keys()
	keys_b = vector_b.keys()
	for word in min(keys_a,keys_b):
		if word in keys_a and word in keys_b:
			total = total + (vector_a.get(word) * vector_b.get(word))
	return total / (length_vecto_a * length_vecto_b)
	
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
	document_a = read_file("./putin.txt")
	document_b = read_file("./putin2.txt")
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
	vector_a = {}
	vector_b = {}
	idf_dict = {}
	words = []
	
	for word in document_a:
		if word not in words:
			words.append(word)
		#tf_value = tf(word, document_a)
		#idf_value = idf(word, list_document)
		#idf_dict.append({word:idf_value})
		#tfidf_value = tfidf(tf_value,idf_value)
		#vector_a.append(tfidf_value)
		#print word, " ", tf_value, " ", idf_value, " ", tfidf_value
		
	print "**************************"
	
	for word in document_b:
		if word not in words:
			words.append(word)
		#tf_value = tf(word, document_b)
		#idf_value = idf(word, list_document)
		#idf_dict.append({word:idf_value})
		#tfidf_value = tfidf(tf_value,idf_value)
		#vector_b.append(tfidf_value)
		#print word, " ", tf_value, " ", idf_value, " ", tfidf_value
	print words
	for word in words:
		idf_value = idf(word, list_document)
		idf_dict[word] = idf_value
	
	print idf_dict
	
	print "**************************"
	for word in document_a:
		if word in idf_dict:
			tf_value = tf(word, document_a)
			idf_value = idf_dict.get(word)
			vector_a[word] = tfidf(tf_value, idf_value)
			
			
		#print word, " ", tf_value, idf_value, tfidf(tf_value, idf_value)
	print "**************************"
	for word in document_b:	
		#print "word1:", word
		if word in idf_dict:
			#print "word:", word
			tf_value = tf(word, document_b)
			idf_value = idf_dict.get(word)
			vector_b[word] = tfidf(tf_value, idf_value)
			#print "vector_b:", vector_b
			
		
		#print word, " ", tf_value, idf_value, tfidf(tf_value, idf_value)
			
	print "vector_a:", vector_a
	print "vector_b:", vector_b
	print "cosine(vector_a,vector_b):", cos_sim(vector_a,vector_b)
	print "cosine(vector_a,vector_a):", cos_sim(vector_a,vector_a)