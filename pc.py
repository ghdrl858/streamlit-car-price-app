import streamlit as st
import pandas as pd
import time

def main() :
    # sidebar에 selectbox 응용해서 만들기
    menu = ['Nike', 'Adidas', 'Vans', 'Converse']
    st.sidebar.selectbox("선택", menu)

    # sidebar에 radio + spinner 응용해서 만들기
    with st.sidebar :
        with st.spinner("Loading..."):
            time.sleep(5)
    st.sidebar.radio("Choice your favoirte shoes brand !",
    ["Nike", "Adidas", "Vans", "Converse"])

if __name__ =='__main__' :
    main()