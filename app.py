import streamlit as st
import requests

# 1. 친구에게 받은 진짜 키를 여기에 넣으세요
API_KEY = "AIzaSyCVQU8SFRDux6mDXuzE4_Bnb1D4WnPEo7w"

# 리스트에서 확인된 최신 모델인 gemini-2.5-flash를 사용합니다.
# 2026년 표준 주소 방식입니다.
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

st.set_page_config(page_title="사회성 이야기 생성기", page_icon="🌟")
st.title("🌟 우리 아이 맞춤형 AI 이야기")
st.write("아이의 상황을 입력하면 최신 AI가 다정한 이야기를 들려줍니다.")

situation = st.text_input("상황 입력", placeholder="예: 친구와 장난감을 나눠 쓰기 싫어해요")

if st.button("AI 이야기 만들기"):
    if not situation:
        st.warning("상황을 먼저 입력해주세요.")
    else:
        with st.spinner('최신 Gemini 2.5 모델이 답변을 생성 중...'):
            try:
                # 구글 API 표준 데이터 구조
                payload = {
                    "contents": [{
                        "parts": [{"text": f"너는 다정한 언어치료사야. 5세 아이를 위해 '{situation}' 상황에 대한 따뜻한 이야기 3줄을 지어줘."}]
                    }]
                }
                headers = {'Content-Type': 'application/json'}
                
                response = requests.post(URL, json=payload, headers=headers)
                result = response.json()
                
                # 드디어 성공하는 순간!
                if 'candidates' in result:
                    answer = result['candidates'][0]['content']['parts'][0]['text']
                    st.success("AI 답변 생성 성공!")
                    st.info(answer)
                else:
                    st.error("모델은 찾았으나 다른 오류가 발생했습니다.")
                    st.json(result)
                    
            except Exception as e:
                st.error(f"연결 오류: {e}")

st.caption("© 2026 언어치료 AI - Gemini 2.5 Flash Engine")
