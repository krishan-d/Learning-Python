import unittest
import cap


class TestCap(unittest.TestCase):

    def text_one_word(self):
        text = 'hi'
        res = cap.cap_text(text)
        self.assertEqual(res, 'Hi')

    def test_multiple_words(self):
        text = 'hi there!'
        res = cap.cap_text(text)
        self.assertEqual(res, 'Hi There!')


if __name__ == '__main__':
    unittest.main()
