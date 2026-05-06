import streamlit as st
import google.generativeai as genai
from google.generativeai import client

# 1. API 키 설정
MY_API_KEY = "AIzaSyDiZqvVqJFoga5oVWKwjVaHKt_yFqjERM0"

# 2. [치트키] 서버 주소를 v1beta가 아닌 v1으로 강제 고정
client.DEFAULT_API_VERSION = 'v1'
genai.configure(api_key=MY_API_KEY)

# 3. 모델 선언
model = genai.GenerativeModel('gemini-1.5-flash')

# 4. 화면 구성
st.set_page_config(page_title="사회성 이야기 생성기", page_icon="🌟")
st.title("🌟 우리 아이 사회성 이야기 생성기")
st.write("아이의 상황을 입력하면 AI가 실시간으로 이야기를 지어줍니다.")

situation = st.text_input("어떤 상황인가요?", placeholder="예: 친구에게 장난감을 빌려달라고 해요")

if st.button("AI 이야기 만들기"):
    if not situation:
        st.warning("상황을 입력해주세요.")
    else:
        try:
            with st.spinner('AI가 이야기를 생성 중...'):
                # 5. 생성 시도
                response = model.generate_content(
                    f"다정한 언어치료사처럼 5세 아이를 위한 사회성 이야기를 3문장으로 써줘. 상황: {situation}"
                )
                
            st.success("AI가 이야기를 완성했어요!")
            st.markdown("---")
            st.write(response.text)
            st.markdown("---")
            
        except Exception as e:
            # 만약 이래도 404가 뜨면 계정 자체가 1.5 모델을 지원 안 하는 것이므로 gemini-pro로 시도
            try:
                model_backup = genai.GenerativeModel('gemini-pro')
                response = model_backup.generate_content(f"{situation} 상황의 어린이 사회성 이야기 3줄")
                st.success("AI가 이야기를 완성했어요! (안정화 모델 사용)")
                st.write(response.text)
            except Exception as e2:
                st.error(f"서버 연결 최종 오류: {e2}")

st.caption("© 2026 언어치료 AI 과제")
