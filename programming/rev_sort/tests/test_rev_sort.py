import mock
from .. import rev_sort
from os.path import dirname, abspath
import unittest


class test_codeException(unittest.TestCase):
    def setUp(self):
        self.expected = 'Code exception: method: bad_method: big problem'

    def test_happy_path(self):
        try:
            raise rev_sort.codeException('bad_method', 'big problem')
        except rev_sort.codeException as e:
            self.assertTrue(str(e) == self.expected)

    def test_bad_method_name(self):
        try:
            raise rev_sort.codeException('not_really_bad_method', 'big problem')
        except rev_sort.codeException as e:
            self.assertFalse(str(e) == self.expected)

    def test_bad_msg(self):
        try:
            raise rev_sort.codeException('bad_method', 'tiny problem')
        except rev_sort.codeException as e:
            self.assertFalse(str(e) == self.expected)


class test_check_inputException(unittest.TestCase):
    def setUp(self):
        self.expected = 'Input exception: file: bad_file: big problem'

    def test_happy_path(self):
        try:
            raise rev_sort.inputException('bad_file', 'big problem')
        except rev_sort.inputException as e:
            self.assertTrue(str(e) == self.expected)

    def test_bad_method_name(self):
        try:
            raise rev_sort.inputException('not_really_bad_file', 'big problem')
        except rev_sort.inputException as e:
            self.assertFalse(str(e) == self.expected)

    def test_bad_msg(self):
        try:
            raise rev_sort.inputException('bad_file', 'tiny problem')
        except rev_sort.inputException as e:
            self.assertFalse(str(e) == self.expected)


class test_check_outputException(unittest.TestCase):
    def setUp(self):
        self.expected = 'Output exception: file: bad_file: big problem'

    def test_happy_path(self):
        try:
            raise rev_sort.outputException('bad_file', 'big problem')
        except rev_sort.outputException as e:
            self.assertTrue(str(e) == self.expected)

    def test_bad_method_name(self):
        try:
            raise rev_sort.outputException('not_really_bad_file', 'big problem')
        except rev_sort.outputException as e:
            self.assertFalse(str(e) == self.expected)

    def test_bad_msg(self):
        try:
            raise rev_sort.outputException('bad_file', 'tiny problem')
        except rev_sort.outputException as e:
            self.assertFalse(str(e) == self.expected)


class _ioTestCase(unittest.TestCase):
    def setUp(self):
        path = dirname(abspath(__file__)).rsplit('/', 1)[0]
        self.infile = '%s/input.csv' % path
        self.outfile = '%s/output.csv' % path


class _MockFile():
    def __init__(self, *args, **kwargs):
        self._readlines_value = None

    @property
    def readlines_value(self):
        return self._readlines_value

    @readlines_value.setter
    def readlines_value(self, value):
        self._readlines_value

    def close(self):
        pass

    def readlines(self):
        return self._readlines_value

    def writelines(self, data):
        pass

class test_check_input_file(_ioTestCase):

    def test_happy_path(self):
        rev_sort.check_input_file(self.infile)

    @unittest.expectedFailure
    @mock.patch('os.path.isfile')
    def test_missing(self, mock_exists):
        mock_exists.return_value = False
        rev_sort.check_input_file(self.infile)

    @unittest.expectedFailure
    @mock.patch('os.access')
    def test_unreadable(self, mock_access):
        mock_access.return_value = False
        rev_sort.check_input_file(self.infile)


class test_check_output_path(_ioTestCase):

    def test_happy_path(self):
        rev_sort.check_input_file(self.infile)

    @unittest.expectedFailure
    @mock.patch('os.path.exists')
    def test_missing_path(self, mock_exists):
        mock_exists.return_value = False
        rev_sort.check_output_path(self.outfile)

    @unittest.expectedFailure
    @mock.patch('os.access')
    @mock.patch('os.path.exists')
    def test_existing_unwritable_file(self, mock_access, mock_exists):
        mock_access.return_value = False
        mock_exists.return_value = True
        rev_sort.check_output_path(self.outfile)

    @unittest.expectedFailure
    @mock.patch('os.path.exists')
    @mock.patch('os.access')
    def test_unwritable_path(self, mock_access, mock_exists):
        mock_access.return_value = False
        mock_exists.return_value = False
        rev_sort.check_output_path(self.outfile)


class test_get_args(_ioTestCase):
    def test_happy_path(self):
        expected = ('infile', 'outfile')
        args = rev_sort.get_args()
        self.assertTrue(isinstance(args, dict))
        self.assertTrue(set(args.keys()) >= set(expected))  # check that all
        # expected arguments are present.

class test_get_input(_ioTestCase):
    def test_happy_path(self):
        data = rev_sort.get_input(self.infile)

    @unittest.expectedFailure
    @mock.patch('__builtin__.open')
    def test_too_many_lines(self, mock_open):
        f = _MockFile
        f.readlines_value = ['a,b,c\n', 'd,e,f\n']

        mock_open.return_value = f
        rev_sort.get_input(self.infile)

    @unittest.expectedFailure
    @mock.patch('__builtin__.open')
    def test_missing_newline(self, mock_open):
        f = _MockFile
        f.readlines_value = ['a,b,c']
        mock_open.return_value = f
        rev_sort.get_input(self.infile)


class test_rev_sort(unittest.TestCase):
    def test_happy_path(self):
        self.fail('Not implemented')


@mock.patch('__builtin__.open')
class test_write_output(_ioTestCase):

    def test_happy_path(self, mock_open):
        mock_open.return_value = _MockFile()
        data = ['c,b,a\n']
        rev_sort.write_output(self.outfile, data)

    @unittest.expectedFailure
    def test_missing_newline(self, mock_open):
        mock_open.return_value = _MockFile()
        data = ['c,b,a']
        rev_sort.write_output(self.outfile, data)

    @unittest.expectedFailure
    def test_not_a_list(self, mock_open):
        mock_open.return_value = _MockFile()
        data = 'c,b,a'
        rev_sort.write_output(self.outfile, data)

    @unittest.expectedFailure
    def test_too_many_lines(self, mock_open):
        mock_open.return_value = _MockFile()
        data = ['c,b,a\n', 'f,e,d\n']
        rev_sort.write_output(self.outfile, data)

@mock.patch.object(rev_sort,'write_output')
@mock.patch.object(rev_sort,'rev_sort')
@mock.patch.object(rev_sort,'get_input')
@mock.patch.object(rev_sort,'get_args')
class test_main(unittest.TestCase):
    def test_happy_path(self,mock_get_args,mock_get_input,mock_rev_sort,mock_write_output):
        mock_get_args.return_value = {'infile':'test_in.csv',
                                      'outfile':'test_out.csv'}
        mock_get_input.return_value = ['a,b,c\n']
        mock_rev_sort.return_value = ['c,b,a\n']
        mock_write_output.return_value = True

        rev_sort.main()
