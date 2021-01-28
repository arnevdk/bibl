import unittest

from bibl.lint import lint


class TestBase(unittest.TestCase):

    def test_all_pass(self):
        result = lint("test_data/all_pass.bib", verbose=False)
        self.assertEqual([], result)

    def test_jabref(self):
        lint("test_data/jabref_bci.bib", verbose=True)
        # TODO

    def test_mit(self):
        lint("test_data/mit.bib", verbose=True)
        # TODO

    def test_incorrect_syntax(self):
        lint("test_data/syntax.bib", verbose=False)
        # TODO


if __name__ == '__main__':
    unittest.main()
