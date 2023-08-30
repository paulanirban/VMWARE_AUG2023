
def greet():
    print("Greetings Mr.Sachin, Welcome to the event....")

def greetGst(gst):
    print(f"Greetings Mr.{gst}, Welcome to the event.....")

# gst - non default arg, cty - default arg
def greetGstCty(gst, cty="Mumbai"):
    print(f"Greetings Mr.{gst} from {cty}, Welcome to the event......")


greet()
greetGst("Sachin")
greetGstCty("Sunil")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

print("-" * 60)
def admsn(fnm, lnm, dob, plc, qlf, desig):
    print(f"First Name    :{fnm}")
    print(f"Last Name     :{lnm}")
    print(f"Birth Date    :{dob}")
    print(f"Place         :{plc}")
    print(f"Qualification :{qlf}")
    print(f"Designation   :{desig}")


admsn(plc="Blr", dob='10/07/1981', fnm = "Mark", lnm="Slater", desig="MGR", qlf='MBA')
print("-" * 60)
admsn('kevin', 'costner', desig="CA", qlf="AMGR", dob="01/23/2001", plc="Che")

print("-" * 60)
# functions can return value in python

def MultiplMe(x, y):
    return x * y

i = 10; j = 5
print(f"The product of {i} and {j} is :{MultiplMe(i, j)}")

print("-" * 60)
# recursive calls - factorial of a number, fibanocci series

def ArithematicCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = ArithematicCalc(20, 8)
print(f"res :{res}")


print("-" * 60)
# variable length args =>
# *arg - argument like a list or tuple
# **kwarg - argument like a dictionary

def productAll(*numbers):
    print(numbers)
    print(*numbers)         # unpack
    prod = 1
    for num in numbers:
        prod *= num
    return prod

res = productAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)
def extract_details(**details):
    print(details)
    print(details['name'])
    print(details['oppn'])
    print("-" * 40)
    for k, v in details.items():
        print(k, "=>", v)

extract_details(name="Sachin", age=32, runs=45, oppn="SA")

print("-" * 60)
# funtion documentation

def fun1():
    # this is a comment
    "This is a documentation string"
    print("Hello World")

fun1()
print(fun1.__doc__)

print("=" * 60)

def fun2(x, y):
    """
    fun2(x, y)
    ----------

    function fun2 takes two arguments
    1. if both the arguments are numbers then it will return a sum of it
    2. if both the arguments are strings then it will concatenate the string and return it.
    3. if the arguments are of different types then it will throw an error
    """
    print("hello world")
    return x + y


print(fun2("hello", "world"))
print(fun2(100, 200))
# print(fun2("hello", 200))

print("-" * 60)
help(fun2)
