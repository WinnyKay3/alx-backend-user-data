#!/usr/bin/env python3
"""Function that filters datum"""
import logging
import re
from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "ip",)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Filter datum filters fields with redaction"""
    for f in fields:
        message = re.sub(
            fr"(?<!\w)({f}=)([^;{separator}]+)", fr"\1{redaction}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the record to a string representation"""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        self._style.fmt = self.FORMAT
        return super().format(record)


def get_logger() -> logging.Logger:
    """Get the logger"""
    logger = logging.Logger("user_data", logging.INFO)
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.propagate = False
    return logger
