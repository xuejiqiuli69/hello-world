def curve_pr():
    a=25
    def curve():
        a=20
        print(a)
    print(a)
    curve()
    print(a)

curve_pr()
# a=10
# f=curve_pr()
# print(f.__closure__)
# print(f.__closure__[0].cell_contents)
# print(f(1))