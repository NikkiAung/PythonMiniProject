import math as m
def calculate(length):
    area = length*length
    return area

def get_hypotenuse(a,b):
    hypotenuse = m.sqrt(calculate(a) + calculate(b))
    return hypotenuse

length1 = 3
length2 = 4
hypotenuse = get_hypotenuse(length1,length2)
print(hypotenuse)