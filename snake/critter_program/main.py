#Critter Project
#Danson Coats
import random
class Critter(object):
    days = 0
    hours = 0

    def __init__(self):
        self.age = 0
        self.health = 100
        self.hunger = 0
        self.height = 0
        self.weight = 0
        self.name = " "
        self.happy = 100
        self.isAlive = True

        #setters
    def setName(self,name):
        if len(name) > 4 or len(name) < 4:
            if "uck" not in name:
                if "sh" not in name:
                    if "unt" not in name:
                            self.name = name

    def die(self):
        print("Your pet has died, you probably shouldn't own a pet in real life.")
        self.isAlive = False

    #getters
    def getName(self):
        return self.name
    def gethealth(self):
        return self.health
    def gethunger(self):
        return self.hunger
    def getheight(self):
        return self.height
    def getweight(self):
        return self.weight
    def gethappy(self):
         return self.happy
    def getisAlive(self):
        return self.isAlive

    def intro(self):
        print("Hello My name is "+self.name)

    def feed(self,food):
        if food == "pizza":
            self.hunger -= 8
        elif food == "cheese burger":
            self.hunger -= 18
        elif food == "steak":
            self.hunger -= 25
        elif food == "taco":
            self.hunger -= 5
        elif food == "cheesecake":
            self.hunger -= 100
        elif food == "poison":
            self.hunger -= 50
            self.die()
        else:
            self.hunger -= 10


    def pass_time(self,hours):
        for i in range(hours):
            self.hunger += 5
            if self.hunger > 50:
                self.weight -= .5
                self.happy -= 15
                self.health -= 5
            if self.hunger < 0:
                self.weight += .5
                self.happy += 15
                self.health -= 2
            self.happy -= 5
            self.height += .01
            Critter.hours += 1
            if hours == 5:
                Critter.days += 1
                Critter.hours = 0
            if Critter.days % 10 == 0:
                self.age += 1
            if self.age >=99:
                chance = random.randint(5)
                if chance ==0:
                    self.die()

    def play(self,time):
        self.pass_time(self,time)
        self.happy += 10 * time
        self.health += 2 * time
        if self.happy > 100:
            self.happy = 100
        if self.health > 100:
            self.health = 100

    def hud(self):
        print("Pet Name: "+self.getName())
        print("pet height: "+str(self.getheight()))
        print("pet weight: "+str(self.getweight()))
        print("pet age: "+str(self.age))
        health = self.gethealth()
        if health > 80:
            print("Health: Great")
        elif health > 60:
                print("Health: Good")
        elif health > 50:
            print("Health: fair")
        elif health == 0:
            self.die()
        else:
            print ("Health: poor")

        hunger = self.gethunger()
        if hunger > 40:
            print("Hunger: Starving")
        elif hunger > 20:
            print("Hunger: Really hungry")
        elif hunger > 10:
            print("Hunger: Full")
        else:
            print("Hunger: Hungry")
        if hunger == 100:
            self.die()
        if hunger == -100:
            self.die()

        happy = self.gethappy()
        if happy > 50:
            print("Happy: Happy")
        elif happy > 35:
            print("Happy: Grumpy")
        else:
            print("Happy: mad")



def main():
    pet = Critter()
    pet.setName(input("What is your pets name"))
    pet.hud()
    while pet.getisAlive():
        pet.pass_time(1)
        answer = input("What would you like to do with your pet (Feed, play, or ignore)").lower()
        if answer == "feed":
            food = input("what do you want to feed your pet").lower()
            pet.feed(food)
        if answer == "play":
            time = int(input("how long will you play with your pet"))
            pet.play(time)
        pet.hud()
main()
