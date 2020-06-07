name = "perry sui"
print(type(name))

print(name.strip())

name = "    perry     "
print(name)
print(name.strip())  # removes all the white spaces before and after

name = "     perry"   # white space on left side of string
print(name.lstrip())  # removes white space from LHS

name= "perry      "
print(name.rstrip()) # removes white space from right side

name = "   perry      sui        "

print(name.strip())

name="perry sui"

print(name.title())  # capitalize first letter of each word

print(name.upper())   # makes whole sentence capital

print(name.lower())    # convert whole sentence to lower letters

print(name.startswith('a'))  # checks if string starts with specific letter

print(name.startswith('p'))  # checks if string starts with specific letter
                               # it will return True

print(name.startswith('P'))  # will return False

# startswith is case sensitive

print(name.endswith('a'))  # checks if string ends with specific letter --- False

print(name.endswith('i'))  # checks if string starts with specific letter -- True
                               # it will return True

print(name.endswith('I'))  # will return False

# startswith is case sensitive

# isalpha() checks if string has only alphabets

print(name.isalpha())   # prints False

name = "perry"

print(name.isalpha())   # prints True

print('asdd12344'.isalpha())   # prints False as it contains numbers too

# isdigit() checks for only digits
print('12345'.isdigit())  # return True

print('12345.234'.isdigit())  # return False






