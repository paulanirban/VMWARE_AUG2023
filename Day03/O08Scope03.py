# Nested Functions

def outerFun(gname):        # local variable
    print(f'Outer before :{gname}')
    def InnerFun():
        nonlocal gname
        gname = "Mr." + gname + " " + "Dravid"
        print(f"Hello {gname}")

    InnerFun()
    print(f"Outer :{gname}")

outerFun("Rahul")

