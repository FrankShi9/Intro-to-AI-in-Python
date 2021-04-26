#import numpy as np

graph = [{0:0,'h':0,0:0,'j':0},{'g':0,0:0,'i':0,0:0},{0:0,'h':0,0:0,'j':0},{'g':0,0:0,'i':0,0:0}]
map = {'g':0,'h':1,'i':2,'j':3}
cnt = 0

def DFS(G):

    for ele in graph:
        for key in ele.keys():
            if key != 0:
                if ele.get(key) == 0:
                    dfs(key)

def dfs(input):
    global cnt
    cnt += 1
    index = map.get(input)

    for ele in graph[index]:
        for key in ele.keys():
            if key != 0:
                if ele.get(key) == 0:
                    dfs(key)
