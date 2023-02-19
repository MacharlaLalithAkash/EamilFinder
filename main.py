import email_permutator as ep
from EmailValidator import app
import concurrent.futures
from colorama import Fore

firstName = input("First Name: ")
lastName = input("Last Name: ")
domainName = input("Domain Name: ")
email_array = ep.permute_email(firstName, lastName, domainName)

email_validator = app.MailChecker()


def check_deliverable(email):
    return email_validator.is_delivrable(email)


with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(check_deliverable, email) for email in email_array]

    for future, email in zip(concurrent.futures.as_completed(futures), email_array):
        isDeliverable = future.result()
        if isDeliverable['Delivrable'] == 'True':
            print(Fore.GREEN + isDeliverable['email'] + ' :Deliverable')
        else:
            print(Fore.RED + isDeliverable['email'] + ' :Not-Deliverable')
