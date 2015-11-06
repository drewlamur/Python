import unittest
import pdb

class ArtistToGenre(object):
    
    def __init__(self, artist):
      self.artist = artist
      self.genre_map = { "Kenny Rogers": "Country",  "Biggie Smalls": "Rap", "Yanni": "Instrumental", "Alex Lifeson": "Rock", "Chuck Garvey": "Greatness" }
      self.order_map = { "Kenny Rogers": 5,  "Biggie Smalls": 4, "Yanni": 3, "Alex Lifeson": 2, "Chuck Garvey": 1 }

    def is_type(self, data, type):
      return isinstance(data, type)

class ArtistToGenreTest(unittest.TestCase):

    def test_kenny_mappings(self):
      object = ArtistToGenre("Kenny Rogers")
      self.assertEquals(object.genre_map[object.artist], "Country")
      self.assertTrue(object.is_type(object.genre_map[object.artist], basestring))
      self.assertEquals(object.order_map[object.artist], 5)
      self.assertTrue(object.is_type(object.order_map[object.artist], int))

    def test_biggie_mappings(self):
      object = ArtistToGenre("Biggie Smalls")
      self.assertEquals(object.genre_map[object.artist], "Rap")
      self.assertTrue(object.is_type(object.genre_map[object.artist], basestring))
      self.assertEquals(object.order_map[object.artist], 4)
      self.assertTrue(object.is_type(object.order_map[object.artist], int))

    def test_yanni_mappings(self):
      object = ArtistToGenre("Yanni")
      self.assertEquals(object.genre_map[object.artist], "Instrumental")
      self.assertTrue(object.is_type(object.genre_map[object.artist], basestring))
      self.assertEquals(object.order_map[object.artist], 3)
      self.assertTrue(object.is_type(object.order_map[object.artist], int))

    def test_alex_mappings(self):
      object = ArtistToGenre("Alex Lifeson")
      self.assertEquals(object.genre_map[object.artist], "Rock")
      self.assertTrue(object.is_type(object.genre_map[object.artist], basestring))
      self.assertEquals(object.order_map[object.artist], 2)
      self.assertTrue(object.is_type(object.order_map[object.artist], int))

    def test_chuck_mappings(self):
      object = ArtistToGenre("Chuck Garvey")
      self.assertEquals(object.genre_map[object.artist], "Greatness")
      self.assertTrue(object.is_type(object.genre_map[object.artist], basestring))
      self.assertEquals(object.order_map[object.artist], 1)
      self.assertTrue(object.is_type(object.order_map[object.artist], int)) 
      
if __name__ == "__main__":
    unittest.main() 