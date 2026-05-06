import streamlit as st
import requests

# 1. 학생님의 진짜 API 키를 여기에 넣으세요
API_KEY = "AIzaSyDyZbzfvP_UaUSuRAb4SJw9W-Pa50SjEes"

# 모델명을 주소에서 빼고, 가장 기본형 주소를 사용합니다.
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

st.set_page_config(page_title="사회성 이야기 생성기", page_icon="🌟")
st.title("🌟 AI 언어치료사 이야기")

situation = st.text_input("상황 입력", placeholder="예: 친구와 싸웠어요")

if st.button("AI 이야기 만들기"):
    if not situation:
        st.warning("상황을 입력해주세요.")
    else:
        with st.spinner('진짜 AI가 답변을 생성 중입니다...'):
            try:
                # 구글 API 최신 규격 (가장 안정적인 형태)
                payload = {
                    "contents": [{
                        "parts": [{"text": f"너는 다정한 언어치료사야. 5세 아이를 위해 '{situation}' 상황에 대한 따뜻한 이야기 3줄을 지어줘."}]
                    }]
                }
                headers = {'Content-Type': 'application/json'}
                
                response = requests.post(URL, json=payload, headers=headers)
                result = response.json()
                
                # [성공]
                if 'candidates' in result:
                    answer = result['candidates'][0]['content']['parts'][0]['text']
                    st.success("AI 답변 생성 성공!")
                    st.write(answer)
                # [실패] 여전히 404가 뜬다면 아래 '특약 처방'을 보세요.
                else:
                    st.error("구글 서버가 모델을 찾지 못하고 있습니다.")
                    st.json(result)
                    
            except Exception as e:
                st.error(f"통신 오류 발생: {e}")

st.caption("© 2026 Gemini API 연동 모드")
