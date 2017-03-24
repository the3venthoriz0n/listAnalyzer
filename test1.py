'''
Andrew Kaplan ComSci II

LIST ANALYZER

# All original work, in colaboration with Marty Lewinter. Computer Science II Final Project
# We will be analyzing this list of numbers, each new number is generated from the sums of the 2nd and 3rd back numbers.
# Alternitivly you could import a different list from another location and use this program to analyze it
# Started on 4/28/13
# Python Version 2.7.3

#****To use NON generator version, uncomment the function calls at the bottom of the page********

# The Generator seems to work much better, and much faster than the NON GENERATOR. The Generator still has some bugs but I was curious so I tried both

# Interesting Things About The List:

The next perfect square after 49 in the list is 342455327734937699822198518336 !!!!!

The next perfect cube after 1 is 281562873505308265688573224949357787944!

The Parity of numbers is OOOEEOE. This pattern loops over and over for infinity

'''

import math
import time
from sympy import nsimplify # * import all names in this module
from collections import deque # For generator part
from itertools import islice # For using generator

''' This Part of the program does NOT use a generator / an alternative way to write this program is below using a generator
--------------------------------------------------------------------------------------------------------------------------
'''

start = [1,1,1] #the list must start with three 1's
ammountOfNumbers = int(raw_input("Enter the ammount of numbers to be generated: "))# value to dictate length of generated list
emptyList = [] # empty list to aappend values to


#Timer from vegaseat

def print_timing(func): # to time functions
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)#function with any number of arguments
        t2 = time.time()
        print
        print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper

'''
GENERATES LIST (NON GENERATOR)
------------------------------
'''
#**uncomment for NON Gen version
#@print_timing
def solve(start,n): # function for generating list
    if n<=3: 
        return start[:n] #prints from begining of list to n while n is <= 3
    while len(start)!= n: #while the length does not equal the n value run this
        start.append(start[-2]+start[-3]) # adds the 2nd and 3rd back numbers to the list
        #print start #test
    return start

'''
GIVES ANALYSIS (NON GENERATOR)
------------------------------
'''
#@print_timing
def evaluate(l,end): #function to help analyze list(s)
    
    #print"Max Value: ",max(l) # maximum value in list
    
    sqRtNum = [nsimplify(math.sqrt(x)) for x in l if math.sqrt(x).is_integer()] #take square root of numbers in l and only show ones that a perfect int
    print
    print"Square Roots IN list: ",sqRtNum

    allSqr = [x**2 for x in range(0,end) if x not in sqRtNum]# all perfect squares NOT in the list
    perfAllSqr = [nsimplify(math.sqrt(x)) for x in allSqr if math.sqrt(x).is_integer()]
    print
    print"All Perfect Square Roots NOT in list:", perfAllSqr #allSqr

    squares = [x**2 for x in sqRtNum] # l numbers squared. square the numbers
    print
    #print"The Perfect Squares: ", squares
 
    cubRtNum = [nsimplify(x**(0.333333)) for x in l if (x**(0.333333)).is_integer()] # cube root all numbers, displays only perfect cubes
    print
    print"Cube Roots: " ,cubRtNum

##    cubes = [x**3 for x in cubRtNum] # l numbers cubed. cubes all numbers
##    print
##    print"The Perfect Cubes: ", cubes
##
##    parity = ['E' if(x%2)==0 else 'O' for x in l] # shows the list Parity of odds to evens "e" for even and "o" for odd. continues indefinitely
##    print
##    print "List Parity: ",parity
##    
##    even = [x for x in l if(x%2)==0] # all even numbers in l
##    print
##    print"Evens: ",even
##    
##    odd = [x for x in l if(x%2)==1] #all odd numbers in l
##    print
##    print"Odds: ",odd
    
    return None


'''
USING A GENERATOR
------------------------------------------------------------------------------------------------------------
'''


#With a little help from user mgilson @stackoverflow.com

#@print_timing
def realGen(seed,func): #nested generator, doesnt work quite like I wanted it to
    seed = list(seed) #make sure seed is list
    que = deque(seed,len(seed)) 
    for x in seed:
        yield seed
    while True:
        out = func(que)
        yield out
        que.append(out)

series = realGen(start,lambda x:x[-3] + x[-2]) # formula for series with lambda function
for item in list(islice(series,0,ammountOfNumbers)): #turn generator into a list
    #print"~ ",item
    emptyList.append(item)
    
#print"GenList: ",emptyList #using generator, but the first three ones are all screwed up!
#print"GenAnalysis: ",evaluate(emptyList) #getting "type error?"




##@print_timing # to time function
##def useGen(start,ammountOfNumbers,emptyList): # very nice nested generator function
##    series =(start,lambda x:x[-3] + x[-2]) # the recurrence relation using lambda 
##    for x in list(islice(series,ammountOfNumbers)):# using islice loop through list in range(0 ammountOfNumbers) (iterable,stop)
##        emptyList.append(series)
##        print"GenList: ", x
##        return emptyList 

#--------------------------Function Calls---------------------------------------------------------------------------

#**Uncomment for NON GEN Version
final = solve(start,ammountOfNumbers) #final equals finished list # uncomment for NON GEN
print
print"List: ", final # prints original list in range (ammountOfNumbers) #uncomment to use NON GEN version
print
print"Analysis: ", evaluate(final,ammountOfNumbers) # calls evaluate function # uncomment to use NON GEN version


###uncomment for GENERATOR version
##print
##print"With Generator: "
##print"--------------------------------------------------------------------------------"
##print
##genFinal = useGen(start,ammountOfNumbers,emptyList)# call generator function #comment out when using NON gen version
##print"Analysis: ",evaluate(genFinal) #returning empty list
##print

