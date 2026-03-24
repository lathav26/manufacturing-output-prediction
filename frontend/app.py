import streamlit as st
import sys
import os

# Backend path fix
current_dir = os.path.dirname(__file__)
backend_path = os.path.join(current_dir, "..", "backend")
sys.path.append(backend_path)

from predict import predict_output

# Page config
st.set_page_config(page_title="Manufacturing Prediction", layout="wide")

# Sidebar (left panel)
st.sidebar.title("⚙ Equipment Parameters")

temp = st.sidebar.number_input("Injection Temperature (°C)", value=200.0)
pressure = st.sidebar.number_input("Injection Pressure", value=120.0)
cycle = st.sidebar.number_input("Cycle Time", value=30.0)
cooling = st.sidebar.number_input("Cooling Time", value=10.0)
viscosity = st.sidebar.number_input("Material Viscosity", value=250.0)
ambient = st.sidebar.number_input("Ambient Temperature", value=25.0)
machine_age = st.sidebar.number_input("Machine Age", value=5.0)
operator_exp = st.sidebar.number_input("Operator Experience", value=50.0)
maintenance = st.sidebar.number_input("Maintenance Hours", value=20.0)

# Main UI
st.title("🏭 Manufacturing Equipment Output Prediction")
st.write("Predict the number of units produced based on machine parameters.")

st.subheader("📊 Current Input Parameters")
st.write(f"• Temperature: {temp} °C")
st.write(f"• Pressure: {pressure}")
st.write(f"• Cycle Time: {cycle}")
st.write(f"• Cooling Time: {cooling}")
st.write(f"• Viscosity: {viscosity}")
st.write(f"• Ambient Temperature: {ambient}")
st.write(f"• Machine Age: {machine_age}")
st.write(f"• Operator Experience: {operator_exp}")
st.write(f"• Maintenance Hours: {maintenance}")

# Predict button
if st.button("🔮 Predict Output"):
    data = [
        temp, pressure, cycle, cooling,
        viscosity, ambient, machine_age,
        operator_exp, maintenance
    ]

    result = predict_output(data)

    st.success("✅ Prediction retrieved successfully!")

    st.subheader("📈 Predicted Output")
    st.metric(label="Parts Produced Per Hour", value=f"{result:.2f}")