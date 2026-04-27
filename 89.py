#import re
text = "python is a high level programming language.python is object oriented language.python is widely used language."
pattern = r"object"
matches = re.search(pattern, text)
if matches:
    print("pattern found:", matches.group())
else:    print("pattern not found")