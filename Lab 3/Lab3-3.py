from collections import defaultdict

class Model(object):
	def __init__(self):
		self.counts = defaultdict(float)
		self.counts['total'] = 0.0
		self.wordcounts = defaultdict(float)
		self.wordcounts['total'] = 0.0
		self.words = defaultdict(float)
		self.allwords = defaultdict(float)

	def train(self, type, examples):
		if not type in self.counts:
			self.counts[type] = 0.0
		if not type in self.wordcounts:
			self.wordcounts[type] = 0.0
		for example in examples:
			self.counts['total'] += 1.0
			self.counts[type] += 1.0
			if not type in self.words:
				self.words[type] = defaultdict(float)
			for word in example.split(' '):
				self.wordcounts['total'] += 1.0
				self.wordcounts[type] += 1.0
				self.allwords[word] = True
				if not word in self.words[type]:
					self.words[type][word] = 1.0
				else:
					self.words[type][word] += 1.0

	def prior(self, type):
		return self.implementation.prior(type)

	def probability(self, word, type):
		return self.implementation.probability(word, type)

	def classify(self, type, data):
		return self.implementation.classify(type, data)

class Smoothing(Model):
	def __init__(self, k = 1):
		Model.__init__(self)
		self.k = k

	def prior(self, type):
		return (self.counts[type] + self.k) / (self.counts['total'] + (self.k * len(self.words.keys())))

	def probability(self, word, type):
		a = self.words[type][word] + self.k
		b = self.wordcounts[type] + (self.k * len(self.allwords))
		return a / b

	def classify(self, type, data):
		if not isinstance(data, list):
			a = self.probability(data, type) * self.prior(type)
			b = 0.0
			for _type in self.words:
				b += self.probability(data, _type) * self.prior(_type)
			return a / b
		else:
			a = self.prior(type)
			for word in data:
				a *= self.probability(word, type)
			b = 0.0
			for _type in self.words:
				bb = self.prior(_type)
				for word in data:
					bb *= self.probability(word, _type)
				b += bb
			return a/b

class MaximumLikelihood(Smoothing):
	def __init__(self, k = 0):
		Smoothing.__init__(self,k)

# procedure of the classifier model.
# .prior(label) : get prior probability of label in the model
# .probability(feature, label) :  the probability that input values with that label will have that feature
# .initialization(k) of the model
#       - k == 0: no-smooth mode
#       - k != 0: smooth mode
def Lab3_3a():
	print ('Lab3_3a')
	MOVIE = ['a perfect world', 'my perfect woman', 'pretty woman']
	SONG = ['a perfect day', 'electric storm', 'another rainy day']

	model_smooth = MaximumLikelihood(1)    
	model_smooth.train('movie', MOVIE)
	model_smooth.train('song', SONG)


	print('\n---------------TASK 1.a.1---------------')
	print("Prior probability of label 'movie':", model_smooth.prior('movie'))
	print("Prior probability of label 'song':", model_smooth.prior('song'))

	
	print('\n---------------TASK 1.a.2---------------')
	a = model_smooth.probability("perfect", "movie")
	b = model_smooth.probability("storm", "movie")
	c = model_smooth.probability("perfect", "song")
	d = model_smooth.probability("storm", "song")
	print("\nProbability of word 'perfect' having tag 'movie': ", a)
	print("Probability of word 'storm' having tag 'movie': ", b)
	print("Probability of word 'perfect' having tag 'song': ", c)
	print("Probability of word 'storm' having tag 'song': ", d)

	print('\n---------------TASK 1.a.3---------------')
	print("\nwith smoothing on movie:", model_smooth.probability("perfect storm", "movie"))
	print("with smoothing on song:", model_smooth.probability("perfect storm", "song"))

	model_rough = MaximumLikelihood(0)
	model_rough.train('movie', MOVIE)
	model_rough.train('song', SONG)
	print("no smoothing on movie:", model_rough.probability("perfect storm", "movie"))
	print("no smoothing on song:", model_rough.probability("perfect storm", "song"))
	
def Lab3_3b():
	print ('\nLab3_3b')

	HAM = ["play sport today", "went play sport", "secret sport event", "sport is today", "sport costs money"]
	SPAM = ["offer is secret", "click secret link", "secret sport link"]

	model = MaximumLikelihood(0)
	model.train('S', SPAM)
	model.train('H', HAM)

	print('\n---------------TASK 1.b.1---------------')
	print("Prior probability of label 'SPAM':", model.prior('S'))
	print("Prior probability of label 'HAM':", model.prior('H'))

	print('\n---------------TASK 1.b.2---------------')


	print('\n---------------TASK 1.b.3---------------')
	print("no smoothing on S:", model.probability("today is secret", "S"))
	print("no smoothing on H:", model.probability("today is secret", "H"))

	model_smooth = MaximumLikelihood(1)
	model_smooth.train('S', SPAM)
	model_smooth.train('H', HAM)
	print("\nwith smoothing on S:", model_smooth.probability("today is secret", "S"))
	print("with smoothing on H:", model_smooth.probability("today is secret", "H"))
	

if __name__ == '__main__':
	Lab3_3a()
	Lab3_3b()
