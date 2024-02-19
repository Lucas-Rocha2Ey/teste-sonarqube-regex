import re  # python regex module

pattern = r"(?im)(?P<type>dirs|files|bytes)\s+[:]\s+(?P<total>\d+)" \
          r"\s+(?P<copied>\d+)\s+(?P<skipped>\d+)\s+(?P<mismatch>\d+)" \
          r"\s+(?P<failed>\d+)\s+(?P<extras>\d+)"

# Sample multi-line text
f = open('text_reged_example7.txt', 'r')
text = f.read()


print('Pattern:', pattern)
print('Text:', text)
print()

match_iter = re.finditer(pattern, text)

i = 1
for match in match_iter:
    print(f'Match:{i}')
    for key,value in match.groupdict().items():
        print(f"{key}:{value}")
    print()
    i += 1