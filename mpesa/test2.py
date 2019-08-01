# data={
#     "name":"Alby",
#     "age":23
# }


# print (data['age'])

# def foo():
#     print("Hellow world")
#     return 1

# print (foo())
# a="aa"

class MyClass():
    def fn1(self):
        self.var1="Some shit"

    def fn2(self):
        print (self.var1)


foo=MyClass()
foo.fn1()
foo.fn2()

