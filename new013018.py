#!/usr/bin/python

ar1 = '5'
var2 = 'fuck'
print("I am {} years old and {} it".format(var1, var2))
var3 = input("What? ")

print("I said {}".format(var3))


def user_name():
    return "Rolf"


def greeting():
    return "Hello, {}, how are you?".format(user_name())

jammies = greeting()
print(jammies)