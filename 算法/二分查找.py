"""
适用于有序的数列
"""

def search(list, item):
    start = 0;
    end = len(list) - 1
    while start <= end:
        middle = (start + end) // 2
        if list[middle] == item:
            return middle
        if list[middle] > item:
            end = middle - 1
        else:
            start = middle + 1
    return None

print(search([4,5,6,13,53,64,75],75))
print(search([4,5,6,13,53,64,75],123))
print(search([4,5,6,13,53,64,75],53))

