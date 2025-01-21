def remove(str):
    vowels="aeiouAEIOU"
    count=0
    for i in str:
        if i in vowels:
            count=count+1
    return count
str=input("enter the string")
run=remove(str)
print(run)
