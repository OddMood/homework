import heapq


def calculate_network_delay(_times: list[list[int]], _n: int, _x: int) -> int:
    edges = dict()
    for [start, end, time] in _times:
        edges[start] = edges.get(start, []) + [[time, end]]
    heap_of_nodes = [[0, _x]]
    visited_nodes = set()
    total_time = 0
    while heap_of_nodes:
        edge = heapq.heappop(heap_of_nodes)
        if edge[1] in visited_nodes:
            continue
        visited_nodes.add(edge[1])
        total_time = edge[0]
        for [time, end_node] in edges.get(edge[1], []):
            if end_node not in visited_nodes:
                heapq.heappush(heap_of_nodes, [edge[0] + time, end_node])

    return total_time if len(visited_nodes) == _n else -1


if __name__ == "__main__":
    times = eval(input())
    n = int(input())
    x = int(input())
    out = calculate_network_delay(times, n, x)
    print(out)

