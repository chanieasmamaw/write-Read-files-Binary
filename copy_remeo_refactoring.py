import string
from collections import Counter

from Reomeyo_refactory_text import PLAY


#TOP_N = 50


def get_words(text):
	translated_table = str.maketrans("", "", string.punctuation)
	clean_table = text.translate(translated_table)
	clean_table_lower = clean_table.lower()
	return clean_table_lower.split(text)


def words_frequency(words_list):
	return Counter(words_list)


def top_n_words(freq_dict, n):
	return freq_dict.most_common(n)


def main():
	words_list = get_words(PLAY)
	freq_dict = words_frequency(words_list)
	top_50_words = top_n_words(freq_dict, 50)
	print("Top 50 most frequent words:")
	for word, count in top_50_words:
		print(f"{word}: {count}")


if __name__ == "__main__":
	main()
