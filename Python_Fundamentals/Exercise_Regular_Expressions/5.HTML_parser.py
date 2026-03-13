import re

html_input = input()

title_match = re.search(r'<title>(.*?)</title>', html_input)
title = title_match.group(1) if title_match else ""

body_match = re.search(r'<body>(.*?)</body>', html_input)
body_content = body_match.group(1) if body_match else ""

tag_pattern = r'<.*?>'
cleaned_content = re.sub(tag_pattern, '', body_content)

cleaned_content = cleaned_content.replace('\\n', ' ')
cleaned_content = " ".join(cleaned_content.split())

print(f"Title: {title}")
print(f"Content: {cleaned_content}")