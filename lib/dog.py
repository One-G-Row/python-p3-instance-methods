#!/usr/bin/env python3

class Dog:
    # bark becomes a method of all instances of Dogs
    def bark(self):
        print("Woof!")
    def sit(self):
        print("The dog is sitting.")

fido = Dog()
fido.bark()
fido.sit()

snoopy = Dog()
snoopy.bark()
snoopy.sit()
    
