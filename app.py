import streamlit as st
import requests

# 1. API 설정 (학생님의 진짜 키를 따옴표 안에 넣어주세요!)
API_KEY = "AIzaSyAS7Ezm0cTnR0_KDle6ERumw0ESYQKv1g0"

# 가장 호환성이 높은 gemini-pro 모델 경로로 설정했습니다.
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

st.set_page_config(page_title="사회성 이야기 생성기", page_icon="🌟")
st.title("🌟 우리 아이 맞춤형 AI 이야기")
st.write("아이의 상황에 맞춰 AI가 다정한 이야기를 들려줍니다.")

situation = st.text_input("상황을 입력하세요", placeholder="예: 친구와 장난감을 나눠 쓰기 싫어해요")

if st.button("AI 이야기 만들기"):
    if not situation:
        st.warning("상황을 먼저 입력해주세요.")
    else:
        with st.spinner('AI 선생님이 이야기를 구성하고 있어요...'):
            try:
                # 구글 API 표준 데이터 형식
                payload = {
                    "contents": [{
                        "parts": [{"text": f"너는 다정한 언어치료사야. 5세 아이를 위해 '{situation}' 상황에 대한 따뜻한 이야기 3줄을 지어줘."}]
                    }]
                }
                headers = {'Content-Type': 'application/json'}
                
                response = requests.post(URL, json=payload, headers=headers)
                result = response.json()
                
                # 결과 확인 및 출력
                if 'candidates' in result and len(result['candidates']) > 0:
                    answer = result['candidates'][0]['content']['parts'][0]['text']
                    st.success("AI 선생님의 맞춤 이야기 도착!")
                    st.info(answer)
                else:
                    # 또 에러가 날 경우를 대비해 상세 이유를 보여줍니다.
                    st.error("AI가 답변을 생성하지 못했습니다. 아래 내용을 확인해주세요.")
                    st.json(result)
                    
            except Exception as e:
                st.error(f"통신 중 오류가 발생했습니다: {e}")

st.caption("© 2026 언어치료 AI 과제 제출용")
