
def doubleMesh(fnc):
    def helper(*args):
        print("=" * 40)
        fnc(*args)  # callback
        print("#" * 40)
    return helper


def startSingle(fnc):
    def helper(*args):
        print("*" * 40)
        fnc(*args)  # callback
        print("_" * 40)
    return helper


@startSingle
@doubleMesh
def fun1():
    print("fun1 called")


# @startSingle
# @doubleMesh
# def fun2(x):
#     print("funx called", x)
# @startSingle
# @doubleMesh
# def fun3(x, y):
#     print("fun3 called", x, y)
#
#
# @startSingle
# @doubleMesh
# def fun4(x, y, z):
#     print("fun4 called", x, y, z)


fun1()

# fun2(10)
#
# fun3(1, 2)
#
# fun4(3, 4, 5)