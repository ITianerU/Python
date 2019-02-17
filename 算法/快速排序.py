"""
快速排序
"""

def quickSort(list):
    if len(list) < 2:
        return list
    pivot = list[0]
    left = [i for i in list[1:] if i <= pivot]
    right = [i for i in list[1:] if i > pivot]
    return quickSort(left) + [pivot] + quickSort(right)

if __name__ == '__main__':
    print(quickSort([5,3,6,12,5,7,9,1]))


