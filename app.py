import streamlit as st
import requests

# 1. 친구에게 받은 키를 여기에 넣으세요
API_KEY = "AIzaSyCVQU8SFRDux6mDXuzE4_Bnb1D4WnPEo7w"

# v1 주소와 가장 최신 안정화 모델인 gemini-1.5-flash 조합입니다.
URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"

st.set_page_config(page_title="사회성 이야기 생성기", page_icon="🌟")
st.title("🌟 우리 아이 맞춤형 AI 이야기")

situation = st.text_input("상황 입력", placeholder="예: 친구와 장난감을 나눠 쓰기 싫어해요")

if st.button("AI 이야기 만들기"):
    if not situation:
        st.warning("상황을 먼저 입력해주세요.")
    else:
        with st.spinner('AI 선생님이 대답을 생각하고 있어요...'):
            try:
                # 가장 원초적이고 에러 없는 데이터 구조
                payload = {
                    "contents": [{
                        "parts": [{"text": f"5세 아이를 위한 사회성 이야기 3줄: {situation}"}]
                    }]
                }
                headers = {'Content-Type': 'application/json'}
                
                response = requests.post(URL, json=payload, headers=headers)
                result = response.json()
                
                # 성공 시
                if 'candidates' in result:
                    answer = result['candidates'][0]['content']['parts'][0]['text']
                    st.success("AI 선생님의 이야기:")
                    st.info(answer)
                # 실패 시 (여전히 404가 뜨면 아래를 보세요)
                else:
                    st.error("구글 서버와 연결이 불안정합니다.")
                    st.json(result)
                    
            except Exception as e:
                st.error(f"오류: {e}")

st.caption("© 2026 언어치료 AI - 최적화 모드")
