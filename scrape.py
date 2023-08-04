from bs4 import BeautifulSoup

import pandas as pd


def export_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)


with open("partnermails.html") as html_file:
    soup = BeautifulSoup(html_file, "lxml")


def user_details(email):
    if "@" not in email:
        return {"First Name": email, "Last Name": " ", "email": email}
    elif "." not in email.split("@")[0]:
        return {
            "First Name": email.split("@")[0].capitalize(),
            "Last Name": " ",
            "email": email,
        }
    else:
        first_name, last_name = email.split("@")[0].split(".")
        return {
            "First Name": first_name.capitalize(),
            "Last Name": last_name.capitalize(),
            "email": email,
        }


people = []

for email in soup.find_all("span", class_="account-name"):
    email = email.text
    print(email)
    # print(user_details(email))
    # people.append(user_details(email))
    # print(people)

# export_to_excel(people, "AccessPowerSysMails.xlsx")
