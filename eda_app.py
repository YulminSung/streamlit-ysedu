# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import utils

def run_eda_app():
    st.subheader("탐색적 자료 분석")

    iris = pd.read_csv('data/iris.csv')
    st.markdown('## IRIS 데이터 확인')
    st.write(iris.head())

    # 메뉴 지정
    submenu = st.sidebar.selectbox('하위메뉴', ['기술통계량', '그래프분석', '통계분석'])
    if submenu == '기술통계량':
        st.dataframe(iris)

        with st.expander('데이터 타입'):
            result1 = pd.DataFrame(iris.dtypes)
            st.write(result1)
        with st.expander('기술 통계량'):
            result2 = iris.describe()
            st.write(result2)
        with st.expander('타깃 빈도 수 확인'):
            st.dataframe(iris['species'].value_counts())
    elif submenu == '그래프분석':
        st.title('Title')
        with st.expander('산점도'):
            fig1 = px.scatter(iris,
                             x = 'sepal_width',
                             y = 'sepal_length',
                             color = 'species',
                             size = 'petal_width',
                             hover_data=['petal_length'])
            st.plotly_chart(fig1)

        # layouts
        col1, col2 = st.columns(2)
        with col1:
            st.title('Seaborn')
            # 그래프 작성
            fig, ax = plt.subplots()
            sns.boxplot(iris, x="species", y='sepal_length', ax=ax)
            st.pyplot(fig)

        with col2:
            st.title('Matplotlib')
            # 그래프 작성
            fig, ax = plt.subplots()
            ax.hist(iris['sepal_length'], color='green')
            st.pyplot(fig)

        # Tabs
        tab1, tab2, tab3, tab4 = st.tabs(['탭1', '탭2', '탭3', '탭4'])
        with tab1:
            st.write('탭1')
            # 종 선택할 때마다
            # 산점도 그래프가 달라지도록 함.
            # plotly 그래프로 구현
            fig = px.bar(iris, x='species', y='petal_length')
            fig.update_layout(title='petal_length_Express_Chart')
            st.plotly_chart(fig)

        # load train_peptides.csv
        tr_pep = pd.read_csv('data/train_peptides.csv')

        # load train_peptides.csv
        tr_pep = pd.read_csv('data/train_peptides.csv')
        tr_clinic = pd.read_csv('data/train_clinical_data.csv')

        with tab2:
            st.write('탭2')
            # 캐글 데이터
            # 해당 데이터 그래프 1개만 그려보기

            fig = px.line(tr_clinic, x='visit_month', y='patient_id',color='updrs_3',
                          markers = True)
            st.plotly_chart(fig)

            # fig = px.line(tr_pep, x='visit_id', y='PeptideAbundance')
            # st.plotly_chart(fig)

            ## 필터 필요함 / 데이터 너무 많아서 안나옴
            # fig = px.box(tr_pep, x='patient_id', y='PeptideAbundance'
            #              ,points='all',color="visit_id")
            # st.plotly_chart(fig)



    elif submenu == '통계분석':
        pass
    else:
        st.warning('뭔가 없어요!')