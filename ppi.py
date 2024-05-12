import streamlit as st
import requests
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#retrieve the ppi
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
    st.set_option('deprecation.showPyplotGlobalUse', False)
    df = retrieve_ppi(protein_name)
    ppi_graph = nx.from_pandas_edgelist(df, "preferredName_A", "preferredName_B")
    graph = nx.spring_layout(ppi_graph)
    #nx.draw(ppi_graph, graph, with_labels = True, node_size = 500, node_color = 'lightgreen', edge_color = 'green', font_size = 8)
    plt.figure(figsize=(8, 6))
    nx.draw(ppi_graph, graph, with_labels=True, node_size=500, node_color='lightgreen', edge_color='green', font_size=8)
    plt.title("Protein-Protein Interaction Graph")
    plt.axis('off')  # Turn off axis
    st.pyplot()  # Display the graph in Streamlit
    get_charactesristics(ppi_graph)
    
    
def get_charactesristics(ppi_graph):
    st.write("Number of edges: ", ppi_graph.number_of_edges())
    st.write("Number of nodes: ", ppi_graph.number_of_nodes())
    st.write("Number of interactions: ", ppi_graph.degree())
    degree_central = nx.degree_centrality(ppi_graph)
    st.write("Degree distribution: ", degree_central)
    top_5_protein = sorted(degree_central.items(), key = lambda x:-x[1])[:5]
    st.write("Top 5 proteins by degree centrality: ", top_5_protein)