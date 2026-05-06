import streamlit as st
import google.generativeai as genai

# 페이지 설정
st.set_page_config(page_title="사회성 이야기 생성기", page_icon="🌟")

# 사이드바에서 API 키 입력 받기 (보안을 위해)
api_key = "AIzaSyCjBz0BEihJ9SYKHrJ3vamDKlYGdUvuy4k"

# 메인 화면
st.title("🌟 우리 아이 사회성 이야기 생성기")
st.write("아이의 특정 상황을 입력하면, 눈높이에 맞는 3~5문장의 짧은 이야기를 만들어줍니다.")

# 사용자 입력
situation = st.text_input("어떤 상황에 대한 이야기가 필요하신가요?", placeholder="예: 치과에 가요, 친구에게 장난감을 빌려달라고 해요")

if st.button("이야기 만들기"):
    if not api_key:
        st.error("API 키를 먼저 입력해주세요!")
    elif not situation:
        st.warning("상황을 입력해주세요.")
    else:
        try:
            # Gemini 설정
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # 프롬프트 설정 (페르소나 부여)
            prompt = f"""
            너는 다정한 언어치료사야. 5~7세 아이가 이해하기 쉬운 단어를 사용해서 '{situation}' 상황에 대한 사회성 이야기를 만들어줘.
            다음 규칙을 지켜줘:
            1. 3~5문장 내외로 작성할 것.
            2. 아이의 감정을 공감해주고, 바람직한 행동 방향을 제시할 것.
            3. 마지막은 긍정적인 다짐으로 끝낼 것.
            4. 각 문장은 이해하기 쉽게 줄바꿈을 해줘.
            """
            
            with st.spinner('이야기를 짓는 중...'):
                response = model.generate_content(prompt)
                
            st.success("완성되었습니다!")
            st.markdown("---")
            st.subheader(f"📖 [{situation}] 이야기")
            st.write(response.text)
            st.markdown("---")
            
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")

# 푸터
st.caption("© 2024 언어치료 AI 도구 - 바이브 코딩으로 제작됨")
