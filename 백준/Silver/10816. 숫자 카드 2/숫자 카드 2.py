N = int(input())
card_list = list(map(int, input().split()))
M = int(input())
number_list = list(map(int, input().split()))

result = {}

for card in card_list:
    if card in result:
        result[card] += 1
    else:
        result[card] = 1

for number in number_list:
    if number in result:
        print(result[number], end = ' ')
    else:
        print(0, end = ' ')
