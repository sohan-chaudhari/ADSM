def watch(str,str1):
    i=str1
    if i in str:
        return True
    else:
        return False

str=input("enter the string :")
str1=input("enter the another string :")
value=watch(str,str1)
print(value)

