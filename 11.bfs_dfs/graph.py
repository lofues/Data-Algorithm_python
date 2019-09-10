"""
    图的基本定义
    Author by : Lofues
"""

# 无向图
class Undigraph(object):
    def __init__(self,vertex_num):
        self.v_num = vertex_num
        self.adj_vertex = []
        for i in range(self.v_num+1):
            self.adj_vertex.append([])

    def add_edge(self,s,t):
        if s > self.v_num or t > self.v_num:
            return False
        self.adj_vertex[s].append(t)
        self.adj_vertex[t].append(s)

    def __getitem__(self, item):
        if item > self.v_num:
            raise IndexError('No Such Vertex!')
        return self.adj_vertex[item]

    def __repr__(self):
        print(self.adj_vertex)

    def __len__(self):
        return self.v_num

    def __str__(self):
        return str(self.adj_vertex)

# 有向图
class Digraph(object):
    def __init__(self,vertex_num):
        self.v_num = vertex_num
        self.adj_vertex = []
        for i in range(self.v_num):
            self.adj_vertex.append([])

    def add_edge(self,s,t):
        if s > self.v_num or t > self.v_num:
            return False
        self.adj_vertex[s].append(t)

    def __getitem__(self, item):
        if item > self.v_num:
            raise IndexError("No Such Vertex!")
        return self.adj_vertex[item]

    def __repr__(self):
        return str(self.adj_vertex)

    def __str__(self):
        return str(self.adj_vertex)


if __name__ == '__main__':
    ug = Undigraph(10)
    ug.add_edge(1, 9)
    ug.add_edge(1, 3)
    ug.add_edge(3, 2)
    print(ug)

    dg = Digraph(10)
    dg.add_edge(1, 9)
    dg.add_edge(1, 3)
    dg.add_edge(3, 4)
    print(dg)













