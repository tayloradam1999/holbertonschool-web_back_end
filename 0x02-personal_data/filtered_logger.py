#!/usr/bin/env python3
"""
Obfuscating log msgs
"""
import re
import logging
import os
import mysql.connector
import datetime
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Obfuscate log msg

    The function should use regex to replace occurences of certain field values

    Function should be < 5 lines and use re.sub() to perform all regex in one
    statement

    Args:
        fields (str): list of strs representing all fields to obfuscate
        redaction (str): str representing what field will be replaced with
        message (str): str representing the log message
        seperator (str): str representing the seperator between fields

    Returns:
        str: str representing the obfuscated log message
    """
    log = message.split(separator)

    for field in fields:
        for i in range(len(log)):
            log[i] = re.sub(field + '=.*', field + '=' + redaction, log[i])
    return separator.join(log)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Filters values in incoming log records using <filter_datum>

        Values for fields in <fields> should be filtered.

        DO NOT extrapolate <FORMAT> manually. The <format> method
        should be less than 5 lines long.

        Args:
            record (logging.LogRecord): log record to be formatted

        Returns:
            str: formatted log record
        """
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg,
                                  self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    Logger named <user_data> that logs up to <logging.INFO>

    Does not propagate messages to other loggers.

    Uses <StreamHandler> with <RedactingFormatter> as the formatter.

    Use <PII_FIELDS> to parameterize the formatter.

    Args:
        None

    Returns:
        logging.Logger: logger object named <user_data>
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connects to the database named <holberton> to read the <users> table

    Uses <os> module to obtain credentials from environment

    Uses <mysql-connector-python> to connect to MySQL Database

    Args:
        None

    Returns:
        mysql.connector.connection.MySQLConnection: connection to <holberton>
    """
    user = os.environ.get("PERSONAL_DATA_DB_USERNAME")
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD")
    host = os.environ.get("PERSONAL_DATA_DB_HOST")
    database = os.environ.get("PERSONAL_DATA_DB_NAME")
    return mysql.connector.connect(user=user, password=password, host=host,
                                   database=database)


def main():
    """
    Obtains a database connection using get_db() and retrieves all rows in the
    <users> table.

    Displays each row under a filtered format using get_logger() and
    <PII_FIELDS> to filter the fields.

    Args:
        None

    Returns:
        None
    """
    logger = get_logger()
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    for row in cursor:
        # Instantiate list of tuples of <row>'s key/pair values
        tuple_list = row.items()
        # Convert to string of key/value pairs with separator
        str = '; '.join(f"{tuple[0]}={tuple[1]}" for tuple in tuple_list)
        # Pass string to logger to log in specified format
        logger.info(str)
    db.close()

main()