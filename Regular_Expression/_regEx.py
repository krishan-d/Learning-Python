"""
Regular Expression:
"""

import re

eText = "There is an error!."

# Searching Basic Pattern:
'error' in eText  # True

# re.search(pattern, string) -> Match | None
match = re.search(pattern=r'error', string=eText)
# NOTE: In (r'an'), r stands for raw.
# Raw string is different from regular string, it won't interpret \ char as an escape char.
print(match)
print("Start Index :", match.start())
print("End Index :", match.end())
print("Span:", match.span())

eText = eText + " error is being removed."
for match in re.finditer(pattern=r'error', string=eText):
    print(match.group())

pattern = 'NOT IN TEXT!'
match = re.search(pattern, string=eText)
print(match)  # None


"""
Metacharacters:
    \	    Used to drop the special meaning of character following it.
    []	    Represent a character class
    ^	    Matches the beginning
    $	    Matches the end
    .	    Matches any character except newline
    |	    Means OR (Matches with any of the characters separated by it.
    ?	    Matches zero or one occurrence
    *?,+?,?? Non-greedy versions of the previous three special characters.
    *	    Any number of occurrences (including 0 occurrences)
    +	    One or more occurrences
    {m,n}	Indicate the number of occurrences of a preceding regex to match.
    {m,n}?   Non-greedy version of the above.
    ()	Matches the RE inside the parentheses.

    (?aiLmsux) The letters set the corresponding flags defined below.
    (?:...)  Non-grouping version of regular parentheses.
    (?P<name>...) The substring matched by the group is accessible by name.
    (?P=name)     Matches the text matched earlier by the group named name.
    (?#...)  A comment; ignored.
    (?=...)  Matches if ... matches next, but doesn't consume the string.
    (?!...)  Matches if ... doesn't match next.
    (?<=...) Matches if preceded by ... (must be fixed length).
    (?<!...) Matches if not preceded by ... (must be fixed length).
    (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
    the (optional) no pattern otherwise.
"""

# \
s = "cowin.in"
match = re.search(r'.', s)
print(match)  # -> <re.Match object; span=(0, 1), match='c'>
# using \
match = re.search(r'\.', s)
print("\\ :", match)  # -> <re.Match object; span=(5, 6), match='.'>

# [] Square Bracket:
# Represents a character class consisting of a set of characters that we wish to match.
# [abc] : match any single a, b or c.
# [0,3] : as [0123]
# [a-c] : as [abc]
# [^0,3] : any number except 0,1,2 or 3
# [^a-c] : any char except a,b,c

# ^ Caret:
# matches if a string starts with a certain character.
# ^c : covid, can..

# $ Dollar:
# matches if a string ends with a certain character.
# s$ : as, eyes

# . Period:
# matches any single character (except newline '\n').
# a.b -> acb, acbd
# .. -> ac, acde

# | Or:
# a|b :  acd, abcd.

# ?
# zero or one occurrence.
# a?bc -> ac, abc
print("? :", re.search(r'ab?c', "ac"))
print("? :", re.search(r'ab?c', "abcb"))

# * star:
# matches zero or more occurrences of the pattern left to it.
# ab*c -> ac, abc, abbc, abbbc, ...

# + :
# matches zero or more occurrences of the pattern left to it.
# ab+c -> abc, abbc, ...

# {m,n} :
# {3}-> Exactly 3 Times// {3,}-> 3 or more
# a{2,4} -> -aa-, -aaa-, -aaaa-
print(re.search(r'a{2,4}', "xaaaz"))

# (<regex>) : Group
# To group sub patterns.
# (a|b)cd -> -acd-, -bcd-
print(re.search(r'(a|b)', "xbcd"))

# Special Sequences...
# \A	Matches if the string begins with the given character.
# \AFor -> For me, Forever

# \b	Matches if the word begins or ends with the given character.
# \b(string) will check for the beginning of the word and (string)\b will check for the ending of the word.
# \bge	-> geek, get

# \B	It is the opposite of the \b i.e. the string should not start or end with the given regex.
# \Bge	Together, Forge

# \d	Matches any decimal digit, this is equivalent to the set class [0-9]
# \d	147, code0

# \D	Matches any non-digit character, this is equivalent to the set class [^0-9]
# \D	code, 3dMax

# \s	Matches any whitespace character.
# \s	gee ks, a bc a

# \S	Matches any non-whitespace character.
# \S	a bd, abcd

# \w	Matches any alphanumeric character,
# This is equivalent to the class [a-zA-Z0-9_].
# \w	10043, code4u

# \W	Matches any non-alphanumeric character.
# \W	>$, Hi<>

# \Z	Matches if the string ends with the given regex.
# or\Z	For, No

# \\    Matches a literal backslash.


s = "Hi, I have an Id number : 166301036 and ssn : 100000"
# re.findall(pattern, string, flags=0)-> List
# returns a list of strings containing all matches.
print("\nre.findall...")
matches = re.findall(r'\d+', s)
print(matches)  # -> ['166301036', '100000']

# re.compile(pattern, flags=0) -> pattern object:
# Compile a regex pattern, returning a Pattern object.
print("\nre.compile...")
p = re.compile('[a-e]')
print("pattern object:", p)
print(p.findall("Hey, Mr. Eve"))  # -> ['e', 'e']
q = re.compile(r'\d+')
print(q.findall("10 A.M. on 4Th December 2021"))  # -> ['10', '4', '2021']
print(q.findall("Hey There!"))  # []

# re.split(pattern, string, maxSplit=0, flags=0):
# Split the source string by the occurrences of the pattern, return List of resulting substrings.
print("re.split:", re.split(r'\W+', "Hey, Mr./ Eve"))  # -> ['Hey', 'Mr', 'Eve']

# re.sub(pattern, repl, string)-> String // Substitute
# Return string obtained by replacing the leftmost non-overlapping occurrences of the pattern in string.
# repl can be either a string or callable.
print("re.sub:", re.sub(r'\sAnd\s', ' & ', "Baked Beans and Spam", flags=re.IGNORECASE))
# -> Baked Beans & Spam


# re.subn(pattern, repl, string, count=0, flags=0) -> tuple[AnyStr, int]: ...
# Return a 2-tuple containing (new_string, number).
# new_string is the string obtained by replacing the leftmost non-overlapping occurrences of the pattern
# in the source string by the replacement repl.
# number is the number of substitutions that were made.
print("re.subn:", re.subn(r'\sAnd\s', ' & ', "Baked Beans and Spam", flags=re.IGNORECASE))
# -> ('Baked Beans & Spam', 1)


# re.escape(pattern: AnyStr) -> AnyStr: ...
# Escape special characters in a string.
print("re.escape:", re.escape("I Asked what is this [a-9], he said \t ^WoW"))
# -> I\ Asked\ what\ is\ this\ \[a\-9\],\ he\ said\ \	\ \^WoW


# re.search()
regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "I was born on June 24")
if match is not None:
    print("\nIndex : [{}, {}]".format(match.start(), match.end()))  # -> [14, 21]
    print(match.groups())  # -> ('June', '24')
else:
    print("\nNo match!")

# Match Object...
# contains information about search and result.
# Getting string and regex of matched string:

match = re.search(r'(Ev)+', "Hi Eve! How is Evina ?")
print("\nre.search...")
if match:
    print("match object:", match)  # -> <re.Match object; span=(0, 1), match='H'>
    print("re:", match.re)  # # Returns regular expression object
    print("string:", match.string)  # Return passed string

    print("group:", match.group())  # returns the part of the string where there is a match
    print(match.groups())

    print(match.endpos)  # -> 22
    print(match.lastgroup)  # -> None
    print(match.lastindex)  # -> 1
    print(match.pos)  # -> 0

    print("start:", match.start(), "end:", match.end())  # -> 3 5
    print("span:", match.span())  # -> (3, 5)
else:
    print("Pattern not found!")

# re.match()
# match(pattern: Pattern[AnyStr], string: AnyStr, flags: _FlagsType = ...) -> Match[AnyStr] | None: ...
# Try to apply the pattern at the start of the string,
# returning a Match object, or None if no match was found.
print("\nre.match...")
match = re.match(regex, "I was born on June 24")
print("match object:", match)  # -> None
match = re.match(regex, "December 10, The day I was born")
print("match object:", match)  # -> <re.Match object; span=(0, 11), match='December 10'>

# re.fullmatch():
# fullmatch(pattern: Pattern[AnyStr], string: AnyStr, flags: _FlagsType = ...) -> Match[AnyStr] | None: ...
# Try to apply the pattern to all the string,
# returning a Match object, or None if no match was found.
print("\nre.fullmatch...")
match = re.fullmatch(regex, "I was born on June 24")
print(match)  # -> None
ch = re.fullmatch(regex, "Id 10083276 is expired!")
print(ch)
match = re.fullmatch(regex, "Id 10083276")
print(match)  # -> <re.Match object; span=(0, 11), match='Id 10083276'>
