'''
SI 507 W18 homework 3: Classes and Inheritance
Name: Siyu Jia
Your discussion section: 009, Jie-wei Wu
People you worked with:

######### DO NOT CHANGE PROVIDED CODE ############
'''

#######################################################################
#---------- Part 1: Class
#######################################################################

'''
Task A
'''
import sys
from random import randrange


class Explore_pet:
  boredom_decrement = -4
  hunger_decrement = -4
  boredom_threshold = 6
  hunger_threshold = 10
  def __init__(self, name="Coco"):
    self.name = name
    self.hunger = randrange(self.hunger_threshold)
    self.boredom = randrange(self.boredom_threshold)

  def mood(self):
    if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
        return "happy"
    elif self.hunger > self.hunger_threshold:
        return "hungry"
    else:
        return "bored"

  def __str__(self):
    state = "I'm " + self.name + '. '
    state += 'I feel ' + self.mood() + '. '
    if self.mood() == 'hungry':
      state += 'Feed me.'
    if self.mood() == 'bored':
      state += 'You can teach me new words.'
    return state
coco = Explore_pet()

#your code begins here . . .
# print("######### Part 1, Task A #########")
# coco.boredom = 10
# print(coco)
#
# brian = Explore_pet("Brian")
# brian.hunger = 15
# print(brian)


'''
Task B
'''
#add your codes inside of the Pet class
class Pet:
  boredom_decrement = -4
  hunger_decrement = -4
  boredom_threshold = 6
  hunger_threshold = 10
  words = ["hello"]

  def __init__(self, name="Coco", age=0):
    self.name = name
    self.hunger = randrange(self.hunger_threshold)
    self.boredom = randrange(self.boredom_threshold)
    self.words = self.words[:]#an additional instance variable
    self.age = age

  def mood(self):
    if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
        return "happy"
    elif self.hunger > self.hunger_threshold:
        return "hungry"
    else:
        return "bored"

  def __str__(self):
    state = "I'm " + self.name + '. '
    state += 'I feel ' + self.mood() + '. '
    if self.mood() == 'hungry':
      state += 'Feed me.'
    if self.mood() == 'bored':
      state += 'You can teach me new words.'
    return state

#additional methods
  def clock_tick(self):
    self.hunger += 2
    self.boredom += 2

  def say(self):
    print("I know how to say")
    for word in self.words:
      return word

  def teach(self, word):
    self.words.append(word)
    self.boredom = max(0, self.boredom + self.boredom_decrement)

  def feed(self):
    self.hunger = max(0, self.hunger + self.hunger_decrement)

  def hi(self):
      return self.words[randrange(len(self.words))]




'''
Task C
'''

def teaching_session(my_pet,new_words):
  #your code begins here . . .
  for word in new_words:
    my_pet.teach(word) ## .append??
    print(my_pet.hi())
    print(my_pet)

    if my_pet.mood == "hungry":
      my_pet.feed()

    my_pet.clock_tick()
    #print(my_pet.hunger)
    #print(my_pet.boredom)


# print("######### Part 1, Task B&C #########")
# oscar = Pet("Oscar")
# teaching_session(oscar,['I am sleepy', 'You are the best','I love you, too'])
# print(kitty.words)
# print(kitty)
# print(kitty.hunger)
# print(kitty.boredom)





#######################################################################
#---------- Part 2: Inheritance - subclasses
#######################################################################
'''
Task A: Dog and Cat
'''
#your code begins here . . .
class Dog(Pet):

  def __str__(self):
    return super().__str__()[:-2] + ", arrrf!"

  def clock_tick(self):
    super().clock_tick()
    if self.age > 16:
      return "leave the world"
    self.age += 2





class Cat(Pet):
  def __init__(self,name, meow_count):
    super().__init__(name)
    self.meow_count = meow_count

  def hi(self):
    return self.meow_count * super().hi()

  def clock_tick(self):
    super().clock_tick()
    if self.age > 15:
      return "leave the world"
    self.age += 2


# lulu = Dog("Lulu")
# print(lulu)
# tiger = Cat("Tiger",3)
# print(tiger.meow_count)
# print(tiger.hi())


'''
Task B: Poodle
'''
#your code begins here . . .
class Poodle(Dog):

  def dance(self):
    return "Dancing in circles like poodles do!"

  def say(self):
    print(self.dance())
    return super().say()


# #create two instances
# print("######### Part 2 #########")
# max = Poodle("Max")
# print(max.say())
# kitty = Cat("Kitty", 5)
# print(kitty.hi())

'''
Extra credit 1
'''

def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None # no pet matched

pet_types = {'dog': Dog, 'poodle': Poodle, 'cat': Cat}
def whichtype(adopt_type="general pet"):
    return pet_types.get(adopt_type.lower(), Pet)

def play():
    animals = []

    option = ""
    base_prompt = """
        Quit
        Adopt <petname_with_no_spaces> <adopt_type - choose dog, cat, poodle, or another unknown pet type>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: """
    feedback = ""
    while True:
        action = input(feedback + "\n" + base_prompt)
        feedback = ""
        words = action.split()
        if len(words) > 0:
            command = words[0]
        else:
            command = None
        if command == "Quit":
            print("Exiting...")
            return
        elif command == "Adopt" and len(words) > 1:
            if whichone(animals, words[1]):
                feedback += "You already have a pet with that name\n"
            else:
                # figure out which class it should be
                if len(words) > 2:
                    Cl = whichtype(words[2])
                else:
                    Cl = Pet
                # Make an instance of that class and append it
                animals.append(Cl(words[1]))
        elif command == "Greet" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again.\n"
                print()
            else:
                pet.hi()
        elif command == "Teach" and len(words) > 2:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.teach(words[2])
        elif command == "Feed" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.feed()
        else:
            feedback+= "I didn't understand that. Please try again."

        for pet in animals:
            pet.clock_tick()
            feedback += "\n" + pet.__str__()


play()


userInput = input("Enter 'R' to restart or 'X' to exit").capitalize()

if userInput == "R":
  play()
else:
  print('Goodbye.')
  play().quit()
