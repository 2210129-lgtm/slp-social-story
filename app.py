import google.generativeai as genai
from google.generativeai.types import RequestOptions

# 1. API 키 설정
genai.configure(api_key="AIzaSyDiZqvVqJFoga5oVWKwjVaHKt_yFqjERM0")

# 2. 모델 선언 (이 부분이 핵심입니다!)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. 호출할 때 'v1' 주소를 강제로 사용하도록 설정 (404 v1beta 에러 방지)
try:
    response = model.generate_content(
        "안녕?",
        request_options=RequestOptions(api_version='v1') # 이 코드가 결제 에러를 피하게 해줍니다.
    )
    st.write(response.text)
except Exception as e:
    st.error(f"에러 내용: {e}")
st.title("🌟 우리 아이 사회성 이야기 생성기")
st.write("아이의 상황을 입력하면 AI가 실시간으로 이야기를 지어줍니다.")

situation = st.text_input("어떤 상황인가요?", placeholder="예: 친구에게 장난감을 빌려달라고 해요")

if st.button("AI 이야기 만들기"):
    if not api_key or "AIza" not in api_key:
        st.error("올바른 API 키를 입력해주세요!")
    elif not situation:
        st.warning("상황을 입력해주세요.")
    else:
        try:
            # 설정 초기화
            genai.configure(api_key=api_key)
            
            # [핵심 변경] 'models/'를 생략하고 가장 기초적인 'gemini-pro'를 먼저 시도합니다.
            # gemini-pro는 v1beta와 v1 모두에서 가장 잘 응답하는 모델입니다.
            model = genai.GenerativeModel('gemini-pro')
            
            with st.spinner('AI 선생님이 이야기를 짓고 있어요...'):
                # 답변 생성
                response = model.generate_content(
                    f"5세 아이를 위한 사회성 이야기. 상황: {situation}. 3문장으로 다정하게 써줘.",
                    generation_config={"temperature": 0.7}
                )
                
            st.success("AI가 이야기를 완성했어요!")
            st.markdown("---")
            st.subheader(f"📖 AI가 지어준 이야기")
            st.write(response.text)
            st.markdown("---")
            
        except Exception as e:
            # 여기서도 에러가 나면, 모델 이름을 다시 한번 교체해서 시도합니다.
            try:
                model = genai.GenerativeModel('gemini-1.0-pro')
                response = model.generate_content(f"{situation}에 대한 어린이 동화 3줄")
                st.success("AI가 이야기를 완성했어요!")
                st.write(response.text)
            except:
                st.error(f"서버 연결 오류: {e}")
                st.info("💡 팁: API 키가 활성화되는 데 시간이 걸릴 수 있습니다. 5분 뒤에 다시 시도해 보세요.")

st.caption("© 2026 언어치료 AI 과제")
