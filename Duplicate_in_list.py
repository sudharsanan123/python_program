list1=list(map(int,input().split()))
list2=set(list1) #set is a built-in function which remove duplicate values
if len(list1)==len(list2):
    print("No Duplicate")
else:
    print(list2)
    
