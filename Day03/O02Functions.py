
from collections import namedtuple
def ArithematicCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    nmdTpl = namedtuple("Arithematic", "sum diff prod quot")
    arthObj = nmdTpl(sum, diff, prod, quot)
    return arthObj

res = ArithematicCalc(20, 8)
print(res)
print("-" * 60)
print(f"sum =  {res.sum}")
print(f"diff = {res.diff}")
print(f"prod = {res.prod}")
print(f"quot = {res.quot}")


