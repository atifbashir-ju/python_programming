class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    def skill3(self):
        print("Coding")

c = Child()
c.skill1()   # Father se
c.skill2()   # Mother se
c.skill3()   # Child ka apna
