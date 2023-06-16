# app.py, main.py, streamlit_app.py, home.py ...
# 리팩토링 -> 코드를 깔끔하고 간명하게 만드는 작업...

# streamlit
import streamlit as st # streamlit 기능묶음(패키지) -> import 불러오고, as ~한 변수명으로 쓰겠다.
# 짧은 별칭(별명) -> 길다보니까 사용성이 낮아져서...
from widget.food_list import get_food_list
from widget.food_detail import get_food_detail

st.title("스팀 게임 추천")
# streamlit run app.py
# -> 프로젝트 생성 -> 가상환경 (파이썬 관련 설치를 매번 독립적)
# 새로운 프로젝트를 만들면 -> 새롭게 설치
# pip install streamlit

# https://crop-circle.imageonline.co/
# store1 = {
#     "name": "모스키친",
#     "img": "img/s1.png",
#     "star": 5,
#     "desc": "**모스키친**은 신대방삼거리역에 위치한 돈까스 전문점입니다. 이곳의 돈까스는 프리미엄 등심돈까스와 스페셜 등심돈까스 등으로 구성되어 있으며, 특히 스페셜 등심돈까스는 가브리살이 포함되어 더욱 쫄깃한 식감을 제공합니다. 이들 메뉴는 품질에 비해 가격이 매우 합리적이며, 맛있는 음식과 함께 접객이 빠른 서비스로 많은 손님들에게 인기가 있습니다. 최고의 맛을 위해 히말라야 소금에 콕 찍어 와사비를 얹어 먹는 것을 추천합니다."
# }
def make_store(name, img, star, desc, map, link):
    return dict(name=name, img=img, star=star, desc=desc, map=map, link=link)
store1 = make_store(
    "몬스터 헌터 월드", "img/s1.png", 5,
    "**몬스터 헌터 월드**는 capcom에서 2018년에 출시한 헌팅 액션 게임으로,"\
    "뛰어난 그래픽과 화려한 액션으로 큰 인기를 끌었습니다.."\
    "특히, 살아 숨쉬는 다양한 생태계와 다양한 장비를 통한 커스터마이징과 사냥의 재미가 뛰어납니다.",
    "https://youtu.be/fsoxwI4Etbw",
    "https://store.steampowered.com/app/582010/Monster_Hunter_World/",
)
store2 = make_store(
    "어쌔신 크리드 오디세이", "img/s2.png", 4,
    "**어쌔신 크리드 오디세이**는 ubisoft에서 2018년에 출시한 오픈월드 액션 게임으로,"\
    "펠로폰네소스 전쟁 시기의 고대 그리스 시대의 한 용병이 되어 넓은 세계를 탐험하고, 다양한 이야기의 주인공이 되어가는 게임입니다.\
    '고대 그리스를 그대로 옮겨 놓은듯한 풍경과 플레이어가 선택할 수 있는 3가지 전투 시스템을 통한 액션이 큰 매력인 작품입니다.'",
    "https://youtu.be/dJNs91zv_Dk",
    "https://store.steampowered.com/app/812140/Assassins_Creed_Odyssey/",
)
store3 = make_store(
    "다크 소울 3", "img/s3.png", 3,
    "**다크소울 3**는 fromsoftware에서 2016년에 출시한 소울라이크 rpg 게임으로,"\
    "멸망을 앞두고 있는 어두운 세계에서 마지막 사명을 부여받은 주인공이 되어 역경을 헤쳐나가는 내용입니다."\
    "이 무너져가는 세계는 유저들에게 한시도 방심할 수 없는 긴장감을 제공하며"\
    "강대한 보스들과 어둡지만 인상적인 디자인, 개성있는 등장인물들의 조화로 이 세계에 빠져들게 만드는 게임입니다.",
    "https://youtu.be/doFPq8n1qGY",
    "https://store.steampowered.com/app/374320/DARK_SOULS_III/?l=koreana",
)

stores = [store1, store2, store3]

# 일종의 딕셔너리 (페이지가 모두 공유하는 딕셔너리)
if 'detail' not in st.session_state:  # key를 확인해서
    st.session_state['detail'] = ""  # 초기값
    st.session_state['map'] = ""  # 초기값
    st.session_state['link'] = ""  # 초기값

# 맛집 리스트
get_food_list(stores)

# 맛집 상세보기
if st.session_state['detail']:  # 초기값의 빈 문자열
    get_food_detail()  # 처음에는 실행하지 않고... 클릭했을 때 반응해서 그려지게