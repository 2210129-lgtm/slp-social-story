import streamlit as st
import requests

# 1. 친구에게 받은 '진짜 키'를 여기에 넣으세요!
API_KEY = "AIzaSyCVQU8SFRDux6mDXuzE4_Bnb1D4WnPEo7w"

# 가장 안정적인 v1beta 주소와 gemini-1.5-flash 모델 경로입니다.
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

st.set_page_config(page_title="사회성 이야기 생성기", page_icon="🌟")
st.title("🌟 우리 아이 맞춤형 AI 이야기")
st.write("아이의 상황을 입력하면 AI 선생님이 다정한 이야기를 들려줍니다.")

situation = st.text_input("상황을 입력하세요", placeholder="예: 친구와 장난감을 나눠 쓰기 싫어해요")

if st.button("AI 이야기 만들기"):
    if not situation:
        st.warning("상황을 먼저 입력해주세요.")
    else:
        with st.spinner('AI 선생님이 이야기를 지어내고 있어요...'):
            try:
                # 구글 API 표준 페이로드
                payload = {
                    "contents": [{
                        "parts": [{"text": f"너는 다정한 언어치료사야. 5세 아이를 위해 '{situation}' 상황에 대한 따뜻한 이야기 3줄을 지어줘."}]
                    }]
                }
                headers = {'Content-Type': 'application/json'}
                
                response = requests.post(URL, json=payload, headers=headers)
                result = response.json()
                
                # 답변 출력 성공 시
                if 'candidates' in result:
                    answer = result['candidates'][0]['content']['parts'][0]['text']
                    st.success("AI 선생님의 맞춤 이야기 도착!")
                    st.info(answer)
                else:
                    # 만약 여기서도 에러가 나면 친구 계정도 설정이 필요한 상태인 거예요.
                    st.error("AI 응답을 가져오지 못했습니다.")
                    st.json(result)
                    
            except Exception as e:
                st.error(f"연결 오류: {e}")

st.caption("© 2026 언어치료 AI 과제 제출용")
