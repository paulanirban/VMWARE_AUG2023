
glbX = 100

def fun(y):                 # local variable
    global glbX             # do not assign any value to the variable here
    print(f"y :{y}")
    glbX = 500              # local variable
    print(f"glbX inside :{glbX}")

print(f"glbX before :{glbX}")

fun(10)

print(f"glbX after :{glbX}")
