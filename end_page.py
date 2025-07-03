import streamlit as st

st.image("end_title_stars.png")
st.write("")
st.write("")

images = ["score0.png", "score1.png", "score2.png", "score3.png"]
st.image(images[st.session_state.score])

if st.session_state.score == 3:
    st.balloons()