import time
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import pandas as pd
from algoritmos import bubble_sort, selection_sort, insertion_sort, merge_sort_gen

st.set_page_config(page_title="Ordenação Visual", layout="centered")

st.markdown("<h2 style='text-align:center'>Crie seu próprio vetor de ordenação desenhando barras verticais</h2>", unsafe_allow_html=True)

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

btn_extract = st.button("Extrair barras")
start = st.button("Iniciar Ordenação")

def extract_heights(canvas):
    if not canvas or not canvas.json_data:
        return []
    objs = canvas.json_data.get("objects", [])
    rects = [o for o in objs if o.get("type") == "rect" or ("width" in o and "height" in o)]
    rects_sorted = sorted(rects, key=lambda o: o.get("left", 0))
    heights = [int(round(o.get("height", 0))) for o in rects_sorted]
    return heights

def draw_bars(arr, placeholder):
    if not arr:
        placeholder.info("Sem barras para mostrar. Desenhe retângulos e clique em 'Extrair barras'.")
        return
    df = pd.DataFrame({"val": arr})
    placeholder.bar_chart(df)

if btn_extract:
    heights = extract_heights(canvas_result)
    if not heights:
        st.warning("Nenhuma barra detectada. Desenhe retângulos verticais no canvas.")
    else:
        st.success(f"{len(heights)} barras extraídas")
        draw_bars(heights, area_ordenacao)
        

if start:
    heights = extract_heights(canvas_result)
    if not heights:
        st.warning("Nenhuma barra detectada para ordenar.")
    else:
        arr = heights.copy()
        if algoritmos == "Bubble Sort":
            gen = bubble_sort(arr)
        elif algoritmos == "Selection Sort":
            gen = selection_sort(arr)
        elif algoritmos == "Insertion Sort":
            gen = insertion_sort(arr)
        else:
            gen = merge_sort_gen(arr)

        for state in gen:
            draw_bars(state, area_ordenacao)
            time.sleep(Speed)
        st.success("Ordenação finalizada")

