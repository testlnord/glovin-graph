import networkx
import networkx.generators.classic
import networkx.drawing
import scipy, scipy.sparse
import glove
import matplotlib.pyplot as plt

def main():
    wheel_graph = networkx.generators.classic.wheel_graph(10)
    model = glove.Glove(2,learning_rate=0.01, alpha=0.2, max_count=1000)

    adj_matrix = networkx.adjacency_matrix(wheel_graph)
    adj_matrix = adj_matrix.toarray().astype('d')
    normalized_adj_matrix = scipy.divide(adj_matrix, adj_matrix.sum(1)[:,scipy.newaxis])
    model.fit(scipy.sparse.coo_matrix(normalized_adj_matrix), epochs=1000)

    vertex_positions = {vertex_idx:tuple(model.word_vectors[vertex_idx]) for vertex_idx in range(wheel_graph.order())}

    networkx.drawing.draw(wheel_graph, pos=vertex_positions)
    plt.savefig("asdf.png")
    pass

if __name__ == "__main__":
    main()