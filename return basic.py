def greet_user(msg, user):
    #data = (msg, user)
    return f'{msg.title()}, {user.title()}'
greetings = greet_user(msg = "hi ", user = "manju")
print(greetings)


def square(num):
    return num*num
print(square(2))
