from random import randint as ri
from collections import Counter
import matplotlib.pyplot as plt

nums = ""

for _ in range(200000):
    nums += '{:05d}'.format(ri(0,99999))
    #nums += str(ri(0,99999))

item_counts = Counter(nums)
sorted_items = sorted(item_counts.items())
for item, count in sorted_items:
    print(f"Item {item} occurs {count} times")

labels, sizes = zip(*sorted_items)

plt.pie(sizes, labels=labels, autopct='%1.3f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the pie chart
plt.show()

