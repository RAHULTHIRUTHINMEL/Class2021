#binary search
pos = -1
def search(list,n):
    l = 0
    u = len(list)-1
    while l<=u:
        mid = (l+u)//2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid]< n:
                l = mid;
            else:
                u=mid;
list = [1,2,3,4,5,6,7,8,9]
n = 3
if search(list,n):
    print("Found at ",pos+1)
else:
    print("didnot find")

