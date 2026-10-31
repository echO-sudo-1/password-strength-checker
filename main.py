MIN_LENGTH = 8

print("Password Strength Checker\n")

end = False

while end == False:
    password = input("Enter your password to check its strength: ")

    # Rule 1: minimum length 
    if len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
    else:
        print("Password meets the minimum length requirement.")

    # Rule 2: at least one digit 
    has_number = False

    for char in password:
        if char.isdigit():
            has_number = True
            break

    if has_number:
        print("Password contains at least one number.")
    else:
        print("Password must contain at least one number.")

    # Rules 3 and 4: at least one uppercase and one lowercase letter
    has_uppercase = False
    has_lowercase = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        if char.islower():
            has_lowercase = True

    if has_uppercase:
        print("Password contains at least one uppercase letter.")
    else:
        print("Password must contain at least one uppercase letter.")

    if has_lowercase:
        print("Password contains at least one lowercase letter.")
    else:
        print("Password must contain at least one lowercase letter.")

    # Scoring: one point for each rule that is satisfied
    points = 0

    if len(password) >= MIN_LENGTH:
        points += 1
    if has_number:
        points += 1
    if has_uppercase:
        points += 1
    if has_lowercase:
        points += 1

    # Final rating 
    if points == 4:
        print("Strong Password")
    elif points >= 2:
        print("Medium Password")
    else:
        print("Weak Password")

    # Ask whether to continue 
    answer = input("\nPress Enter to check another password or type 'quit' to exit:\n")
    if answer == "quit":
        end = True
        print("Exiting Password Strength Checker.")
