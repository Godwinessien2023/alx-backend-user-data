#!/usr/bin/env python3
"""
A functiontion that returns logg message
"""


import logging
import re


def filter_datum(fields, redaction, message, separator):
    """function that returns log message"""
    pattern = r'({})=([^{}]*)'.format('|'.join(map(re.escape, fields)),
                                      re.escape(separator))\

    return re.sub(pattern, r'\1=' + redaction, message)
