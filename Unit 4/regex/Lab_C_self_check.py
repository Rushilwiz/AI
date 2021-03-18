import sys; args = sys.argv[1:]

PATTERNS = [

# Q50: Match all words where some letter appears twice in the same word.
r'(\w)+\w*\1\w*',

# Q51: Match all words where some letter appears four times in the same word.
r'(\w)+(\w*\1){3}\w*',

# Q52: Match all non-empty binary strings with the same number of 01 substrings as 10 substrings.
r'^1[10]*1$|^0[10]*0$',

# Q53: Match all six letter words containing the substring cat.
r'\b(?=\w*cat)\w{6}\b',

# Q54: Match all 5 to 9 letter words containing both the substrings bri and ing.
r'\b(?=\w*bri)(?=\w*ing)\w{5,9}\b',

# Q55: Match all six letter words not containing the substring cat.
r'\b(?!\w*cat)\w{6}\b',

# Q56: Match all words with no repeated characters.
r'\b((\w)(?!\w*\2))+\b',

# Q57: Match all binary strings not containing the forbidden substring 10011.
r'^(?!.*10011)[01]*$',

# Q58: Match all words having two different adjacent vowels.
r'\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*',

# Q59: Match all binary strings containing neither 101 nor 111 as substrings.
r'^(?!.*1.1)[01]*$'

]

idx = int(args[0])-50
print(PATTERNS[idx])