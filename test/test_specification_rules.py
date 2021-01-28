import unittest
from bibl.config import set_config
from bibl.lint import lint


class TestFieldRules(unittest.TestCase):

    def test_S00_pass(self):
        set_config('select', ['S00'])
        result = lint('test_data/all_pass.bib', verbose=False)
        self.assertEqual([], result)

    def test_S00_fail(self):
        set_config('select', ['S00'])
        result = lint('test_data/rules/S00_fail.bib', verbose=False)
        self.assertEqual(1, len(result))

    def test_S01_pass(self):
        set_config('select', ['S01'])
        result = lint('test_data/all_pass.bib', verbose=False)
        self.assertEqual([], result)

    def test_S01_fail(self):
        set_config('select', ['S01'])
        result = lint('test_data/rules/S01_fail.bib', verbose=False)
        self.assertEqual(1, len(result))

    def test_S02_all_pass(self):
        set_config('select', ['F01*'])
        result = lint('test_data/all_pass.bib', verbose=False)
        self.assertEqual([], result)

    def test_S02_all_fail(self):
        set_config('select', ['S02*'])
        result = lint('test_data/rules/S02_all_fail.bib', verbose=False)
        self.assertEqual(34, len(result))

    def test_S02_separate_fail(self):
        req_fields = {
            'article': 4,
            'book': 3,
            'booklet': 1,
            'conference': 3,
            'inbook': 3,
            'incollection': 4,
            'inproceedings': 3,
            'manual': 1,
            'mastersthesis': 3,
            'misc': 0,
            'phdthesis': 3,
            'proceedings': 2,
            'techreport': 3,
            'unpublished': 1
        }
        for entry_type, num_req_fields in req_fields.items():
            set_config('select', [f'S02_{entry_type}_*'])
            result = lint('test_data/rules/S02_all_fail.bib', verbose=False)
            self.assertEqual(num_req_fields, len(result))

    def test_S03_all_pass(self):
        set_config('select', ['S03*'])
        result = lint('test_data/all_pass.bib', verbose=False)
        self.assertEqual([], result)

    def test_S03_all_fail(self):
        set_config('select', ['S03*'])
        result = lint('test_data/rules/S03_all_fail.bib', verbose=False)
        self.assertEqual(14, len(result))


if __name__ == '__main__':
    unittest.main()
