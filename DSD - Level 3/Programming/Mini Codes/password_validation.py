print("Hello, welcome to the password validation. Please enter your password to check if it meets the requirements!")

print("==== PASSWORD REQUIREMENTS ====")
print("(1): Is in the range of 8 to 16 characters.")
print("(2): Contains special characters.")
print("(3): Contains a mix of both uppercases and lowercases.")

passed_requirements = [""] # length, special, cases

while True:
    print("\nEnter your password below")
    password = input("Password: ")

    pass_length = len(password)

    def contains_special_character(s):
        special_characters = set('!@#$%^&*()_+{}:"<>?[];\'\\,./`~')
        return bool(set(s) & special_characters)

    if pass_length >= 8 and pass_length <= 16:
        passed_requirements.append("length")
        
    special_chars = contains_special_character(password)
    if special_chars == True:
        passed_requirements.append("special")

    uppercases = False
    lowercases = False

    # checks if it has any uppercases
    for case in password:
        if case.islower():
            uppercases = True
            break

    #checks if it has any lowercases
    for case in password:
        if case.isupper():
            lowercases = True
            break

        if uppercases == True and lowercases == True:
            passed_requirements.append("cases")

    # Results calcuation
    print("==== PASSWORD VALIDATION RESULTS ====")
    result = 0

    if "length" in passed_requirements:
        print("[1]: In range of 8 to 16 characters. - [TRUE]")
        result +=1
    else:
        print("[1]: In range of 8 to 16 characters. - [FALSE]")

    if "special" in passed_requirements:
        print("[2]: Contains special characters. - [TRUE]")
        result +=1
    else:
        print("[2]: Contains special characters. - [FALSE]")

    if "cases" in passed_requirements:
        print("[3]: Contains mix of uppercase and lowercases. - [TRUE]")
        result +=1
    else:
        print("[3]: Contains mix of uppercase and lowercases. - [FALSE]")

    print(f"Password Rating - {result}/3!")
