
from collections import deque


def search(dict, start, end):
    # 创建队列
    search_queue = deque()
    search_queue += dict[start]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person == end:
                temp = person
                result = [person]
                for i in range(len(searched)-1, -1, -1):
                    if temp in dict[searched[i]]:
                        result.append(searched[i])
                        temp = searched[i]
                result.append(start)
                for i in reversed(result):
                    print(i)
                return True
            else:
                search_queue += dict[person]
                searched.append(person)
    print('None')
    return False

if __name__ == '__main__':
    d = dict()
    d['a'] = ['b', 'c', 'd']
    d['b'] = ['e', 'f']
    d['c'] = ['f']
    d['d'] = ['g', 'h']
    d['e'] = ['i']
    d['f'] = []
    d['g'] = []
    d['h'] = []
    d['i'] = []
    search(d, 'a', 'i')
