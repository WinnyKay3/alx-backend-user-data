#!/usr/bin/env python3
"""Function that filters datum"""
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Filter datum filters fields with redaction"""
    for field in fields:
        message = re.sub(
           fr"(?<!\w)({field}=)([^;{separator}]+)", fr"\1{redaction}", message)
    return message
