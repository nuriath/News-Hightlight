import unittest
from models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("Romain Dillet","Coinbase users can now withdraw Bitcoin SV following BCH fork",
         "https://techcrunch.com/wp-content/uploads/2017/08/bitcoin-split-2017a.jpg?w=711",
         "2019-02-15T14:53:40Z","If youre a Coinbase user, you may have seen some new tokens on your account. The Bitcoin Cash chain split into two different chains back in November. It means that if you held Bitcoin Cash on November 15, you became the lucky owner of Bitcoin SV and Bitcoin A… [+1514 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()