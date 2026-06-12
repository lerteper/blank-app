import streamlit as st

st.title("🎈 My new app")
val = st.slider('slide', 0, 1000)
data = {
    
}
for i in range(0, val):
    data[i] = i
    data[2 * val - i] = i
st.bar_chart(data, color = [val / 1000, (1000 - val)/1000, 0])
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
