import sys
out = []
t = input() # 数据组数
# print(t)
t = int(t)
for i in range(t):
    n = sys.stdin.readline()
    # print(n)
    n = int(n)
    input = sys.stdin.readline().split()
    output = sys.stdin.readline().split()
    input = [int(i) for i in input] # 进入顺序
    output = [int(j) for j in output] # 驶出顺序
    # print(input)
    # print(output)
    output.reverse()
    buffer = []
    i = 0 
    while i < n:
        buffer.append(input[i])

        i += 1
        nn = len(buffer)
        for k in range(nn):
            if buffer[-1] == output[-1]:
                buffer.pop()
                output.pop()
            
        
    if buffer == []:
        out.append('Yes') 
    else:
        out.append('No') 

for item in out:
    print(item+'\n')
