import streamlit as st
import pandas as pd
import numpy as np

print('funziona?')
st.title(':blue[Bel tempo] :sunglasses:')

st.text('24/03/2023   12:00')






col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "30 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "10%", "4%")



chart_data = pd.DataFrame(
    np.random.randn(25,2),
    columns=["a","b"])
st.dataframe(chart_data)

st.bar_chart(chart_data)



