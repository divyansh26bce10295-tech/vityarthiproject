class Account:
    def __init__(self, acc_no, principal):
        self.acc_no = acc_no
        self.principal = principal

    def display(self):
        print("The Account Number is", self.acc_no)
        print("The Principal Amount is Rs.", self.principal)


class Simple_Interest(Account):
    def __init__(self, acc_no, principal, rate, time):
        super().__init__(acc_no, principal)
        self.rate = rate
        self.time = time

    def Interest(self):
        SI = (self.principal * self.rate * self.time) / 100
        return SI

    def display(self):
        super().display()
        print("The Rate of Interest is", self.rate,
              "and Time is", self.time)


class Compound_Interest(Account):
    def __init__(self, acc_no, principal, rate, time):
        super().__init__(acc_no, principal)
        self.rate = rate
        self.time = time

    def Interest(self):
        CI = self.principal * ((1 + self.rate / 100) ** self.time) - self.principal
        return CI

    def display(self):
        super().display()
        print("The Rate of Interest is", self.rate,
              "and Time is", self.time)


acc_no = int(input("Enter Account Number: "))
principal = float(input("Enter Principal Amount: "))

ch = 0

while ch != 3:
    print("\nMain Menu")
    print("Press 1 to check Simple Interest")
    print("Press 2 to check Compound Interest")
    print("Press 3 to Exit")

    ch = int(input("Please Enter Your Choice: "))

    if ch == 1:
        rate = float(input("Rate: "))
        time = float(input("Time: "))

        obj = Simple_Interest(acc_no, principal, rate, time)

        SI = obj.Interest()
        obj.display()

        print("Simple Interest:", SI)

    elif ch == 2:
        rate = float(input("Rate: "))
        time = float(input("Time: "))

        obj = Compound_Interest(acc_no, principal, rate, time)

        CI = obj.Interest()
        obj.display()

        print("Compound Interest:", CI)

    elif ch == 3:
        print("THANK YOU!")

    else:
        print("Invalid Choice")
