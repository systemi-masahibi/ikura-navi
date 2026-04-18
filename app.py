import math
import streamlit as st

st.set_page_config(
    page_title="いくらナビ",
    page_icon="🍺",
    layout="centered",
)

st.title("🍺 いくらナビ")
st.caption("飲み会・食事の割り勘計算アプリ")

st.header("入力")

unit_price = st.number_input(
    "コース単価（円/人）",
    min_value=0,
    value=0,
    step=100,
)
people = st.number_input(
    "人数（人）",
    min_value=1,
    value=1,
    step=1,
)
kanpa = st.number_input(
    "カンパ金（円）※任意",
    min_value=0,
    value=0,
    step=500,
)

total = int(unit_price) * int(people)
remaining = total - int(kanpa)
per_person = math.ceil(remaining / int(people))

st.divider()
st.header("計算結果")

col1, col2, col3 = st.columns(3)
col1.metric("合計金額", f"¥{total:,}")
col2.metric("カンパ後の残り", f"¥{remaining:,}")
col3.metric("一人あたり", f"¥{per_person:,}")
