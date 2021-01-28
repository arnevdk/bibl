import unittest
from bibl.config import set_config
from bibl.lint import lint

class TestFieldRules(unittest.TestCase):

    def test_M00_pass(self):
        set_config('select', ['M00'])
        result = lint('test_data/pass_all.bib', verbose=False)
        self.assertEqual([], result)

    def test_M00_fail(self):
        set_config('select', ['M00'])
        result = lint('test_data/rules/M00_fail.bib', verbose=False)
        self.assertEqual(1, len(result))

    def test_M01_pass(self):
        set_config('select', ['M01*'])
        result = lint('test_data/pass_all.bib', verbose=True)
        self.assertEqual([], result)

    def test_M01_fail(self):
        set_config('select', ['M01*'])


if __name__ == '__main__':
    unittest.main()