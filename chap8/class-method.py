class employee:
    a = 1
    @classmethod
    def show(self):
        print(f"the class value is {self.a}")
e = employee()
e.a = 5
e.show()