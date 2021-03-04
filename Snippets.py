""" 
Useful resources:
* https://www.w3schools.com/python/python_dictionaries.asp
* https://github.com/aloctavodia/BAP
* https://learnbayesstats.com
* https://www.freecodecamp.org/news/an-a-z-of-useful-python-tricks-b467524ee747/

# conda activate snips
"""

# %% Multithreading with priority queue using threading module
import queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print ("Starting " + self.name)
      process_data(self.name, self.q)
      print ("Exiting " + self.name)

def process_data(threadName, q):
   while not exitFlag:
      queueLock.acquire()
      if not q.empty():
         data = q.get()
         queueLock.release()
         print ("%s processing %s" % (threadName, data))
         time.sleep(5)
      else:
         queueLock.release()
         time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")

# %% Multithreading with _thread module
import _thread
import time
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

try:
   _thread.start_new_thread( print_time, ("Thread-1", 2) )
   _thread.start_new_thread( print_time, ("Thread-2", 4) )
except:
   print ("Error: unable to start thread")

while 1:
    pass


# %% operator overloading
class Thing:
    def __init__(self, value):
        self.__value = value
    def __gt__(self, other):
        return Thing(self.__value > other.__value)
    def __lt__(self, other):
        return Thing(self.__value < other.__value)
    def __add__(self, other):
        return Thing(self.__value + other.__value)
    def __sub__(self, other):
        return Thing(self.__value - other.__value)
    def __eq__(self, other):
        return self.__value == other.__value

something = Thing(100)
nothing = Thing(0)

something > nothing
something < nothing
(something + nothing) == something
(something - nothing) == something


# %% add / multiply, tuple, list and array
import numpy
a1 = np.array([1,2,3])
a2 = [1,2,3]
a3 = (1,2,3)
a4 = "hi"

print(a1+a1) #concat
print(a2+a2) #concat
print(a3+a3) #elementwise
print(a4+a4) #concat

print(a1*a1) #elementwise
#print(a2*a2) error
#print(a3*a3) error
#print(a4*a4) error

# %% Comma is needed to distinguish single element
# tuple from grouping
print((1,))
print((1))

# %% multiplying tuples and lists copies them
(1,2)*2    # (1,2,1,2)
((1,2),)*2 # ((1,2),(1,2))
[1,2]*2    # [1,2,1,2]
[[1,2]]*2  # [[1,2],[1,2]]

# %% hstack and vstack
import numpy as np
print(np.hstack(([1,2,3],)*2))
print(np.vstack(([1,2,3],)*2))
print(np.vstack(([1,2,3],)*2).T)

# %% Python newspaper module
# guide https://pypi.org/project/newspaper3k/
# conda install -c conda-forge newspaper3k
import newspaper as ns
url = "https://www.economist.com/united-states/2021/03/01/donald-trump-emerges-from-seclusion-before-an-adoring-crowd"
article = ns.Article(url)
article.download()
article.html
article.parse()
article.authors
print(article.text)

# %% map a lambda function over a list
z = [1,2,3]
y = map(lambda x : x + 1, z) 
print(list(y)) # map returns an iterable

# %% list comprehension
numbers = list(range(1,8))
evens = [x for x in numbers if x % 2 is 0]
odds = [y for y in numbers if y not in evens]
print(evens); print(odds)

# %% *args - the arguments become a tuple
def myfunction(*args):
    return args
myfunction("a","b","c")

# %% **kwargs - the dictionary is unravelled to arguments
dictionary = {"a": 1, "b": 2}
def someFunction(a, b, c):
    print(a + b + c)
    return
# these do the same thing:
someFunction(**dictionary, c=4)
someFunction(a=1, b=2, c=4)


# %% Get source, or just press F12, or just CTRL + leftclick
import inspect as ins
object = ins.getsource
print("RESULT 1:", ins.getsource(object)) # source code
print("RESULT 2:", ins.getmodule(object)) # module in which defined
print("RESULT 3:", ins.currentframe().f_lineno) # own line number
lines, lnum = ins.getsourcelines(object)
print("RESULT 4:", ''.join(lines))

# %% Join / concatenate a list or tuple of strings together
''.join(['a','b','c'])
''.join(('a','b','c'))


# %%
# conda install -c conda-forge geopy 
from geopy import GoogleV3
place = "221b Baker Street, London"
key = 'enter API key' # From Google Cloud
location = GoogleV3(api_key=key).geocode(place)
print(location.address)
print(location.point)
location.raw

# %% Look inside python object
x = {'a':1, 'b':2}
dir(x)
dir(dir)

# %% Import features from future versions of python
from __future__ import print_function
print("Hello World!")

# %% any, all and not
x = [True, True, False]
if any(x):
    print("At least one True")
if all(x):
    print("Not one False")
if any(x) and not all(x):    
    print("At least one True and one False")

# %% Collections
from collections import OrderedDict, Counter
# Remembers the order the keys are added!
x = OrderedDict(a=1, b=2, c=3)
# Counts the frequency of each character
y = Counter("Hello World!")


# %% Using pickle to read and write binary
import pickle
import numpy as np

def savep(filename):
    write_file = open(filename, 'wb')
    pickle.dump(obj, write_file)
    write_file.close()

def loadp(filename):
    read_file = open(filename, 'rb')
    obj = pickle.load(read_file)
    read_file.close()
    return obj

obj = np.repeat('doony',500)
filename = "myobj.doony"
savep(filename)
loadp(filename )


# %% attributes can be added to classes on the fly
class MyClass:
    x = 5
m = MyClass()
m.x
m.config = "config string"
m.mydic = {"thing":1, "other-thing":2}
m.__class__
m.x.__class__

# %% to give parameters to the constructor, use __init__
# note that self does not need to be named self, just
# needs to be the first parameter of any function in the class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# %% Object attributes can be deleted from a class
# as can objects themselves
del p1.name
del p1

# %% An empty class can be created with pass
class Person:
    pass

# %% Class inheritance example
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
x = Person("John", "Doe")
x.printname() 
# Use the superclass as argument to create subclass.
# Note that the child __init__ overrides parent __init__
# (default without __init__ is to inherit everything).
# You can explicitly call parent __init__ to keep it
# here super() can be a replacement for "Person".
class Student(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        self.graduationyear = year
    def welcome(self):
        print(
            "Welcome", self.firstname, 
            self.lastname, "to the class of", 
            self.graduationyear)
x = Student("Mike", "Olsen", 2019)
x.printname()
x.welcome()

# %% Use assert to sanitise inputs
class TopStudent(Student):
    def __init_(self, fname, lname, mark):
        Person.__init__(self, fname, lname)
        assert mark >= 85
        self.mark = mark

# %%
# generator functions return iterable results
def square_generator(input_data):
    for num in input_data:
        res = num*num
        yield res

data = [1,2,3,4]
sg = square_generator(data)
print(sg)
print('1st result: ', next(sg))
print('2nd result: ', next(sg))
print('3nd result: ', next(sg))

# %% 
# Check that tensorflow is using the GPU
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
import tensorflow as tf
tf.config.list_physical_devices('GPU')

# %%
# To find out which devices your operations and tensors are assigned to
tf.debugging.set_log_device_placement(True)

# %%
# Create some tensors to check set_log_device_placement output
a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
c = tf.matmul(a, b)
print(c)

# %% A matplotlib of normal distributions
# Notice: 
# * the scipy stats pdf
# * the indexable subplots
# * the empty vector trick to remove legend line
# * the labelpad param for spacing p(x)
# * arviz just sets the dark grid style
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import arviz as az
az.style.use('arviz-darkgrid')
mu = [-1,0,1]
sd = [0.5, 1, 1.5]
x = np.linspace(-7,7,200)
_, ax = plt.subplots(len(mu), len(sd), 
                     sharex = True, sharey = True,
                     figsize = (9,7), 
                     constrained_layout = True)
for i in range(len(mu)):
    for j in range(len(sd)):
        mu_i = mu[i]
        sd_j = sd[j]
        y = stats.norm(mu_i,sd_j).pdf(x)
        lab = "μ = {:3.2f}\nσ = {:3.2f}"
        lab = lab.format(mu_i, sd_j)
        ax[i,j].plot(x,y)
        ax[i,j].plot([], label=lab, alpha=0)
        ax[i,j].legend(loc=1)
ax[2,1].set_xlabel('x')
ax[1,0].set_ylabel('p(x)', rotation=0, labelpad=20)
ax[1,0].set_yticks([])

# %% Strings are immutable in Python
a = "ahah"
a = a+"b"
# a[1] = 'c' error (not mutable)

# %% f strings
name = "Danny"
a = f"Hello {name}"
print(a)
