import streamlit as st
import google.generativeai as genai
from google.generativeai.types import RequestOptions

# 1. 설정 및 API 키 입력
# (방금 알려주신 키를 변수에 담아 아래에서 공통으로 사용합니다)
MY_API_KEY = "AIzaSyDiZqvVqJFoga5oVWKwjVaHKt_yFqjERM0"
genai.configure(api_key=MY_API_KEY)

# 2. 모델 선언 (가장 성능이 좋은 1.5-flash 사용)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. 화면 구성
st.set_page_config(page_title="사회성 이야기 생성기", page_icon="🌟")
st.title("🌟 우리 아이 사회성 이야기 생성기")
st.write("아이의 상황을 입력하면 AI가 실시간으로 이야기를 지어줍니다.")

# 입력창
situation = st.text_input("어떤 상황인가요?", placeholder="예: 친구에게 장난감을 빌려달라고 해요")

# 버튼 클릭 시 실행
if st.button("AI 이야기 만들기"):
    if not situation:
        st.warning("상황을 입력해주세요.")
    else:
        try:
            with st.spinner('AI 선생님이 이야기를 구성하고 있어요...'):
                # 호출 시 'v1' 주소를 강제 사용하여 404 에러 방지
                response = model.generate_content(
                    f"너는 다정한 언어치료사야. 5세 아이를 위한 사회성 이야기를 만들어줘. 상황: {situation}. 딱 3문장으로 다정하게 써줘.",
                    request_options=RequestOptions(api_version='v1')
                )
                
            st.success("AI가 이야기를 완성했어요!")
            st.markdown("---")
            st.subheader(f"📖 AI가 지어준 이야기")
            st.write(response.text)
            st.markdown("---")
            
        except Exception as e:
            # 혹시라도 에러가 나면 상세 내용을 보여줍니다.
            st.error(f"오류가 발생했습니다: {e}")
            st.info("💡 팁: API 키가 활성화되는 중일 수 있습니다. 잠시 후 다시 시도해 보세요.")

st.caption("© 2026 언어치료 AI 과제")
