import re  # python regex module

pattern = r"(?m)^(?!(exl)|(xle)).+$"

# Sample multi-line text
text = """exl-accord
ex-accord
se-camry
xle-camry
exl-civic"""

print('Pattern:', pattern)
print('Text:', text)
print()

match_iter = re.finditer(pattern, text)

print('Match:')
for match in match_iter:
    print(' ', match.group(0), 'at index:', match.start())