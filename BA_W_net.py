import random
import networkx as nx
import matplotlib.pyplot as plt


def ba_bip_graph(n):
    g = nx.DiGraph()
    f = open("start.txt")
    line = f.readline()
    repeated_user_nodes = []
    repeated_item_nodes = []
    while line:
        repeated_user_nodes.append(line.strip('\n').split(" ")[0])
        repeated_item_nodes.append(line.strip('\n').split(" ")[1])
        line = f.readline()
    users = 5
    user_line = 0
    item_line = 0
    while users < n:
        m1 = random.randint(1, 10)                                   #新增一个user，添加随机0-9个边
        # print("m1:", m1)
        item_target = set()
        while len(item_target) < m1:
            x = random.choice(repeated_item_nodes)
            item_target.add(x)
        label = []
        f = open("user_name.txt")
        line = f.readline()
        while line:
            label.append(line.strip('\n').split(" ")[0])
            line = f.readline()
        # print([label[user_line]] * m1)
        # print(item_target)
        r = zip([label[user_line]]*m1, item_target)
        for each in r:
            w = random.randint(1, 10)
            # g.add_edge(each[0], each[1], time=w)
            g.add_weighted_edges_from([(each[0], each[1], w)])
        repeated_item_nodes.extend(item_target)
        repeated_user_nodes.extend([label[user_line]]*m1)
        user_line += 1
        f.close()
        #新增一个user，新增4个item
        repeat = 0
        while repeat < 4:
            m2 = random.randint(1, 5)
            # print("m2:", m2)
            user_target = set()
            while len(user_target) < m2:
                x = random.choice(repeated_user_nodes)
                user_target.add(x)
            label = []
            f_item = open("item_name.txt")
            line = f_item.readline()
            while line:
                label.append(line.strip('\n').split(" ")[0])
                line = f_item.readline()
            r = zip(user_target, [label[item_line]]*m2)
            for each in r:
                w = random.randint(1, 10)
                # g.add_edge(each[0], each[1], time=w)
                g.add_weighted_edges_from([(each[0], each[1], w)])
            # g.add_edges_from(zip([label[item_line]]*m2, user_target))
            repeated_user_nodes.extend(user_target)
            repeated_item_nodes.extend([label[item_line]] * m2)
            item_line += 1
            f.close()
            repeat += 1
        users = users+1
    return g


BA = ba_bip_graph(20)
pos = nx.circular_layout(BA)
nx.draw(BA, pos, with_labels=True, node_size=20, rotate=True)
plt.show()
f = open('dataset.txt', 'a')
f.write('user item time\n')
for edge in BA.edges(data=True):
    # print(edge)
    for key, value in BA.get_edge_data(edge[0], edge[1]).items():
        f.write(edge[0]+' '+edge[1]+' '+str(value)+'\n')
f.close()
