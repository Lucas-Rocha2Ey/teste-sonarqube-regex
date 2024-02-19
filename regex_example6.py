import re  # python regex module

pattern = r"(?im)(?P<ts>^\d{4}/\d{2}/\d{2}\s*\d{2}[:]\d{2}[:]\d{2}\s+)ERROR\s+(?P<error>\d{1}.+)$"

# Sample multi-line text
text = """2016/05/28 19:24:30 ERROR 2 (0x00000002) Accessing Source Directory C:\RegularExpressionsWithDotNet\\robocopytest\\source2\\
The system cannot find the file specified."""


print('Pattern:', pattern)
print('Text:', text)
print()

match_iter = re.finditer(pattern, text)

i = 1
for match in match_iter:
    print(f'Match:{i}')
    print('ts:', match.group(1))
    print('error:', match.group(2))
    print("\n")
    i += 1