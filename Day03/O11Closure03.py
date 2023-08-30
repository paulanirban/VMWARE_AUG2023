
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):
            from emojis import emojis

            emojized = emojis.encode(greet + " :" + sep + ": " + gname)

            print(emojized)

        return innerMostFun

    return innerFun


kanGreet = outerFun("Namaskara")
kanGrtTgr = kanGreet("lion")
kanGrtTgr("Prabhakar")

"""
engGreet = outerFun("Welcome")
hndGreet = outerFun("Namaskar")

engGrtSngArw = engGreet("------>")
hndGrtSngArw = hndGreet("------>")
engGrgDblArw = engGreet("======>>")
hndGrgDblArw = hndGreet("======>>")

engGrgDblArw("Sachin")
hndGrtSngArw("Rahul")

"""

