def count_increasing(array):
    result = 0
    prev = array[0]
    for n in array:
        if n > prev:
            result += 1

        prev = n

    return result


def count_increasing_threes(array):
    result = 0
    prev_sum = sum(array[:3])
    curr_sum = prev_sum
    for i in range(3, len(array)):
        curr_sum += array[i] - array[i - 3]
        if curr_sum > prev_sum:
            result += 1

        prev_sum = curr_sum

    return result


if __name__ == "__main__":
    f = open("day1", "r")
    a = [int(n) for n in f.readlines()]
    print(count_increasing(a))
    print(count_increasing_threes(a))

