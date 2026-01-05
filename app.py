import streamlit as st
import pickle
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="DIABETES PREDICTION",
    layout="wide"
)

# ---------------- LOAD ML MODEL ----------------
with open("diabetes_model.pkl", "rb") as file:
    model = pickle.load(file)

# ---------------- CSS STYLE ----------------
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}
.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #fff;
}
.sub-title {
    text-align: center;
    color: #fff;
}
.stButton>button {
    width: 100%;
    height: 55px;
    font-size: 18px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<div class='main-title'>🩺 DIABETES PREDICTION</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Machine Learning Based Health Risk Analysis</div>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ---------------- INPUT SECTION ----------------
st.subheader("📋 Patient Details")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age (Years)", 1, 120)
    glucose = st.number_input("Glucose Level (mg/dL)", 50, 400)

with col2:
    hba1c = st.number_input("HbA1c (%)", 3.0, 15.0)
    cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 400)

with col3:
    systolic = st.number_input("Systolic BP (mmHg)", 80, 200)
    diastolic = st.number_input("Diastolic BP (mmHg)", 40, 140)

# ---------------- BUTTONS ----------------
colA, colB, colC = st.columns(3)

with colA:
    predict_btn = st.button("🔍 Predict Risk")

with colB:
    preview_btn = st.button("👁 Preview Input")

with colC:
    reset_btn = st.button("🔄 Reset")

# ---------------- PREVIEW ----------------
if preview_btn:
    st.info(f"""
    👤 Age: {age}  
    🧪 Glucose: {glucose}  
    🩸 HbA1c: {hba1c}  
    🧬 Cholesterol: {cholesterol}  
    💓 BP: {systolic}/{diastolic}
    """)

# ---------------- ML PREDICTION ----------------
if predict_btn:

    st.subheader("🧠 Machine Learning Prediction")

    # ⚠️ ORDER MUST MATCH TRAINING
    input_data = np.array([[age, glucose, hba1c, cholesterol, systolic, diastolic]])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    if prediction[0] == 1:
        st.error(f"🚨 DIABETES DETECTED (Risk: {probability[0][1]*100:.1f}%)")
    else:
        st.success(f"✅ NO DIABETES (Risk: {probability[0][0]*100:.1f}%)")

    st.markdown("---")
    st.subheader("📊 Health Parameter Analysis")

    # ---- Blood Glucose & HbA1c (Support Info) ----
    if hba1c >= 8:
        st.error("🚨 HbA1c: HIGH RISK")
    elif 7 <= hba1c < 8:
        st.warning("⚠️ HbA1c: MEDIUM RISK")
    elif 5.7 <= hba1c < 7:
        st.warning("⚠️ HbA1c: PREDIABETES")
    else:
        st.success("✅ HbA1c: NORMAL")

    # ---- Blood Pressure ----
    if systolic < 90 or diastolic < 60:
        st.warning("⚠️ Blood Pressure: LOW BP")
    elif systolic > 140 or diastolic > 90:
        st.error("⚠️ Blood Pressure: HIGH BP")
    else:
        st.success("✅ Blood Pressure: NORMAL")

    # ---- Cholesterol ----
    if cholesterol >= 240:
        st.error("⚠️ Cholesterol: HIGH")
    elif 200 <= cholesterol < 240:
        st.warning("⚠️ Cholesterol: BORDERLINE HIGH")
    else:
        st.success("✅ Cholesterol: NORMAL")

# ---------------- RESET ----------------
if reset_btn:
    st.experimental_rerun()

st.markdown("<hr>", unsafe_allow_html=True)
st.info("⚠️ This application is for academic & educational purposes only.")
