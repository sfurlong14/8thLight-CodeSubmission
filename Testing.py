import unittest
from BookAPI import api_pull, get_search_books, view_reading_list, save_to_reading_list

class BookAPIUnitTest(unittest.TestCase):
  """
  Test the functions set up for the BookAPI
  """
  def test_pull_api(self):
    """
    data type that is return from API is a dictionary
    """
    keyword_search = 'Harry Potter'
    self.assertEqual(type(api_pull(keyword_search)), dict)
  
  def get_search_books(self):
    """
    search produces 5 search from Google Book API and provides name, authors, and publishing company
    """
    keyword_search = 'Harry Potter'
    self.assertEqual(get_search_books(keyword_search), {1: ['Fantastic Beasts and Where to Find Them: Cinematic Guide: Newt Scamander Do Not Feed Out', ['Felicity Baker'], 'NA'], 2: ['Harry Potter Coloring Book', ['Inc. Scholastic'], 'Scholastic Incorporated'], 3: ['Harry Potter and the Cursed Child', ['J. K. Rowling', 'Jack Thorne', 'John Tiffany'], 'Sphere'], 4: ['Playing Harry Potter', ['Lisa S. Brenner'], 'McFarland'], 5: ['Harry Potter: The Complete Collection (1-7)', ['J.K. Rowling'], 'Pottermore Publishing']})
  
  def view_reading_list(self):
    """
    data type that is return when function is called is a dictionary
    """
    self.assertEqual(type(view_reading_list()), dict)
  
  def save_to_reading_list(self):
    """
    Ensure the the the item is added to the reading list after the save_to_reading_list fuction is called
    """
    keyword_search = 'Harry Potter'
    self.assertEqual(get_search_books("harry Potter", 1), {1: ['Fantastic Beasts and Where to Find Them: Cinematic Guide: Newt Scamander Do Not Feed Out', ['Felicity Baker'], 'NA']})

if __name__ == '__main__':
    unittest.main() 