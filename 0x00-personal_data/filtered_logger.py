#!/usr/bin/env python3
"""Function that filters datum"""
import re


def filter_datum(fields, redaction, message, separator):
    """Filter datum filters fields with redaction"""
    for field in fields:
        message = re.sub(
           fr"(?<!\w)({field}=)([^;{separator}]+)", fr"\1{redaction}", message)
    return message
