from random import randint as ri
from collections import Counter

nums = []

# generates random numbers between 0 and 9
# 1 million times and shows how random each selection is
for _ in range(1000000):
    nums.append(ri(0,9))

item_counts = Counter(nums)
sorted_items = sorted(item_counts.items())

for item, count in sorted_items:
    print(f"Item {item} occurs {count} times")
