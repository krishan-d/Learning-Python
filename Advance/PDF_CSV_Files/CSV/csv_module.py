"""
CSV: Comma separated variables
Most common import and export format for spreadsheets and databases.
"""

import csv
import sys
import pandas as pd

# NOTE: csv contains raw data/information only. Formulas, Images and Macros can't be in csv.

"""
pandas:
  - Full data analysis library, can work with almost any tabular data type.
  - Runs visualizations and analysis.
    
openpyxl:
  - Designed specifically for Excel files.
  - Retains a lot of Excel specific functionality.
  - Supports Excel formulas.
  - python-excel.org tracks various other Excel based python libraries.
    
Google Sheets Python API:
  - Direct python interface for working with google spreadsheets.
  - Allow to directly make changes to spreadsheets hosted online.
  - More complex syntax, but available in many programming languages.
"""

# csv module Functions:

# csv.reader(csvfile, dialect='excel', *args, **kwargs):
# Return a reader object which will iterate over lines in the given csvfile.
# csvfile : any object which supports iterator protocol and returns a string each time its __next__() method is called.
# File objects / List objects.
# If csvfile is a file object, it should be opened with newline=''.

# Note:  For csv.reader(), the default quote-char argument is the double quote, '"'.

filename = 'Example.csv'
with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    try:
        print("Dialect:", reader.dialect)
        # The number of lines read from the source iterator.
        print("Line Number:", reader.line_num)

        # for row in reader: print(row)  # Return all data
        # print("....", next(reader))

        data_rows = list(reader)  # Making List of Lists(optional)
        for row in data_rows[:4]: print('\t', ', '.join(row))

    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))


# csv.writer(csvfile, dialect='excel', *args, **kwargs):
# Return a writer object responsible for converting the user’s data into delimited strings on given file-like object.

fields = ['Name', 'Branch', 'Year', 'CGPA']

rows = [['Edwina', 'CSE', 2, 9.0], ['Eve', 'CSE', 4, 9.2], ['Liam', 'ECE', 3, 8.8]]

with open('University_records.csv', mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    print("\nDialect:", writer.dialect)

    writer.writerow(fields)
    writer.writerows(rows)


# csv.register_dialect(name[, dialect[, **fmtparams]]) -> None: ...
# Associate dialect with name.
# csv.register_dialect('unixpwd', delimiter=':', quoting=csv.QUOTE_NONE)

# csv.unregister_dialect(name: str) -> None: ...
# Delete the named dialect from the dialect registry. An Error is raised if name is not a registered dialect name.

# csv.get_dialect(name: str) -> Dialect: ...
# Return immutable dialect associated with name. An Error is raised if name is not a registered dialect name.
dialect = csv.get_dialect('excel')
print("\nGet dialect:", dialect)

# csv.list_dialects() -> list[str]: ...
# Return the names of all registered dialects.
print("Dialects List:", csv.list_dialects())

# csv.field_size_limit([new_limit]):
# Returns the current maximum field size allowed by the parser. If new_limit is given, this becomes the new limit.


# csv module classes:

# csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwargs):
# Parameters:
#       fieldnames: sequence of keys that identify the order in which values in dictionary should be passed.
#       restval: value to be written if dictionary is missing a key in fieldnames.
#       extrasaction: If a key not found in fieldnames, the extrasaction parameter indicates what action to take.
#       -If it is set to raise a ValueError will be raised.
#       dialect: Name of the dialect to be used.

# Create an object which operates like a regular writer but maps dictionaries onto output rows.

dict_data = [{'Name': 'Edwina', 'Branch': 'CSE', 'Year': 2, 'CGPA': 9.0},
             {'Name': 'Emma', 'Branch': 'CSE', 'Year': 4, 'CGPA': 9.2},
             {'Name': 'Noah', 'Branch': 'ECE', 'Year': 3, 'CGPA': 8.8}]

with open('Records.csv', 'w+', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields, restval='None')

    # writeheader():
    # Write a row with the field names to the writer’s file object, formatted according to the current dialect.
    writer.writeheader()

    writer.writerow({'Name': 'Zara', 'Year': 3, 'CGPA': 9.0})
    writer.writerows(dict_data)


# csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwargs)
# Create an object that operates like a regular reader but maps the information in each row to a dict,
# whose keys are given by fieldnames parameter.

with open('Records.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    print("\nDictionary keys/ Fieldnames:", reader.fieldnames)

    for row in reader:
        print('\t', row['Name'], row['Branch'])
    print("End row:", row)

# class csv.Dialect
# The Dialect class is a container class whose attributes contain information for how to handle-
# double quotes, whitespace, delimiters, etc.
# Due to the lack of a strict CSV specification, different applications produce subtly different CSV data.
# Dialect instances define how reader and writer instances behave.

with open('unix.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='unix')

# csv module constants:
# csv.QUOTE_ALL:
# Instructs writer objects to quote all fields.

# csv.QUOTE_MINIMAL:
# Instructs writer objects to only quote those fields which contain special characters such as delimiter,
# quote-char or any of the characters in line-terminator.

# csv.QUOTE_NONNUMERIC:
# Instructs writer objects to quote all non-numeric fields.
# Instructs the reader to convert all non-quoted fields to type float.

# csv.QUOTE_NONE:
# Instructs writer objects to never quote fields.
# When the current delimiter occurs in output data it is preceded by the current escape-char character.
# If escape-char is not set, the writer will raise Error if any characters that require escaping are encountered.
# Instructs reader to perform no special processing of quote characters.

# exception csv.Error:
# Raised by any of the functions when an error is detected.


# Dialects and Formatting Parameters:
# Dialect.delimiter:
# A one-character string used to separate fields. It defaults to ','.

# Dialect.doublequote:
# Controls how instances of quote-char appearing inside a field should themselves be quoted.
# True: character is doubled./ default
# False: the escape-char is used as a prefix to the quote-char.
# output: False and no escape char is set -> Error is raised if a quote char is found in a field.

# Dialect.escapechar:
# To escape the delimiter if quoting is set to QUOTE_NONE and quotechar if doublequote is False.
# On reading, the escapechar removes any special meaning from the following character.
# default: None, which disables escaping.

# Dialect.lineterminator:
# The string used to terminate lines produced by the writer.
# default: '\r\n'.

# Dialect.quotechar:
# To quote fields containing special characters (delimiter or quotechar, or which contain new-line characters).
# default: '"'.

# Dialect.quoting:
# Controls when quotes should be generated by the writer and recognised by the reader.
# default: QUOTE_MINIMAL

# Dialect.skipinitialspace:
# True: whitespace immediately following the delimiter is ignored. False: default.

# Dialect.strict:
# True: raise exception Error on bad CSV input. False: default.


# pandas.read_csv():
print("\nReading csv using pandas...")
csv = pd.read_csv('Example.csv')
print(csv)
