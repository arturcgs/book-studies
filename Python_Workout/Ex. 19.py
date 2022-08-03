
def passwd_to_dict(file_path):
    with open(file_path) as f:
        username_id = {}
        for line in f:
            if line[0] == "#": #checking if it beggins with #
                continue
            items = line.split(':') #splitting in the :
            username_id[items[0]] = items[2] #adding the username as key and ID as item
        return username_id

#saving the dictionary to a varible
user_ids = passwd_to_dict('files/password.txt')

#printing as a pretty table
print(f"|{'-':-^24}|------|") #header
print(f"|{'Username':^24}|{'ID':^6}|") #header
print(f"|{'-':-^24}|------|") #header
for key, item in user_ids.items():
    print(f"|{key:^24}|{item:^6}|") #printind each item
print(f"|{'_':_^24}|______|") #finishing the table