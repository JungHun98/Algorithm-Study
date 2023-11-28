M = int(input())

def print_star(N):
    if N == 1:
        return ['*']

    stars = print_star(N//3)
    result = []

    for star in stars:
        result.append(star*3)
    for star in stars:
        result.append(''.join([star, ' '*(N//3), star]))
    for star in stars:
        result.append(star * 3)
    return result

for ans in print_star(M):
    print(ans)
