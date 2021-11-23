class ComplexNumber:
        def __init__(self,x,y):
            self.Real = x
            self.Imag = y

        def show_complex(self):
            if self.Imag == (-1):
                print(f'{self.Real}-i')
            elif self.Imag == (1):
                print(f'{self.Real}+i')
            elif self.Imag < 0:
                print(f'{self.Real}{self.Imag}i')
            elif self.Imag > 0:
                print(f'{self.Real}+{self.Imag}i')
            elif self.Imag == 0:
                print(f'{self.Real}')
            elif self.Real == 0 :
                print(f'{self.Imag  }')

        def complex_add(self,a):
            result_Real = self.Real + a.Real
            result_Imag = self.Imag + a.Imag
            result = ComplexNumber(result_Real, result_Imag)
            return result

        def complex_multi(self, a):
            result_Real = (self.Real * a.Real) - (self.Imag * a.Imag)
            result_Imag = (self.Real * a.Imag) + (self.Imag * a.Real)
            result = ComplexNumber(result_Real,result_Imag)
            return result

        def complex_sub(self, a):
            result_Real = self.Real - a.Real
            result_Imag = self.Imag - a.Imag
            result = ComplexNumber(result_Real, result_Imag)
            return result

print(''' <This is too Complex>

1- Add two complex numbers
2- Subtract two complex numbers
3- Multiply two complex numbers
4- Exit
''')

while(True):
    user_input = int(input("Enter your choice->"))
    if user_input == 1:
        Real1_str, Imag1_str = input("Enter your Real part and Imaginary part of your first complex number in order").split()
        Real1 = int(Real1_str)
        Imag1 = int(Imag1_str)

        Real2_str, Imag2_str = input( "Enter your Real part and Imaginary part of your second complex number in order").split()
        Real2 = int(Real2_str)
        Imag2 = int(Imag2_str)

        a = ComplexNumber(Real1,Imag1)
        b = ComplexNumber(Real2,Imag2)

        result = a.complex_add(b)
        result.show_complex()


    elif user_input == 2:
        Real1_str, Imag1_str = input(
            "Enter your Real part and Imaginary part of your first complex number in order").split()
        Real1 = int(Real1_str)
        Imag1 = int(Imag1_str)

        Real2_str, Imag2_str = input(
            "Enter your Real part and Imaginary part of your second complex number in order").split()
        Real2 = int(Real2_str)
        Imag2 = int(Imag2_str)

        a = ComplexNumber(Real1, Imag1)
        b = ComplexNumber(Real2, Imag2)

        result = a.complex_sub(b)
        result.show_complex()


    elif user_input == 3:
        Real1_str, Imag1_str = input(
            "Enter your Real part and Imaginary part of your first complex number in order").split()
        Real1 = int(Real1_str)
        Imag1 = int(Imag1_str)

        Real2_str, Imag2_str = input(
            "Enter your Real part and Imaginary part of your second complex number in order").split()
        Real2 = int(Real2_str)
        Imag2 = int(Imag2_str)

        a = ComplexNumber(Real1, Imag1)
        b = ComplexNumber(Real2, Imag2)

        result = a.complex_multi(b)
        result.show_complex()



    elif user_input == 4:
        print("i hope this was not too COMPLEX for you ")
        break
    else:
        print("Invalid input try again")
