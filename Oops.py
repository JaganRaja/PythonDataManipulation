''' class parrot:

    #class attribute
    species = "bird"

    #instance attribute
       
    def __init__ (self,name,age):
        self.name = name
        self.age = age

    # instance method
    def sing(self,song):
        return "{} sings {}".format(self.name, song)
    def dance(self):
        return "{} is now dancing at this age {}".format(self.name, self.age)

#instatiate the parrot class

# instantiate the object
blu = parrot("blu",11)




# call our instance methods
print(blu.sing("happy"))
print(blu.dance())
 woo = parrot ("woo", 18)



    # access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))


#access the instance attributes
print("{} is the {} old".format(blu.name,blu.age))
print("{} is the {} old".format(woo.name,woo.age))

 '''

''' # parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisthis(self):
        print("Bird")
    
    def swim(self):
        print("swim faster")

# child class

class Penguin(Bird):
    
    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")


    def whoisthis(self):
        print("Penguin")

    def run(self):
        print("Run Faster")

peggy = Penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()

birdy = Bird()

birdy.whoisthis()

 '''
''' 
class computer:
    
    def __init__(self):
        self.__maxprice =  123
    
    def sell(self):
        print("selling price is {}".format(self.__maxprice))
    
    def setMaxPrice(self,price):
        
        self.__maxprice = price

c =  computer()

c.sell()

#change the price

c.__maxprice = 234
c.sell()

# using setter function

c.setMaxPrice(988)
c.sell() '''

class Parrot:
    
    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot cant swim")

class Penguin:
    
    def fly(self):
        print("Penguin cant fly")

    def swim(self):
        print("Penguin can swim")

# common interface

def flyingTest(bird):
    bird.fly()

#instantiate objects

blu = Parrot()
peggy = Penguin()


#passing the object
flyingTest(blu)
flyingTest(peggy)

