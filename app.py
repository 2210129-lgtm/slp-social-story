import streamlit as st
import requests

# 1. 방금 새로 만든 키를 아래 따옴표 안에 넣으세요!
API_KEY = "AIzaSyAS7Ezm0cTnR0_KDle6ERumw0ESYQKv1g0"
URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"

st.set_page_config(page_title="사회성 이야기 생성기", page_icon="🌟")
st.title("🌟 우리 아이 맞춤형 AI 이야기")

situation = st.text_input("상황을 입력하세요", placeholder="예: 친구와 장난감을 나눠 쓰기 싫어해요")

if st.button("AI 이야기 만들기"):
    if not situation:
        st.warning("상황을 먼저 입력해주세요.")
    else:
        with st.spinner('AI 선생님이 이야기를 지어내고 있어요...'):
            try:
                # 실시간으로 상황에 맞춰 답변을 생성하는 설정
                payload = {
                    "contents": [{
                        "parts": [{"text": f"너는 다정한 언어치료사야. 5세 아이를 위해 '{situation}' 상황에 대한 따뜻한 이야기 3줄을 지어줘."}]
                    }]
                }
                headers = {'Content-Type': 'application/json'}
                
                response = requests.post(URL, json=payload, headers=headers)
                result = response.json()
                
                # 답변이 잘 왔는지 확인
                if 'candidates' in result:
                    answer = result['candidates'][0]['content']['parts'][0]['text']
                    st.success("AI 선생님의 맞춤 이야기:")
                    st.info(answer)
                else:
                    # 만약 여기서 또 candidates 에러가 나면 원인을 분석해줍니다.
                    st.error("구글 서버 응답에 문제가 있습니다.")
                    st.json(result)
                    
            except Exception as e:
                st.error(f"연결 오류가 발생했습니다: {e}")

st.caption("© 2026 언어치료 AI 과제 제출용")
