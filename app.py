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
    color: #0A2647;
}
.sub-title {
    text-align: center;
    color: #555;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}
.stButton>button {
    width: 100%;
    height: 55px;
    font-size: 18px;
    border-radius: 10px;
}
.predict {
    background-color: #0A2647;
    color: white;
}
.reset {
    background-color: #888;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<div class='main-title'>🩺 DIABETES PREDICTION</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Professional Health Risk Analysis System</div>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ---------------- INPUT SECTION ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
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

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ---------------- BUTTONS ----------------
colA, colB, colC = st.columns(3)

with colA:
    predict_btn = st.button("🔍 Predict Risk")

with colB:
    preview_btn = st.button("👁 Preview Input")

with colC:
    reset_btn = st.button("🔄 Reset")

# ---------------- PREDICTION ----------------
if predict_btn:

    st.subheader("🩺 Health Analysis Report")

    # ---- Diabetes Check ----
    if glucose >= 140 or hba1c >= 6.5:
        st.error("⚠️ Blood Glucose: HIGH RISK")
    elif 100 <= glucose < 140:
        st.warning("⚠️ Blood Glucose: PREDIABETES")
    else:
        st.success("✅ Blood Glucose: Excellent")

    # ---- Blood Pressure Check ----
    if systolic < 90 or diastolic < 60:
        st.warning("⚠️ Blood Pressure: LOW BP")
    elif systolic > 140 or diastolic > 90:
        st.error("⚠️ Blood Pressure: HIGH BP")
    else:
        st.success("✅ Blood Pressure: NORMAL")

    # ---- Cholesterol Check ----
    if cholesterol >= 240:
        st.error("⚠️ Cholesterol Level: HIGH")
    elif 200 <= cholesterol < 240:
        st.warning("⚠️ Cholesterol Level: BORDERLINE HIGH")
    else:
        st.success("✅ Cholesterol Level: NORMAL")

    # ---- Overall Health Summary ----
    if (glucose >= 140 or hba1c >= 6.5) or systolic > 140 or cholesterol >= 240:
        st.error("🚨 Overall Health: NEEDS MEDICAL ATTENTION")
    else:
        st.success("💚 Overall Health: GOOD CONDITION")

# ---------------- RESET ----------------
if reset_btn:
    st.experimental_rerun()
# ---------------- EXTRA INFO ----------------
st.markdown("<hr>", unsafe_allow_html=True)
#st.info("⚠️ This application is designed for academic demonstration only.")





