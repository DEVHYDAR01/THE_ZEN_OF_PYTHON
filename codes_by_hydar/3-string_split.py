
#!/usr/bin/env python3

money = "my name is hydar, i am funny, i love coding"
dollar = money.split(", ")
print(dollar)
addlist = input("enter what you want to append:")
listadded = addlist.split(", ")
dollar.extend(listadded)
print(dollar)
