import streamlit as st

class Button:
    def __init__(self, num):
        if st.button(f"Button Number is {num}"):
            self.calc(num)


    def calc (self, num):
        if num % 2 ==0:
            st.snow()
        else:
            st.balloons()

for i in range(10):
    Button(i)