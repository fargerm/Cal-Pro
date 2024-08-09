import streamlit as st

# Function to perform the calculations
def calculate(operation, num1, num2):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        return num1 / num2

# Streamlit UI
st.title("Simple Calculator")

# User inputs
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])
num1 = st.number_input("Enter the first number", value=0.0, step=0.1)
num2 = st.number_input("Enter the second number", value=0.0, step=0.1)

# Perform the calculation
if st.button("Calculate"):
    if operation == "Divide" and num2 == 0:
        st.error("Division by zero is not allowed!")
    else:
        result = calculate(operation, num1, num2)
        st.success(f"The result is: {result}")
