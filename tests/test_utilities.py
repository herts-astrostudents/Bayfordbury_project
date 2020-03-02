import unittest


class TestFilter(unittest.TestCase):

    def test_import(self):
        """
        basic import test
        """
        try:
            from bayfordbury import Filter
        except ImportError:
            self.fail("Failed to import Filter")


    def test_photometric(self):
        """
        test photometric filter names
        """
        from bayfordbury import Filter

        # correct names
        testnames = [
            "red",      "Red",   "R", "r ",
            "green",    "Green", "G", "V", "v", "g",
            "blue",     "Blue",  "B", " b",
            "Infrared", "IR",    "I", "   i  "
        ]
        for testname in testnames:
            self.assertTrue(Filter.is_allowed(testname), "'{}' did not work.".format(testname))

        # wrong names
        for testname in ["f", "-", "Infrareeeeed", "somefilter"]:
            self.assertFalse(Filter.is_allowed(testname), "'{}' should not have worked.".format(testname))


    def test_narrowband(self):
        """
        test narrowband filter names
        """
        from bayfordbury import Filter

        # correct names
        testnames = [
            "S-II",    "s ii",    "sii",
            "O-III",   "o iii",   "oiii",
            "H-alpha", "h alpha", "halpha",
            "465nm",   "465 nm"
        ]
        for testname in testnames:
            self.assertTrue(Filter.is_allowed(testname), "'{}' did not work.".format(testname))

        # wrong names
        for testname in ["O II", "S iii", "Ha", "otherfilter"]:
            self.assertFalse(Filter.is_allowed(testname), "'{}' should not have worked.".format(testname))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFilter)
    unittest.TextTestRunner(verbosity=3).run(suite)
