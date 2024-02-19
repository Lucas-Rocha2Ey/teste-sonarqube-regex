import re  # python regex module

pattern = r"(?m).+(?<!\.09)$"

"""
We use a negative look behind to exclude products that end in .99

The capture pattern .+ matches all the characters in the line; however, at the end, we have a negative 
lookahead condition combined with end of text anchor (?<!\.99)$. The negative lookahead ensures that 
capture is successful only if the text does not end in ".99". The multiline flag is used to ensure 
$ checks each line in a multiline text

"""


# Sample multi-line text
text = """chair 4.98
coffee 1.99
fan 10.97
car 11499.59
banana 0.09"""

print('Pattern:', pattern)
print('Text:', text)
print()

match_iter = re.finditer(pattern, text)

print('Match:')
for match in match_iter:
    print(' ', match.group(0), 'at index:', match.start())