# Scrabble
Output leaderboard of words ranked by value


Scrabble™ is a long-established and popular word game in many different languages.The object of the game is to build valid words (for this exercise words are valid if they are present in the wordlist.txt file supplied) from a set of letter (tiles) that the player holds.

Each letter carries a different score value based on its frequency in the language. For example in English vowels such as A and E score only 1 point but less frequent letters such as K and J score 5 and 8 points respectively. The score for any particular word is the sum of the values of all the letters that make up the word. So for example:the word cabbage scores C3 + A1 + B3 + B3 + A1 + G2 + E1 = 14 points. The score values of letters in English are shown in the letterValues.txt file (also supplied).

The objective of this coding challenge is twofold:

1. to create a leaderboard of the 100 highest scoring words in English based on the words in the wordlist.txt file. Words should be ordered in descending order with the highest scoring first. If several words have the same score they should be ordered alphabetically.

2. to create a leaderboard of the valid words that can be created from a supplied String of random letters. For example for the random String deora, some of the valid words are: road; read; and adore. The length of the random String may vary but can be assumed to be in the range of 5-15 characters. Again, words should be ordered in descending order with the highest scoring first. If several words have the same score they should be ordered alphabetically.

Some skeleton Python code is provided for the exercise. Please do not change the supplied code, but create additional code as required. 

def build_leaderboard_for_word_list(self):

def build_leaderboard_for_letters(self, starting_letters):
