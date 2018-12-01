from django.test import TestCase
import parser


class StubTestCase(TestCase):
    def test_stub(self):
        self.assertEqual(True, True)


class TestWordParser(TestCase):
    # Тестирование парсера на разбиение слов
    def test_parser_1(self):
        '''
        in:''
        out:[]
        '''
        test_word = ['']
        res_word = parser.parse_into_words('')
        self.assertListEqual(res_word, test_word)
    def test_parser_2(self):
        '''
        in:Петр семья.
        out:['Петр', 'семья']
        '''
        test_word = ['Петр', 'семья.']
        res_word = parser.parse_into_words('Петр семья.')
        self.assertListEqual(res_word, test_word)
    def test_parser_3(self):
        '''
        in:Петр! семья?
        out:['Петр!', 'семья?']
        '''
        test_word = ['Петр!', 'семья?']
        res_word = parser.parse_into_words('Петр! семья?')
        self.assertListEqual(res_word, test_word)
    def test_parser_4(self):
        '''
        in:Петр 1700 г.
        out:['Петр ', '1700 ', 'г.']
        '''
        test_word = ['Петр', '1700', 'г.']
        res_word = parser.parse_into_words('Петр 1700 г.')
        self.assertListEqual(res_word, test_word)


class TestSentencesParser(TestCase):
    # Тестирование парсера на разбиение предложений
    def test_parser_5(self):
        '''
        in:
        out:[['']]
        '''
        test_word = [['']]
        res_word = parser.parse_into_sentences([''])
        self.assertListEqual(res_word, test_word)
    def test_parser_6(self):
        '''
        in:['С', 'юных', 'лет', 'проявляя', 'интерес.', 'Пётр', 'был', 'первым.']
        out:[['С', 'юных', 'лет', 'проявляя', 'интерес'],
        ['Пётр', 'был', 'первым'], []]
        '''
        test_word = [['С', 'юных', 'лет', 'проявляя', 'интерес'],
                     ['Пётр', 'был', 'первым'], []]
        res_word = parser.parse_into_sentences(['С', 'юных', 'лет',
                                                'проявляя', 'интерес.',
                                                'Пётр', 'был', 'первым.'])
        self.assertListEqual(res_word, test_word)
    '''
    in:['С', 'юных', 'лет', ',', 'проявляя', 'интерес.',
    'Пётр', 'был', 'первым.']
    out:[['С', 'юных', 'лет', ',', 'проявляя', 'интерес'],
    ['Пётр', 'был', 'первым'], []]
    '''
    def test_parser_7(self):
        '''
        in:[['С', 'юных', 'лет', ',', 'проявляя', 'интерес'],
        ['Пётр', 'был', 'первым'], []]
        out:['С', 'юных', 'лет', ',','проявляя', 'интерес.',
        'Пётр', 'был', 'первым.']
        '''
        test_word = [['С', 'юных', 'лет', ',', 'проявляя', 'интерес'],
                     ['Пётр', 'был', 'первым'], []]
        res_word = parser.parse_into_sentences(['С', 'юных', 'лет', ',',
                                                'проявляя', 'интерес.',
                                                'Пётр', 'был', 'первым.'])
        self.assertListEqual(res_word, test_word)
