import networkx as nx
import matplotlib.pyplot as plt


weight_matrix = [
    [0, 3, 0, 0, 0, 0],
    [3, 0, 1, 0, 0, 0],
    [0, 1, 0, 7, 0, 2],
    [0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 2, 0, 1, 0]
]


G = nx.Graph()


G.add_nodes_from(range(1, len(weight_matrix) + 1))




for i in range(len(weight_matrix)):
    for j in range(i + 1, len(weight_matrix)):
        if weight_matrix[i][j] != 0:
            G.add_edge(i + 1, j + 1, weight=weight_matrix[i][j])


edge_labels = {}
for i in range(len(weight_matrix)):
    for j in range(i + 1, len(weight_matrix)):
        if weight_matrix[i][j] != 0:
            edge_labels[(i + 1, j + 1)] = weight_matrix[i][j]


pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

plt.title('Biểu đồ đường đi trên đồ thị')
plt.show()
