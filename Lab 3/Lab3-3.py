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

	movie_prior = model_smooth.prior("movie")
	song_prior = model_smooth.prior("song")

	print('\n---------------TASK 3.a.1---------------')
	print("Prior probability of label 'movie':", movie_prior)
	print("Prior probability of label 'song':", song_prior)

	
	print('\n---------------TASK 3.a.2---------------')
	a = model_smooth.probability("perfect", "movie")
	b = model_smooth.probability("storm", "movie")
	c = model_smooth.probability("perfect", "song")
	d = model_smooth.probability("storm", "song")
	print("\nProbability of word 'perfect' having tag 'movie': ", a)
	print("Probability of word 'storm' having tag 'movie': ", b)
	print("Probability of word 'perfect' having tag 'song': ", c)
	print("Probability of word 'storm' having tag 'song': ", d)

	print('\n---------------TASK 3.a.3---------------')
	print("\n'perfect storm' with smoothing on movie:", model_smooth.probability("perfect storm", "movie"))
	print("'perfect storm' with smoothing on song:", model_smooth.probability("perfect storm", "song"))

		# YOUR CODE HERE!

		# Returns the values.
		# 1. Prior probability of labels used in training. (movie, song)
		# 2. Probability of word under given prior label (i.e., P(word|label)) according to this NB model.
		#         a. P(perfect|movie)

		#         b. P(storm|movie)
		#         c. P(perfect|song)
		#         d. P(storm|song)
		# 3. Probability of the title 'perfect storm' is labeled as 'movie' and 'song' with no-smooth mode and smooth mode (k=1)
	

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

	"""
		YOUR CODE HERE!
		Returns the values.
		1. Prior probability of labels for SPAM, HAM data.
		2. Probability of word 'secret', 'sport' under given prior label (SPAM, HAM)
		3. Probabilities of: The word 'today is secret' is labeled as SPAM, HAM with no-smooth mode and smooth mode (k=1)
	"""



	print('\n---------------TASK 3.b.1---------------')
	spam_prior = model.prior("S")
	ham_prior = model.prior("H")
	print("Prior probability of label 'spam':", spam_prior)
	print("Prior probability of label 'ham':", ham_prior)


	print('\n---------------TASK 3.b.2---------------')
	# TODO DO TO

	print('\n---------------TASK 3.b.3---------------')
	print("\n'today is secret' without smoothing on ham:", model.probability("today is secret", "H"))
	print("'today is secret' without smoothing on spam:", model.probability("today is secret", "S"))

	model_without_smoothing = MaximumLikelihood(1)
	model_without_smoothing.train('S', SPAM)
	model_without_smoothing.train('H', HAM)

	print("\n'today is secret' with smoothing on ham:", model_without_smoothing.probability("today is secret", "H"))
	print("'today is secret' with smoothing on spam:", model_without_smoothing.probability("today is secret", "S"))


	
if __name__ == '__main__':
	Lab3_3a()
	Lab3_3b()
