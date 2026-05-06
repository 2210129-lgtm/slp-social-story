import streamlit as st
import requests

# 1. 친구에게 받은 키를 넣어주세요
API_KEY = "AIzaSyCVQU8SFRDux6mDXuzE4_Bnb1D4WnPEo7w"

# 내 키로 사용 가능한 모델 목록을 가져오는 주소입니다.
LIST_URL = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

st.title("🔍 내 API 키 모델 확인하기")

if st.button("내 키로 쓸 수 있는 모델 찾기"):
    with st.spinner('구글 서버에서 목록을 가져오는 중...'):
        try:
            response = requests.get(LIST_URL)
            data = response.json()
            
            if 'models' in data:
                st.success("모델 목록을 가져왔습니다! 아래 이름을 저에게 알려주세요.")
                # 모델 이름들만 골라서 보여줍니다.
                model_names = [m['name'] for m in data['models']]
                st.write(model_names)
            else:
                st.error("목록을 가져오지 못했습니다. 에러 내용:")
                st.json(data)
        except Exception as e:
            st.error(f"연결 오류: {e}")
