import time
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import pandas as pd
from algoritmos import bubble_sort, selection_sort, insertion_sort, merge_sort_gen

st.set_page_config(page_title="Ordenação Visual", layout="centered")

st.markdown("<h2 style='text-align:center'>Desenhe barras verticais (retângulos)</h2>", unsafe_allow_html=True)

st.info("Desenhe retângulos verticais no canvas. Depois clique em 'Extrair barras'.")

canvas_result = st_canvas(
    stroke_width=2,
    stroke_color="#000000",
    background_color="#FFFFFF",
    height=400,
    width=800,
    drawing_mode="rect",
    key="canvas",
)

st.write("")
area_ordenacao = st.empty()

algoritmos = st.selectbox("Algoritmo", ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort"])    

