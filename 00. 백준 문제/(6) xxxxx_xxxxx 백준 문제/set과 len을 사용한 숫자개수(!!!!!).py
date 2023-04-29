num_list = []
for i in range(10):
    number = int(input())
    num_list.append(number % 42)

num_list = set(num_list)
print(len(num_list))