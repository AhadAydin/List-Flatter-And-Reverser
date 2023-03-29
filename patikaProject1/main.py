


def flatter(x):
    result = []
    for i in x:
        if type(i) == list:
            inner_list = flatter(i)
            for j in inner_list:
                result.append(j)
        else:
            result.append(i)
    return result

def reverser(x):
    result = []
    for i in x[::-1]:
        if type(i) == list:
            result.append(reverser(i))
        else:
            result.append(i)
    return result


sample_list = [1, 2, [3, 4], [5, [6, [7, 8]], 9], 10]

print(flatter(sample_list))
print(reverser(sample_list))