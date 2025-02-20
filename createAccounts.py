from faker import Faker

def main():
    fake = Faker()

    list_of_emails = []
    for i in range(2000):
        user_part = fake.user_name()
        custom_email = user_part + "@gmail.com"
        list_of_emails.append(custom_email)
        print(list_of_emails[i])

    with open("FakedEmail.txt", "w", encoding='utf-8') as file:
        for email in list_of_emails:
            file.write(email + "\n")
if __name__ == "__main__":
    main()