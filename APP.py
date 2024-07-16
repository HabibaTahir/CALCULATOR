import streamlit as st
from ADDITION import add
from SUBTRACT import subtract
from MULTIPLICATION import multiply
from DIVISION import divide

st.title('Calculator')

num1 = st.number_input('Enter the first number')
operation = st.selectbox('Select operation', ('+', '-', '*', '/'))
num2 = st.number_input('Enter the second number')
if st.button('Calculate'):
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        result = 'Invalid operation'

    st.write(f'Your result is : {result}')
