def build_prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix


def range_sum(prefix, i, j):
    if i == 0:
        return prefix[j]
    return prefix[j] - prefix[i - 1]


study_hours = [2, 3, 1, 4, 2, 5, 3, 2]
prefix = build_prefix_sum(study_hours)

print("Sum from day 2 to day 5:", range_sum(prefix, 2, 5))
print("Sum from day 0 to day 3:", range_sum(prefix, 0, 3))