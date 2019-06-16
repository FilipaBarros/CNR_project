#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle
import networkx as nx
import matplotlib.pyplot as plt

FILENAME = "graph_properties_nobel_ger_demand_ger_uniform_Link_Disjoint.pkl"

G = nx.Graph()

def add_proprieties(protection_distance, demands, working_distance):
    for key in protection_distance.keys():
        G.add_edge(key[0], key[1], 
                   protection_distance=protection_distance.get(key),
                   demand=demands.get(key),
                   working_distance = working_distance.get(key))
        G[key[0]][key[1]]['color']='grey'

def add_working_paths(obj):
    for key in obj.keys():
        print(key[0], key[1])
        for key_inner in obj.get(key): 
            G.add_edge(key_inner[0], key_inner[1], type='working_path', connection=key)
            G[key_inner[0]][key_inner[1]]['color']='blue'

def add_protection_path(obj):
    for key in obj.keys():
        print(key[0], key[1])
        for key_inner in obj.get(key): 
            G.add_edge(key_inner[0], key_inner[1], type='protection_path', connection=key)
            G[key_inner[0]][key_inner[1]]['color']='red'


with open(FILENAME, 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    data = pickle.load(f)
    protection_distance = data["protection_distance"]
    demands = data["demands"]
    working_distance = data["working_distance"]
    add_proprieties(protection_distance, demands, working_distance)

    working_paths = data["working_paths"]
    add_working_paths(working_paths)
    protection_path = data["protection_path"]
    add_protection_path(protection_path)
    print(data)
    
edges = G.edges()

colors = []

for (u,v,attrib_dict) in list(G.edges.data()):
    colors.append(attrib_dict['color'])


nx.draw(G, with_labels=True, edges=edges, edge_color=colors)

plt.show()
