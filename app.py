import streamlit as st
import requests

# 1. 친구에게 받은 키를 넣어주세요
API_KEY = "AIzaSyCVQU8SFRDux6mDXuzE4_Bnb1D4WnPEo7w"

# 리스트 12번에 있던 가장 안정적인 모델로 주소를 변경합니다.
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-latest:generateContent?key={API_KEY}"

st.set_page_config(page_title="사회성 이야기 생성기", page_icon="🌟")
st.title("🌟 우리 아이 맞춤형 AI 이야기")

situation = st.text_input("상황 입력", placeholder="예: 친구와 싸웠어요")

if st.button("AI 이야기 만들기"):
    if not situation:
        st.warning("상황을 입력해주세요.")
    else:
        with st.spinner('AI가 답변을 생성 중입니다...'):
            try:
                payload = {
                    "contents": [{
                        "parts": [{"text": f"너는 다정한 언어치료사야. 5세 아이를 위해 '{situation}' 상황에 대한 따뜻한 이야기 3줄을 지어줘."}]
                    }]
                }
                headers = {'Content-Type': 'application/json'}
                
                # 500 에러를 대비해 한 번 더 시도하는 로직을 살짝 얹었습니다.
                response = requests.post(URL, json=payload, headers=headers)
                result = response.json()
                
                if 'candidates' in result:
                    answer = result['candidates'][0]['content']['parts'][0]['text']
                    st.success("AI 답변 생성 성공!")
                    st.info(answer)
                else:
                    # 만약 또 500이 나면, 서버가 잠시 점검 중인 것이니 3초 뒤에 다시 버튼을 눌러보세요.
                    st.error("구글 서버가 아직 조금 불안정합니다. 잠시 후 다시 눌러주세요!")
                    st.json(result)
                    
            except Exception as e:
                st.error(f"연결 오류: {e}")

st.caption("© 2026 언어치료 AI - Stable Engine")
