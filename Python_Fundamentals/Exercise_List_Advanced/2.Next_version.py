version = input().split(".")
version_as_integer = int("".join(version))
next_version = version_as_integer + 1
next_version_as_list = [digit for digit in str(next_version)]
print(".".join(next_version_as_list))
