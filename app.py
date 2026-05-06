import streamlit as st
import requests

# 1. 학생님의 진짜 API 키를 여기에 넣으세요
API_KEY = "AIzaSyAS7Ezm0cTnR0_KDle6ERumw0ESYQKv1g0"

# 구글이 권장하는 최신 엔드포인트 구조입니다.
# 모델명 앞에 'models/'를 명시적으로 붙여서 404 에러를 방지합니다.
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

st.set_page_config(page_title="사회성 이야기 생성기", page_icon="🌟")
st.title("🌟 우리 아이 맞춤형 AI 이야기")

situation = st.text_input("상황을 입력하세요", placeholder="예: 친구에게 장난감을 빌려달라고 말하고 싶어요")

if st.button("AI 선생님에게 물어보기"):
    if not situation:
        st.warning("아이의 상황을 입력해주세요!")
    else:
        with st.spinner('AI 선생님이 실시간으로 답변을 작성 중입니다...'):
            try:
                # 구글 API가 요구하는 정확한 JSON 구조입니다.
                payload = {
                    "contents": [{
                        "parts": [{
                            "text": f"너는 다정한 언어치료사야. 5세 아이를 위해 '{situation}' 상황에 대한 따뜻한 위로와 교육적인 이야기 3줄을 지어줘."
                        }]
                    }]
                }
                headers = {'Content-Type': 'application/json'}
                
                response = requests.post(URL, json=payload, headers=headers)
                result = response.json()
                
                # 답변 추출 성공 시
                if 'candidates' in result:
                    ai_story = result['candidates'][0]['content']['parts'][0]['text']
                    st.success("AI 선생님의 맞춤 이야기 도착!")
                    st.info(ai_story)
                # 에러 발생 시 (학생님이 보신 에러가 여기 찍힐 겁니다)
                else:
                    st.error("AI 응답 생성에 실패했습니다.")
                    st.json(result) # 여기서 에러 내용을 다시 확인해봐요.
                    
            except Exception as e:
                st.error(f"연결 오류: {e}")

st.caption("© 2026 언어치료 AI 과제 - 진짜 AI 모드")
