import streamlit as st

code = '''
def hello():
    print('Hello World!')
'''
st.code(code, language='python')
