password = input()

checks = (str.isdigit, str.isupper, str.islower)

length_ok = len(password) >= 7

rules_ok = all(any(f(char) for char in password) for f in checks)

print(("NO", "YES")[length_ok and rules_ok])