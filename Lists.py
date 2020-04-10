if __name__ == '__main__':
    N = int(input())
    result = []
    for n in range(N):
        x = input().split(" ")
        command = x[0]
        if command == 'append':
            result.append(int(x[1]))
        elif command == 'print':
            print(result)
        elif command == 'insert':
            result.insert(int(x[1]), int(x[2]))
        elif command == 'reverse':
            result.reverse()
        elif command == 'pop':
            result.pop()
        elif command == 'sort':
            result.sort()
        elif command == 'remove':
            result.remove(int(x[1]))
        
