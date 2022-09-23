FIRST_NODE = 0
SECOND_NODE = 1
EDGE = 2


class Node_data_set:

    def __init__(self, first_node, second_node, way_weight):
        self.first_node = first_node
        self.second_node = second_node
        self.way_weight = way_weight

    def return_way_weight(self):
        return self.way_weight

    def bool_operator(self, node_edge_weight):
        return self.way_weight < node_edge_weight


def sort_node_edge(node):
    for i in range(0, len( node ) ):
        for x in range(i, len( node ) ):
            if node[i].way_weight > node[x].way_weight:

                temp = node[i].way_weight
                node[i].way_weight = node[x].way_weight
                node[x].way_weight = temp

                temp = node[i].first_node
                node[i].first_node = node[x].first_node
                node[x].first_node = temp

                temp = node[i].second_node
                node[i].second_node = node[x].second_node
                node[x].second_node = temp
    return node

def get_parent(list_set, x):
    if list_set[x] == x:
        return x
    list_set[x] = get_parent( list_set, list_set[x] )
    return list_set[x]

def union_parent(list_set, a, b):
    a = get_parent(list_set, a)
    b = get_parent(list_set, b)

    if a < b:
        list_set[b] = a
    else:
        list_set[a] = b

    return list_set

def find(list_set, a, b):
    a = get_parent(list_set, a)
    b = get_parent(list_set, b)

    if a == b:
        return True
    else:
        return False


def cruscal_algorithm(node, number_of_node):

    node = sort_node_edge( node )

    list_set = []
    list_set_count = []

    for i in range(0, number_of_node):
        list_set.append( i )
        list_set_count.append(0)
    sum = 0
    for i in range(0, len( node) ):
        if find( list_set, node[i].first_node - 1, node[i].second_node -1 ) == False and list_set_count[ node[i].first_node - 1 ] < 2 and list_set_count[ node[i].second_node - 1 ] < 2:
            print( "연결된 노드 : " + str(node[i].first_node) + " and " + str(node[i].second_node) + "\nedge_weight = " + str(node[i].way_weight) + "\n" )
            list_set_count[ node[i].first_node - 1  ] += 1
            list_set_count[ node[i].second_node - 1 ] += 1
            sum += node[i].way_weight
            union_parent( list_set, node[i].first_node - 1, node[i].second_node - 1 )
        else:
            print( "연결x 노드 : " + str(node[i].first_node) + " and " + str(node[i].second_node) + "\nedge_weight = " + str(node[i].way_weight) + "\n" )
    print(sum)

if __name__ == "__main__":

    #case_1
    node = []
    node.append( Node_data_set(1, 2, 16) )
    node.append( Node_data_set(1, 4, 7 ) )
    node.append( Node_data_set(2, 4, 12) )
    node.append( Node_data_set(2, 6, 15) )
    node.append( Node_data_set(3, 5, 40) )
    node.append( Node_data_set(4, 6, 25) )
    node.append( Node_data_set(1, 3, 9 ) )
    node.append( Node_data_set(1, 5, 50) )
    node.append( Node_data_set(2, 5, 25) )
    node.append( Node_data_set(3, 4, 12) )
    node.append( Node_data_set(3, 6, 32) )
    node.append( Node_data_set(5, 6, 9 ) )

    cruscal_algorithm(node, 6)

    #case_2
    node_data_list  = [ [1, 7, 12], [1, 4, 28], [1, 2, 67], [1, 5, 17], [2, 4, 24], [2, 5, 62], [3, 5, 20], [3, 6, 37], [4, 7, 13], [5, 6, 45], [5, 7, 73] ]

    new_node = []
    for i in range(0, len( node_data_list ) ):
        new_node.append( Node_data_set(node_data_list[i][FIRST_NODE], node_data_list[i][SECOND_NODE], node_data_list[i][EDGE] ) )

    cruscal_algorithm(new_node, 7)

    #case_3
    node_data_list = [ [1, 2, 9], [1, 3, 23], [1, 4, 5], [1, 5, 35],
                       [2, 4, 14], [2, 5, 17],
                       [3, 4, 10], [3, 6, 23], [3, 7, 53],
                       [4, 5, 20], [4, 6, 19],
                       [5, 6, 47], [5, 7, 32],
                       [6, 7, 37] ]
    new_node1 = []
    for i in range(0, len( node_data_list ) ):
        new_node1.append( Node_data_set(node_data_list[i][FIRST_NODE], node_data_list[i][SECOND_NODE], node_data_list[i][EDGE] ) )

    cruscal_algorithm(new_node1, 7)

    #case_4

    node_data_list = [ [1, 2, 1], [1, 5, 3],
                       [2, 3, 6], [2, 4, 2],
                       [3, 5, 4],
                       [4, 5, 5] ]
    new_node1 = []
    for i in range(0, len(node_data_list)):
        new_node1.append(
            Node_data_set(node_data_list[i][FIRST_NODE], node_data_list[i][SECOND_NODE], node_data_list[i][EDGE]))

    cruscal_algorithm(new_node1, 5)

    #case_5

    node_data_list = [ [1, 2, 5], [1, 4, 3], [1, 5, 4],
                       [2, 4, 3], [2, 8, 2],
                       [3, 4, 3], [3, 7, 4],
                       [4, 5, 3], [4, 6, 3],
                       [5, 6, 2],
                       [6, 7, 6],
                       [7, 8, 3] ]
    new_node1 = []
    for i in range(0, len(node_data_list)):
        new_node1.append(
            Node_data_set(node_data_list[i][FIRST_NODE], node_data_list[i][SECOND_NODE], node_data_list[i][EDGE]))

    cruscal_algorithm(new_node1, 8)
