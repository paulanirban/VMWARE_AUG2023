
"""
local variable - have lexical scope (cannot be accessed outside the block of code)
"""

def fun(y):
    print(f"y :{y}")
    lclX = 100
    print(f"lclX inside :{lclX}")

fun(50)
# print(f"lclX inside :{lclX}")

