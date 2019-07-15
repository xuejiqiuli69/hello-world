# def OnceSort(a,begin,end):
#     i,j=begin,end
#     pivot=a[begin]
#     while i<j:
#         while i<j and a[j]>pivot:
#             j=j-1
#         if i<j:
#             a[i]=a[j]
#         while i<j and a[i]<=pivot:
#             i=i+1
#         if i<j:
#             a[j]=a[i]
#         if i==j:
#             a[i]=pivot
#     return i
#
# def Qsort(a,begin,end):
#     if begin<end:
#         k=OnceSort(a,begin,end)
#         Qsort(a,begin,k-1)
#         Qsort(a,k+1,end)
def Heapfi(a,i,ln):
    father=i
    temp=a[father]
    son=2*father+1
    while son<ln:
        if (son+1<ln) and (a[son]<a[son+1]):
            son=son+1
        if temp>a[son]:
            break
        else:
            a[father]=a[son]
            father=son
            son=2*father+1
    a[father]=temp


def HeapSort(a):
    ln=len(a)
    for i in range(ln//2-1,-1,-1):
        Heapfi(a,i,ln)
    for i in range(ln-1,0,-1):
        temp=a[i]
        a[i]=a[0]
        a[0]=temp
        Heapfi(a,0,i)

a=[34,65,12,34,43,67,5,78,10,3,70]
print(a)
# Qsort(a,0,len(a)-1)
HeapSort(a)
for i in a:
    print(str(i)+' ',end='')
print('')
print('test')
print('test')