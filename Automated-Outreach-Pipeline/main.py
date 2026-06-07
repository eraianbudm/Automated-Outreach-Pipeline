from ocean import find_similar_companies
from prospeo import find_decision_makers
from eazyreach import find_email
from brevo import send_email

domain = input("Enter company domain: ")

companies = find_similar_companies(domain)

print("\nCompanies Found:")
print(companies)

choice = input("\nSend emails? (yes/no): ")

if choice.lower() != "yes":
    print("Process Stopped")
    exit()

for company in companies:

    print("\n========================")
    print("Company:", company)

    people = find_decision_makers(company)

    for person in people:

        print("\nName:", person["name"])
        print("Role:", person["role"])

        email = find_email(person["linkedin"])

        print("Email:", email)

        status = send_email(email, person["name"])

        print(status)