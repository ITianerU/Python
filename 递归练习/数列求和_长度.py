
# 求和
def sum(list):
    if not list:
        return 0
    return list[0] + sum(list[1:])

def count(list):
    if not list:
        return 0
    return count(list[1:])+1

if __name__ == '__main__':
    list = [1, 2, 3, 4, 5]
    print(sum(list))
    print(count(list))
