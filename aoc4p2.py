with open("aoc4Input", "r") as tf:
    lines = tf.read().strip().split("\n")

n = len(lines)
m = len(lines[0])


dd =[]
for dx in range(-1,2):
    for dy in range(-1,2):
        if dx != 0 or dy !=0:
            dd.append((dx,dy))

def count_xmas(i, j):
    if not(1<=i<n-1 and 1<=j<m-1):
         return False
    if (lines[i][j] != 'A'):
         return False
    diag1 = lines[i-1][j+1]+lines[i][j]+lines[i+1][j-1]
    diag2 = lines[i+1][j+1]+lines[i][j]+lines[i-1][j-1]

    if (diag1 in ['MAS','SAM'] and diag2 in ['MAS','SAM']):
        return True 
    return False


ans = 0
for i in range(n):
    for j in range(m):
            ans += count_xmas(i,j)
print(ans)

