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
        for source in wordforms.iter('source'):
            self.sentence = source.text

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


corpus = Corpus()
corpus.load('annot.opcorpora.no_ambig.xml')
i_sent = corpus.show_sentence(5)
print(i_sent.sentence)
i_word = i_sent.show_wordform('1')
i_gram = i_word.show_grammems()
print(i_gram)


class Tests(unittest.TestCase):

    def test_grammems(self):
        a = corpus.show_sentence(0).show_wordform(0).show_grammems()
        b = ['PNCT']
        self.assertEqual(a, b)

    def test_grammems2(self):
        a = corpus.show_sentence(1).show_wordform(0).show_grammems()
        b = ['VERB', 'perf', 'intr', 'sing', '3per', 'futr', 'indc']
        self.assertEqual(a, b)

    def test_sentence(self):
        a = corpus.show_sentence(0).sentence
        b = '«Школа злословия» учит прикусить язык'
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()