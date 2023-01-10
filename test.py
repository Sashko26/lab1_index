import unittest

import forwarded_index
import inverted_index

valid_data = {'to': ['C:\\Users\\DELL\\Desktop\\ISS_Lab1-main\\lab1\\data/doc1.txt',
                      'C:\\Users\\DELL\\Desktop\\ISS_Lab1-main\\lab1\\data/doc2.txt',
                      'C:\\Users\\DELL\\Desktop\\ISS_Lab1-main\\lab1\\data/doc3.txt']}


class TestToolset(unittest.TestCase):

    def test_forwarded_index(self):
        db = forwarded_index.Storage()
        index = forwarded_index.ForwardIndex(db)
        forwarded_index.index_file(index)

        search_term = 'to'
        expected = valid_data

        self.assertEqual(index.lookup_query(search_term), expected)

    def test_cap_text_forward(self):
        db = forwarded_index.Storage()
        index = forwarded_index.ForwardIndex(db)
        forwarded_index.index_file(index)

        search_term = 'TO'
        expected = valid_data

        self.assertEqual(index.lookup_query(search_term), expected)

    def test_spaced_text_forward(self):
        db = forwarded_index.Storage()
        index = forwarded_index.ForwardIndex(db)
        forwarded_index.index_file(index)

        search_term = ' to . '
        expected = valid_data
        print(index.lookup_query(search_term))
        self.assertEqual(index.lookup_query(search_term), expected)

    def test_unfounded_text_forward(self):
        db = forwarded_index.Storage()
        index = forwarded_index.ForwardIndex(db)
        forwarded_index.index_file(index)

        search_term = 'mood'
        expected = "\033[1;32;40m mood not found \033[0;0m"

        self.assertEqual(index.lookup_query(search_term), expected)

    def test_unfounded_cap_text_forward(self):
        db = forwarded_index.Storage()
        index = forwarded_index.ForwardIndex(db)
        forwarded_index.index_file(index)

        search_term = 'MOOD'
        expected = "\033[1;32;40m MOOD not found \033[0;0m"

        self.assertEqual(index.lookup_query(search_term), expected)

    def test_unfounded_spaced_text_forward(self):
        db = forwarded_index.Storage()
        index = forwarded_index.ForwardIndex(db)
        forwarded_index.index_file(index)

        search_term = ' mood . '
        expected = "\033[1;32;40m  mood .  not found \033[0;0m"

        self.assertEqual(index.lookup_query(search_term), expected)

    def test_inverted_index(self):
        db = inverted_index.Storage()
        index = inverted_index.InvertedIndex(db)
        forwarded_index.index_file(index)
        search_term = 'to'
        expected = valid_data
        print(expected)
        print(index.lookup_query(search_term))
        self.assertEqual(index.lookup_query(search_term), expected)

    def test_cap_text_invert(self):
        db = inverted_index.Storage()
        index = inverted_index.InvertedIndex(db)
        inverted_index.index_file(index)

        search_term = 'TO'
        expected = valid_data

        self.assertEqual(index.lookup_query(search_term), expected)

    def test_spaced_text_invert(self):
        db = inverted_index.Storage()
        index = inverted_index.InvertedIndex(db)
        inverted_index.index_file(index)

        search_term = ' To . '
        expected = valid_data

        self.assertEqual(index.lookup_query(search_term), expected)

    def test_unfounded_inverted_index(self):
        db = inverted_index.Storage()
        index = inverted_index.InvertedIndex(db)
        forwarded_index.index_file(index)

        search_term = 'mood'
        expected = "\033[1;32;40m mood not found \033[0;0m"

        self.assertEqual(index.lookup_query(search_term), expected)

    def test_unfounded_cap_text_invert(self):
        db = inverted_index.Storage()
        index = inverted_index.InvertedIndex(db)
        forwarded_index.index_file(index)

        search_term = 'MOOD'
        expected = "\033[1;32;40m MOOD not found \033[0;0m"

        self.assertEqual(index.lookup_query(search_term), expected)

    def test_unfounded_spaced_text_invert(self):
        db = inverted_index.Storage()
        index = inverted_index.InvertedIndex(db)
        forwarded_index.index_file(index)

        search_term = ' mood . '
        expected = "\033[1;32;40m  mood .  not found \033[0;0m"

        self.assertEqual(index.lookup_query(search_term), expected)


if __name__ == '__main__':
    unittest.main()
