
import logging

'''
'''

logging.basicConfig(level=logging.INFO)


class codeException(Exception):
    '''
    Exception class to handle assertions in code, as opposed to other types of issues.
    '''

    def __init__(self,method,msg,*args,**kwargs):
        msg = 'Code exception: method: %s: %s' % (method,msg)
        Exception.__init__(self,msg,*args,**kwargs)


class inputException(Exception):
    # TODO: And  docstring
    # TODO: Add boilerplate input-problem message
    pass

def check_input_file(filename):
    # TODO: Write a function to check existence of input file.
    #  Raise an exception if not OK

    return True

def check_output_path(filename):
    # TODO: Write a function to check that output is possible.
    # path exists,
    # permissions are OK to write to this locaion,
    # file can be over-written if it exists.
    # Raise exception if not OK

    return True

def get_args():
    # TODO: Add docstring
    try:

        args = {'infile':'./input.csv',
                'outfile':'./output.csv'}

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

    try:
        assert False
    except Exception as e:
        raise codeException('Code assertion, method get_input: %s'%e)


def rev_sort(s):
    '''
    Sort elements of a comma-separated string into reverse order.
    :param s: A comma-separated string
    :return: A CSV string, with the elements of the input CSV sorted in descending order
    '''

    def clean_up(s):  # TODO: expand the set of problematic substrings.  Remove leading spaces.  Preserve internal space.
        pass


    def do_sort(s):
        pass

    def post_process(s):
        _s = '%s\n' % s
        return _s

    try:
        assert False

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
        assert False

    except Exception as e:
        raise codeException('Code assertion: method write_output: write_output: %s' % e)


def main():
    # TODO: Add docstring
    try:
        assert False

    except codeException as c:
        logging.debug('Code exception %s' % c)

    except Exception as e:
        logging.fatal('Unexpected program error %s' % e)


if __name__ == "__main__":  # pragma: no cover
    main()
