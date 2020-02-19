import unittest


class TestApiMethods(unittest.TestCase):

    def test_import(self):
        from archive import ArchiveApi


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApiMethods)
    unittest.TextTestRunner(verbosity=3).run(suite)