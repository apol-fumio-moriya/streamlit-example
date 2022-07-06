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
        horizontal=True,
        )
    decide2 = st.radio(
        f"受信箱がごちゃごちゃするのが我慢できず、できるだけ早くEメールに返答しようとする。",
        options=["Yes", "No"],
        horizontal=True,
        )
    decide3 = st.radio(
        f"プレッシャーがあるときでも常にリラックスし、集中できる。",
        options=["Yes", "No"],
        horizontal=True,
        )
    
    st.text("通常、自分から話を始めることはない。")
    temp_options = ['はい', 'どちらでもない','いいえ']
    temp = st.select_slider("", options=temp_options)

    submit_button = st.form_submit_button(label="次へ")
    
with st.form(key='my_result'):
    st.subheader("あなたの ilodoli タイプは建築家です。")
    st.image("https://kuku-keke.com/wp-content/uploads/2021/01/4537_6.png")
    st.text("この上なく孤独、そして最も希少で戦略に長けている性格タイプ。")
    
    submit_button = st.form_submit_button(label="OK")
