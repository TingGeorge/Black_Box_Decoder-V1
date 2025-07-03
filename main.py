import streamlit as st

st.logo("sidebar_logo.png", icon_image="uc_logo.png")

# main.py
if "score" not in st.session_state:
    st.session_state.score = 0

# questions_page.py
# level 1
if "answer_1" not in st.session_state:
    st.session_state.answer_1 = ""
if "level_1_correct" not in st.session_state:
    st.session_state.level_1_correct = False
if "fail_answer_1" not in st.session_state:
    st.session_state.fail_answer_1 = False
if "score_calculated_1" not in st.session_state:
    st.session_state.score_calculated_1 = False
if "text_1" not in st.session_state:
    st.session_state.text_1 = ""

#level 2
if "answer_2" not in st.session_state:
    st.session_state.answer_2 = ""
if "level_2_correct" not in st.session_state:
    st.session_state.level_2_correct = False
if "fail_answer_2" not in st.session_state:
    st.session_state.fail_answer_2 = False
if "score_calculated_2" not in st.session_state:
    st.session_state.score_calculated_2 = False
if "text_2" not in st.session_state:
    st.session_state.text_2 = ""

#level 3
if "answer_3" not in st.session_state:
    st.session_state.answer_3 = ""
if "level_3_correct" not in st.session_state:
    st.session_state.level_3_correct = False
if "fail_answer_3" not in st.session_state:
    st.session_state.fail_answer_3 = False
if "score_calculated_3" not in st.session_state:
    st.session_state.score_calculated_3 = False
if "text_3" not in st.session_state:
    st.session_state.text_3 = ""

first_page = st.Page("first_page.py", title="首頁", icon=":material/home:")
questions_page = st.Page("questions_page.py", title="題目", icon=":material/menu:")
end_page = st.Page("end_page.py", title="解題進度", icon=":material/flag:")

pages = st.navigation([first_page, questions_page, end_page])
pages.run()