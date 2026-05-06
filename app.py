import streamlit as st
import requests  # 이 라이브러리가 주소를 직접 호출하게 해줍니다.

# 1. 설정
API_KEY = "AIzaSyDiZqvVqJFoga5oVWKwjVaHKt_yFqjERM0"
# 주소를 'v1'으로 직접 고정했습니다.
API_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# 2. 화면 구성
st.set_page_config(page_title="사회성 이야기 생성기", page_icon="🌟")
st.title("🌟 우리 아이 사회성 이야기 생성기")
st.write("아이의 상황을 입력하면 AI가 이야기를 지어줍니다.")

situation = st.text_input("어떤 상황인가요?", placeholder="예: 친구에게 장난감을 빌려달라고 해요")

if st.button("AI 이야기 만들기"):
    if not situation:
        st.warning("상황을 입력해주세요.")
    else:
        try:
            with st.spinner('AI 선생님이 이야기를 구성하고 있어요...'):
                # 구글 서버에 직접 편지를 보냅니다.
                payload = {
                    "contents": [{
                        "parts": [{"text": f"다정한 언어치료사처럼 5세 아이를 위한 사회성 이야기를 3문장으로 써줘. 상황: {situation}"}]
                    }]
                }
                headers = {'Content-Type': 'application/json'}
                
                # 주소로 직접 요청 전송
                response = requests.post(API_URL, json=payload, headers=headers)
                result = response.json()
                
                # 결과에서 텍스트만 뽑아내기
                answer = result['candidates'][0]['content']['parts'][0]['text']
                
            st.success("AI가 이야기를 완성했어요!")
            st.markdown("---")
            st.write(answer)
            st.markdown("---")
            
        except Exception as e:
            st.error(f"최종 호출 실패: {e}")
            st.info("💡 팁: 이 방식은 서버 주소를 직접 타격하므로 라이브러리 오류를 무시합니다.")

st.caption("© 2026 언어치료 AI 과제")
