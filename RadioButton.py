import streamlit as st

genre = st.radio(
    "# What's Your favorite movie genre",
    ('comedy', 'Drama', 'Documentary'))

if genre == 'comedy':
    st.write('You selected comedy.')
else:
    st.write('You did not selected comedy.')