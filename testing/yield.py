def provider():
    for i in range(1,10):
        print("before")
        yield i
        print("after")


p = provider()
print(next(p))
print(next(p))