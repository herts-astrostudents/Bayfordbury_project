import unittest


class TestFilterMethods(unittest.TestCase):

    def test_import(self):
        from bayfordbury import Filter


    def test_colours_correct(self):
        from bayfordbury import Filter
        testnames = [
            "red",      "Red",   "R", "r ",
            "green",    "Green", "G", "V", "v", "g",
            "blue",     "Blue",  "B", " b",
            "Infrared", "IR",    "I", "   i  "
        ]
        for testname in testnames:
            self.assertTrue(Filter.is_allowed(testname), "'{}' did not work.".format(testname))


    def test_colours_wrong(self):
        from bayfordbury import Filter
        for testname in ["f", "-", "Infrareeeeed", "somefilter"]:
            self.assertFalse(Filter.is_allowed(testname), "'{}' should not have worked.".format(testname))


    def test_narrow_correct(self):
        from bayfordbury import Filter
        testnames = [
            "S-II",    "s ii",    "sii",
            "O-III",   "o iii",   "oiii",
            "H-alpha", "h alpha", "halpha",
            "465nm",   "465 nm"
        ]
        for testname in testnames:
            self.assertTrue(Filter.is_allowed(testname), "'{}' did not work.".format(testname))


    def test_narrow_wrong(self):
        from bayfordbury import Filter
        for testname in ["O II", "S iii", "Ha", "otherfilter"]:
            self.assertFalse(Filter.is_allowed(testname), "'{}' should not have worked.".format(testname))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFilterMethods)
    unittest.TextTestRunner(verbosity=3).run(suite)
