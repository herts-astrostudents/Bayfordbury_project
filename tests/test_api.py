import unittest


class TestApiMethods(unittest.TestCase):

    def test_import(self):
        from bayfordbury import ArchiveApi

    def test_search(self):
        raise NotImplementedError

    def test_download(self):
        raise NotImplementedError


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApiMethods)
    unittest.TextTestRunner(verbosity=3).run(suite)