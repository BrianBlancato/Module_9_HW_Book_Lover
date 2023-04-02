import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        b1 = BookLover('Bob', 'bob@email.com', 'Fiction')
        b1.add_book("The Return of The King", 5)
        self.assertTrue(b1.has_read("The Return of The King"), "Book was not added")
    
    def test_2_add_book(self):
        b2 = BookLover('Bob', 'bob@email.com', 'Fiction')
        b2.add_book("The Two Towers", 5)
        b2.add_book("The Two Towers", 5)
        self.assertEqual(len(b2.book_list[b2.book_list.book_name == "The Two Towers"]), 1)
    
    def test_3_has_read(self):
        b3 = BookLover('Bob', 'bob@email.com', 'Fiction')
        b3.add_book("The Fellowship of The Ring", 5)
        self.assertTrue(b3.has_read("The Fellowship of The Ring"))

    def test_4_has_read(self):
        b4 = BookLover('Bob', 'bob@email.com', 'Fiction')
        b4.add_book("The Return of The King", 5)
        self.assertFalse(b4.has_read("The Two Towers"))

    def test_5_num_books_read(self):
        b5 = BookLover('Bob', 'bob@email.com', 'Fiction')
        b5.add_book("The Fellowship of The Ring", 5)
        b5.add_book("The Two Towers", 5)
        b5.add_book("The Return of The King", 5)
        self.assertEqual(b5.num_books_read(), 3)

    def test_6_fav_books(self):
        b6 = BookLover('Bob', 'bob@email.com', 'Fiction')
        b6.add_book("The Fellowship of The Ring", 5)
        b6.add_book("The Two Towers", 5)
        b6.add_book("The Return of The King", 5)
        b6.add_book("Harry Potter", 2)
        b6.add_book("The Winds of Winter", 1)
        b6.add_book("Generic Star Wars Book Title", 1)
        fav_book_test = b6.fav_books()
        fav_book_test_ratings = fav_book_test['book_rating']
        self.assertTrue((fav_book_test_ratings > 3).all())
    
if __name__ == '__main__':
    unittest.main(verbosity=3)

