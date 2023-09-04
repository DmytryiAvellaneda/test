def def_enter():
    list1 = [3, 8, 1, 6, 12, 99, 2, 200, 1000, 5]
    list2 = [99, 7, 3, 101, 12, 22, 67]
    handling(list1, list2)

def custom_enter():
    print("Enter the list of numbers 1: ")
    list1 = [int(b) for b in input().split()]    
    print("Enter the list of numbers 2: ")
    list2 = [int(b) for b in input().split()]
    handling(list1, list2)

def handling(list1, list2):
    print("handling")
    c=input("select operation:\na - list of elements which exist in both lists\nb - list of elements which exist only in one list\nc - both lists sorted in ascending order\nd - both lists sorted in descending order\ne - list of all elements of two lists that are less than 30'\n")
    match c:
        case "a":
            i=0
            j=0
            k=len(list1)
            n=len(list2)
            while i<k:
                while j<n:
                    if list1[i]==list2[j]:
                        print(list1[i])
                    j+=1
                j=0
                i+=1
        case "b":
            i=0
            j=0
            k=len(list1)
            n=len(list2)
            while i<k:
                flag=0
                while j<n:
                    if list1[i]==list2[j]:
                        flag=1
                        break
                    j+=1
                if flag == 0:
                    print(list1[i])                        
                j=0
                i+=1
        case "c":
            i=0
            buff=0            
            k=len(list1)
            n=len(list2)
            while i<k-1:
                j=0
                while j<k-i-1:
                    if list1[j]>list1[j+1]:
                        buff=list1[j]
                        list1[j]=list1[j+1]
                        list1[j+1]=buff
                    j+=1
                i+=1
            print(list1)
            i=0
            buff=0            
            while i<n-1:
                j=0
                while j<n-i-1:
                    if list2[j]>list2[j+1]:
                        buff=list2[j]
                        list2[j]=list2[j+1]
                        list2[j+1]=buff
                    j+=1
                i+=1
            print(list2)
        case "d":
            i=0
            buff=0            
            k=len(list1)
            n=len(list2)
            while i<k-1:
                j=0
                while j<k-i-1:
                    if list1[j]<list1[j+1]:
                        buff=list1[j]
                        list1[j]=list1[j+1]
                        list1[j+1]=buff
                    j+=1
                i+=1
            print(list1)
            i=0
            buff=0            
            while i<n-1:
                j=0
                while j<n-i-1:
                    if list2[j]<list2[j+1]:
                        buff=list2[j]
                        list2[j]=list2[j+1]
                        list2[j+1]=buff
                    j+=1
                i+=1
            print(list2)
        case "e":
            i=0
            j=0
            k=len(list1)
            n=len(list2)
            while i<k:
                if list1[i]<30:
                    print(list1[i])
                i+=1
            while j<n:
                if list2[j]<30:
                    print(list2[j])
                j+=1
        case _:
            print("Unknown option")

def main():
    a=1
    dig=int(input("Select data:\n1 - default 2 - custom\n"))
    while a==1:
        if dig == 1:
            def_enter()
            a=0;
        elif dig == 2:
            custom_enter()
            a=0;
        else:
            print("Incorrect item. Please re-enter:")
            dig=int(input("Select data:\n1 - default 2 - custom\n"))

main()    
