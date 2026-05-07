import streamlit as st
import requests

# 1. 친구에게 받은 키를 그대로 사용하세요
API_KEY = "AIzaSyDiZqvVqJFoga5oVWKwjVaHKt_yFqjERM0"

# 무료 티어에서 가장 넉넉한 할당량을 가진 gemini-flash-latest를 사용합니다.
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={API_KEY}"

st.set_page_config(page_title="사회성 이야기 생성기", page_icon="🌟")
st.title("🌟 우리 아이 맞춤형 AI 이야기")

situation = st.text_input("상황 입력", placeholder="예: 친구와 싸웠어요")

if st.button("AI 이야기 만들기"):
    if not situation:
        st.warning("상황을 입력해주세요.")
    else:
        # 에러 메시지에서 51초 기다리라고 했으니, 혹시 모르니 조금만 여유를 가집시다.
        with st.spinner('AI가 따뜻한 이야기를 생각하고 있어요...'):
            try:
                payload = {
                    "contents": [{
                        "parts": [{"text": f"너는 다정한 언어치료사야. 5세 아이를 위해 '{situation}' 상황에 대한 따뜻한 이야기 3줄을 지어줘."}]
                    }]
                }
                headers = {'Content-Type': 'application/json'}
                
                response = requests.post(URL, json=payload, headers=headers)
                result = response.json()
                
                if 'candidates' in result:
                    answer = result['candidates'][0]['content']['parts'][0]['text']
                    st.success("AI 답변 생성 성공!")
                    st.info(answer)
                elif 'error' in result and result['error']['code'] == 429:
                    st.error("구글 서버가 잠시 쉬고 싶어 하네요. 1분만 기다렸다가 다시 버튼을 눌러보세요!")
                else:
                    st.error("오류가 발생했습니다.")
                    st.json(result)
                    
            except Exception as e:
                st.error(f"연결 오류: {e}")

st.caption("© 2026 언어치료 AI - Flash Engine")
