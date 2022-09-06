import streamlit as st

with st.form(key='profile_form'):
    # テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')

    # ラジオボタン
    age_category = st.radio(
        '年齢層',
        ('子供(18才未満)', '大人(18才以上)')
    )

    # マルチセレクト
    hobby = st.multiselect(
        '趣味',
        ('スポーツ', '読書', 'プログラミング', 'アニメ', '釣り', '料理')
    )

    # ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'よううこそ！{name}さん.{address}に送りました.')
        st.text(f'年齢層: {age_category}')
        st.text(', '.join(hobby))
