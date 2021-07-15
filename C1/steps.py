import sys

height = int(sys.argv[1])
for i in range(height):
    j = -1
    for j in range(height - 1 - i):
        print(' ', end='')
    for k in range(height - 1 - j):
        print('#', end='')
    print('\n', end='')

