"""Dictionary related utility functions."""

__author__ = "730523735"

# Define your functions below


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table."""
    result: list[dict[str, str]] = []
    # Open a handle to data file
    file_handle = open(filename, "r", encoding="utf8")
    # prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)
    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(rows: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with only the first `N` (a parameter) rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in rows:
        new_new: list[str] = []
        for hey in range(n):
            new_new.append(rows[column][hey])
            result[column] = new_new
    return result


def select(rows: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for val in names:
        result[val] = rows[val]
    return result


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in a:
        result[column] = a[column] 
    for column in b:
        if column in result:
            result[column] += b[column]
        else:
            result[column] = a[column]
    return result


def count(list_vals: list[str]) -> dict[str, int]:
    """This function will produce a `dict[str, int]` where each key is a unique value in the given list and each value associated is the _count_ of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for item in list_vals:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result