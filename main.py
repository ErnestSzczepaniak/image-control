import argparse, create
from argparse import RawTextHelpFormatter
from typing import List

# /* ---------------------------------------------| help |--------------------------------------------- */

DESCRIPTION = """
"""

EPILOG = """Usage examples:
"""

# /* ---------------------------------------------| parsers |--------------------------------------------- */

parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, description=DESCRIPTION, epilog=EPILOG)

def add_arguments(parser: argparse.ArgumentParser, arguments):
    for argument in arguments:
        parser.add_argument(argument[0], **argument[1])    

add_arguments(parser, create.ARGUMENTS)

args = parser.parse_args()

create.execute(**vars(args))


# patryk chojecki