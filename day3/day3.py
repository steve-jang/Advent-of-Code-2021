def getGamma(nums):
    result = ""
    for i in range(len(nums[0])):
        result += getMostCommonBitAt(i, nums)

    return result


def bitwiseNOT(bits):
    result = ""
    converted = {"0": "1", "1": "0"}
    for b in bits:
        result += converted[b]

    return result


def multiplyBinary(x, y):
    return int(x, 2) * int(y, 2)


def powerConsumption(nums):
    gamma = getGamma(nums)
    epsilon = bitwiseNOT(gamma)
    return multiplyBinary(gamma, epsilon)


def getMostCommonBitAt(i, nums):
    zeros = 0
    ones = 0
    for n in nums:
        if n[i] == "0":
            zeros += 1
        else:
            ones += 1

    if ones >= zeros:
        return "1"
    else:
        return "0"


def getLeastCommonBitAt(i, nums):
    converted = {"1": "0", "0": "1"}
    return converted[getMostCommonBitAt(i, nums)]


def getRating(nums, criteria):
    candidates = nums[:]
    i = 0
    while len(candidates) > 1 and i < len(nums[0]):
        b = criteria(i, candidates)
        candidates = [n for n in candidates if n[i] == b]
        i += 1

    return candidates[0]


def getOxygen(nums):
    return getRating(nums, getMostCommonBitAt)


def getCO2(nums):
    return getRating(nums, getLeastCommonBitAt)


def lifeSupport(nums):
    return multiplyBinary(getOxygen(nums), getCO2(nums))


if __name__ == "__main__":
    lines = open("day3.txt", "r").readlines()
    nums = [line[:-1] for line in lines]
    print(powerConsumption(nums))
    print(lifeSupport(nums))

