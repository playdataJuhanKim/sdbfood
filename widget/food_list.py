import streamlit as st

def set_detail(name):
    st.session_state['detail'] = name

def get_food_list(stores):
    # 가게 리스트
    # 4개 열 -> 4개 열마다 사진, 가게명, 간단한 설명.
    # for col in st.columns(4):
    for idx, col in enumerate(st.columns(len(stores))):
        # st.columns(4) -> 4개의 열이 묶인 리스트
        # 해당 열들을 순서대로 col이라는 변수로 사용
        # ...
        store = stores[idx]  # <- 외부에서 데이터를 받아서...
        # col.header("맛집이름")
        # col.header(store["name"])
        col.markdown(f"""<h2 style="height:110px;">{store['name']}</h2>""", unsafe_allow_html=True)
        # col.image("https://cdn.pixabay.com/photo/2017/02/10/08/38/pasta-2054656_640.jpg")
        col.image(store["img"])
        # star_count = 5
        star_count = store["star"]
        col.write("".join(["⭐"] * star_count))
        # col.write("설명 설명...")
        col.write(store['desc'])
        # There are multiple identical st.button widgets with the same generated key.
        # st.button -> bool => 눌리면 해당 button => True
        if col.button("자세히보기", key=f"button{idx}", use_container_width=True):
            # 눌렀을 때 실행되는 코드...
            # col.write(store["name"])
            st.session_state['detail'] = store["name"]
            st.session_state['map'] = store["map"]
            st.session_state['link'] = store["link"]
        # 버튼마다 다른 key가 있어야함.