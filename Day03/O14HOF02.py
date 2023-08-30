
def funLogger(fnc):
    def helper():
        print("My Info logged into Service....")
        fnc()
        print("My Info logger channel closed......")
        print("-" * 40)

    return helper

def normalFun():
    print("I should be called normal.....")

funLogger(normalFun)        # no output
print('-' * 60)
funLogger(normalFun)()
print('-' * 60)
res_fun = funLogger(normalFun)
res_fun()
print('-' * 60)

normalfun = funLogger(normalFun)
normalfun()

print('-' * 60)
print('-' * 60)
print('-' * 60)

@funLogger              # decorator
def basicFun():
    print("I should be called Basic.......")

basicFun()