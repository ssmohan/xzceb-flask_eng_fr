import unittest 
from translator import english_to_french, french_to_english

class TestEngToFr(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('hello'), 'Bonjour')
        self.assertEqual(english_to_french('thanks'), 'Merci' )
        self.assertNotEqual(english_to_french('thanks'), 'thanks')
        self.assertEqual(english_to_french(' '), ' ')

class TestFrToEng(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('bonjour'), 'Hello')
        self.assertEqual(french_to_english('Merci'), 'Thank you')
        self.assertNotEqual(french_to_english('Merci'), 'Merci')
        self.assertEqual(french_to_english(' '), ' ')
        
unittest.main()