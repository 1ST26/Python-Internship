import random

# Function to generate a random password
def generate_password():
    
    print("Welcome to the Password Generator!")

    # Ask the user for the desired password length
    length = int(input("Enter the length of the password: "))

    # Check if the length is valid
    if length < 4:
        print("Password length should be at least 4.")
        return

    # Define character sets for the password
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
    lowercase = "abcdefghijklmnopqrstuvwxyz"  
    numbers = "0123456789" 
    special = "@#$%&*"  

    # Combine all character sets
    all_characters = uppercase + lowercase + numbers + special

    # Initialize the password with one character from each category
    password = []
    password.append(random.choice(uppercase))  # Add one uppercase letter
    password.append(random.choice(lowercase))  # Add one lowercase letter
    password.append(random.choice(numbers))  # Add one number
    password.append(random.choice(special))  # Add one special character

    # Fill the rest of the password length with random characters
    for i in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Print the generated password
    print("Your password is: " + ''.join(password))

# Call the function to generate a password
generate_password()
