def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]

        if total == target:
            return left, right
        elif total < target:
            left += 1
        else:
            right -= 1

    return -1, -1


prices = [100, 250, 400, 600, 850, 1000]
budget = 1250

left_idx, right_idx = two_sum_sorted(prices, budget)

if left_idx != -1:
    print(f"Found: {prices[left_idx]} + {prices[right_idx]} = {budget}")
else:
    print("No matching pair found.")