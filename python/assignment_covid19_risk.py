age = input("Are you a cigarette addict older than 75 years old? (Only Yes/No) :").title()
chronic = input("Do you have a severe chronic disease? (Only Yes/No) :").title()
immune = input("Is your immune system too weak? (Only Yes/No) : ").title()

if age == "Yes" and chronic == "Yes" and immune == "Yes":
  print("You are in risky group")
else:
  print("You are not in risky group")


while True :
  age = input("Are you a cigarette addict older than 75 years old? (Only Yes/No) :").title()
  chronic = input("Do you have a severe chronic disease? (Only Yes/No) :").title()
  immune = input("Is your immune system too weak? (Only Yes/No) : ").title()
  if (age != "Yes" and age != "No") or (chronic != "Yes" and chronic != "No")  or (immune != "Yes" and immune != "No"):
   print("Please You could enter correct word")
  elif age == "Yes" and chronic == "Yes" and immune == "Yes":
    print("You are in risky group")
    break
  else :
   print("You are not in risky group")
   break