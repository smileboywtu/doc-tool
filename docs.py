#!/usr/bin/env python
# -*- coding: utf-8 -*-

# tools to generate python source code header docs
# Created: 2016-07-01
# Copyright: (C) 2016<smileboywtu@gmail.com>


import argparse
import datetime
from string import Template


def docs(author, description, date=None):
    """func to generate doc

    use source code auther and description information to
    generage the code header.

    Args:
        author(str): source code file auther information.
        description(str): file module description.
        date(object, optional): file created time.

    Return:
        str: docs for source code

    """
    if not date:
        date = datetime.datetime.now()

    docs_template = """\
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $description
# Created: $date
# Copyright: (C) $year<$author>
"""
    year = date.year
    date = date.strftime("%Y-%m-%d")

    return Template(docs_template).safe_substitute({
        'description': ' '.join(description),
        'date': date,
        'year': year,
        'author': author
    })


def command_line():
    parser = argparse.ArgumentParser("python source code doc generate tool.")
    parser.add_argument('-u', '--author', dest='author',
                        help='File create author')
    parser.add_argument('-m', '--description', dest='description',
                        type=str, nargs='*', help='module function description')
    args = vars(parser.parse_args())
    print docs(**args)


if __name__ == '__main__':
    command_line()
