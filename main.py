def file_permissions(n, files, m, queries):

    files = {}
    for i in range(n):
        file, permissions = files[i].split()
        files[file] = permissions

    results = []
    for i in range(m):
        operation, file_name = queries[i].split()

        if file_name not in files:
            results.append('Access denied')
            continue

        if operation in files[file_name]:
            results.append('OK')
        else:
            results.append('Access denied')

    return results

#for _ in range(n):
    #file_name, operations = input('Введіть назву файлу та допустимі операції: ')
    #files[file_name] = set(operations)

#m = int(input('Введіть кількість запитів: '))

#for _ in range(m):
   # operation, file_name = input('Введіть операцію та назву файлу: ')
