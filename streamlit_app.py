import streamlit as st
import streamlit.components.v1 as stc
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
    stc.html("""
                <div class="dot"></div>
                <div class="-\33 94"></div>
                <div class="-\34 12"></div>
                <div class="-\33 90"></div>
                <div class="-\33 96"></div>
                <div class="-\33 98"></div>
                <div class="-\33 91"></div>
                <div class="-\34 11"></div>
                <div class="-\33 95"></div>
                <div class="-\33 92"></div>
                <div class="-\34 10"></div>
                <div class="-\33 93"></div>
                <div class="-\33 99"></div>
                <div class="-\33 97"></div>
                <span class="\-">
  エンゲージメント解析サービス
イロドリ
</span>
                <div class="ilodloli_logo_220708_fix"></div>
                <span class="\-">
  あなたの
“働くマインド”は何タイプ？
</span>
                <div class="-\36 63"></div>
                <span>
  診断スタート
</span>
                <span class="Powerd-by">
  Powerd by
</span>
                <div class="Rectangle-25"></div>
                <span class="APOLLO-Inc">
  ©APOLLO, Inc.
</span>
             """
            )
        
def page2():
    st.write(
        """
    # ilodoli タイプ診断
    ilodoli にてあなたのタイプを診断してみませんか。
    """
    )

    def change_page_yes():
        st.session_state["page-select"] = "page3"
    def change_page_no():
        st.session_state["page-select"] = "page1"

    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://www2.kek.jp/ilc/wp-content/uploads/2018/10/michinokaimei_img1.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

    with st.form(key="name-form"):
        st.text("受信箱がごちゃごちゃするのが我慢できず、できるだけ早くEメールに返答しようとする。")
        col1, col2 = st.columns(2)
        col1.form_submit_button(label="はい", on_click=change_page_yes)
        col2.form_submit_button(label="いいえ", on_click=change_page_no)
                                              
def page3():
    st.write(
        """
    # ilodoli タイプ診断
    ilodoli にてあなたのタイプを診断してみませんか。
    """
    )

    def change_page_yes():
        st.session_state["page-select"] = "page4"
    def change_page_no():
        st.session_state["page-select"] = "page2"

    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://www2.kek.jp/ilc/wp-content/uploads/2018/10/michinokaimei_img3.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

    with st.form(key="name-form"):
        st.text("プレッシャーがあるときでも常にリラックスし、集中できる。")
        col1, col2 = st.columns(2)
        col1.form_submit_button(label="はい", on_click=change_page_yes)
        col2.form_submit_button(label="いいえ", on_click=change_page_no)
                                              
def page4():
    def change_page():
        st.session_state["page-select"] = "page1"

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("https://assets.media-platform.com/lifehacker/dist/images/2021/03/16/210317brain_top-w1280.jpg");
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
     )

    with st.form(key='my_result'):
        
        with open('style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
        st.subheader("あなたの ilodoli タイプは建築家です。")
        #st.image("https://kuku-keke.com/wp-content/uploads/2021/01/4537_6.png")
        st.text("この上なく孤独、そして最も希少で戦略に長けている性格タイプ。")

        col1, col2, col3 = st.columns(3)
        col1.metric("知力", "120", "12%")
        col2.metric("体力", "90", "-8%")
        col3.metric("気力", "140", "4%")        
        
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

