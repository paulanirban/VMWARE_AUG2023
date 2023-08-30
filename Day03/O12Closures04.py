
def sum(x, y):
    return x + y

def diff(x, y):
    return x - y

def log_details(fnc):
    logInfo = "Logging into the service"

    def innerFun(*args):
        print(logInfo)
        print(fnc(*args))           # callback
        print("-" * 60)

    return innerFun


sum_logger = log_details(sum)
diff_logger = log_details(diff)

sum_logger(85, 58)
diff_logger(97, 64)