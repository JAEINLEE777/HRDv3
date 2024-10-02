import streamlit as st
import pandas as pd

# 하드코딩된 샘플 데이터
data = {
    '날짜': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-03'],
    '직원': ['김철수', '이영희', '김철수', '이영희', '김철수', '이영희'],
    '부서': ['영업', '마케팅', '영업', '마케팅', '영업', '마케팅'],
    '직무역량': ['직무', 'Global', '직무', 'SKValues', 'Global', '직무'],
    '학습시간': [2, 3, 1, 4, 3, 2]
}

df = pd.DataFrame(data)

def main():
    st.title('간소화된 학습시간 이수현황 대시보드')

    # 데이터 전처리
    df['날짜'] = pd.to_datetime(df['날짜'])
    df['월'] = df['날짜'].dt.to_period('M').astype(str)

    # 월별 총 학습시간
    monthly_total = df.groupby('월')['학습시간'].sum().reset_index()
    
    st.subheader('월별 총 학습시간')
    st.bar_chart(monthly_total.set_index('월'))

    # 직원별 총 학습시간
    employee_total = df.groupby('직원')['학습시간'].sum().reset_index()
    
    st.subheader('직원별 총 학습시간')
    st.bar_chart(employee_total.set_index('직원'))

    # 직무역량별 총 학습시간
    competency_total = df.groupby('직무역량')['학습시간'].sum().reset_index()
    
    st.subheader('직무역량별 총 학습시간')
    st.bar_chart(competency_total.set_index('직무역량'))

    # 원본 데이터 표시
    st.subheader('원본 데이터')
    st.dataframe(df)

if __name__ == '__main__':
    main()
