#importing required modules and files
import random
from datetime import datetime

#bot greets and introduces itself
def greet_and_introduce():
    #list of responses
    responses = [
        "Hi There I'm MathBot. I can help you to do some calculations. May I know your name please?",
        "Hey I'm MathBot. It's nice to meet you. How can I help you"
    ]
    #picks a response at random
    print(random.choice(responses))

#greets the user according to the current time
def get_timeofday_greeting():
    current_time = datetime.now()
    timeofday_greeting = "Good Morning"
    if current_time.hour > 12 and current_time.hour < 17:
        timeofday_greeting = "Good Afternoon"
    elif current_time.hour >= 17 and current_time.hour < 22 :
        timeofday_greeting = "Good Evening"
    elif current_time.hour > 22:
        timeofday_greeting = "Yoo, It's late!!!"
    return timeofday_greeting


def welcome(name):
    #list of messages
    messages = [
        "Nice to meet you",
        "Let's have some good time together"
    ]
    print(f"{get_timeofday_greeting()}, {random.choice(messages)}")
