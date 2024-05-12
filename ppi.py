import requests
import pandas as pd
import networkx as nx

def retrieve_ppi(protein_name):
    string_url = "https://string-db.org/api/json/network"
    params = {
        "identifiers": protein_name,
        "species": 9606 #homo sapiens
    }
    response = requests.get(string_url, params = params)
    data = response.json() #parse to json

    network_df = pd.json_normalize(data)

    return network_df

def visualize_ppi(protein_name):
    df = retrieve_ppi(protein_name)
    ppi_graph = nx.from_pandas_edgelist(df, "preferredName_A", "preferredName_B")
    get_charactesristics(ppi_graph)
    graph = nx.spring_layout(ppi_graph)
    nx.draw(ppi_graph, graph, with_labels = True, node_size = 500, node_color = 'lightgreen', edge_color = 'green', font_size = 8)

def get_charactesristics(ppi_graph):
    print("Number of edges: ", ppi_graph.number_of_edges())
    print("Number of nodes: ", ppi_graph.number_of_nodes())
    print("Number of interactions: ", ppi_graph.degree())
    degree_central = nx.degree_centrality(ppi_graph)
    print("Degree distribution: ", degree_central)
    top_5_protein = sorted(degree_central.items(), key = lambda x:-x[1])[:5]
    print("Top 5 proteins by degree centrality: ", top_5_protein)