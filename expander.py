import streamlit as st

st.bar_chart({"data": [1, 5, 2, 6, 2]})
with st.expander("Expand me to see some text"):
    st.write("Some text written inside expander")
