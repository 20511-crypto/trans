import streamlit as st
from deep_translator import GoogleTranslator

# 페이지 기본 설정
st.set_page_config(page_title="다국어 번역기", page_icon="🌐", layout="centered")

st.title("🌐 한국어 다국어 번역기")
st.markdown("한국어를 입력하면 **영어, 중국어(간체), 일본어**로 동시에 번역해 줍니다.")

# 사용자 입력 창
text_to_translate = st.text_area("번역할 한국어 문장을 입력하세요:", height=150, placeholder="여기에 텍스트를 입력하세요...")

# 번역 버튼
if st.button("번역하기"):
    if text_to_translate.strip():
        with st.spinner("번역 중입니다... 잠시만 기다려주세요 ⏳"):
            try:
                # 번역기 객체 생성 및 번역 실행
                en_result = GoogleTranslator(source='ko', target='en').translate(text_to_translate)
                zh_result = GoogleTranslator(source='ko', target='zh-CN').translate(text_to_translate)
                ja_result = GoogleTranslator(source='ko', target='ja').translate(text_to_translate)
                
                st.success("번역이 완료되었습니다!")
                
                # 결과 출력
                st.subheader("🇺🇸 영어")
                st.info(en_result)
                
                st.subheader("🇨🇳 중국어")
                st.info(zh_result)
                
                st.subheader("🇯🇵 일본어")
                st.info(ja_result)
                
            except Exception as e:
                st.error(f"번역 중 오류가 발생했습니다: {e}")
    else:
        st.warning("번역할 텍스트를 먼저 입력해주세요.")
