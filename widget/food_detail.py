import streamlit as st

def get_food_detail():
    st.header(st.session_state['detail'])
    # 맛집 상세보기
    # st.image("https://cdn.pixabay.com/photo/2018/05/17/16/03/compass-3408928_1280.jpg")
    st.video(st.session_state['map'])
    # link = "https://naver.com"
    link = st.session_state['link']
    st.write(f"[**🔗 스팀 상점 페이지**]({link})")