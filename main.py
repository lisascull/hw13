operation = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}
n = int(input())

files = {}

for i in range(n):
    file_data = input().split()
    filename = file_data[0]
    operations = set(file_data[1:])
    files[filename] = operations

m = int(input())

for i in range(m):
    operation, filename = input().split()

    if operation in files[filename]:
        output += 'OK\n'
    else:
        output += 'Access denied\n'
print(output)