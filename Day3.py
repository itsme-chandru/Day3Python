import sys
import random
import re
import logging

logging.basicConfig(filename="test.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=1)


class Day3Parent:
    outputFileName = "output#"
    output_num = random.randrange(1, 1000)
    outputFileName = outputFileName.replace("#", str(output_num))
    list_words = []

    def __init__(self, f_name):
        logging.info("Parent class constructor is called")
        self.f_name = f_name

    def readfile(self):
        logging.info("The readfile function starts and the data is read")
        self.content=self.f_name.read()
        self.list_words=self.content.split()
        return self.list_words
    def Writefile(self, print_items):
        self.print_items = print_items
        with open(self.outputFileName + ".txt", mode="a") as op:
            op.write(str(print_items))
            op.close()


class operations(Day3Parent):
    list_words = []
    prefix_lst = []
    suffix_lst = []
    palindrome_lst = []
    vowels_split = []
    semicolon_list = []
    myDict = {}
    new_string = ""
    most_repeated = ""

    def __init__(self, f_name):
        logging.info("The child class constructor is called")
        super().__init__(f_name)
        self.list_words=super().readfile()

    def prefix(self, word):

        if (word.startswith("To") or word.startswith("to")):
            self.prefix_lst.append(word)

    def suffix(self, word):

        if (word.endswith("ing")):
            self.suffix_lst.append(word)

    def most_repeated_word(self):

        self.most_repeated = max(set(self.list_words), key=self.list_words.count)

    def palindrome(self, word):

        if (word == word[::-1] and len(word) != 1):
            self.palindrome_lst.append(word)

    def splitvowels(self, word):

        words_split = re.split("a|e|i|o|u", word)  # splitting words based on vowels
        self.vowels_split.append(words_split)

    def capitalize3rdletter(self, word):

        self.capitalize = self.list_words[:]
        if (len(word) >= 3):
            word1 = word[:2] + word[2].upper() + word[3:]
            self.capitalize[self.capitalize.index(word)] = word1

    def Cap_5th_word(self):

        self.new_list = self.list_words[:]
        self.new_list[4] = self.new_list[4].upper()

    def uniquewords(self):

        self.list_words_new = set(self.list_words)
        self.list_words_new = list(self.list_words_new)

    def makedict(self):
        self.myDict = dict(zip(range(len(self.list_words)), self.list_words))

    def replace(self, ):
        self.new_string = self.content.replace(" ", "-")
        self.new_string = self.new_string.replace("\n", ";")

    def doOperations(self):
        try:
            logging.info("Starting the Do operations class ")
            for word in self.list_words:
                self.prefix(word)
                self.suffix(word)
                self.palindrome(word)
                self.splitvowels(word)
                self.capitalize3rdletter(word)
                self.Cap_5th_word()
                self.uniquewords()
                self.makedict()
                self.most_repeated_word()
                self.replace()
            logging.info("All the Operations are done successfully")
        except Exception as err:
            logging.error("An error has occurred",err)
    def print_list(self):
        try:
            logging.info("Starting the print_list class ")
            print("The words that has the prefix to/To is ", self.prefix_lst)
            print("The words that has the suffix  ing is ", self.suffix_lst)
            print("The palindrome in the file are ", self.palindrome_lst)
            print("The most repeated word in the file is", self.most_repeated)
            print("The unique words in the file is", self.list_words_new)
            print("The dictionary with index as key and word in the file as value ", self.myDict)
            logging.info("Print list class is Finished")
        except Exception as err:
            logging.error("An error has occurred",err)

    def write_to_list(self):
        try:
            logging.info("Starting the Write to list class ")
            super().Writefile("split the words based on vowels \n" + str(self.vowels_split) + "\n")
            super().Writefile("\n Capitalize every 3rd letter in the words \n" + str(self.capitalize) + "\n")
            super().Writefile("\n Capitalize the 5th word in the file \n" + str(self.new_list) + "\n")
            super().Writefile("\n Replacing the space with - and new line with ; \n" + self.new_string + "\n")
            logging.info("Writing to the file is finished")
        except Exception as err:
            logging.error("An error has occurred",err)

try:
    f_name = sys.argv[1]
    logging.info("The file is taken as a input argument")
    with open(f_name, mode="r") as f:
        logging.info("The Class object is created")
        classobj = operations(f)
        classobj.doOperations()
        classobj.print_list()
        classobj.write_to_list()
        f.close()
    logging.info("The program is finished")
except Exception as err:
    logging.error("There is a error",err)
