from pyvis.network import Network
import graph_util
import book_recommendation as br
import pandas as pd
import numpy as np
import re


# seleciona uma quantia de dados dentro do dataset
def get_sample_dataset(raw_data, len_sample, data_name="amazon-meta"):
    count = 1
    left_text = 0
    dataset = []
    
    if data_name=="amazon-meta":
        amazon_data = raw_data[3:]
        
        for i, line in enumerate(amazon_data):
            if line == '\n':
                dataset.append(amazon_data[left_text:i])
                left_text = i
                
                if count==len_sample:
                    return dataset
                count+=1

# separa itens desejados
def get_amazon_metadata(dataset):
    
    discontinued_product = re.findall(r"discontinued product", dataset)
    id_product = re.findall(r"Id:.*?\n", dataset)
    asin_product = re.findall(r"ASIN:.*?\n", dataset)
    cutomer_product = re.findall(r"cutomer:.*?\w+", dataset)
    
    if not asin_product or discontinued_product or not cutomer_product:
        return None
    
    rate_cutomer = re.findall(r"rating:\s(\d+)", dataset)
    similar_asin_products = re.findall(r"similar:.*?\n", dataset)
    category_product = re.findall(r"group:.*?\n", dataset)
    
    if not category_product[0].endswith('Book\n'):
        return None
    
    title_product = re.findall(r"title:(.*?)\n", dataset)

    ids = list(filter(None, id_product[0].split(" ")))[1].replace('\n', '')
    source = [i.split(' ')[-1] for i in cutomer_product]
    target = list(len(source) * (asin_product[0].split(" ")[1].replace('\n', ''),))
    weight = rate_cutomer[1:]
    name = title_product[0].strip()

    return ids, source, target, weight, name

# gera o grafo de forma visual
def create_visual_network(customer, book, stars):
    got_net = Network(notebook=True)

    got_net.barnes_hut()

    edge_data = zip(customer, book, stars)

    for e in edge_data:
        src = e[0]
        dst = e[1]
        w = e[2]

        got_net.add_node(src, src, title=src)
        got_net.add_node(dst, dst, title=dst)
        got_net.add_edge(src, dst, value=w)

    neighbor_map = got_net.get_adj_list()

    for node in got_net.nodes:
                    node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
                    node["value"] = len(neighbor_map[node["id"]])

    return got_net.show("books.html")

# 
def get_vertex_list(products_filtered):
    all_vertex_list = []
    customers = []
    books = []

    for product in products_filtered:
        for customer_item in product[1]:
            all_vertex_list.append(customer_item)
            customers.append(customer_item)
        books.append(product[2][0])
        all_vertex_list.append(product[2][0])
    return all_vertex_list, books, customers

def get_components(all_vertex_list, products_filtered):

    g = graph_util.Graph(len(all_vertex_list))

    # add edge
    for product in products_filtered:
        for i in range(len(product[1])):
            g.add_edge(all_vertex_list.index(product[2][0]), all_vertex_list.index(product[1][i]))
    
    return g.connected_components()

def get_all_books(book_search, products_filtered, all_vertex_list, books, connected_components_g):
        
    results = {}
    all_results = []
    
    for product in products_filtered:
        if book_search == product[4]:
            book_search_idx = all_vertex_list.index(product[2][0])
            for conected_vertex in connected_components_g:
                if book_search_idx in conected_vertex:
                    conections_items = [all_vertex_list[i] for i in conected_vertex]
                    
    books = np.array(books)
    mask = np.isin(books, np.array(conections_items))
    all_books = books[mask].tolist()

    for product in products_filtered:
        for book_s in all_books:
            if book_s == product[2][0]:
                int_rating = [int(i) for i in product[3]]
                book_name = product[4]
                results['book_name'] = book_name
                results['rating_mean'] = round(np.mean(int_rating), 2)
                results['book_id'] = book_s
                results['qtd_customers'] = len(product[1])
                all_results.append(results)
                results = {}
    
    results_qtd_customers = sorted(all_results, key=lambda x: x['qtd_customers'], reverse=True)
    results_rating_mean = sorted(all_results, key=lambda x: x['rating_mean'], reverse=True)
    
    return results_qtd_customers, results_rating_mean
