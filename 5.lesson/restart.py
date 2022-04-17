# from this import d


# def f(x):
#    return x * 2
# result = f(5)
# print(result )

# result = f(int(input("enter number: ")))
# print (result)

# def a(k,b,d):
#     return k + b + d
# super = a(int(input("Enter Number: ")),int(input("Enter Number: ")),int(input("Enter Number: ")))
# print (super)

# def num(x):
#     return x * 5
# result = num(int(input("enter number ")))

# if result > 25:
#     print(str(result) + " Більше 25 ")
# else:
#     print(str(result) + " Меньше 25 ")
    
#   #__________________________________________  
def month(d):
    if d == 1 :
        return "Січень"
    elif d == 2:
        return "Лютий"
    elif d == 3:
        return "Березень"
    elif d == 4:
        return "Квітень"
    elif d == 5:
        return "Травень"
    elif d == 6:
        return "Червень"
    elif d == 7:
        
        return "Липень"
    elif d == 8:
        return "Серпень"
    elif d == 9 :
        return "Вересень"
    elif d == 10:
        return "Жовтень"
    elif d == 11:
        return"Листопад"
    elif d == 12:
        return "Грудень"    
result = month(int(input("Ведіть число від 1 до 12 ")))
print(result)


#______________________________________________

def aref(d,f,x):
    return d + f + x / 3
result = aref(int(input("введіть число ")),int(input("введіть число")),int(input("введіть число ")))
print(result)


    
    



