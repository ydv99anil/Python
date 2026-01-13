userName = "Anil Yadav"

print("Scope Testing - 1")

def scopeTest():
    # userName = "Rinku Jai"
    print(userName) 
    #It will print glabally declared username


print(userName)
scopeTest()



print("Scope Testing - 2")

x = 99
def scopeTest2(y):
    z = x + y
    return z

print(scopeTest2(1))


print("Scope Testing - 3")

def scopeTest3():
    x = 88 # Agar m yhaa x ko comment krr du to niche vala x global x ki value lega
    def func2():
        print(x)
    func2()
scopeTest3()


print("Closure Testing - 1")

def scopeTest4():
    x = 88
    def func3():
        print(x)
    return func3
result = scopeTest4()
result()


print("Closure Testing - 2: this is proper closure")

def closureTest1(num):
    def actual(n):
        return n ** num
    return actual

testResult = closureTest1(8)
finalResult = testResult(2)
print(finalResult)