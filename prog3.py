def evenodd(a,b):
    print("hello1")
    i=0
    j=0
    c=[]
    k=len(a)
    n=len(b)
    while i<k:
        if i%2==0:
            c.append(a[i])
        i+=1        
    while j<n:
        if j%2!=0:
            c.append(b[j])
        j+=1
    print(c)
    return c
   
def ascsort(a):
    i=0
    buff=0
    k=len(a)
    while i<k-1:
        j=0
        while j<k-i-1:
            if a[j]>a[j+1]:
                buff=a[j]
                a[j]=a[j+1]
                a[j+1]=buff
            j+=1
        i+=1
    print(a)

def dessort(a):
    i=0
    buff=0
    k=len(a)
    while i<k-1:
        j=0
        while j<k-i-1:
            if a[j]<a[j+1]:
                buff=a[j]
                a[j]=a[j+1]
                a[j+1]=buff
            j+=1
        i+=1
    print(a)
    
def main():
    list1 = [3, 8, 1, 6, 12, 99, 2, 200, 1000, 5]
    list2 = [99, 7, 3, 101, 12, 22, 67, 55, 11, 2]
    a=1
    b=1
    while a==1:
        dig=input("select operation:\na - Display a list that consists of all the even index elements of the first list and the odd index ones from the second\nb - Display a list that consists of all the even index elements of the second list and the odd index ones from the first\nc - Display a list from the task item a, but sorted in ascending order\nd - Display a list from the task item a, but sorted in descending order\ne - Display a list from the task item b, but sorted in ascending order\nf - Display a list from the task item b, but sorted in descending order\ng - Finish\n")
        if dig == "a":
            d=evenodd(list1, list2)
            b=0
        elif dig == "b":
            e=evenodd(list2, list1)
            b=2
        elif dig == "c":
            if b == 0:
                ascsort(d)
            else:
                print("Select option a first")
        elif dig == "d":
            if b == 0:
                dessort(d)
            else:
                print("Select option a first")
        elif dig == "e":
            if b == 2:
                ascsort(e)
            else:
                print("Select option b first")
        elif dig == "f":
            if b == 2:
                dessort(e)
            else:
                print("Select option b first")
        elif dig == "g":
            break
        else:
            print("Incorrect item. Please re-enter:")

main()
