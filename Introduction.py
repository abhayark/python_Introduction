#Variables

num = 10            #int
per = 85.60        #float
name = "ark"        #string
choice = True      #boolean


#Python Math:

#addition(+):
print(2 + 3)
#subtraction(-)
print(2 - 3)
#multiplication(*)
print(2 * 3)   
#division(/)
print(2 / 3)
#exponential(**)
print(2 ** 3)
#modulus(%)
print(2 % 3)
# Floor division operator()
print(2 // 3)

#------------------------------------------#

#type function:
print(type(10))     #class int
print(type(12.0))   #class float

#------------------------------------------#

# Variables

name = "Abhay Ark"
country,city  = 'India','Latur'
age = 18

person_info = {
    'Abhay',
    'India',
    'latur'
    }       #It randamizes the values position

print("My Name is ",name)
print(f"Im from {city} Which is in {country}")
print(f"My age is {age}")
print(person_info)

#------------------------------------------#

#Type casting:

#int to float:
n = 10
print(f"number in int:{n}")         # 10
num = float(n)
print(f"number in float:{num}")   # 10.0

#float to int:
pi = 3.14
print(int(pi))  #3

#int to string:
num_int = 10
print(num_int)               # 10
num_str = str(num_int)
print(num_str)               # '10'

#string to int & float:
num_str = '10'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

#------------------------------------------------#
