import streamlit as st
import pandas as pd
import random

# 페이지 기본 설정
st.set_page_config(page_title="자동 시간표 생성기", page_icon="📅", layout="centered")

st.title("📅 자동 시간표 생성기")
st.markdown("과목들을 입력하면 **월요일부터 금요일까지(하루 6교시)** 무작위로 시간표를 짜드립니다.")

# 사용자 입력 창
subjects_input = st.text_input(
    "과목을 쉼표(,)로 구분해서 입력하세요:", 
    placeholder="예: 국어, 영어, 수학, 사회, 과학, 체육, 미술"
)

# 생성 버튼
if st.button("시간표 만들기"):
    if subjects_input.strip():
        # 1. 입력받은 문자열을 리스트로 변환 (공백 제거)
        subjects = [s.strip() for s in subjects_input.split(",") if s.strip()]
        
        if len(subjects) > 0:
            with st.spinner("시간표를 구성하는 중입니다... ⏳"):
                # 2. 총 30칸(5일 * 6교시) 채우기
                total_slots = 30
                timetable_slots = []
                
                # 과목들을 30칸에 도달할 때까지 반복해서 추가
                while len(timetable_slots) < total_slots:
                    timetable_slots.extend(subjects)
                
                # 딱 30개로 자르고 무작위로 섞기
                timetable_slots = timetable_slots[:total_slots]
                random.shuffle(timetable_slots)
                
                # 3. 데이터프레임 만들기 (열: 월~금, 행: 1~6교시)
                days = ["월요일", "화요일", "수요일", "목요일", "금요일"]
                schedule_data = {
                    day: timetable_slots[i*6:(i+1)*6] for i, day in enumerate(days)
                }
                
                # 행 인덱스 설정
                index_labels = [f"{i}교시" for i in range(1, 7)]
                df = pd.DataFrame(schedule_data, index=index_labels)
                
                # 4. 화면에 출력하기
                st.success("시간표가 완성되었습니다!")
                st.table(df)
        else:
            st.warning("과목을 하나 이상 제대로 입력해주세요.")
    else:
        st.warning("과목을 먼저 입력해주세요.")
