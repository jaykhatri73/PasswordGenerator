import random
import string

# collecting different types of characters


def generate_password():
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

# different combinations of each group
    characters1 = lowercase_letters
    characters2 = lowercase_letters + uppercase_letters + numbers
    characters3 = lowercase_letters + uppercase_letters + symbols

    password = []

    password.append(''.join(random.choice(characters1)
                            for i in range(5)))

    password.append(''.join(random.choice(characters2)
                            for i in range(5)))

    password.append(''.join(random.choice(characters3)
                            for i in range(5)))

    password = '-'.join(password)
    return password


# main function
password = generate_password()
print(password)
