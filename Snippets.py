""" 
Useful resources:
* https://www.w3schools.com/python/python_dictionaries.asp
* https://github.com/aloctavodia/BAP
* https://learnbayesstats.com
"""

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
