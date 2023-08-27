from scipy import optimize

def value(vector):
    #compute the value of a branching verctor
    def h(x):
        return sum([x**-v for v in vector]) -1
    return optimize.brenth(h, 1, 10)

while 1 : 
    vector = eval(input('please input  the vector\n'))

    print(value(vector))