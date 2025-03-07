import re

text = "My email is example@mail.com"
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

match = re.search(pattern, text)
if match:
    print("Email Found:", match.group())  # Output: example@mail.com
