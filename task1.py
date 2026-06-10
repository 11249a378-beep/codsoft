import datetime
import random
import re

# User Information
name = ""
age = ""
address = ""

# Indian-style Greeting
utc_time = datetime.datetime.utcnow()
india_time = utc_time + datetime.timedelta(hours=5,minutes=30)
print("Indian Time:",india_time)
current_hour = india_time.hour
print("Current hour from server:",current_hour)
print("Current datatime from server:",
datetime.datetime.now())
if 5 <= current_hour < 12:
    greeting = "Good Morning"
elif 12 <= current_hour < 17:
    greeting = "Good Afternoon"
elif 17  <= current_hour < 21:
    greeting = "Good Evening"
else:
    greeting = "Good Night"

print("=" * 50)
print("          SMART CHATBOT")
print("=" * 50)
print(f"Bot: {greeting}! How can I help you today?")

# Jokes
jokes = [
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the math book sad? Because it had too many problems!"
]

while True:
    user = input("\nYou: ")
    text = user.lower().strip()

    # Exit
    if text in ["bye", "exit", "quit"]:
        print("Bot: Thank you for chatting with me!")
        print("Bot: Goodbye! Have a nice day.")
        break

    # Greetings
    elif text in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    # How are you
    elif "how are you" in text:
        print("Bot: I'm doing great. Thanks for asking!")

    # Thank You
    elif "thank you" in text or "thanks" in text:
        print("Bot: You're welcome! Happy to help.")

    # Sorry
    elif "sorry" in text:
        print("Bot: No worries. It's okay!")

    # Save Name
    elif "my name is" in text:
        name = user[11:].strip()
        print(f"Bot: Nice to meet you, {name}!")

    # Recall Name
    elif "what is my name" in text:
        if name:
            print(f"Bot: Your name is {name}.")
        else:
            print("Bot: I don't know your name yet.")

    # Save Age
    elif "years old" in text:
        nums = re.findall(r"\d+", text)
        if nums:
            age = nums[0]
            print(f"Bot: Okay! You are {age} years old.")

    # Recall Age
    elif "what is my age" in text:
        if age:
            print(f"Bot: You are {age} years old.")
        else:
            print("Bot: I don't know your age yet.")

    # Save Address
    elif "my address is" in text:
        address = user.replace("my address is", "").replace("My address is", "").strip()
        print("Bot: Address saved successfully.")

    # Recall Address
    elif "what is my address" in text:
        if address:
            print(f"Bot: Your address is {address}.")
        else:
            print("Bot: I don't know your address yet.")

    # Time
    elif "time" in text:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Bot: Current time is {current_time}")

    # Date
    elif "date" in text:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {current_date}")

    # Joke
    elif "joke" in text:
        print("Bot:", random.choice(jokes))

    # Arithmetic
    elif any(op in text for op in ["+", "-", "*", "/"]):
        try:
            result = eval(text)
            print(f"Bot: Answer = {result}")
        except:
            print("Bot: Please enter a valid calculation.")

    # General Knowledge
    elif "capital of india" in text:
        print("Bot: The capital of India is New Delhi.")

    elif "what is python" in text:
        print("Bot: Python is a popular programming language used for AI, web development, automation, and more.")

    elif "what is ai" in text:
        print("Bot: AI stands for Artificial Intelligence. It enables computers to learn and solve problems.")

    elif "who made you" in text:
        print("Bot: I was created using Python programming.")

    # Default Response
    else:
        print("Bot: Sorry, I don't understand that yet. Please ask something else.")