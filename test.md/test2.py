def seq_search(arr,arr2):
    flag=0
    for i in arr2:
        for j in arr:
            if arr2[i]==arr[j]:
                print(1,end=" ")
                flag=1
                break
            else:
                continue

    if flag==0:
        print(0,end=" ")

    
arr=[]
n=int(input())

arr=[None]*n


arr=list(map(int,input(f"상근이 입력: ").split()))



arr2=[]
n2=int(input())

arr2=[None]*n2


arr2=list(map(int,input(f"카드 입력: ").split()))

seq_search(arr,arr2)
















