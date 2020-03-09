import unittest

# coordinates and search radius of Andromeda galaxy, converted to decimal degrees
andromeda = {
    "ra"     : (00 + 42./60 + 44.330/3600) * 360/24,
    "dec"    : (41 + 16./60 + 7.50/3600),
    "radius" : 0.1
}
# some image (first image returned from the search above)
andromeda_image_id = 13822

alphaCenA = {
    "ra"     : (14 + 39./60 + 29.83/3600) * 360/24,
    "dec"    : (-60 + 48./60 + 58.2/3600),
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


    def test_credentials1(self):
        """
        Test credentials in credentials.py
        """
        from bayfordbury import ArchiveApi
        from credentials import api_key, observer_id
        api = ArchiveApi(api_key=api_key, observer_id=observer_id)
        search_results = api.search(**andromeda)
        self.assertIsInstance(search_results, list)


    def test_credentials2(self):
        """
        Test exceptions returned by the server and raised by ArchiveApi
        """
        from bayfordbury import ArchiveApi
        api = ArchiveApi(api_key="somekey", observer_id=1234567) # random values, must be wrong
        self.assertRaises(PermissionError, lambda: api.search(**andromeda))


    def test_search1(self):
        """
        Test ArchiveApi.search() by searching Southern hemisphere.
        """
        from bayfordbury import ArchiveApi
        from credentials import api_key, observer_id
        api = ArchiveApi(api_key=api_key, observer_id=observer_id)
        search_results = api.search(**alphaCenA)
        self.assertEqual(len(search_results), 0, "Search of Southern hemisphere did not return an empty list.")


    def test_search2(self):
        """
        Test ArchiveApi.search() by searching Andromeda images.
        """
        from bayfordbury import ArchiveApi
        from credentials import api_key, observer_id
        andromeda_images = ArchiveApi(api_key=api_key, observer_id=observer_id).search(**andromeda)
        self.assertGreater(len(andromeda_images), 0, "Didn't find any Andromeda images")


    def test_download1(self):
        """
        Test ArchiveApi.search() by searching Andromeda images.
        """
        from bayfordbury import ArchiveApi
        from credentials import api_key, observer_id
        from astropy.io import fits
        with ArchiveApi(api_key=api_key, observer_id=observer_id).download(andromeda_image_id) as andromeda_image:
            self.assertIsInstance(andromeda_image, fits.hdu.hdulist.HDUList)


    def test_download2(self):
        """
        Test ArchiveApi.search() by searching Andromeda images.
        """
        from bayfordbury import ArchiveApi
        from credentials import api_key, observer_id
        from astropy.io import fits
        api = ArchiveApi(api_key=api_key, observer_id=observer_id)
        self.assertRaises(FileNotFoundError, lambda: api.download(-45))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApi)
    unittest.TextTestRunner(verbosity=3).run(suite)