def jump(self, nums):
    import queue
    def BFS(graph,nums):
        q=queue.Queue()
        value = nums[0]
        if nums[0] == nums[-1]:
            return 0
        for value in graph[nums[0]]:
            q.put((value,1))
        while not q.empty():
            node = q.get()
            if node[0] == nums[-1]:
                return 	node[1]
            for value in graph[node[0]]:
                lists  = [p[0] for p in  list(q.queue)]
                if value not in  lists :
                    q.put((value,node[1]+1))



    length = len(nums)
    graph = {}
    nums[-1] = max(nums)+1
    for j in range(length):
        num = nums[j]
        graph[num] = []
        for i in range(j+1,num+j+1):
            if i<length:
                graph[num].append(nums[i])
    return BFS(graph,nums)