import random
import string

def generate_email():
    """Generate a random email address."""
    # Generate a random string for the local part of the email
    local_part_length = random.randint(5, 10)  # You can adjust the length range as needed
    local_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=local_part_length))
    
    # List of common email domains
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'example.com']
    
    # Randomly select a domain
    domain = random.choice(domains)
    
    # Concatenate local part and domain to form the email address
    email = local_part + '@' + domain
    return email

def save_emails_to_file(num_lines, filename):
    """Generate random email addresses and save them to a file."""
    with open(filename, 'w') as file:
        for _ in range(num_lines):
            email = generate_email()
            file.write(email + '\n')

# Asking for user input
num_lines = int(input("Number of lines to generate: "))
filename = input("Enter the name of the text file: ")

# Call the function
save_emails_to_file(num_lines, filename)
print(f"{num_lines} emails saved to {filename}.")
