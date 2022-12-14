class Caesar1:
    alphabet = {1: 'a',
                2: 'b',
                3: 'c',
                4: 'd',
                5: 'e',
                6: 'f',
                7: 'g',
                8: 'h',
                9: 'i',
                10: 'j',
                11: 'k',
                12: 'l',
                13: 'm',
                14: 'n',
                15: 'o',
                16: 'p',
                17: 'q',
                18: 'r',
                19: 's',
                20: 't',
                21: 'u',
                22: 'v',
                23: 'w',
                24: 'x',
                25: 'y',
                26: 'z'}  # 1..26 / a..z

    @staticmethod
    def get_key(val):
        for key, value in Caesar1.alphabet.items():
            if val == value:
                return key

    @staticmethod
    def encrypt(text, shift):
        encrypted = ''
        for char in text:
            encrypted += Caesar1.alphabet[(Caesar1.get_key(char) + shift) % 26]
        return encrypted

    @staticmethod
    def decrypt(text, shift):
        decrypted = ''
        for char in text:
            decrypted += Caesar1.alphabet[(Caesar1.get_key(char) - shift + 26) % 26]
        return decrypted


class Caesar2:
    alphabet_initial = {1: 'a',
                        2: 'b',
                        3: 'c',
                        4: 'd',
                        5: 'e',
                        6: 'f',
                        7: 'g',
                        8: 'h',
                        9: 'i',
                        10: 'j',
                        11: 'k',
                        12: 'l',
                        13: 'm',
                        14: 'n',
                        15: 'o',
                        16: 'p',
                        17: 'q',
                        18: 'r',
                        19: 's',
                        20: 't',
                        21: 'u',
                        22: 'v',
                        23: 'w',
                        24: 'x',
                        25: 'y',
                        26: 'z'}  # 1..26 / a..z
    alphabet_new = {1: 'a',
                    2: 'b',
                    3: 'c',
                    4: 'd',
                    5: 'e',
                    6: 'f',
                    7: 'g',
                    8: 'h',
                    9: 'i',
                    10: 'j',
                    11: 'k',
                    12: 'l',
                    13: 'm',
                    14: 'n',
                    15: 'o',
                    16: 'p',
                    17: 'q',
                    18: 'r',
                    19: 's',
                    20: 't',
                    21: 'u',
                    22: 'v',
                    23: 'w',
                    24: 'x',
                    25: 'y',
                    26: 'z'}

    @staticmethod
    def get_key_new(val):
        for key, value in Caesar2.alphabet_new.items():
            if val == value:
                return key

    @staticmethod
    def encrypt(text, word, shift):
        letters = []
        counter = 1

        for char in word:
            if char not in letters:
                letters.append(char)
                Caesar2.alphabet_new[counter] = char
                counter += 1
            else:
                return "Error: letters should not repeat"

        counter = 1

        for i in range(len(word) + 1, 26):
            while Caesar2.alphabet_initial[counter] in letters:
                counter += 1
            Caesar2.alphabet_new[i] = Caesar2.alphabet_initial[counter]
            counter += 1
            if counter == 27:
                counter = 1

        encrypted = ''
        for char in text:
            encrypted += Caesar2.alphabet_new[(Caesar2.get_key_new(char) + shift) % 26]
        return encrypted

    @staticmethod
    def decrypt(text, word, shift):
        letters = []
        counter = 1

        for char in word:
            if char not in letters:
                letters.append(char)
                Caesar2.alphabet_new[counter] = char
                counter += 1
            else:
                return "Error: letters should not repeat"

        # counter = 1

        # for i in range(len(word) + 1, 26):
        #     while Caesar2.alphabet_initial[counter] in letters:
        #         print(counter, "counter")
        #         print(Caesar2.alphabet_initial[counter])
        #         counter += 1
        #     Caesar2.alphabet_new[i] = Caesar2.alphabet_initial[counter]
        #     counter += 1
        #     if counter == 27:
        #         counter = 1

        decrypted = ''
        for char in text:
            decrypted += Caesar2.alphabet_new[(Caesar2.get_key_new(char) - shift + 26) % 26]

        return decrypted


class Vigenere:
    # generates the key in a cyclic manner until
    # it's length isn't equal to the length of original text
    @staticmethod
    def cyclic_key(string, key):
        key = list(key)
        if len(string) == len(key):
            return key
        else:
            for i in range(len(string) - len(key)):
                key.append(key[i % len(key)])
        return "".join(key)

    @staticmethod
    def encryption(string, key):
        cipher_text = []
        for i in range(len(string)):
            x = (ord(string[i]) +
                 ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        return "".join(cipher_text)

    @staticmethod
    def decryption(cipher_text, key):
        orig_text = []
        for i in range(len(cipher_text)):
            x = (ord(cipher_text[i]) -
                 ord(key[i]) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
        return "".join(orig_text)


class Atbash:
    key_table = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
                 'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
                 'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
                 'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
                 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}

    @staticmethod
    def encryption(message):
        cipher = ''
        for letter in message:
            # checks for space
            if letter != ' ':
                # adds the corresponding letter from the lookup_table
                cipher += Atbash.key_table[letter]
            else:
                # adds space
                cipher += ' '

        return cipher

    @staticmethod
    def decryption(message):
        cipher = ''
        for letter in message:
            # checks for space
            if letter != ' ':
                # adds the corresponding letter from the lookup_table
                cipher += Atbash.key_table[letter]
            else:
                # adds space
                cipher += ' '

        return cipher


# Caesar 1
# message = Caesar1.encrypt("attack", 3)
# print(message)
# print(Caesar1.decrypt(message, 3))

# Caesar 2
# message = Caesar2.encrypt("attack", 'halo', 3)
# print(message)
# print(Caesar2.alphabet_new)
# print(Caesar2.decrypt(message, 'halo', 3))

# Vigenere
# string = "ATTACK"
# keyword = "HALO"
# key = Vigenere.cyclic_key(string, keyword)
# message = Vigenere.encryption(string, key)
# print(message)
# print(Vigenere.decryption(message, key))

# Atbash
# message = Atbash.encryption("ATTACK")
# print(message)
# print(Atbash.decryption(message))
