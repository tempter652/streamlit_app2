import streamlit as st
import pandas as pd

# データ分析関連
df = pd.read_csv('./data/temperature.csv', index_col='月')
# st.dataframe(df)
st.line_chart(df)
st.bar_chart(df['2021年'])
