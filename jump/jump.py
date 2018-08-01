def jump(self, nums):
    import queue
    def BFS(graph,name):
        q=queue.Queue()
        if name[0] == name[-1]:
            return 0
        for value in graph[name[0]]:
            q.put((value,1))
        while not q.empty():
            node = q.get()
            if node[0] == name[-1]:
                return  node[1]
            for value in graph[node[0]]:
                lists  = [p[0] for p in  list(q.queue)]
                if value not in  lists :
                    q.put((value,node[1]+1))


    length = len(nums)
    graph = {}
    name = [j for j in range(length)]
    for j in range(length):
        num = nums[j]
        graph[j] = []
        for i in range(j+1,num+j+1):
            if i<length:
                graph[j].append(name[i])
    return BFS(graph,name)
