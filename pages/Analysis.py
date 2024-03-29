import numpy as np
import pandas as pd
import streamlit as st

import MEDA as md

tab_1 ,tab_2 = st.tabs(['Visualization','Discuss'])

with tab_1:
    st.title("Figure Between Price And Fuel")
    fact = st.radio('Choose Fact',['price'],horizontal=True)
    st.plotly_chart(md.tob_10_carss(fact))



with tab_2:
    st.title('The Previos Figure Shows That To Us:')
    st.write("   -the relation between price and fuel which shows us that:")
    st.write("    1-the top type of fuels has been sold is Diesel with total price equal (88000)")
    st.write("    2-and the lowest sold is Ethanol with total price equal (4900) ")

     