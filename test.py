from subscripts.parseFile import fileParser
from subscripts.userStories.UserStoriesVD import us01, us10, us15, us16
from subscripts.userStories.UserStoriesDP import us03, us08, us06, us04
from subscripts.userStories.UserStoriesSS import us02, us09, us12, us11
from subscripts.userStories.UserStoriesYD import us05, us18, us20

import unittest


class TestCases(unittest.TestCase):
    gedcom_error = "../sprint_02.ged"
    d = fileParser(gedcom_error)

    def test_us01(self):
        f = open("test.txt", "w+")
        value = us01(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us02(self):
        f = open("test.txt", "a")
        value = us02(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us03(self):
        f = open("test.txt", "a")
        value = us03(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us04(self):
        f = open("test.txt", "a")
        value = us04(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us05(self):
        f = open("test.txt", "a")
        value = us05(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us06(self):
        f = open("test.txt", "a")
        value = us06(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)


    def test_us08(self):
        f = open("test.txt", "a")
        value = us08(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us09(self):
        f = open("test.txt", "a")
        value = us09(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us10(self):
        f = open("test.txt", "a")
        value = us10(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us11(self):
        f = open("test.txt", "a")
        value = us11(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us12(self):
        f = open("test.txt", "a")
        value = us12(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us15(self):
        f = open("test.txt", "a")
        value = us15(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us16(self):
        f = open("test.txt", "a")
        value = us16(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)


    def test_us18(self):
        f = open("test.txt", "a")
        value = us18(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us20(self):
        f = open("test.txt", "a")
        value = us20(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)