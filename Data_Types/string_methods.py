# Methods...

newStr = "    my nAME Is Tim  "
print(newStr)
print("String methods : ")
print("Length : ", len(newStr))  # -> 20

print("Count : ", newStr.count("m"))  # -> 2

# Changing case:
print("Islower :", newStr.islower())
print("Isupper :", newStr.isupper())

# casefold(self, /):
# Return a version of the string suitable for caseless comparisons.
print("Case Fold : " + str(newStr.casefold()))  # ->     my name is tim

# capitalize(self, /):
# Return a capitalized version of the string.
# More specifically, make the first character have upper case and the rest lower case.
print("Capitalize() : " + str("never Ever".capitalize()))  # -> Never ever

# center(self, width, fillchar=' ', /):
# Return a centered string of length width.
print("center() :", "Machine Learning".center(20, '_'))

# encode(self, /, encoding='utf-8', errors='strict')
print("Encode : " + str(newStr.encode("UTF-8")))  # -> b'    my nAME Is Tim  '

# S.endswith(suffix[, start[, end]]) -> bool
# Return True if S ends with the specified suffix, False otherwise.
# suffix can also be a tuple of strings to try.
print("Endswith : " + str(newStr.endswith(" ")))  # -> True
print("Endswith : " + str(newStr.endswith((' ', 'Tim'))))  # -> True

# expandtabs(self, /, tabsize=8)
# Return a copy where all tab characters are expanded using spaces.
print("expandtabs : " + str(newStr.expandtabs(tabsize=4)))  # ->     my nAME Is Tim

# S.find(sub[, start[, end]]) -> int
# Return the lowest index in S where substring sub is found.
# Return -1 on failure.
print("Find : " + str(newStr.find("Tim")))  # -> 15


# S.index(sub[, start[, end]]) -> int
# Return the lowest index in S where substring sub is found.
# Raises ValueError when the substring is not found.
print("Index : " + str(newStr.index("Is")))  # -> 12


# Is check methods:
alpha = "abcdABCD"
print("Isalpha :", alpha.isalpha())
alphaNumeric = "abcd0001"
print("Isalnum/ alpha-numeric :", alphaNumeric.isalnum())


digitString = '24'
print("Isdigit :", digitString.isdigit())
numericStr = "12345678"
print("Isnumeric :", numericStr.isnumeric())


# isidentifier(self, /)
# Return True if the string is a valid Python identifier, False otherwise.
identifierStr = "class"  # class, def such keywords are identifiers
print("Is identifier :", identifierStr.isidentifier())

print("Is printable :", newStr.isprintable())  # -> True

# isascii() : True if all characters in the string are ASCII, False otherwise.
print("Isascii :", newStr.isascii())  # -> True

# isspace(self, /):
# Return True if the string is a whitespace string, False otherwise.
spaceString = "     "  # contains only space
print("Isspace :", spaceString.isspace())

# istitle(self, /):
# Return True if the string is a title-cased string.
print("Istitle :", newStr.istitle())


# join(self, iterable, /):
# Concatenate any number of strings.
# The string whose method is called is inserted in between each given string.
# The result is returned as a new string.
print("Join :", '_'.join(['ab', 'pq', 'rs']))  # -> ab_pq_rs


# ljust(self, width, fillchar=' ', /)
# Return a left-justified string of length width.
# Padding is done using the specified fill character (default is a space).
print("Left-justification :", newStr.ljust(24, '-'))  # ->     my nAME Is Tim  ----


print("Lower :", newStr.strip().lower())  # -> my name is tim


# lstrip(self, chars=None, /):
# Return a copy of the string with leading whitespace removed.
# If chars is given and not None, remove characters in chars instead.
print("Left-strip :", newStr.lstrip())  # -> my nAME Is Tim


# partition(self, sep, /):
# Partition the string into three parts using the given separator.
# returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.
print("Partition : " + str("Hi Lyn !".partition(' ')))  # -> ('Hi', ' ', 'Lyn !')
print("Partition : " + str("Hi Lyn !".partition('.')))  # -> ('Hi Lyn !', '', '')


# removeprefix(self, prefix, /):
# Return a str with the given prefix string removed if present.
# If the string starts with the prefix string, return string[len(prefix):].
# Otherwise, return a copy of the original string.
print("Remove prefix :", "preHi There!".removeprefix('pre'))  # -> Hi There!
print("Remove prefix :", "preHi There!".removeprefix(''))  # -> preHi There!


# removesuffix(self, suffix, /):
print("Remove suffix :", "Hi Darek!".removesuffix('!'))  # Hi Darek


# replace(self, old, new, count=-1, /):
# Return a copy with all occurrences of substring old replaced by new.
# count: Maximum number of occurrences to replace.
# -1 (the default value) means replace all occurrences.
print("Replace :", "Know your value!".replace("value", "worth", 1))  # -> Know your worth!


# S.rfind(sub[, start[, end]]) -> int
# Return -1 on Failure.
print("rFind : " + str(newStr.rfind("Is", 10)))  # -> 12


# S.rindex(sub[, start[, end]]) -> int
# Return the highest index in S where substring sub is found.
# Raises ValueError when the substring is not found.
print("rIndex : " + str(newStr.rindex("Tim", 14)))  # -> 15


# rjust(self, width, fillchar=' ', /):
# Return a right-justified string of length width.
print("Right justification :", newStr.rjust(24, '/'))


# rpartition(self, sep, /):
# Partition the string into three parts using the given separator.
# Starting at the end. If the separator is found, returns a 3-tuple containing the
# part before the separator, the separator itself, and the part after it.
print("r-partition :", "Pathetic but aesthetic".rpartition(' '))  # -> ('Pathetic but', ' ', 'aesthetic')


# rsplit(self, /, sep=None, maxsplit=-1):
# Starting from end of the string.
# Return a list of the words in the string, using sep as the delimiter string.
# sep(None = whitespace) : The delimiter according which to split the string.
# maxsplit : Maximum number of splits to do.
# -1 (the default value) means no limit.
print("rSplit :", newStr.rsplit(None, 2))  # -> ['    my nAME', 'Is', 'Tim']
print("rSplit :", newStr.rsplit())  # -> ['my', 'nAME', 'Is', 'Tim']
print("rSplit :", newStr.rsplit("Is"))  # -> ['    my nAME ', ' Tim  ']


# rstrip(self, chars=None, /):
# Return a copy of the string with trailing whitespace removed.
print("rStrip :", newStr.rstrip())  # ->     my nAME Is Tim


# strip(self, chars=None, /):  # As trim() in java
# Return a copy of the string with leading and trailing whitespace removed.
print("Strip :", newStr.strip())  # -> my nAME Is Tim


# split(self, /, sep=None, maxsplit=-1):
# Return a list of the words in the string, using sep as the delimiter string.
print("Split :", newStr.split())  # -> ['my', 'nAME', 'Is', 'Tim']
print("Split :", newStr.split(" "))  # -> ['', '', '', '', 'my', 'nAME', 'Is', 'Tim', '', '']


# splitlines(self, /, keepends=False):
# Return a list of the lines in the string, breaking at line boundaries.
# Line breaks are not included in the resulting list unless keepends is given and True.
spString = "Hi There\n Krish."
print("Splitlines :", spString.splitlines())  # -> ['Hi There', ' Krish.']
print("Splitlines :", spString.splitlines(True))  # -> ['Hi There\n', ' Krish.']


# S.startswith(prefix[, start[, end]]) -> bool
# Return True if S starts with the specified prefix, False otherwise.
# prefix can also be a tuple of strings to try.
print("Startswith :", newStr.startswith(" "))  # -> True


# swapcase(self, /):
# Convert uppercase characters to lowercase and lowercase characters to uppercase.
print("Swap case :", newStr.strip().swapcase())  # -> MY Name iS tIM


# title(self, /):
# Return a version of the string where each word is titlecased.
print("Title :", newStr.strip().title())  # -> My Name Is Tim


# translate(self, table, /):
# Replace each character in the string using the given translation table.
# table :
# Translation table, which must be a mapping of Unicode ordinals to Unicode ordinals, strings, or None.
# The table must implement lookup/indexing via __getitem__, for instance a dictionary or list.
# If this operation raises LookupError, the character is left untouched.  Characters mapped to None are deleted.
x, y, z, s = "abc", "ghi", "ab", "abcde"
translation_table = s.maketrans(x, y, z)
print("Translate :", s.translate(translation_table))  # -> ide
trans_table = {97: None, 98: None, 99: 105}
print("Translate :", s.translate(trans_table))  # -> ide


print("Upper :", newStr.strip().upper())  # -> MY NAME IS TIM


# zfill(self, width, /):
# Pad a numeric string with zeros on the left, to fill a field with the given width.
# The string is never truncated.
print("zFill :", newStr.strip().zfill(20))  # -> 000000my nAME Is Tim

print(newStr)
