from datetime import*
class Time:
    def __init__(self,h,m,s):
        self.hour = h
        self.minute = m
        self.second = s
        self.time_fixer()

    def show_time(self):
        print(f'{self.hour}:{self.minute}:{self.second}')

    def time_fixer(self):
        if self.second >= 60:
            self.second = self.second - 60
            self.minute +=1
        if self.minute >= 60:
            self.minute = self.minute - 60
            self.hour +=1

    def time_add(self,a):
        result_second = self.second + a.second
        result_minute = self.minute + a.minute
        result_hour   = self.hour + a.hour

        result = Time(result_second,result_minute,result_hour)
        return result

    def time_sub(self,a):
        result_second = abs(self.second - a.second)
        result_minute = abs(self.minute - a.minute)
        result_hour   = abs(self.hour - a.hour)

        result = Time(result_hour, result_minute, result_second)
        return result

    def time_to_sec(self):
        result = (self.hour * 3600) + (self.minute * 60) + self.second
        return result

    def sec_to_time(self):
        while (self.second >= 60):
            self.time_fixer()
        self.show_time()

print(''' <Time Machine>

1- Add two time
2- Subtract two time
3- Time to Seconds
4- Seconds to Time
5- Exit
''')

while(True):
    user_input = int(input("Enter your choice->"))
    if user_input == 1:
        h_str1,m_str1,s_str1 = input("Please enter First Time (Hour/Minutes/Seconds) in this order").split()
        h1 = int(h_str1); m1= int(m_str1) ; s1 = int(s_str1)

        h_str2, m_str2, s_str2 = input("Please enter Second Time (Hour/Minutes/Seconds) in this order").split()
        h2 = int(h_str2);m2 = int(m_str2);s2 = int(s_str2)

        a = Time(h1,m1,s1)
        b = Time(h2, m2, s2)

        c = a.time_add(b)
        c.show_time()

    elif user_input == 2:
        h_str1, m_str1, s_str1 = input("Please enter First Time (Hour/Minutes/Seconds) in this order").split()
        h1 = int(h_str1);
        m1 = int(m_str1);
        s1 = int(s_str1)

        h_str2, m_str2, s_str2 = input("Please enter Second Time (Hour/Minutes/Seconds) in this order").split()
        h2 = int(h_str2);
        m2 = int(m_str2);
        s2 = int(s_str2)

        a = Time(h1, m1, s1)
        b = Time(h2, m2, s2)

        c = a.time_sub(b)
        c.show_time()

    elif user_input == 3:
        h_str1, m_str1, s_str1 = input("Please enter  Time (Hour/Minutes/Seconds) in this order").split()
        h1 = int(h_str1)
        m1 = int(m_str1)
        s1 = int(s_str1)

        a = Time(h1, m1, s1)
        result=a.time_to_sec()
        print(f'converted time to second is {h1}:{m1}:{s1}-->{result}s ')

    elif user_input == 4:
        second = int(input("Please enter the Seconds your want to convert to real time"))
        a = Time(0,0,second)
        a.sec_to_time()


    elif user_input == 5:
        print("Thanks for Spending your TIME with us ")
        break
    else:
        print("Invalid input try again")


