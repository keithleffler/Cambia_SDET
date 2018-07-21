import unittest
from .. import rev_sort

class _testCase(unittest.TestCase):
    pass

class test_codeException(unittest.TestCase):
    def setUp(self):
        self.expected = 'Code exception: method: bad_method: big problem'

    def test_happy_path(self):
        try:
            raise rev_sort.codeException('bad_method','big problem')
        except rev_sort.codeException as e:
            self.assertTrue(str(e)==self.expected)

    def test_bad_method_name(self):
        try:
            raise rev_sort.codeException('not_really_bad_method','big problem')
        except rev_sort.codeException as e:
            self.assertFalse(str(e)==self.expected)

    def test_bad_msg(self):
        try:
            raise rev_sort.codeException('bad_method','tiny problem')
        except rev_sort.codeException as e:
            self.assertFalse(str(e)==self.expected)

class test_check_input_file(unittest.TestCase):
    def test_happy_path(self):
        self.fail('Not implemented')

class test_check_output_file(unittest.TestCase):
    def test_happy_path(self):
        self.fail('Not implemented')

class test_get_args(_testCase):
    def test_happy_path(self):
        self.fail('Not implemented')

class test_get_input(_testCase):
    def test_happy_path(self):
        self.fail('Not implemented')

class test_rev_sort(_testCase):
    def test_happy_path(self):
        self.fail('Not implemented')

class test_write_output(_testCase):
    def test_happy_path(self):
        self.fail('Not implemented')

class test_main(_testCase):
    def test_happy_path(self):
        self.fail('Not implemented')