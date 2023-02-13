#palindrome
n = input("enter string:")
m = n[::-1]
if (n == m):
    print("it is palindrome")
else:
    print("Not a palindrome")


#clockwise
def rotate(L, d, n):
    k = L.index(d)
    new_lis = []
    new_lis = L[k+1:]+L[0:k+1]
    return new_lis
 
 
if __name__ == '__main__':
    arr = list(map(int,input().split()))
    d = int(input("enter a number:"))
    N = len(arr)
 
    # Function call
    arr = rotate(arr, d, N)
    for i in arr:
        print(i, end=" ")


#highest frequency
frequency = list(map(int,input().split()))
k = 0
number = frequency
for i in frequency:
    value = frequency.count(i)
    if(value> k):
        k = value
        number = i
 
print(number)

#duplicate elements
array = list(map(int,input().split()))
l = []
k = []
for i in array:
    if i not in l:
        l.append(i)
for i in l:
    if array.count(i) > 1:
        k.append(i)
# print(k, end = " ")
print(*k,sep= ' ')
