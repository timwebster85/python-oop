import random
import string


chars = string.ascii_lowercase + string.digits + '!"£$%^&*('
domains = ['yahoo.com', 'gmail.com', 'outlook.com']
names = ["jake", "jon", "bill"]

for name in names:
    name_extra = ''.join(random.choice(string.digits) for _ in range(5))
    
    username = name.lower() + name_extra + '@' + random.choice(domains)

    print(username)
