def solution(gems):
    gem_set = set(gems)
    gem_count = len(gem_set)

    answer = [1, len(gems)]
    dic = {}
    start = 0

    for end, gem in enumerate(gems):
        dic[gem] = end + 1

        while len(dic) == gem_count:
            if end - start < answer[1] - answer[0]:
                answer = [start + 1, end + 1]

            gem = gems[start]
            dic[gem] = max(dic[gem], start + 1)
            if dic[gem] == start + 1:
                del dic[gem]

            start += 1

    return answer
