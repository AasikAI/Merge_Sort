def merge(arr):
    if len(arr)>2:
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        merge(l)
        merge(r)
        i = j = k = 0
        while i<len(l) and j<len(r):
            if l[i]<=r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k+=1
        while i<len(l):
            arr[k] = l[i]
            i+=1
            k+=1
        while j<len(r):
            arr[k] = r[j]
            j+=1
            k+=1
def printl(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print("\r")
if __name__ == '__main__':
    arr = [5,2,8,3,6]
    print("Unsorted array |")
    printl(arr)
    print("Sorted array |")
    merge(arr)
    printl(arr)

