# CYSE_476 HW01

def word_to_pattern(word: str):
    """Takes word"""
    ascii_start = 97  # ASCII code for 'a'
    pattern_dict = {}
    pattern_str = ''
    word = word.lower()  # Want the pattern to be case-insensitive
    word = word.strip()  # Removes any extra spaces from word given
    for char in word:
        if char not in pattern_dict:
            pattern_dict[char] = chr(ascii_start)
            ascii_start += 1
    for char in word:
        pattern_str += pattern_dict[char]

    return pattern_str


def word_list_to_pattern(file):
    word_pattern_dict = {}
    try:
        with open(file, 'r') as f:
            for line in f:
                line = line.strip() # Removes extra newline
                pattern = word_to_pattern(line)
                word_pattern_dict[line] = pattern
    except FileNotFoundError:
        print(f'Please put word list: {file} in same directory as this python script')
        exit(1)

    return word_pattern_dict


def pattern_to_word(pattern):
    list_of_possible_words = []
    for entry in list_of_patterns:
        if list_of_patterns[entry] == pattern:
            list_of_possible_words.append(entry)
    for word in list_of_possible_words:
        print(word)


if __name__ == '__main__':
    word_list = "words_alpha.txt"
    list_of_patterns = word_list_to_pattern(word_list)
    user_word = input("Enter word >>> ")
    word_to_pattern(user_word)
    pattern = input("Enter pattern >>> ")
    pattern_to_word(pattern)
