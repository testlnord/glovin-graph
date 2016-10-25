import csv
import os

import glove
import scipy
import scipy.sparse

FITTED_MODEL_FILENAME = 'fitted_model.glove'


def load_graph_adj_matrix():
    adj_list_in_ids = {}
    tag_name_to_idx = {}
    with open('graph.csv') as graph_file:
        graph_reader = csv.DictReader(graph_file)
        tag_names = set()
        for row in graph_reader:
            tag_name_1 = row['tag1']
            tag_name_2 = row['tag2']
            post_count = int(row['post_count'])

            tag_names.add(tag_name_1)
            tag_names.add(tag_name_2)
            try:
                adj_list_in_ids[tag_name_1].append((tag_name_2, post_count))
            except KeyError:
                adj_list_in_ids[tag_name_1] = [(tag_name_2, post_count)]


        tag_name_to_idx = {tag_name: idx for idx, tag_name in enumerate(sorted(tag_names))}

    # initialize empty matrix
    tags_count = len(adj_list_in_ids)
    adj_matrix = scipy.zeros((tags_count, tags_count))
    for tag_name, adj_row in adj_list_in_ids.items():
        tag_namex = tag_name_to_idx[tag_name]
        for adj_tag, post_count in adj_row:
            adj_tag_namex = tag_name_to_idx[adj_tag]
            adj_matrix[tag_namex, adj_tag_namex] = post_count
            adj_matrix[adj_tag_namex, tag_namex] = post_count
    # normalization
    normalized_adj_matrix = scipy.divide(adj_matrix, adj_matrix.sum(1)[:,scipy.newaxis])

    #ordered_by_idx_tag_names = sorted(tag_name_to_idx.keys(), key=lambda tag_name: tag_name_to_idx[tag_name])
    return scipy.sparse.coo_matrix(normalized_adj_matrix), tag_name_to_idx


def main():

    if os.path.exists(FITTED_MODEL_FILENAME):
        glove_model = glove.Glove.load(FITTED_MODEL_FILENAME)
    else:
        matrix, dictionary = load_graph_adj_matrix()
        glove_model = glove.Glove(2)
        glove_model.fit(matrix, epochs=10)
        glove_model.add_dictionary(dictionary=dictionary)
        glove_model.save(FITTED_MODEL_FILENAME)

    graph_positions = {}
    for vertex_idx, vertex_name in glove_model.inverse_dictionary.items():
        vertex_pos = tuple(glove_model.word_vectors[vertex_idx])
        graph_positions[vertex_name] = vertex_pos



    pass

if __name__ == '__main__':
    main()