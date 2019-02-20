
def search():

    # 创建图
    graph = {}

    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2

    graph['a'] = {}
    graph['a']['end'] = 1

    graph['b'] = {}
    graph['b']['a'] = 3
    graph['b']['end'] = 5

    graph['end'] = {}

    # 创建开销表
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    infinity = float("inf")
    costs["end"] = infinity

    # 创建父节点表,记录路径
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["end"] = None

    searched = ["start"]

    # 取开销表最小开销节点
    node = find_lowest_cost_node(costs, searched)
    while node is not None:
        # 开销
        cost = costs[node]
        # 相邻节点(只包含后续要经过的节点)
        neighbors = graph[node]
        for n in neighbors.keys():
            # 计算新路径的开销
            new_cost = cost + neighbors[n]
            # 比较新路径的开销是否小于旧路径的开销
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        # 将该节点记录
        searched.append(node)
        node = find_lowest_cost_node(costs, searched)
    return searched

def find_lowest_cost_node(costs, searched):
    """
    取开销表最小开销节点
    :param searched:
    :param costs:
    :return:
    """
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in searched:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


if __name__ == '__main__':
    print(search())
