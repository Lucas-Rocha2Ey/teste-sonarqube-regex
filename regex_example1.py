import re  # python regex module

pattern = r"(?m)(?P<ip>\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3})(?P<http>.GET)" \
          r"(?P<resource>.[/]\w+([.]\w+){1})(?P<bytes>.\d+)" \
          r"(?P<duration>.\d+[.]\d{3})"

"""
(?m) => since the input contains multiple lines, we need to use the multi-line flag to ensure the 
anchors ^ and $ process each line separately

(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) => This pattern captures the IP address
The IP address is followed by one or more spaces. The log entries are delimited by space or tab. 
\s+ captures all whitespace characters



(?P<http>\w+) => This pattern captures the HTTP request method



(?P<resource>/[\w.]+) => This pattern captures a / followed by any word character or "." 
character. For example, this pattern will match the text /index.html

Similarly, we capture the bytes and duration values

"""

# Sample multi-line text
text = """192.168.0.20 GET /index.html 32504 1.030
192.168.0.55 GET /index.html 32504 0.500"""

print('Pattern:', pattern)
print('Text:', text)
print()

match_iter = re.finditer(pattern, text)

print('Match:')
for match in match_iter:
    print('', match.group(0), 'at index:', match.start())

    for key, value in match.groupdict().items():
        print('  ', key, ':', value)