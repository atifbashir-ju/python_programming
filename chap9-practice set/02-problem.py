class animal:
    @staticmethod
    def walk():
        print("Animal is walking")
class pets:
    @staticmethod
    def pet_info(): 
        print("Pets are friendly animals")
class dog(pets):
    @staticmethod
    def bark():
        print("Bhav Bhav")

d = dog()
d.bark()
d.pet_info()
animal.walk()   

