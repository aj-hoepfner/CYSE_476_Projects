# CYSE_476 HW01

# Reference: https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
WORD_PERCENTAGES = {'a': 8.12,
                    'b': 1.49,
                    'c': 2.71,
                    'd': 4.32,
                    'e': 12.02,
                    'f': 2.30,
                    'g': 2.03,
                    'h': 5.92,
                    'i': 7.31,
                    'j': 0.10,
                    'k': 0.69,
                    'l': 3.98,
                    'm': 2.61,
                    'n': 6.95,
                    'o': 7.68,
                    'p': 1.82,
                    'q': 0.11,
                    'r': 6.02,
                    's': 6.28,
                    't': 9.10,
                    'u': 2.88,
                    'v': 1.11,
                    'w': 2.09,
                    'x': 0.17,
                    'y': 2.11,
                    'z': 0.07}

def word_to_pattern(word: str):
    """Converts a word to a pattern."""
    ascii_start = 97  # ASCII code for 'a'
    pattern_dict = {}
    pattern_str = ''
    word = word.lower()  # Make the word case-insensitive
    word = word.strip()  # Removes any extra spaces from the word
    for char in word:
        if char not in pattern_dict:
            pattern_dict[char] = chr(ascii_start)
            ascii_start += 1
    for char in word:
        pattern_str += pattern_dict[char]

    return pattern_str


def word_list_to_pattern(file):
    """Converts a list of words to their corresponding patterns."""
    word_pattern_dict = {}
    try:
        with open(file, 'r') as f:
            for line in f:
                line = line.strip()  # Removes extra newline
                pattern = word_to_pattern(line)
                word_pattern_dict[line] = pattern
    except FileNotFoundError:
        print(f'Please put word list: {file} in the same directory as this Python script')
        exit(1)

    return word_pattern_dict


def pattern_to_word(pattern):
    """Converts a pattern to a list of possible words."""
    list_of_possible_words = []
    for entry in list_of_patterns:
        if list_of_patterns[entry] == pattern:
            list_of_possible_words.append(entry)
    for word in list_of_possible_words:
        print(word)


def histo(string: str):
    """Calculates the frequency of letters in a string."""
    freq_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0,
                 'e': 0, 'f': 0, 'g': 0, 'h': 0,
                 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                 'm': 0, 'n': 0, 'o': 0, 'p': 0,
                 'q': 0, 'r': 0, 's': 0, 't': 0,
                 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                 'y': 0, 'z': 0}
    string = string.lower()
    for char in string:
        if char not in freq_dict:  # Skip any non-alpha characters
            continue
        freq_dict[char] += 1

    total_chars = 0
    for char in freq_dict:
        total_chars += freq_dict[char]
    freq_dict_percent = {}
    for char in freq_dict:
        percent = freq_dict[char] / total_chars * 100
        percent = round(percent, 2)  # Rounds to hundredths place
        freq_dict_percent[char] = percent
    # Sorting the dictionary by percent values in descending order
    sorted_freq_dict = {k: v for k, v in sorted(freq_dict_percent.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_freq_dict)
    return sorted_freq_dict

def decode_part_3():
    """Decodes Part 3 of the assignment."""
    cipher = "VUMQ KG XGR BEQ VUEF XGR NLGPP M NUSDHMFZEE VSQU M PNSEFQSPQ? M PQELFCX VGLKEK CEQQEL YLGD QUE EQUSNP OGMLK."
    histo_stats = histo(cipher)


def decode_part_4():
    """Decodes Part 4 of the assignment."""
    cipher = "7 12 26 20   14 4   22 4 15   14 4   7 12 3 2   22 4 15   12 26 16 3   2 15 6 3 24 25 5   5 4 14 3 23 24 26 20 12 3 24   20 12 26 2   26 8 9 12 26 18 3 20 25 5 ?   26 2 23 7 3 24 :   20 12 3   23 26 6 3   20 12 25 2 10 .   23 25 6 9 8 3   23 15 18 23 20 26 20 25 4 2 23  24 3 9 8 26 5 3   4 2 3   23 22 6 18 4 8   4 21   9 8 26 25 2 20 3 17 20   7 25 20 12   4 2 3  23 22 6 18 4 8   4 21   5 25 9 12 3 24 20 3 17 20 ."

    # Convert numbers to letters
    cipher_letters = ""
    for num in cipher.split():
        if num.isdigit():
            letter = chr(int(num) + 96)  # Adding 96 to convert ASCII values to lowercase letters (a=97)
            cipher_letters += letter
        else:
            cipher_letters += num  # Keep non-numeric characters as they are

    print(cipher_letters)
    histo_stats = histo(cipher_letters)

    return cipher_letters


if __name__ == '__main__':
    word_list = "words_alpha.txt"
    list_of_patterns = word_list_to_pattern(word_list)
    while True:
        menu = int(input("1: Convert word to pattern\n"
                         "2: Convert pattern to possible word list\n"
                         "3: Decode Part 3\n"
                         "4: Decode Part 4\n"
                         "5: Quit\n"
                         ">>> "))
        if menu == 1:
            user_word = input("Enter word >>> ")
            p = word_to_pattern(user_word)
            print(p)
        elif menu == 2:
            pattern = input("Enter pattern >>> ")
            pattern_to_word(pattern)
        elif menu == 3:
            decode_part_3()
        elif menu == 4:
            decode_part_4()
        elif menu == 5:
            print("Goodbye")
            exit(0)
