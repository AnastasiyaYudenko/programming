import re
import numpy as np
import nltk
import os.path
import unittest



class Klas:
    def __init__(self, filename):
        self.__df = {}
        self.__idf = {}
        self.__dict_tf = {}
        self.user_text = ''
        try:
            self.text = open(filename, 'r').read().split('\n')
            self.docs = []
            for document in self.text:
                doc = re.sub('[^a-zA-Zа-яА-Я0-9]', ' ', document)
                self.docs.append(nltk.word_tokenize(doc))

        except OSError as err:
            print("OS error: {0}".format(err))
            raise err

        self.__idf_file()

    def __calculate_idf(self):
        df_dict = {}
        idf_dict = {}
        for docs in self.docs:
            for doc in docs:
                tokens = list(set(nltk.word_tokenize(doc)))

                for token in tokens:
                    if token not in list(df_dict.keys()):
                        df_dict[token] = 1
                    else:
                        df_dict[token] += 1
                    idf = np.log(1 + (len(self.docs) / (df_dict[token] + 1)))
                    idf_dict[token] = idf

        self.__df = df_dict
        self.__idf = idf_dict

    def __idf_file(self):
        if os.path.isfile('text_idf.txt'):
            with open('text_idf.txt', 'r') as file:
                lines = file.read().split('\n')
                for line in lines:
                    if line:
                        word, idf = line.split(':')
                        self.__idf[word] = float(idf)
        else:
            with open('text_idf.txt', 'w') as file:
                self.__calculate_idf()
                for word, idf in self.__idf.items():
                    file.write(word + ':' + str(idf) + '\n')

    def __tf(self):
        doc = re.sub('[^a-zA-Zа-яА-Я0-9]', ' ', self.user_text)
        tokens = nltk.word_tokenize(doc)
        all = len(tokens)
        slovar = {}
        for token in tokens:
            if token not in list(slovar.keys()):
                slovar[token] = 1
            else:
                slovar[token] += 1
        for tf_token in list(slovar.keys()):
            freq = slovar[tf_token]
            self.__dict_tf[tf_token] = freq / all

    def tf_idf(self, text):
        self.user_text = text
        doc = re.sub('[^a-zA-Zа-яА-Я0-9]', ' ', self.user_text)
        tokenized = nltk.word_tokenize(doc)
        self.__tf()
        result = {}
        for token in tokenized:
            try:
                tf = self.__dict_tf[token]
                idf = self.__idf[token]
                tf_idf = tf * idf
                result[token] = tf_idf
                if token == 'a':
                    print(tf, idf, self.__df[token], len(self.text))
            except KeyError:
                result[token] = 0

        return list(result.items())


klas = Klas('text11.txt')
text = input('your text: ')
result = klas.tf_idf(text)
print(result)


class Tests(unittest.TestCase):

    def test_tf_idf(self):
        a = klas.tf_idf('There are many good theatres in Great Britain.')
        b = [('There', 0.10943359216923748), ('are', 0.05744154117230503), ('many', 0.15049660054074201),
             ('good', 0.15049660054074201), ('theatres', 0.10943359216923748), ('in', 0.047874031532013236),
             ('Great', 0.18800967459703427), ('Britain', 0.12645011395980998)]
        self.assertEqual(a, b)

    def test_tf_idf2(self):
        a = klas.tf_idf('dve nedeli nado mnogo mnogo progat')
        b = [('dve', 0), ('nedeli', 0), ('nado', 0), ('mnogo', 0), ('progat', 0)]
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()