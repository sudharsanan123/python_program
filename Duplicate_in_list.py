list1=list(map(int,input().split()))
list2=set(list1) 
if len(list1)==len(list2):
    print("No Duplicate")
else:
    print(list2)
    
