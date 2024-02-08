#!/usr/bin/env python3
"""Function that filters datum"""
import re
from typing import List


def filter_datum(f: List[str], r: str, m: str, s: str) -> str:
    """Filter datum filters fields with redaction"""
    for field in f:
        message = re.sub(
            fr"(?<!\w)({field}=)([^;{s}]+)", fr"\1{r}", m)
    return message
