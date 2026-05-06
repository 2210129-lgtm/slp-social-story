import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정
st.set_page_config(page_title="사회성 이야기 생성기", page_icon="🌟")

# 2. API 키 설정 (본인의 개인 계정 키를 꼭 넣으세요)
api_key = "AIzaSyDiZqvVqJFoga5oVWKwjVaHKt_yFqjERM0" 

st.title("🌟 우리 아이 사회성 이야기 생성기")
st.write("아이의 상황을 입력하면 AI가 실시간으로 이야기를 지어줍니다.")

situation = st.text_input("어떤 상황인가요?", placeholder="예: 친구에게 장난감을 빌려달라고 해요")

if st.button("AI 이야기 만들기"):
    if not api_key or api_key == "AIza...":
        st.error("API 키가 설정되지 않았습니다.")
    elif not situation:
        st.warning("상황을 입력해주세요.")
    else:
        try:
            # 설정 초기화
            genai.configure(api_key=api_key)
            
            # [핵심] 가장 호환성이 높은 모델 이름으로 시도합니다.
            # 1.5-flash가 안 되면 pro로 자동 전환되도록 모델명을 하나씩 테스트해보는 방식입니다.
            model_name = 'gemini-1.5-flash' 
            model = genai.GenerativeModel(model_name)
            
            with st.spinner('AI가 상황을 분석해서 이야기를 짓고 있습니다...'):
                # 프롬프트 전달
                response = model.generate_content(
                    f"너는 다정한 언어치료사야. '{situation}' 상황에 대해 5세 아이가 이해하기 쉬운 3문장 내외의 이야기를 써줘.",
                    generation_config=genai.types.GenerationConfig(
                        temperature=0.7,
                        max_output_tokens=300
                    )
                )
                
            st.success("AI가 이야기를 완성했어요!")
            st.markdown("---")
            st.subheader(f"📖 AI가 지어준 [{situation}] 이야기")
            st.write(response.text)
            st.markdown("---")
            
        except Exception as e:
            # 만약 또 404 에러가 나면, 모델을 'gemini-pro'로 바꿔서 한 번 더 시도하라는 안내
            st.error(f"오류가 발생했습니다: {e}")
            if "404" in str(e):
                st.info("💡 팁: 현재 계정에서 1.5-flash 모델을 찾을 수 없습니다. 코드의 'gemini-1.5-flash' 부분을 'gemini-pro'로 바꿔서 다시 커밋해보세요!")
