import re  # python regex module

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!?^$]).+$"  # pattern

test_data = ["Av!1", "abcd", "Av&1", "!cA3R"]  # list of input

print('Pattern:', pattern)
print()

for text in test_data:
    print('Text:', text)
    match = re.search(pattern, text)

    if match:
        print(' **match**', match.group(0), 'at index:', match.start())