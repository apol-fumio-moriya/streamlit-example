import streamlit as st
from st_btn_select import st_btn_select

st.set_page_config(
    page_title="ilodoli タイプ判断", page_icon="📊", initial_sidebar_state="expanded"
)

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://cdn.pixabay.com/photo/2020/06/19/22/33/wormhole-5319067_960_720.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

def page1():
    set_bg_hack_url()
    st.write(
        """
    # ilodoli タイプ診断
    ilodoli にてあなたのタイプを診断してみませんか。
    """
    )

    st.text("自分の考えに夢中になって、周囲のことを無視したり忘れることがよくある。")
    
    page = st_btn_select(
        ('はい', 'いいえ'),
        nav=True,
        format_func=lambda x: x.capitalize(),
        )
    
    if page == 'はい':
        st.session_state["page-select"] = "page2"
    elif page == 'いいえ':
        st.session_state["page-select"] = "page3"
        
def page2():
    set_bg_hack_url()
    st.write(
        """
    # ilodoli タイプ診断
    ilodoli にてあなたのタイプを診断してみませんか。
    """
    )

    st.text("受信箱がごちゃごちゃするのが我慢できず、できるだけ早くEメールに返答しようとする。")
    option = st_btn_select(        
        ('はい', 'いいえ'),
        nav=True,
        format_func=lambda x: x.capitalize(),)
    if option == 'はい':
        st.session_state["page-select"] = "page4"
    elif option == 'いいえ':
        st.session_state["page-select"] = "page1"
                                              
def page3():
    set_bg_hack_url()
    st.write(
        """
    # ilodoli タイプ診断
    ilodoli にてあなたのタイプを診断してみませんか。
    """
    )

    st.text("プレッシャーがあるときでも常にリラックスし、集中できる。")
    option = st_btn_select(        
        ('はい', 'いいえ'),
        nav=True,
        format_func=lambda x: x.capitalize(),)
    if option == 'はい':
        st.session_state["page-select"] = "page4"
    elif option == 'いいえ':
        st.session_state["page-select"] = "page1"
                                              
def page4():
    def change_page():
        st.session_state["page-select"] = "page1"

    with st.form(key='my_result'):
        st.subheader("あなたの ilodoli タイプは建築家です。")
        st.image("https://kuku-keke.com/wp-content/uploads/2021/01/4537_6.png")
        st.text("この上なく孤独、そして最も希少で戦略に長けている性格タイプ。")

        submit_button = st.form_submit_button(label="確認", on_click=change_page)


pages = dict(
    page1="タイプ診断 1",
    page2="タイプ診断 2",
    page3="タイプ診断 3",
    page4="診断結果",
)

page_id = st.sidebar.selectbox(
    "ページ名",
    ["page1", "page2", "page3", "page4"],
    format_func=lambda page_id: pages[page_id],
    key="page-select",
)

if page_id == "page1":
    page1()

if page_id == "page2":
    page2()
    
if page_id == "page3":
    page3()

if page_id == "page4":
    page4()

