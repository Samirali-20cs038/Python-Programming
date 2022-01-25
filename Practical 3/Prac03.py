n = int(input()) #took input from the student
#split the element
l = list(map(int,input().split()))
#using loop chack the condition
for x in l:
    if l.count(x) == 1:
        print(x)
#store the input
k,arr = int(input()),list(map(int, input().split()))
myset = set(arr)
#print result
print(((sum(myset)*k)-(sum(arr)))//(k-1))