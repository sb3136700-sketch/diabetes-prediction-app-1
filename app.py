import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="DIABETES PREDICTION",
    layout="wide"
)

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
st.markdown("<div class='sub-title'>Professional Health Risk Analysis System</div>", unsafe_allow_html=True)
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

# ---------------- PREDICTION ----------------
if predict_btn:

    st.subheader("🩺 Health Analysis Report")

    # ---- Blood Glucose & HbA1c ----
if glucose >= 200 or hba1c >= 8:
    st.error("🚨 Blood Glucose: HIGH RISK (DIABETIC RANGE)")
    if 7 <= hba1c < 8:
        st.warning("⚠️ Blood Glucose: MEDIUM RISK")
elif 140 <= glucose < 200 or 5.7 <= hba1c < 7:
    st.warning("⚠️ Blood Glucose: PREDIABETES")

elif 100 <= glucose < 140:
    st.info("ℹ️ Blood Glucose: BORDERLINE")

else:
    st.success("✅ Blood Glucose: NORMAL")

    # ---- Blood Pressure ----
    if systolic < 90 or diastolic < 60:
        st.warning("⚠️ Blood Pressure: LOW BP")
    elif systolic > 140 or diastolic > 90:
        st.error("⚠️ Blood Pressure: HIGH BP")
    else:
        st.success("✅ Blood Pressure: NORMAL")

    # ---- Cholesterol ----
    if cholesterol >= 240:
        st.error("⚠️ Cholesterol Level: HIGH")
    elif 200 <= cholesterol < 240:
        st.warning("⚠️ Cholesterol Level: BORDERLINE HIGH")
    else:
        st.success("✅ Cholesterol Level: NORMAL")

    # ---- Overall Health ----
    if (glucose >= 200 or hba1c >= 6.5) or systolic > 140 or cholesterol >= 240:
        st.error("🚨 Overall Health: NEEDS MEDICAL ATTENTION")
    else:
        st.success("💚 Overall Health: GOOD CONDITION")

# ---------------- RESET ----------------
if reset_btn:
    st.experimental_rerun()

st.markdown("<hr>", unsafe_allow_html=True)


