"""
Grace Michael
DS2500: Programming with Data
HW 4
"""
import collections as col
from graph import *
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

class Node:
# The constructor
    def __init__(self, name, category, props={}):
        self.name = name
        self.category = category
        self.props = props
# Get the name of the node
    def get_name(self):
        return self.name
# Get the category of the node
    def get_category(self):
        return self.category
# Get the value for a specified property key
    def get_property(self, key):
        return self.props.get(key)
# Assign the key/value pair to the node
    def set_property(self, key, value):
        self.props[key] = value
# Return all properties for a given node as a dictionary
    def get_all_properties(self):
        return self.props
    def __str__(self):
        return self.name
# Are two nodes, u and v, the same?  E.g., u==v?
    def __eq__(self, other):
        u = self
        v = other
        # seperate objects, even if identical
        if self.get_name() == other.get_name():
            if u.get_category() == v.get_category():
                if u.get_property() == v.get_property():
                    return True
        else:
            return False
# A hashing function so that nodes can be stored as dictionary keys
    def __hash__(self):
        node_dict = {}
        key = (self.name, self.category)
        value = self.props
        node_dict[key] = value
        return hash(self.name + " " + self.category)


class Relationship:
# A constructor
    def __init__(self, category, props={}):
        self.category = category
        self.props = props
# Get the category of the relationship
    def get_category(self):
        return self.category
# Get the value for a specified property key
    def get_property(self, key):
        value = self.props[key]
        return value
# Assign the key/value pair to the Relationship
    def set_property(self, key, value):
        self.props = (key, value)
# Return all properties for a given relationship
    def get_all_properties(self):
        return dict(self.props)


class PropertyGraph(Graph):#PropertyGraphs inherit from a regular directed Graph as done in class.
#The constructorfor a PropertyGraph
    def __init__(self, nodes=[], relationships=[]):
        super().__init__(V = nodes, E = relationships)
        self.nodes = []
        self.rels = []
        self.edges = {}
# Add a node to the graph
    def add_node(self, n):
        super().add_vertex(n)
# Add a relationship(rel) to the graph connecting node n to node m.
    def add_relationship(self, u, v, rel):
        super().add_edge(u,v)
        if u not in self.edges.keys():
            self.add_node(u)
        if v not in self.edges.keys():
            self.add_node(v)
            self.edges[(u,v)] = rel
#Find nodes meeting certain criteria.  For example, having a particular name /
#label or category type, or matching a specific property.These constraints areconsidered to be ANDs.
    def find_nodes(self, name=None, category=None, key=None, value=None):
        criteria = []
        for u in self.G:
            for v in self.G[u]:
                if (u,v) not in criteria and (v,u) not in criteria:
                    criteria.append((u,v))
        return criteria
#Return the subgraph as a PropertyGraph consisting of a specified set of nodes and any interconnecting edges/relationships
    def subgraph(self, V):
        sub = PropertyGraph()
        for u in V:
            sub.add_node(u)
        for u in V:
            for v in V:
                if (u,v) in self.edges:
                    r = self.edges[(u,v)]
                    sub.add_relationship(u,v,r)
        return sub
#return all adjacent nodes, possibly constrained to a particular category of nodes and/or relationships.
#You may optionally want to add further constraints on node / relationship properties.
    def adjacent(self, n, node_category=None, rel_category=None):
        # optional contraints
        super().__getitem__(n)
        adj = []
        for (u,v) in self.edges:
            if u.get_name() == n.get_name():
                adj.append(v.get_name())
            if u.get_category() == node_category:
                adj.append(v.get_name())
            if self.edges[(u,v)] == rel_category:
                adj.append(v.get_name())
        return adj
# Generate a visualization of your graph.  Only the nodes need belabeled.
#You don’t need to label the relationships ordisplay any node or relationship properties.
#Nodes should be color-coded by the category of the node.You may use a Sankeydiagram or a graph produced using the networkx library.
    # Create a DF
    def toDF(self, columns=['u','v']):
        df = pd.DataFrame(columns=columns)
        for(u,v) in self.find_nodes():
            df = df.append({columns[0]:u, columns[1]:v}, ignore_index=True)
            if (u,v) in self.edges and (v,u) in self.edges:
                df = df.append({columns[1]:u, columns[0]:v}, ignore_index=True)

        return df
    # Create edges from DF
    def fromDF(self, df, columns=['u', 'v']):
        edges = list(zip(df[columns[0]], df[columns[1]]))
        for u,v in edges:
            self.add_edge(u,v)
    # Visualize DF
    def visualize(self, node_size=300, node_color='r', fig = 1):
        df = self.toDF()
        G = nx.from_pandas_edgelist(df, df.columns[0], df.columns[1], create_using=nx.DiGraph())
        plt.figure()
        colors=[]
        for node in G:
            if node.category == 'PERSON':
                # people
                colors.append('#E17F93')
            else:
                # movies
                colors.append('#957DAD')
        nx.draw(G, with_labels=True, node_size=node_size, node_color=colors)
        plt.show()


def main():
    # make all Nodes
    p1 = Node('Reuben', 'PERSON', props = {'occupation':'Student'})
    p2 = Node('John','PERSON', props = {'occupation':'Professor'})
    p3 = Node('Laney','PERSON', props = {'occupation':'Professor'})

    m1 = Node('Interstellar', 'MOVIE', props = {'genre':'Sci-Fi', 'rated':'PG-13', 'year':'2014'})
    m2 = Node('Star Trek', 'MOVIE', props = {'genre':'Sci-Fi', 'rated':'PG-13', 'year':'2009'})
    m3 = Node('Princess Bride', 'MOVIE', props = {'genre':'Fantasy', 'rated':'PG', 'year':'1987'})
    m4 = Node('Top Gun', 'MOVIE', props = {'genre':'Action', 'rated':'PG', 'year':'1986'})
    m5 = Node('Keeping the Faith', 'MOVIE', props = {'genre':'Rom-Com', 'rated':'PG-13', 'year':'2000'})
    m6 = Node('Ghostbusters', 'MOVIE', props = {'genre':'Fantasy', 'rated':'PG', 'year':'1984'})


    # make all Relationships
    RI = Relationship('WATCHED', {'rate':5})
    knows = Relationship("KNOWS")
    JI = Relationship('WATCHED', {'rate':5})
    JS = Relationship('WATCHED', {'rate':5})
    JP = Relationship('WATCHED', {'rate':4})
    JT = Relationship('WATCHED', {'rate':3})
    LP = Relationship('WATCHED', {'rate':5})
    LT = Relationship('WATCHED', {'rate':4})
    LK = Relationship('WATCHED', {'rate':4})
    LG = Relationship('WATCHED', {'rate':5})

    # Part B Number 2
    graph = PropertyGraph()

    # add relationships to graph
    graph.add_relationship(p1, m1, RI)
    graph.add_relationship(p2, m1, JI)
    graph.add_relationship(p2, m2, JS)
    graph.add_relationship(p2, m3, JP)
    graph.add_relationship(p2, m4, JT)
    graph.add_relationship(p3, m3, LP)
    graph.add_relationship(p3, m4, LT)
    graph.add_relationship(p3, m5, LK)
    graph.add_relationship(p3, m6, LG)
    graph.add_relationship(p2, p1, knows)
    graph.add_relationship(p2, p3, knows)
    graph.add_relationship(p3, p2, knows)

    # visualize these relationships
    graph.visualize(fig=1)


    # Part B Number 3
    # only people nodes from graph
    subg = graph.subgraph([p1, p2, p3])
    subg.visualize(fig=2)

    # Part B Number 4
    # adjacents of John and Laney
    adj_j = graph.adjacent(p2)
    adj_l = graph.adjacent(p3)

    # return what's in both
    adj_v = []
    for x in adj_j:
        if x in adj_l:
            adj_v.append(x)
    print("John and Laney both watched the following:", adj_v)

    # Part B Number 5

    # adjacents of Reuben
    adj_r = graph.adjacent(p1)

    solos = []
    friends = []
    rec = []

    # filter out Names
    # Keep John's movie's seperate from friends'
    for item in adj_j:
        if item != 'John' and item != 'Laney' and item != 'Reuben':
            solos.append(item)
    for item in adj_l:
        if item != 'John' and item != 'Laney' and item != 'Reuben':
            friends.append(item)
    for item in adj_r:
        if item != 'John' and item != 'Laney' and item != 'Reuben':
            friends.append(item)

    # recommend movies John's friends have seen that he has not
    for item in friends:
        if item not in solos:
            rec.append(item)

    print("It is recommended that John watches the following:", rec)

if __name__ == '__main__':
    main()

'''

John and Laney both watched the following: ['Princess Bride', 'Top Gun']
It is recommended that John watches the following: ['Keeping the Faith', 'Ghostbusters']

'''
