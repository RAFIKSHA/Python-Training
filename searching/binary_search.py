def binary_search(lst,l,h):
    key=24
    while l<=h:
    
        mid=(l+h)//2
        if lst[mid]==key:
          print("key is found",lst[mid])
        elif lst[mid]>key:
          l=mid+1
        else:
          high=mid-1
    else:
       print("element not found") 
lst=[12,15,17,18,20,24,30]
l=0
h=len(lst)-1
binary_search(lst,l,h)