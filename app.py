import streamlit as st
import requests

# 1. API 설정 (주소를 v1beta로 변경하여 호환성 해결)
API_KEY = "AIzaSyAS7Ezm0cTnR0_KDle6ERumw0ESYQKv1g0"
# 모델명을 주소에 포함시키는 표준 형식으로 수정했습니다.
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

st.set_page_config(page_title="사회성 이야기 생성기", page_icon="🌟")
st.title("🌟 우리 아이 맞춤형 AI 이야기")

situation = st.text_input("상황을 입력하세요", placeholder="예: 친구와 장난감을 나눠 쓰기 싫어해요")

if st.button("AI 이야기 만들기"):
    if not situation:
        st.warning("상황을 먼저 입력해주세요.")
    else:
        with st.spinner('AI 선생님이 이야기를 지어내고 있어요...'):
            try:
                payload = {
                    "contents": [{
                        "parts": [{"text": f"너는 다정한 언어치료사야. 5세 아이를 위해 '{situation}' 상황에 대한 따뜻한 이야기 3줄을 지어줘."}]
                    }]
                }
                headers = {'Content-Type': 'application/json'}
                
                response = requests.post(URL, json=payload, headers=headers)
                result = response.json()
                
                # 결과 확인
                if 'candidates' in result:
                    answer = result['candidates'][0]['content']['parts'][0]['text']
                    st.success("AI 선생님의 맞춤 이야기:")
                    st.info(answer)
                else:
                    st.error("응답 구조에 문제가 있습니다.")
                    st.json(result)
                    
            except Exception as e:
                st.error(f"연결 오류: {e}")

st.caption("© 2026 언어치료 AI 과제 제출용")
