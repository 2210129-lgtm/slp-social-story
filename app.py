import streamlit as st
import google.generativeai as genai

# 페이지 설정
st.set_page_config(page_title="사회성 이야기 생성기", page_icon="🌟")

# --- [중요] 여기에 본인의 API 키를 입력하세요 ---
api_key = "AIzaSyDiZqvVqJFoga5oVWKwjVaHKt_yFqjERM0" # 본인의 실제 API 키를 따옴표 안에 넣으세요
# ------------------------------------------

st.title("🌟 우리 아이 사회성 이야기 생성기")
st.write("아이의 상황을 입력하면 다정한 이야기를 만들어줍니다.")

situation = st.text_input("어떤 상황인가요?", placeholder="예: 친구에게 장난감을 빌려달라고 해요")

if st.button("이야기 만들기"):
    if not api_key or api_key == "AIza...":
        st.error("API 키를 정확히 입력해주세요!")
    elif not situation:
        st.warning("상황을 입력해주세요.")
    else:
        try:
            # Gemini 설정
            genai.configure(api_key=api_key)
            
            # 모델 선언 (가장 안정적인 최신 명칭)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # 프롬프트 구성
            prompt = f"""
            너는 다정한 언어치료사야. 
            다음 상황에 대해 5세 아이가 이해하기 쉬운 3문장 내외의 '사회성 이야기'를 작성해줘.
            상황: {situation}
            """
            
            with st.spinner('이야기를 생성 중입니다...'):
                response = model.generate_content(prompt)
                
            st.success("성공적으로 만들어졌어요!")
            st.markdown("---")
            st.subheader(f"📖 [{situation}] 이야기")
            st.write(response.text)
            st.markdown("---")
            
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")
            st.info("팁: API 키가 개인 계정용인지, 그리고 깃허브에 Commit을 했는지 확인해주세요.")

st.caption("© 2024 언어치료 AI 도구")
