import streamlit as st
import requests

# 1. '새 프로젝트'에서 만든 키를 여기에 넣으세요!
API_KEY = "AIzaSyDyZbzfvP_UaUSuRAb4SJw9W-Pa50SjEes"

# 주소 형식을 v1beta가 아닌 v1으로, 모델명을 가장 확실한 것으로 고정합니다.
URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"

st.set_page_config(page_title="사회성 이야기 생성기", page_icon="🌟")
st.title("🌟 우리 아이 맞춤형 AI 이야기")

situation = st.text_input("상황 입력", placeholder="예: 친구와 싸웠어요")

if st.button("AI 이야기 만들기"):
    if not situation:
        st.warning("상황을 입력해주세요.")
    else:
        with st.spinner('AI가 답변을 생성 중입니다...'):
            try:
                # 가장 표준적인 페이로드 구조
                payload = {
                    "contents": [{"parts": [{"text": f"5세 아이를 위한 사회성 이야기 3줄: {situation}"}]}]
                }
                
                res = requests.post(URL, json=payload)
                data = res.json()
                
                if 'candidates' in data:
                    st.success("AI 답변 성공!")
                    st.write(data['candidates'][0]['content']['parts'][0]['text'])
                else:
                    st.error("이번에도 에러가 발생했습니다. 아래 내용을 캡처해서 알려주세요.")
                    st.json(data)
            except Exception as e:
                st.error(f"오류 발생: {e}")
