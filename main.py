import codecs
from time import time


class UnindexedDatabase:
    def __init__(self, db):
        self.db = db
    def db_contains_word(self, word):
        return True
    def word_exist_in_db(self, word):
        return word in self.db
    def __str__(self):
        return "1-unindexed database"


class Node:
    def __init__(self, word: str, letter: str, pre: str=""):
        self.pre = pre
        self.letter = letter
        self.full_name = self.pre + self.letter
        self.num_of_words = 1
        self.has_final = False
        self.inner_nodes = {}
        # print("inserting full name to node:", self.full_name)
        self.insert_new_word(word)

    def insert_new_word(self, word):
        word_len = len(word)
        full_name_len = len(self.full_name)
        un_indexed_words = word[full_name_len: word_len]
        # print("unindexed word:", un_indexed_word)
        if len(un_indexed_words) == 0:
            self.has_final = True
        else:
            next_un_indexed_word = un_indexed_words[0]
            inner_node = self.inner_nodes.get(next_un_indexed_word)
            if inner_node is None:
                # print("unindexed word:", next_un_indexed_word)
                self.inner_nodes[next_un_indexed_word] = Node(word, next_un_indexed_word, self.full_name)
            else:
                self.inner_nodes[next_un_indexed_word].insert_new_word(word)

    def word_exist_in_db(self, word):
        # print("full name:", self.full_name)
        if self.full_name == word and self.has_final:
            return True
        word_len = len(word)
        my_len = len(self.full_name)
        if my_len >= word_len:
            # print("false 1")
            return False
        letters_left = word[my_len: word_len]
        next_letter = letters_left[0]
        # print("next letter:", next_letter)
        inner_node = self.inner_nodes.get(next_letter)
        if inner_node is None:
            # print("no inner node")
            return False
        return inner_node.word_exist_in_db(word)

    def db_contains_word(self, word):
        if self.full_name == word:
            return True
        word_len = len(word)
        my_len = len(self.full_name)
        if my_len >= word_len:
            return False
        letters_left = word[my_len: word_len]
        next_letter = letters_left[0]
        inner_node = self.inner_nodes.get(next_letter)
        if inner_node is None:
            return False
        return inner_node.db_contains_word(word)


class IndexedDatabase:
    def __init__(self, db):
        # self.dir = direc
        # self.file_name = file_name
        # self.file_full_name = self.dir + self.file_name
        self.roots = {}
        self.dictionary_in_list = db
        # self.build_database_from_file()

        self.build_database_from_list()

    def __str__(self):
        return "2-indexed database"

    def build_database_from_list(self):
        for word in self.dictionary_in_list:
            # print("inserting word:", word)
            self.add_word_to_db(word)

    def add_word_to_db(self, word):
        if len(word) < 1:
            return
        first_letter = word[0]
        # print("first letter:", first_letter)
        if self.roots.get(first_letter) is None:
            self.roots[first_letter] = Node(word, first_letter)
        else:
            self.roots[first_letter].insert_new_word(word)

    def db_contains_word(self, word):
        if len(word) < 1:
            return False
        first_letter = word[0]
        root = self.roots.get(first_letter)
        if root is None:
            return False
        return root.db_contains_word(word)

    def word_exist_in_db(self, word):
        if len(word) < 1:
            return False
        first_letter = word[0]
        # print('first:', first_letter)
        root = self.roots.get(first_letter)
        if root is None:
            return False
        return root.word_exist_in_db(word)


class HashedDatabase:
    def __init__(self, db):
        self.db = {}
        for word in db:
            self.db[word] = True

    def db_contains_word(self, word):
        return True

    def word_exist_in_db(self, word):
        return self.db.get(word, False)

    def __str__(self):
        return "3-hashed database"


class AnagramBuilder:
    def __init__(self, dictionary):
        self.main_word = ""
        self.list_of_anagrams = []
        self.dictionary = dictionary

    def init(self, word):
        self.main_word = word
        self.list_of_anagrams = []

    def make_anagrams_for_word(self, word):
        self.init(word)
        word_in_list = [w for w in word]
        self.make_anagrams_with_acceptable_words(word_in_list)
        return self.list_of_anagrams

    def make_anagrams_with_acceptable_words(self, words: list, before: str=''):
        if len(words) == 1:
            final = before + words[0]
            if final == self.main_word:
                return
            if self.dictionary.word_exist_in_db(final):
                if final not in self.list_of_anagrams:
                    self.list_of_anagrams.append(final)
        else:
            for index in range(len(words)):
                word = words[index]
                next_before = before + word
                others = [words[i] for i in range(len(words)) if i != index]
                if self.dictionary.db_contains_word(next_before):
                    self.make_anagrams_with_acceptable_words(others, next_before)


class PrimeNumberFinder:
    def __init__(self):
        self.current_prime_number = None
        self.all_prime_numbers_found = []

    def find_next_prime_number(self):
        if self.current_prime_number is None:
            self.set_new_prime_number_to(2)
            return self.current_prime_number
        next_prime = self.current_prime_number + 1
        while True:
            for found_prime in self.all_prime_numbers_found:
                if next_prime % found_prime == 0:
                    break
            else:
                break
            next_prime += 1
        self.set_new_prime_number_to(next_prime)
        return next_prime

    def set_new_prime_number_to(self, new_prime):
        self.current_prime_number = new_prime
        self.all_prime_numbers_found.append(new_prime)


class PerfectHashedAnagramBuilder:
    def __init__(self, dictionary):
        self.prime_number_finder = PrimeNumberFinder()
        self.main_word = ""
        self.word_to_prime_number = {}
        self.hash_to_anagram = {}
        self.dictionary = dictionary
        self.build_hash_for_anagram()

    def build_hash_for_anagram(self):
        for word in self.dictionary:
            word_hash = self.calculate_hash_for_word(word)
            anagrams_for_word = self.hash_to_anagram.get(word_hash, [])
            if word not in anagrams_for_word:
                anagrams_for_word.append(word)
                self.hash_to_anagram[word_hash] = anagrams_for_word

    def calculate_hash_for_word(self, word):
        word_hash = 1
        for letter in word:
            prime_for_letter = self.word_to_prime_number.get(letter)
            if prime_for_letter is None:
                prime_for_letter = self.prime_number_finder.find_next_prime_number()
                self.word_to_prime_number[letter] = prime_for_letter
            word_hash *= prime_for_letter
        return word_hash

    def make_anagrams_for_word(self, word):
        hash_word = self.calculate_hash_for_word(word)
        all_anagrams = self.hash_to_anagram.get(hash_word, [])
        anagrams_for_word = all_anagrams.copy()
        word_index = all_anagrams.index(word) if word in self.dictionary else None
        if word_index is not None:
            del anagrams_for_word[word_index]
        return anagrams_for_word

    def __str__(self):
        return "4-perfect hashed database"


class Main:
    def __init__(self):
        self.db = {}
        self.build_database()
        print("building unindexed database:")
        tun = time()
        self.unindexed_db = UnindexedDatabase(self.db)
        print("time spent to build unindexed db:", time() - tun)

        print("building indexed database:")
        tin = time()
        self.indexed_db = IndexedDatabase(self.db)
        # self.indexed_db = []
        print("time spent to build indexed db:", time() - tin)

        print("building hashed database:")
        tha = time()
        self.hashed_db = HashedDatabase(self.db)
        print("time spent to build hashed db:", time() - tha)

        self.anagram_builder = AnagramBuilder(self.unindexed_db)

        tph = time()
        self.perfect_anagram_builder = PerfectHashedAnagramBuilder(self.db)
        print("time spent to build pefrect hashed db:", time() - tph)

        self.main_anagram_builder = self.anagram_builder

    def build_database(self):
        database = codecs.open('db/database', encoding='utf-8')
        database_in_str = database.read()
        dictionary_list = database_in_str.split('\r\n')
        dictionary_list.remove('')
        self.db = dictionary_list

    def run(self):
        while True:
            current_db_name = str(self.anagram_builder.dictionary) \
                if self.main_anagram_builder is self.anagram_builder \
                else str(self.main_anagram_builder)
            print("please insert your input:\ncurrent db is: ", current_db_name)
            print("if you want to change the database, "
                  "press 1 for un indexed db, press 2 for indexed db, "
                  "press 3 for hashed db & "
                  "press 4 for perfect hashed db")
            input_word = input()
            print("you entered", input_word)
            if input_word == '1':
                self.anagram_builder.dictionary = self.unindexed_db
                self.main_anagram_builder = self.anagram_builder
            elif input_word == '2':
                self.anagram_builder.dictionary = self.indexed_db
                self.main_anagram_builder = self.anagram_builder
            elif input_word == '3':
                self.anagram_builder.dictionary = self.hashed_db
                self.main_anagram_builder = self.anagram_builder
            elif input_word == '4':
                self.main_anagram_builder = self.perfect_anagram_builder
            else:
                tan = time()
                anagrams = self.main_anagram_builder.make_anagrams_for_word(input_word)
                time_spent = time() - tan
                if len(anagrams) == 0:
                    print("there is no anagram for your input")
                else:
                    for index in range(len(anagrams)):
                        anagram = anagrams[index]
                        print("anagram number %s:" % (index + 1), anagram)
                print("time spent to find anagrams:", time_spent)
            print("\n\n")

# t0 = time()
# database = codecs.open('db/database', encoding='utf-8')
# database_in_str = database.read()
# dictionary_list = database_in_str.split('\r\n')
# dictionary_list.remove('')
# print(time() - t0)
#
# t = time()
# a = IndexedDatabase()
# print(time() - t)
# t11 = time()
# m = {}
# for x in dictionary_list:
#     m[x] = True
# print(time() - t11)
# print("build done\n\n\n")
#
# t3 = time()
# c = ["آرمان" in dictionary_list for i in range(1000)]
# print(time()-t3)
#
# t2 = time()
# b = [a.word_exist_in_db("آرمان") for i in range(10000000)]
# print(time() - t2)
#
# t4 = time()
# e = [m.get("آرمان", False) for i in range(10000000)]
# print(time() - t4)
# print(c)
if __name__ == "__main__":
    main = Main()
    main.run()
