class employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"the class value is {cls.a}")
        @property
        def name(self):
            return self._name
        @name.setter
        def name(self, value):
            self.fname = value.split(" ")[0]
            self.lname = value.split(" ")[1]
        
e = employee()

e.a = 5
e.name ="Atif Bashir"
print(e.name)
e.show()