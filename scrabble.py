"""
Each letter carries a different score value. 

The objective of this coding challenge is twofold:
1. to create a leaderboard of the 100 highest scoring words in English based on the words in the wordlist.txt file. 
	Words should be ordered in descending order with the highest scoring first. 
	If several words have the same score they should be ordered alphabetically.
2. to create a leaderboard of the valid words that can be created from a supplied String of random letters. 
	For example for the random String deora, some of the valid words are: road; read; and adore. 
	The length of the random String may vary but can be assumed to be in the range of 5-15 characters. 
	Again, words should be ordered in descending order with the highest scoring first. 
	If several words have the same score they should be ordered alphabetically.
"""


class HighScoringWords:

	MAX_LEADERBOARD_LENGTH = 100  # the maximum number of items that can appear in the leaderboard
	MIN_WORD_LENGTH = 3  # words must be at least this many characters long
	letter_values = {}
	valid_words = []
	

	def __init__(self, validwords='wordlist.txt', lettervalues='letterValues.txt'):
		"""
		Initialise the class with complete set of valid words and letter values by parsing text files containing the data
		:param validwords: a text file containing the complete set of valid words, one word per line
		:param lettervalues: a text file containing the score for each letter in the format letter:score one per line
		:return:
		"""
		
		self.leaderboard = []  # initialise an empty leaderboard
		
		with open(validwords) as f:
			self.valid_words = f.read().splitlines()
		
		with open(lettervalues) as f:
			for line in f:
				(key, val) = line.split(':')
				self.letter_values[str(key).strip().lower()] = int(val)


	def get_word_val(self, word):
		"""
		function used by "build_leaderboard_for_word_list"
		calculate the value of a word
		:param word: string
		:type return: int
		"""
		val = 0
		for letter in word:
			val += self.letter_values[letter.lower()]
		
		return val


	def build_leaderboard_for_word_list(self):
		"""
		Build a leaderboard of the top scoring MAX_LEADERBOAD_LENGTH words from the complete set of valid words.
		:return:
		"""
		# use max-heap (-1 * val to heapify)
		
		self.leaderboard = []

		import heapq	
		queue = []
		for word in self.valid_words:
			queue.append((-1 * self.get_word_val(word), word))
		
		heapq.heapify(queue)

		count = 0
		while queue and count < HighScoringWords.MAX_LEADERBOARD_LENGTH:
			tmp = heapq.heappop(queue)
			self.leaderboard.append(tmp[1])
			count += 1
	

	def string_permutation(self, letters, start, end, res):
		"""
		function used by "get_words_from_letters" (finally used by "build_leaderboard_for_letters")
		get all possible words with given letters
		:param letters: list of charaters
		:param start & end: start and end index
		:param res: list of string
		"""
		if start == end:
			word = "".join(letters)
			if word not in res:
				res.append(word)
			return
		
		for i in xrange(start, end + 1):
			letters[start], letters[i] = letters[i], letters[start]
			self.string_permutation(letters, start + 1, end, res)
			#backtracking
			letters[start], letters[i] = letters[i], letters[start]


	def get_words_from_letters(self, starting_letters, index, chosen_letters, words):
		"""
		function used by "build_leaderboard_for_letters"
		get all words could be created by starting_letter
		:param starting_letters: string of candidate letters
		:param index: current working index
		:param chosen_letters: list of characters that have been chosen
		:param words: list of string(words)
		"""
		if index == len(starting_letters):
			if len(chosen_letters) >= HighScoringWords.MIN_WORD_LENGTH:
				candidates = []
				self.string_permutation(chosen_letters, 0, len(chosen_letters) - 1, candidates) #return all words made from these letters (permutation)
				for word in candidates:
					if word in self.valid_words and word not in words:
						words.append(word)
			return

		#use or not use current letter (starting_letters[index])
		self.get_words_from_letters(starting_letters, index + 1, chosen_letters + [starting_letters[index]], words)
		self.get_words_from_letters(starting_letters, index + 1, chosen_letters, words)

	
	def build_leaderboard_for_letters(self, starting_letters):
		"""
		Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that can be built using only the letters contained in the starting_letters String.
		The number of occurrences of a letter in the startingLetters String IS significant. If the starting letters are bulx, the word "bull" is NOT valid.
		There is only one l in the starting string but bull contains two l characters.
		Words are ordered in the leaderboard by their score (with the highest score first) and then alphabetically for words which have the same score.
		:param starting_letters: a random string of letters from which to build words that are valid against the contents of the wordlist.txt file
		:return:
		"""
		self.leaderboard = []
		words = []
		self.get_words_from_letters(starting_letters, 0, [], words)

		import heapq
		queue = []
		for word in words:
			queue.append((-1 * self.get_word_val(word), word))
		heapq.heapify(queue)

		count = 0
		while queue and count < HighScoringWords.MAX_LEADERBOARD_LENGTH:
			tmp = heapq.heappop(queue)
			self.leaderboard.append(tmp[1])
			count += 1


# --------------tests------------------------

#test1: input and calculation
test1 = HighScoringWords()
assert len(test1.letter_values) == 26  # number of letters in letterValues.txt
assert len(test1.valid_words) == 172823  # number of words in word_list.txt
assert test1.get_word_val("cabbage") == 14  # example in subject


#test2: build_leaderboard_for_word_list
test2 = HighScoringWords()
test2.build_leaderboard_for_word_list()
assert len(test2.leaderboard) == test2.MAX_LEADERBOARD_LENGTH
#test correct leaderboard
i = 1
while i < len(test2.leaderboard):
	assert test2.get_word_val(test2.leaderboard[i - 1]) >= test2.get_word_val(test2.leaderboard[i])
	i += 1
#test no duplicate words in leaderboard
store = []
for word in test2.leaderboard:
	assert word not in store
	store.append(word)


#test3: build_leaderboard_for_letters
test3 = HighScoringWords()
test3.build_leaderboard_for_letters("deora")  # example in subject
assert "road" in test3.leaderboard
assert "read" in test3.leaderboard
assert "adore" in test3.leaderboard
#test correct leaderboard
i = 1
while i < len(test3.leaderboard):
	assert test3.get_word_val(test2.leaderboard[i - 1]) >= test3.get_word_val(test3.leaderboard[i])
	i += 1
#test no duplicate words in leaderboard
store = []
for word in test3.leaderboard:
	assert word not in store
	store.append(word)