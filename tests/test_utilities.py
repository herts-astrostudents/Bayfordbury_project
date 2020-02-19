import unittest


class TestFilterMethods(unittest.TestCase):

    def test_import(self):
        from utilities import Filter


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFilterMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)