import streamlit as st
import google.generativeai as genai

# 페이지 설정
st.set_page_config(page_title="사회성 이야기 생성기", page_icon="🌟")

# --- 여기에 본인의 API 키를 직접 입력하세요 ---
api_key = "AIzaSyCjBz0BEihJ9SYKHrJ3vamDKlYGdUvuy4k" 
# ------------------------------------------

# 메인 화면
st.title("🌟 우리 아이 사회성 이야기 생성기")
st.write("아이의 특정 상황을 입력하면, 눈높이에 맞는 3~5문장의 짧은 이야기를 만들어줍니다.")

# 사용자 입력
situation = st.text_input("어떤 상황에 대한 이야기가 필요하신가요?", placeholder="예: 치과에 가요, 친구에게 장난감을 빌려달라고 해요")

if st.button("이야기 만들기"):
    if api_key == "본인의_API_키를_여기에_넣으세요" or not api_key:
        st.error("API 키가 설정되지 않았습니다. 코드에서 키를 입력해주세요!")
    elif not situation:
        st.warning("상황을 입력해주세요.")
    else:
        try:
            # Gemini 설정
            genai.configure(api_key=api_key)
            
            # 모델 선언 (가장 확실한 이름으로 설정)
            # 'models/'를 붙이지 않고 선언합니다.
            model = genai.GenerativeModel('models/gemini-1.5-flash')
            
            # 프롬프트 설정
            prompt = f"너는 언어치료사야. 5세 아이 수준으로 '{situation}' 상황에 대한 사회성 이야기를 3문장으로 써줘."
            
            with st.spinner('이야기를 생성 중입니다...'):
                # 호출 시도
                response = model.generate_content(prompt)
                
            st.success("완성되었습니다!")
            st.markdown("---")
            st.subheader(f"📖 [{situation}] 이야기")
            st.write(response.text)
            st.markdown("---")
            
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")
            st.info("팁: API 키가 올바른지, 혹은 Google AI Studio에서 Gemini 1.5 Flash 모델을 사용할 수 있는 상태인지 확인해 보세요.")

st.caption("© 2024 언어치료 AI 도구")
