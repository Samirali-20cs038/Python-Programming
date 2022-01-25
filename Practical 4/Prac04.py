num = int(input())
x = list(map(int, input().split()))
if len(x) == num:
    srt = sorted(set(x), reverse = True)
print(srt[1])