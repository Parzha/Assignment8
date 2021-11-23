import math
class fraction:
    def __init__(self, x, y):
        self.soorat = x
        self.makhraj = y

    def show_friction(self):
      print(f'{self.soorat} / {self.makhraj}')

    def multi(self,b):
       result_soorat = self.soorat * b.soorat
       result_makhraj = self.makhraj * b.makhraj
       result = fraction(result_soorat,result_makhraj)
       return result


    def divi(self,b):
      result_soorat = self.soorat * b.makhraj
      result_makhraj = self.makhraj * b.soorat
      result = fraction(result_soorat, result_makhraj)
      return result

    def sub(self,b):
      result_soorat = (self.soorat * b.makhraj) - (self.makhraj * b.soorat)
      result_makhraj = self.makhraj * b.makhraj
      result = fraction(result_soorat, result_makhraj)
      return result


    def add(self,b):
      result_soorat = (self.soorat * b.makhraj) + (self.makhraj * b.soorat)
      result_makhraj = self.makhraj * b.makhraj
      result = fraction(result_soorat, result_makhraj)
      return result


    def simplify(self):

      result_gcd = math.gcd(self.soorat, self.makhraj)
      result_soorta = self.soorat / result_gcd
      result_makhraj = self.makhraj / result_gcd
      result = fraction(result_soorta,result_makhraj)
      return result





print('''What operaterions you want to do with your fractions
        1- Addition  
        2- Subtraction
        3- Multiplication
        4- Division
        5- Simplification
        6- Exit
         ''')

while (True):
    user_input_menu = int(input("Enter your choice from the list->"))

    if user_input_menu == 1:

        sorat1_str, makhraj1_str = input("Please enter the first numerator and first denominator").split()
        sorat2_str, makhraj2_str = input("Please enter the second numerator and second denominator").split()

        sorat1 = int(sorat1_str)
        sorat2 = int(sorat2_str)
        makhraj1 = int(makhraj1_str)
        makhraj2 = int(makhraj2_str)
        if makhraj1 == 0 or makhraj2 == 0:
            print("Invalid fraction --> Number/0 Try again \n")
        else:
          a = fraction(sorat1, makhraj1)
          b = fraction(sorat2, makhraj2)
          c = a.add(b)
          c.show_friction()


    elif user_input_menu == 2:
        sorat1_str, makhraj1_str = input("Please enter the first numerator and first denominator").split()
        sorat2_str, makhraj2_str = input("Please enter the second numerator and second denominator").split()

        sorat1 = int(sorat1_str)
        sorat2 = int(sorat2_str)
        makhraj1 = int(makhraj1_str)
        makhraj2 = int(makhraj2_str)

        if makhraj1 == 0 or makhraj2 == 0:
            print("Invalid fraction --> Number/0 Try again \n")
        else:
            a = fraction(sorat1,makhraj1)
            b = fraction(sorat2,makhraj2)
            c = a.sub(b)
            c.show_friction()



    elif user_input_menu == 3:
        sorat1_str, makhraj1_str = input("Please enter the first numerator and first denominator").split()
        sorat2_str, makhraj2_str = input("Please enter the second numerator and second denominator").split()

        sorat1 = int(sorat1_str)
        sorat2 = int(sorat2_str)
        makhraj1 = int(makhraj1_str)
        makhraj2 = int(makhraj2_str)
        if makhraj1 == 0 or makhraj2 == 0:
            print("Invalid fraction --> Number/0 Try again \n")
        else:
          a = fraction(sorat1, makhraj1)
          b = fraction(sorat2, makhraj2)
          c = a.multi(b)
          c.show_friction()


    elif user_input_menu == 4:
        sorat1_str, makhraj1_str = input("Please enter the first numerator and first denominator").split()
        sorat2_str, makhraj2_str = input("Please enter the second numerator and second denominator").split()

        sorat1 = int(sorat1_str)
        sorat2 = int(sorat2_str)
        makhraj1 = int(makhraj1_str)
        makhraj2 = int(makhraj2_str)
        if makhraj1 == 0 or makhraj2 == 0:
            print("Invalid fraction --> Number/0 Try again \n")
        else:
          a = fraction(sorat1, makhraj1)
          b = fraction(sorat2, makhraj2)
          c = a.divi(b)
          c.show_friction()

    elif user_input_menu == 5:
      sorat1_str, makhraj1_str = input("Please enter the  numerator and denominator = ").split()
      sorat1 = int(sorat1_str)
      makhraj1 = int(makhraj1_str)

      a = fraction(sorat1,makhraj1)
      b=a.simplify()
      b.show_friction()


    elif user_input_menu == 6:
        print("BYE BYE")
        break

    else:
        print("Invalid input please try again")


