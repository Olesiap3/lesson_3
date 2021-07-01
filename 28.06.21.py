def num(fill):
    def inner(a):
        result = fill(a)
        return result**2
    return inner
@num
def num_1 (a):
    return a

print ( num_1(3))
print ( num_1(2))

print ("------------------------------------")
#**************taske2**********************

print ("-------------------------------------")

def connect(ip, port):
    def printer(func):
        def inner(doc):
            print (f" Connected to IP; {ip}: {port}")
            func(doc)
            print (f"closse connection." )
        return inner
    return printer

@connect(ip = "11.11.11.11", port = 4880)
def hp (doc):
    print (" I am HP printer")
    print (f" printing:{doc}")
@connect(ip = "12.12.12.12", port = 2332)
def cannon (doc):
    print (" I am cannon printer")
    print (f" printing:{doc}")

hp("what‘s goen on")
