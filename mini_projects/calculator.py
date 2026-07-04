import streamlit as st
import math 
st.title("Scientific Calculator")
user_input = st.number_input("Enter a number:- ", value=0.0)
operations = ["sin", "cos", "tan", "square", "mod", "log", "cube", "factorial", '+', '-', '*', '/']
choice = st.selectbox("Choose operation you want to perform:-", operations)
user_input2 = 0.0 
if choice in ['+', '-', '*', '/', 'mod']: 
    user_input2 = st.number_input("Enter second number:- ", value=0.0) 
if st.button("Calculate"):
    result = None
    try:
        if choice == "sin":
            result = math.sin(user_input)
        elif choice == "cos":
            result = math.cos(user_input)
        elif choice == "tan":
            result = math.tan(user_input)
        elif choice == "square":
            result = user_input ** 2
        elif choice == "cube":
            result = user_input ** 3
        elif choice == "factorial":
            result = math.factorial(int(user_input)) if user_input >= 0 else "Error (Negative Factorial)"
        elif choice == "log":
            result = math.log(user_input) if user_input > 0 else "Error (Log of 0 or Negative)"
        elif choice == "mod":
            result = user_input % user_input2 if user_input2 != 0 else "Error (Modulo by Zero)"
        elif choice == "+":
            result = user_input + user_input2
        elif choice == "-":
            result = user_input - user_input2
        elif choice == "*":
            result = user_input * user_input2
        elif choice == "/":
            result = user_input / user_input2 if user_input2 != 0 else "Error (Division by Zero)"
        if isinstance(result, str) and result.startswith("Error"):
            st.error(result)
        else:
            st.success(f"Result : {result}")
    except Exception as e:
        st.error(f"A mathematical error occurred: {e}")
