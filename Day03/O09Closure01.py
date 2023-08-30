
def outerFun(info):
    inf = "Mr." + info
    def innerFun():
        # print(info)
        print(inf)

    return innerFun

infun = outerFun("Rahul")

infun()