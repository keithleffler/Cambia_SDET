import logging

'''
'''

logging.basicConfig(level=logging.INFO)


class _custonException(Exception):
    pass


class notImplemented(_custonException):
    '''
    Exception class to create not-implemented failures during TDD. Helps avoid developer head-scratching and overall confusion.
    '''

    def __init__(self,method,*args,**kwargs):
        msg = 'Method %s not implemented, but was called anyway.  Please implement.' % method
        _custonException.__init__(self,msg,*args,**kwargs)

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
    Check that the input file can be used by the progoram
    :param filename:
    :return: True if all checks succeed.  Otherwise raise an exceptoin
    """

    def check_existence():      # TODO: complete this function
        '''
        Check that the input file exists
        :return:
        '''
        raise notImplemented('check_input_file.check_existence')

    def check_is_readable():    # TODO: and also complete this one.
        '''
        Check that the input file is readable
        :return:
        '''
        raise notImplemented('check_input_file.check_is_readable')

    check_existence()
    check_is_readable()

    return True


def check_output_path(filename):

    '''
    Check that the output path / file are useable by the program.
    :param filename:
    :return:
    '''

    def check_is_writable():    # TODO: complete this function
        raise notImplemented('check_output_path.check_is_writable')

    check_is_writable()
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

        args = {'infile': './input.csv',
                'outfile': './output.csv'}

        check_input_file(args['infile'])
        check_output_path(args['outfile'])

        return args

    except Exception as e:
        raise codeException('Code assertion: method get_args: %s' % e)


def get_input(infile):
    '''
    Read the first line of the input file, and return as a string.
    :return:
    '''

    # TODO - Add check that file is only one line.
    # Fail if this isn't so.
    def check_data_is_valid(data):
        raise notImplemented('get_input.check_data_is_valid')

    try:
        with open(infile,'r') as f:
            data = f.readlines()
        check_data_is_valid(data)
        return data[0]

    except notImplemented:
        raise

    except Exception as e:
        raise codeException('Code assertion, method get_input: %s' % e)


def rev_sort(s):
    '''
    Sort elements of a comma-separated string into reverse order.
    :param s: A comma-separated string
    :return: A CSV string, with the elements of the input CSV sorted in descending order
    '''

    def preprocess(s):  # TODO: expand the set of problematic substrings.  Remove leading spaces.  Preserve internal space.
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
        raise codeException('Code assertion: method rev_sort: %s' % e)


def write_output(outfile, s):
    '''
    Write a string to a text file
    :param outfile:
    :param s:
    :return:
    '''
    try:
       raise notImplemented('write_output')

    except Exception as e:
        raise codeException('Code assertion: method write_output: write_output: %s' % e)


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
