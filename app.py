import book_recommendation.book_recommendation as br
import book_recommendation.graph_util
import streamlit as st
import pandas as pd


# read amazon-meta
with open('amazon-meta.txt', 'r', encoding="utf8", errors='ignore') as f:
    lines = f.readlines()


st.set_page_config(page_title="Book Recommendation", layout="wide")

_, center, _ = st.columns([1,3,1])

center.title("Sistema de Recomendação Baseado em Grafos")

st.sidebar.title("Book Recommendation ✨")

sample_qtd = st.sidebar.slider('Quantidade de dados para busca', 100, 1000, 100, 100)

dataset = br.get_sample_dataset(lines, sample_qtd)
dataset = ["".join(item) for item in dataset]

products_filtered = list(filter(None, [br.get_amazon_metadata(i) for i in dataset]))

book_names = [product[4] for product in products_filtered]

recommend_type = st.sidebar.radio(
        "Escolha como deseja receber a recomendação!",
        options=["Maior número de compras", "Melhor avaliação"]
        )

buff, col, buff2 = st.columns([1,3,1])

book_search = col.selectbox(
    'Escolha o nome de um livro',
    (book_names))

all_vertex_list, books, customers = br.get_vertex_list(products_filtered)
connected_components_g = br.get_components(all_vertex_list, products_filtered)

results_qtd_customers, results_rating_mean = br.get_all_books(book_search, products_filtered,
                                                           all_vertex_list, books, connected_components_g)

if len(results_qtd_customers) > 1:
    results_qtd = st.sidebar.slider('Quantidade de recomendações', 1, len(results_qtd_customers), 1, 1)
else:
    results_qtd = 1


st.subheader(f"Quem comprou o livro escolhido, também comprou:")
if recommend_type == "Maior número de compras":
    st.table(pd.DataFrame(results_qtd_customers[:results_qtd]))
else:
    st.table(pd.DataFrame(results_rating_mean[:results_qtd]))

