import streamlit as st

st.set_page_config(
    page_title="ilodoli タイプ判断", page_icon="📊", initial_sidebar_state="expanded"
)

st.write(
    """
# ilodoli タイプ診断
ilodoli にてあなたのタイプを診断してみませんか。
"""
)

with st.form(key='my_form'):
    decide1 = st.radio(
        f"自分の考えに夢中になって、周囲のことを無視したり忘れることがよくある。",
        options=["Yes", "No"],
        )
    decide2 = st.radio(
        f"受信箱がごちゃごちゃするのが我慢できず、できるだけ早くEメールに返答しようとする。",
        options=["Yes", "No"],
        )
    decide3 = st.radio(
        f"プレッシャーがあるときでも常にリラックスし、集中できる。",
        options=["Yes", "No"],
        )
    decide4 = st.radio(
        f"通常、自分から話を始めることはない。",
        options=["Yes", "No"],
        )
    submit_button = st.form_submit_button(label="次へ")
