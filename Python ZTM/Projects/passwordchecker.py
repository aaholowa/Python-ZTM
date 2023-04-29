import re  # for regular expressions (used for validation)

# prompt user

email = str(input("Please enter your password\nYour password must:\n1.Be at least 8 characters long\n2.One upperscase letter\n3.One lowercase letter\n4.Contain one special character in '$' '%' '#' or '@'\n"))

# regular expression that checks for at least 8 chars, 1 uppercase char, 1 lowercase char, and at least one specila char
pattern = re.compile(
    "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#@$%]).{8,}$")

is_valid = pattern.fullmatch(email)

if is_valid != None:
    print(
        f"Password is valid\nPassword length is {len(email)} characters long:", end=' ')
    for items in email:
        print('*', end='')
elif is_valid == None:
    print("try again")
