import re  # python regex module

pattern = r"(?im)^\s*(?P<type>source|dest)\s*[:]\s*(?P<path>.+)$"

# Sample multi-line text
text = """Source : C:\\RegularExpressionsWithDotNet\\robocopytest\\source\\தமிழ்\\हिन्दी\\English
Dest : C:\\RegularExpressionsWithDotNet\\robocopytest\\destn\\"""

print('Pattern:', pattern)
print('Text:', text)
print()

match_iter = re.finditer(pattern, text)

i = 1
for match in match_iter:
    print(f'Match:{i}')
    print('type:', match.group(1))
    print('dir:', match.group(2))
    print("\n")
    i += 1