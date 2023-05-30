import unittest

class CorpusTest(unittest.TestCase):

    def test_grammems(self):
        corpus = Corpus()
        corpus.load('annot.opcorpora.no_ambig.xml')
        a = corpus.show_sentence(0).show_wordform(0).show_grammems()
        b = ['PNCT']
        self.assertEqual(a, b)

    def test_grammems2(self):
        corpus = Corpus()
        corpus.load('annot.opcorpora.no_ambig.xml')
        a = corpus.show_sentence(1).show_wordform(0).show_grammems()
        b = ['VERB', 'perf', 'intr', 'sing', '3per', 'futr', 'indc']
        self.assertEqual(a, b)

    def test_sentence(self):
        corpus = Corpus()
        corpus.load('annot.opcorpora.no_ambig.xml')
        a = corpus.show_sentence(0).sentence
        b = '«Школа злословия» учит прикусить язык'
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()