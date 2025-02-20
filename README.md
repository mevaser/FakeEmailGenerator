FakeEmailGenerator

A small Python project to generate a list of fake email addresses (seeded by Faker) ending with @gmail.com. By default, the script (createAccounts.py) generates 2,000 email addresses and saves them to FakedEmail.txt.

Table of Contents
Features
Prerequisites
Installation & Usage
Code Explanation
Contributing
License
Features
Uses the Faker library to generate random usernames.
Appends @gmail.com to each username.
Automatically writes the generated emails to a text file, one address per line.
Prerequisites
Python 3.7+ (it’s recommended to use a more recent version).
The Faker library:
bash
Copy code
pip install Faker
Installation & Usage
Clone or download this repository to your local machine.
Make sure the file createAccounts.py is in your project folder.
Install dependencies (if needed):
bash
Copy code
pip install Faker
Run the script:
bash
Copy code
python createAccounts.py
Once the script finishes, a file named FakedEmail.txt will be created in the same folder, containing 2,000 email addresses.
Code Explanation
python
Copy code
from faker import Faker

def main():
    fake = Faker()                       # Create a Faker object for generating fake data

    list_of_emails = []
    for i in range(2000):               # Loop to generate 2,000 email addresses
        user_part = fake.user_name()    # Get a random username (without any domain)
        custom_email = user_part + "@gmail.com"
        list_of_emails.append(custom_email)
        print(list_of_emails[i])        # Print each email address to the console

    # Save to a text file
    with open("FakedEmail.txt", "w", encoding='utf-8') as file:
        for email in list_of_emails:
            file.write(email + "\n")

if __name__ == "__main__":
    main()
Faker object creation: Faker() lets us generate various random data such as usernames, names, addresses, phone numbers, and more.
Loop for email generation: Creates 2,000 email addresses, each constructed by appending "@gmail.com" to a randomly generated username.
Console output: Prints each email address to the terminal so you can see the progress.
Writing to file: The generated email addresses are written to the file FakedEmail.txt in the same folder.
Contributing
To change the number of generated addresses, simply edit the 2000 value in the loop.
Pull requests are welcome, whether for enhancements (e.g., using command-line arguments, supporting different domains, etc.) or bug fixes.
License
This project is released under the MIT License (or choose another license that fits your needs). Feel free to use, modify, and distribute it as you see fit.

Enjoy!
