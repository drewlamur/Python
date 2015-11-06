import unittest
import pdb

class MusicianToGenre(object):
    
    def __init__(self, artist):
      self.musician  = artist
      self.genre_map = { "Kenny Rogers": "Country",  "Biggie Smalls": "Rap", "Yanni": "Instrumental", "Alex Lifeson": "Rock", "Chuck Garvey": "Greatness" }
      self.order_map = { "Kenny Rogers": 5,  "Biggie Smalls": 4, "Yanni": 3, "Alex Lifeson": 2, "Chuck Garvey": 1 }

    def is_type(self, arg, type):
      return isinstance(arg, type)

class MusicianToGenreTest(unittest.TestCase):

    def test_kenny_mappings(self):
      artist = MusicianToGenre("Kenny Rogers")
      self.assertEquals(artist.genre_map[artist.musician], "Country")
      self.assertTrue(artist.is_type(artist.genre_map[artist.musician], basestring))
      self.assertTrue(artist.is_type(artist.order_map[artist.musician], int))

    def test_biggie_mappings(self):
      artist = MusicianToGenre("Biggie Smalls")
      self.assertEquals(artist.genre_map[artist.musician], "Rap")
      self.assertTrue(artist.is_type(artist.genre_map[artist.musician], basestring))
      self.assertTrue(artist.is_type(artist.order_map[artist.musician], int))

    def test_yanni_mappings(self):
      artist = MusicianToGenre("Yanni")
      self.assertEquals(artist.genre_map[artist.musician], "Instrumental")
      self.assertTrue(artist.is_type(artist.genre_map[artist.musician], basestring))
      self.assertTrue(artist.is_type(artist.order_map[artist.musician], int))

    def test_alex_mappings(self):
      artist = MusicianToGenre("Alex Lifeson")
      self.assertEquals(artist.genre_map[artist.musician], "Rock")
      self.assertTrue(artist.is_type(artist.genre_map[artist.musician], basestring))
      self.assertTrue(artist.is_type(artist.order_map[artist.musician], int))

    def test_chuck_mappings(self):
      artist = MusicianToGenre("Chuck Garvey")
      self.assertEquals(artist.genre_map[artist.musician], "Greatness")
      self.assertTrue(artist.is_type(artist.genre_map[artist.musician], basestring))
      self.assertTrue(artist.is_type(artist.order_map[artist.musician], int))  
      
if __name__ == "__main__":
    unittest.main() 