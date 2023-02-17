#-------NUMBERS----------------

#calculus priority
print( 2 + 2 )
print( 10 + 5 * 2 )

#integer and float convertion
print( 17 / 3 ) #int / int = -> convert to float
print( 17 / 3.0 ) #int / float = float
print( 17 // 3.0 ) #floor even if float
print( 17 % 3 ) #reminder as int
print( 17 % 3.0 ) #reminder as float
print( 2 ** 3 ) #power




#-------STRINGS-----------------

print( 'one sentence' )
print( "one sentence" )
print( 'this isn\'t funny' ) #use \ to escape
print( "this isn't funny" )  #use " to define string
print( " \"yes\", he said" )  #use \ to escape
print( ' "yes", he said' )  #use \ to escape

print( 'first line \nsecond line' ) # \n return
print( 'this is a \ttab' ) # \t tab

print( 'C:\my_folder\new_folder' ) # \n is seen as return
print( 'C:\\my_folder\\new_folder' ) # escape the \
print( r'C:\my_folder\new_folder' ) # r'' remove the special meaning of \

print( "Hello, %s, this is a %d, %f" %( 'John', 50.1, 50.1) )
print( "Hello, {}, this is a {}, {}".format( 'John', 50.1, 50.1) )
print( "Hello, {1}, this is a {2}, {0}".format( 'John', 50.1, 50.1) )
print( "Hello, {0}, this is a {0}, {0}".format( 'John', 50.1, 50.1) )

#strings are immutable lists
mystring = 'Hello_world!'
print( mystring[0])
print( mystring[6] ) #7th character ( base 0 )
print( mystring[-1]) #reverse access
print( mystring[-2] )#reverse access
print( mystring[6:]) #range from 6 to end
print( mystring[:6] )#range from 0 to 5 !!!!
print( mystring[2:8] )#range from 2 to 7
start = 3
end = 8
print( mystring[start:end] )#range from 3 to 7
print( mystring[2:8:2] )#range from 2 to 7 step 2

#EXERCICE 1
#get the range that represent the last 6 characters
#>>> world!


#EXERCICE 2
#get the range that represent the last 6 characters except the last one
#>>> world


#EXERCICE 3
#get the range that revert the sentence
#>>> !dlrow_olleH



#string operations
print( mystring + " and you" )
print( mystring + 25 )
print( mystring + str( 25 ) ) #number must be converted before concatenated
print( mystring * 3 )

#some methods
mypath = r'C:\my_folder\new_folder\myfile.txt'
print( mypath.replace('new', 'old') )
print( mypath.replace('_', '&') )
print( mypath.split('_') )
print( mypath.split('\\') )
print( mypath.split('new') )

#EXERCICE 4
#from the mypath variable, return the file name without the extension
#>>> myfile


#---------LISTS-------------------------
emptylist = list()
emptylist = []
myList = [1, 2, 5, 9, 25]
myList[2] = 4  #assign a value
print ( myList )

print ( myList + [100,200,300] ) #append
print ( [0] * 10 ) #multiply
print ( myList * 3 )

myList = ['a', 'b', 'c', 'd', 'e' ,'f', 'g']
myList[2:5] = ['C', 'D', 'E'] #replace a range of same length
print ( myList )

myList = ['a', 'b', 'c', 'd', 'e' ,'f', 'g']
myList[2:5] = [] #replace a range of different length to discard
print ( myList )

myList = ['a', 100, "B", 30.3]
print ( myList )

A = [1,2,3]
B = [7,8,9]
C = [A, B] #list of lists
print (C)

#adding value
myList = ['a', 'b', 'c', 'd', 'e' ,'f', 'g']
myList.append('h')
print (myList)

myList = ['a', 'b', 'c', 'd', 'e' ,'f', 'g']
myList.extend(['h', 'f'])
print (myList)


#EXERCICE 5
#create this list [0, 0, 0, 0, 0, 1, 2, 1, 2, 1, 2, 1] using the + and * operators


#check if value is in list
myList = ['a', 'b', 'c', 'd', 'e' ,'f', 'g']
print( 'c' in myList )
print( 'h' in myList )

#unpacking in  variables
a, b = [1,2]
print (a)
print (b)

#unpacking needs to have the right amount of variables
a,b = [1,2,3] #too many to unpack

# swap
a = 5
b = 6
a, b = b, a
print(a, b)


#EXERCICE 6
myList = ['a', 'b', 'c', 'd', 'e' ,'f', 'g']
#unpack only the two first values of the list myList into 2 variables
#>>> a, b = ...


#--------- TUPLE ---------------------------
x = a, b, "c", 10
print(x)
print(x[1])
x[1] = 10 # not allowed
x = (a, b, "c", 10) # same


#--------- DICT---------------------------
emptydict = dict()
emptydict = {}
myDict = {1:"Aa" , 2:"Bb", 3:"Cc"}
print( myDict )

#keys can be anything.  Creation order is not preserved
myDict = {'first': 100, 'second': 'YES', 5: 100, 6: 'NO'}
print (myDict)

#accessing by key
myDict = {'first': 100, 'second': 'YES', 5: 100, 6: 'NO'}
print (myDict['second'])
print (myDict[6])
print (myDict['third'])  #missing key

#adding a value
myDict = {'first': 100, 'second': 'YES', 5: 100, 6: 'NO'}
myDict['third'] = 'added'
print (myDict)

#getting the values only
print (myDict.values())

#getting keys only
print (myDict.keys())

#test if the key exists
myDict = {'first': 100, 'second': 'YES', 5: 100, 6: 'NO'}
print( 'second' in myDict )
print( 'four' in myDict )



