import getpass
import logging
import os
from os.path import dirname, abspath
import re

'''
'''

logging.basicConfig(level=logging.INFO)


class _customException(Exception):
    pass


class notImplemented(_customException):
    '''
    Exception class to create not-implemented failures during TDD. Helps avoid developer head-scratching and overall confusion.
    '''

    def __init__(self, method, *args, **kwargs):  # pragma: no cover
        msg = 'Method %s not implemented, but was called anyway.  Please implement.' % method
        _customException.__init__(self, msg, *args, **kwargs)


class codeException(_customException):
    '''
    Exception class to handle assertions in code, as opposed to other types of issues.
    '''

    def __init__(self, method, msg, *args, **kwargs):
        msg = 'Code exception: method: %s: %s' % (method, msg)
        _customException.__init__(self, msg, *args, **kwargs)


class inputException(_customException):
    '''
    Exception class to handle problems with the input file.
    '''

    def __init__(self, filename, msg, *args, **kwargs):
        msg = 'Input exception: file: %s: %s' % (filename, msg)
        _customException.__init__(self, msg, *args, **kwargs)


class outputException(_customException):
    '''
    Exception class to handle problems with the output file / path
    '''

    def __init__(self, filename, msg, *args, **kwargs):
        msg = 'Output exception: file: %s: %s' % (filename, msg)
        _customException.__init__(self, msg, *args, **kwargs)


def check_input_file(filename):
    """
    Check that the input file can be used by the program

    :param filename: The name of the input file.
    :return: True if all checks succeed.  Otherwise raise an exception.
    """

    def check_existence():

        if not (os.path.isfile(filename)):
            raise inputException(filename, ' cannot be found.')
        return True

    def check_is_readable():
        '''
        Check that the input file is readable
        :return:
        '''

        if not (os.access(filename, os.R_OK)):
            raise inputException(filename, ' is not readable by user %s' % getpass.getuser())
        return True

    try:
        check_existence()
        check_is_readable()

        return True

    except inputException:
        raise
    except Exception as e:
        raise codeException('check_input', e)


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
            writeable = os.access(filename, os.W_OK)
            if not (writeable):
                raise outputException(filename, '  exists but is not writeable by user %s' % getpass.getuser())

        if not (os.access(path, os.W_OK)):
            raise outputException(path, ' is not writable by user %s' % getpass.getuser())
        return True

    try:
        _path = filename.rsplit('/', 1)[0]
        check_exists(_path)
        check_is_writable(_path)
        return True

    except outputException:
        raise
    except Exception as e:
        raise


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
        return data

    except inputException:
        raise

    except Exception as e:
        raise codeException('get_input', e)


def rev_sort(s):
    '''
    Sort elements of a comma-separated string into reverse order.
    :param s: A comma-separated string
    :return: A CSV string, with the elements of the input CSV sorted in descending order
    '''

    def preprocess(s):
        try:
            regexs = {'\,\s+': ',',     #leading space
                      '(\S)\s+,': '\g<1>,'  # trailing space
                      }

            _s = s[0][:-1]          # get string from list, and remove the trailing \n
            _s = _s.lstrip().rstrip()
            for regex, subst in regexs.items():
                _s = re.sub(regex, subst, _s)

            return _s
        except Exception as e:
            raise codeException('rev_sort.preprocess', e)

    def do_sort(s):
        try:
            _s = ','.join(sorted(s.split(','), reverse=True))
            return _s
        except Exception as e:
            raise codeException('rev_sort.do_sort', e)

    def post_process(s):
        try:
            assert s is not None, 'Parameter s is None in rev_sort.post_process.'
            _s = ['%s\n' % s]
            return _s

        except Exception as e:
            raise codeException('rev_sort.post_process')

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



    def check_data_is_valid(data):
        if not (isinstance(data, list)):
            raise codeException('write_output', ' data is not a list. data = %s' % data)

        if not (len(data) == 1):
            raise codeException('write_output', ' data should be a 1-element list. data = %s' % data)

        if not (data[0][-1] == '\n'):
            raise codeException('write_output',
                                ' string is expected to be terminated with a newline. string = %s' % data[0])

    try:
        check_output_path(outfile)
        check_data_is_valid(data)

        f = open(outfile, 'w')
        f.writelines(data)
        f.close()

    except Exception as e:
        raise codeException('write_output', e)


def main():
    '''
    Main function for reverse sorting exercise.
    :return:
    '''
    try:
        data = {'in': [], 'out': []}
        args = get_args()
        data['in'] = get_input(args['infile'])
        data['out'] = rev_sort(data['in'])

        write_output(args['outfile'], data['out'])


    except _customException as c:
        logging.info('Error occurred: %s' % c)

    except Exception as e:
        logging.fatal('Unexpected program error %s' % e)

    logging.info('read %s' % data['in'])
    logging.info('wrote %s' % data['out'])

if __name__ == "__main__":  # pragma: no cover
    main()
