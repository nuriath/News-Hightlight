import unittest
from models import source
Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("buzzfeed","Buzzfeed","BuzzFeed is a cross-platform, global network for news and entertainment that generates seven billion views each month.",
        '"https://www.buzzfeed.com',"entertainment","en","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))


if __name__ == '__main__':
    unittest.main()