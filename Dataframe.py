import streamlit as st
import pandas as pd
import numpy as np

st.header("This is a Dataframe Demo")
df = pd.DataFrame(
    np.random.rand(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # It is interactive
