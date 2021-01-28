import unittest
from bibl.config import set_config
from bibl.lint import lint

class TestDatabaseRules(unittest.TestCase):

    def test_D00_pass(self):
        set_config('select', ['D00'])
        result = lint('test_data/all_pass.bib', verbose=False)
        self.assertEqual([], result)

    def test_D00_fail(self):
        set_config('select', ['D00'])
        result = lint('test_data/rules/D00_fail.bib', verbose=False)
        self.assertEqual(1,len(result))

    def test_D01_pass(self):
        set_config('select', ['D01'])
        result = lint('test_data/all_pass.bib', verbose=False)
        self.assertEqual([], result)

    def test_D01_fail(self):
        set_config('select', ['D01'])
        result = lint('test_data/rules/D01_fail.bib', verbose=False)
        self.assertEqual(1,len(result))

    def test_D02_pass(self):
        set_config('select', ['D02'])
        result = lint('test_data/all_pass.bib', verbose=False)
        self.assertEqual([], result)

    def test_D02_fail(self):
        set_config('select', ['D02'])
        result = lint('test_data/rules/D02_fail.bib', verbose=False)
        self.assertEqual(1,len(result))



if __name__ == '__main__':
    unittest.main()