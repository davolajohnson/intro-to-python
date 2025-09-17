age = 35 # This is a comment in python === // in JS

# when defining variables we dont need let or const or var
# we just define a name and assign it a value
name = "billie"

# for multiple words we use snake_case instead of camelCase 
# snake_case has a "_" between each word
# let movie
# and later in our code assign movie a value. We cannot do this in python

# In python when creating a variable you must assign it some value
# let favoriteColor = "Green"
favorite_color = "Green"

movie = None # None == nothing or null from JS

favorite_coffee_drink = "Flat White with Soy milk"

# in JS we use ``` for multiline comments in python

print(movie) # this should print "None"

# If I want to update my favorite movie we just reassign the value
movie = "Toy Story"

print(movie) # Should print our updated Movie value


"""
    Constants
    in JS we can define immuateble (variables that cant change)
    by using the const key word

    const birthday = "January 1, 2000" // const cannot be change

    
    In python for Constant use use SCREAMING_SNAKE_CASE

    ALL Uppers === Constant (do not change)
"""

BIRTHDAY = "January 1, 2000" 

"""
This is a multi
lin comment in python

we can use single or double quote for this

"""

'''
This is an example with single quotes

... more notes

'''

print("hello world!") # this === console.log('') from js. Print will print something to the console

print("whats up from billies python file")


# We can check the type of some variable using type(variable)

# movie = "Toy Story"
print(type(movie))

# age = 35
print(type(age))

# Float - Floats are numbers with decimal ex = 1.0
my_age_float = 35.00

print(type(my_age_float))

# Booleans work just like JS but are capital cased

print(type(True))
print(type(False))

# None - Python uses "None" instead of JS's null None === null
print(type(None))

num_tacos = 25

msg = "There are " + str(num_tacos) + " tacos to eat." # For str you can only add another type of str, to string + number will throw an error

print(msg)

first_int = 10

second_int = 5

results = first_int / second_int # / will return a float

print(results)

int_results = first_int // second_int # // will return a Int instead of float

print(int_results)

# multi line string work with """ and '''
really_long_string = """
1
2
3
4
5
6
"""

print(really_long_string)

super = "Super"
bad = "bad"

super_bad = super + ' ' + bad

print(super_bad)

# In JS `The movie is ${super_bad}` String Interpolation

f_string = f"The movie is {super_bad}" # for f string we need a f in the front before the ""

print(f_string)


print(f"There are {num_tacos} tacos to eat.")

print("Ace Of Spades".split(' ')) # Split works just like JS but we cant split "" on empty string

print(list("Ace Of Spades")) # list will convert a string to a list(Array) list === Array

print(f_string.index("a"))


print(f_string.find("z")) # returns -1 if if cannot find the substring
# -1 === False

print(f_string.upper())
print(f_string.lower())


print("eggs" in "green eggs and ham")
# prints: True

print(len("Tacos")) # len == length (give me the length of something)
# prints: 5