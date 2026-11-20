user_greeting = input("Greeting: ")
user_greeting = user_greeting.lower().strip()

if user_greeting.startswith("hello"):
    print("$0")
elif user_greeting.startswith("h"):
    print("$20")
else:
    print("$100")