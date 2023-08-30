
# HOF - Higher Order Function (first class function)
def outerFun(greet):
    def innerFun(gname):
        print(greet, gname)

    return innerFun

# simple curry
engGreet = outerFun("Welcome")
hndGreet = outerFun("Namaskar")

engGreet("Sachin")
engGreet("Rahul")
hndGreet("Sehwag")
