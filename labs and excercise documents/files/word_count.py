def get_words(file_path):
    with open(file_path, 'r') as file:
        return file.read().split(' ')


def get_words_counts(file_path, words):
    words_counts = {word: 0 for word in words}
    with open(file_path, 'r') as file:
        for line in file:
            words_in_line = line.split(" ")
            for word in words:
                if word in line.lower():
                        words_counts[word] +=1

    return words_counts


def print_words_count(words_counts):
    def order_by_value(pair): # key = lambda pair:(pair[1],pair[0])
        (key,value) = pair
        return (value,key)
    sorted_words_counts = sorted(words_counts.items(), key=order_by_value, reverse=True)
    [print(f'{word} - {count}') for (word,count) in sorted_words_counts]
words_file_path = './files/Words Count/words.txt'
text_file_path = './files/Words Count/text.txt'

words_counts = get_words_counts(text_file_path, get_words(words_file_path))
print_words_count(words_counts)
