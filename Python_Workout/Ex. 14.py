menu = {
    'batata': 12,
    'xis-burgui': 35,
    'crepe': 15,
    'suco': 8,
    'bife foda': 62,
    'tapioca': 10
}

def restaurante(menu):
    total = 0
    while True:
        order = input("Order: ").strip().lower()
        if not order:
            print(f"Your total is {total}")
            break
        if order in menu:
            total += menu[order]
            print(f"{order} costs {menu[order]}, total is {total}")
        else:
            print("What kind of restaurant do you think we are?")

#restaurante(menu)

#beyond 1
'''Create a dict in which the keys are usernames and the values are passwords,
both represented as strings. Create a tiny login system, in which the user must
enter a username and password. If there is a match, then indicate that the user
has successfully logged in. If not, then refuse them entry. (Note: This is a nice
little exercise, but please never store unencrypted passwords. It’s a major security risk.)'''

id_pass = {
    'arturcgs': 'batata',
    'luxirio': 'senhaforte',
    'allefante': 'monoaminas',
}

def log_in(id_pass):
    user = input("What's the username: ").strip().lower()
    password = input("Type the password: ").strip()
    if user in id_pass:
        if password == id_pass[user]:
            print("Access granted!")
        else:
            print("Wrong password")

    else:
        print(f"User {user} not found.")

log_in(id_pass)