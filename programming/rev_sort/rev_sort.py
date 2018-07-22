import getpass
import logging
import os
from os.path import dirname, abspath

'''
'''

logging.basicConfig(level=logging.INFO)


class _custonException(Exception):
    pass


class notImplemented(_custonException):
    '''
    Exception class to create not-implemented failures during TDD. Helps avoid developer head-scratching and overall confusion.
    '''

    def __init__(self, method, *args, **kwargs): # pragma: no cover
        msg = 'Method %s not implemented, but was called anyway.  Please implement.' % method
        _custonException.__init__(self, msg, *args, **kwargs)


class codeException(_custonException):
    '''
    Exception class to handle assertions in code, as opposed to other types of issues.
    '''

    def __init__(self, method, msg, *args, **kwargs):
        msg = 'Code exception: method: %s: %s' % (method, msg)
        _custonException.__init__(self, msg, *args, **kwargs)


class inputException(_custonException):
    '''
    Exception class to handle problems with the input file.
    '''

    def __init__(self, filename, msg, *args, **kwargs):
        msg = 'Input exception: file: %s: %s' % (filename, msg)
        _custonException.__init__(self, msg, *args, **kwargs)

class outputException(_custonException):
    '''
    Exception class to handle problems with the output file / path
    '''

    def __init__(self, filename, msg, *args, **kwargs):
        msg = 'Output exception: file: %s: %s' % (filename, msg)
        _custonException.__init__(self, msg, *args, **kwargs)


def check_input_file(filename):
    """
    Check that the input file can be used by the program

    :param filename: The name of the input file.
    :return: True if all checks succeed.  Otherwise raise an exception.
    """

    def check_existence():  # TODO: complete this function
        '''
        Check that the input file exists
        :return: True
        '''
        if not (os.path.isfile(filename)):
            raise inputException(filename, ' cannot be found.')
        return True

    def check_is_readable():  # TODO: and also complete this one.
        '''
        Check that the input file is readable
        :return:
        '''
        if not (os.access(filename, os.R_OK)):
            raise inputException(filename, ' is not readable by user %s' % getpass.getuser())
        return True

    check_existence()
    check_is_readable()

    return True


def check_output_path(filename):
    '''
    Check that the output path / file are useable by the program.
    :param filename:
    :return:
    '''

    def check_exists(path):
        if not (os.path.exists(path)):
            raise outputException(path, ' is not writable by user %s' % getpass.getuser())
        return True

    def check_is_writable(path):

        if os.path.exists(filename):
            writeable = os.access(filename,os.W_OK)
            if not(writeable):
                raise outputException(filename,'  exists but is not writeable by user %s' % getpass.getuser())

        if not (os.access(path, os.W_OK)):
            raise outputException(path, ' is not writable by user %s' % getpass.getuser())
        return True

    _path = filename.rsplit('/', 1)[0]
    check_exists(_path)
    check_is_writable(_path)
    return True


def get_args():
    """
    Return the input and output files.  For this assignment, these are
    fixed, but a these likely would be command line arguments in the real world.
    It would be simple to include and argument parser instance to get these.
    The method calls checks on the validity of the input and output files before returning.
    :return:
    """
    try:
        path = dirname(abspath(__file__))
        args = {'infile': '%s/input.csv' % path,
                'outfile': '%s/output.csv' % path}

        check_input_file(args['infile'])
        check_output_path(args['outfile'])

        return args

    except Exception as e:  # pragma: no cover
        raise codeException('get_args', e)


def get_input(infile):
    '''
    Read the first line of the input file, and return as a string.
    :return:
    '''

    # TODO - Add check that file is only one line.
    # Fail if this isn't so.
    def check_data_is_valid(data):
        if not (isinstance(data, list) and len(data) == 1):
            raise inputException(infile, 'Input file %s should be 1 line.  Please check file format' % infile)
        if not (data[0][-1] == '\n'):
            raise inputException(infile,
                                 "Input line in file %s is expected to end with a newline, but doesn't.  Please check file format." % infile)

    try:
        f = open(infile, 'r')
        data = f.readlines()
        f.close()

        check_data_is_valid(data)
        return data[0][:-1]

    except Exception as e:
        raise codeException('get_input', e)


def rev_sort(s):
    '''
    Sort elements of a comma-separated string into reverse order.
    :param s: A comma-separated string
    :return: A CSV string, with the elements of the input CSV sorted in descending order
    '''

    def preprocess(
            s):  # TODO: expand the set of problematic substrings.  Remove leading spaces.  Preserve internal space.
        raise notImplemented('rev_sort.preprocess')

    def do_sort(s):
        raise notImplemented('rev_sort.do_sort')

    def post_process(s):
        assert s is not None, 'Parameter s is None in rev_sort.post_process.'
        _s = '%s\n' % s
        return _s

    try:
        _s = preprocess(s)
        _s = do_sort(_s)
        _s = post_process(_s)
        return _s

    except Exception as e:
        raise codeException('rev_sort', e)


def write_output(outfile, data):
    '''
    Write a string to a text file
    :param outfile:
    :param data:
    :return:
    '''
    # TODO - Add check that file is only one line.
    # Fail if this isn't so.
    def check_data_is_valid(data):
        if not (isinstance(data, list)):
            raise codeException('write_output', ' data is not a list. data = %s'%data)

        if not (len(data)==1):
            raise codeException('write_output', ' data should be a 1-element list. data = %s'%data)

        if not (data[0][-1] == '\n'):
            raise codeException('write_output', ' string is expected to be terminated with a newline. string = %s'%data[0])


    try:
        check_output_path(outfile)
        check_data_is_valid(data)

        f = open('outfile','r')
        f.writelines(data)
        f.close()

    except Exception as e:
        raise codeException('write_output', e)


def main():
    # TODO: Add docstring
    try:
        raise notImplemented('main')

    except codeException as c:
        logging.debug('Code exception %s' % c)

    except Exception as e:
        logging.fatal('Unexpected program error %s' % e)


if __name__ == "__main__":  # pragma: no cover
    main()
