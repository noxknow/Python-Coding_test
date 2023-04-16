import sys
input = sys.stdin.readline
testCases = int(input().rstrip("\n"))
for _ in range(testCases):
    n = int(input().rstrip("\n"))
    nums = list(map(int, input().rstrip("\n").split()))
    value=0
    max=0
    for i in range(len(nums)-1,-1,-1):
        if(nums[i] > max):
            max = nums[i]
        else:
            value+=max-nums[i]
    print(value)
