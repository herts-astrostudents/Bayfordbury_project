import unittest

# coordinates and search radius of Andromeda galaxy, converted to decimal degrees
andromeda = {
    "ra"     : (00 + 42./60 + 44.330/3600) * 360/24,
    "dec"    : (41 + 16./60 + 7.50/3600),
    "radius" : 0.1
}

class TestApi(unittest.TestCase):

    def test_import(self):
        """
        Test the API class and credentials file import 
        """
        try:
            from bayfordbury import ArchiveApi
        except ImportError:
            self.fail("Failed to import ArchiveApi")
        try:
            from credentials import api_key, observer_id
        except ImportError:
            self.fail("Failed to import credentials")


    def test_exceptions(self):
        """
        Test exceptions returned by the server and raised by ArchiveApi
        """
        from bayfordbury import ArchiveApi
        from credentials import api_key, observer_id
        api = ArchiveApi(api_key="somekey", observer_id=1234567) # random values, must be wrong
        self.assertRaises(PermissionError, lambda: api.search(**andromeda))


    def test_search(self):
        """
        Test ArchiveApi.search() by searching Andromeda images.
        """
        from bayfordbury import ArchiveApi
        from credentials import api_key, observer_id
        andromeda_images = ArchiveApi(api_key=api_key, observer_id=observer_id).search(**andromeda)
        self.assertGreater(len(andromeda_images), 0, "Didn't find any Andromeda images")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApi)
    unittest.TextTestRunner(verbosity=3).run(suite)