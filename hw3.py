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
print("######### Part 1, Task A #########")
coco.boredom = 10
print(coco)

brian = Explore_pet("Brian")
brian.hunger = 15
print(brian)


'''
Task B
'''
#add your codes inside of the Pet class
class Pet:
  boredom_decrement = -4
  hunger_decrement = -4
  boredom_threshold = 6
  hunger_threshold = 10
  word_list = ["hello"]

  def __init__(self, name="Coco"):
    self.name = name
    self.hunger = randrange(self.hunger_threshold)
    self.boredom = randrange(self.boredom_threshold)
    self.words = self.word_list[:]#an additional instance variable

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


print("######### Part 1, Task B&C #########")
oscar = Pet("Oscar")
teaching_session(oscar,['I am sleepy', 'You are the best','I love you, too'])
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


class Cat(Pet):
  def __init__(self,name, meow_count):
    super().__init__(name)
    self.meow_count = meow_count

  def hi(self):
    print(self.meow_count * super().hi())


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
    print(super().say())

#create two instances
print("######### Part 2 #########")
max = Poodle("Max")
max.say()
kitty = Cat("Kitty", 5)
kitty.hi()
