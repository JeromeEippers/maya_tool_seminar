#--------------------- CONDITION --------------------
x = 2
print(x == 2) 
print(x == 3) 
print(x < 3)
print(x != 3)

print('John' in ["John", "Rick"])
print('Jeff' in ["John", "Rick"])
print('Jeff' not in ["John", "Rick"])
print('c' in 'abracadabra')
print('e' in 'abracadabra')


#--------------------- IF ---------------------------



#if else
x = 0
if x < 0:
    print ('negative')
else:
    print ('positive')


#if elif else
x = 0
if x < 0:
    print ('negative')
elif x == 0:
    print ('zero')
elif x == 1:
    print ('one')
else:
    print ('big number')
    
    
#and or
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
    
    
#empty list is tested as False
myList = []
if myList:
    print('there is some values')
else:
    print('there is no value')

myList = [1]
if myList:
    print('there is some values')
else:
    print('there is no value')
    
    
#EXERCICE 1
#Change the values of the 4 variables of this exercice so all tests return true
number = 10
second_number = 2
first_array = []
second_array = [1,2,3]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
#------
    
    
    

#--------------------- LOOPS ---------------------------
# Measure some strings:
words = ['cat', 'window', 'dog']
for w in words:
    print (w, len(w))
    
#range function
print( range(5) )
print( range(3,9) )
print( range(3,9,2) )

for x in range(5):
    print (x)
    
    
#mix range and len function to loop over indexes of list
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print (i, a[i])
    
    
#break
myList = list()
for x in range(10):
    myList.append( x )
    if x == 5:
        break
print (myList)
        

#continue     
myList = list()
for x in range(10):
    myList.append( x )
    if x == 5:
        continue
print (myList)


#EXERCICE 2
#loop on this list and print all the even numbers but stop at the number 237
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
#>>> [402, 984, 360, 408, 980, 544, 390, 984, 592, 236, 942, 386, 462, 418, 344, 236, 566, 978, 328, 162, 758, 918]


#loop and dictionnaries
myDict = {1:"Aa" , 2:"Bb", 3:"Cc"}
for key in myDict.keys():
    print (key)
    
myDict = {1:"Aa" , 2:"Bb", 3:"Cc"}
for value in myDict.values():
    print (value)
    
myDict = {'first': 100, 'second': 'YES', 5: 100, 6: 'NO'}
for key, value in myDict.items():
    print (key, value)
    
    
    
#--------------------- FUNCTIONS ---------------------------
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
print (x)


#default argument ------
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print ("-- This parrot wouldn't", action,)
    print ("if you put", voltage, "volts through it.")
    print ("-- Lovely plumage, the", type)
    print ("-- It's", state, "!")
    
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


#multiple return and unpack
def myFunction():
    return (10 , 20)
    
x, y = myFunction()
print (x)
print (y)



#EXERCICE 3
#Modify this function to return a list of names
def get_name_list():
    pass
    
#Modify this function to return the name concatenated with the sentence 'was here'
def get_sentence( name ):
    pass
    
def test_exercice():
    for name in get_name_list():
        print( get_sentence( name ) )
test_exercice()