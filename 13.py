import xml.etree.ElementTree as etree
import unittest


class Corpus:

    def __init__(self):
        self._sentences = []
        self._sents_text = []

    def load(self, path_to_corpus: str):
        try:
            tree = etree.parse(path_to_corpus)
            root = tree.getroot()
            for sentence in root.iter('sentence'):
                self._sentences.append(Sentence(sentence))
                for sent in sentence.iter('source'):
                    self._sents_text.append(sent.text)

        except OSError as err:
            print("OS error: {0}".format(err))

    def show_sentence(self, number: int):
        try:
            return self._sentences[number]
        except TypeError:
            try:
                return self._sentences[int(number)]
            except TypeError as err:
                print('введи число, которое int')
                raise err
        except IndexError as err:
            print('слишком большое число')
            raise err


class Sentence:

    def __init__(self, wordforms):
        self._wordforms = []
        self.sentence = ''
        for tokens in wordforms.iter('tokens'):
            for token in tokens.iter('token'):
                self._wordforms.append(Wordform(token))

        self.sentence = wordforms.find('source').text

    def show_wordform(self, number: int):
        try:
            return self._wordforms[number]
        except TypeError:
            try:
                return self._wordforms[int(number)]
            except TypeError as err:
                print('введи число, которое int')
                raise err

        except IndexError as err:
            print('слишком большое число')
            raise err


class Wordform:

    def __init__(self, token):
        self._wordform = token.get('text')
        self._grammems = []
        for g in token.iter('g'):
            self._grammems.extend(list(g.attrib.values()))

    def show_grammems(self):
        return self._grammems

    def show_i_gram(self, i):
        try:
            return self._grammems[i]
        except IndexError:
            return 'there is no grammem with this index('

