import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- 1. إعدادات الهوية البصرية ---
st.set_page_config(page_title="بروتوكول هندسة الاستخلاف", page_icon="⚖️", layout="wide")

# --- 2. نظام اللغات ---
if 'lang' not in st.session_state: st.session_state.lang = "العربية"
selected_lang = st.sidebar.radio("Language / اللغة", ["العربية", "English"], index=0 if st.session_state.lang == "العربية" else 1)
st.session_state.lang = selected_lang

L = {
    "العربية": {
        "title": "🏛️ بروتوكول هندسة الاستخلاف الاقتصادي الرقمي",
        "sidebar_title": "💎 فهرس النماذج السيادية",
        "choose": "اختر نموذج الدراسة:",
        "overview": "الرئيسية (Overview)",
        "mission": "Mission-Driven Function (الوظيفة الرسالية)",
        "leadership": "Tazkiyah Leadership (القيادة المتزكية)",
        "zva": "Tazkiyah Value Added (ZVA)",
        "market": "Market Engineering (هندسة السوق)",
        "monetary": "Sovereign Monetary Policy (السياسة النقدية)",
        "amanah": "Amanah Protocol (بروتوكول أمانة)",
        "fortification": "Sovereign Fortification (التحصين السيادي)"
    },
    "English": {
        "title": "🏛️ Sovereign Stewardship Engineering Protocol",
        "sidebar_title": "💎 Sovereign Models Index",
        "choose": "Choose Economic Domain:",
        "overview": "Overview (الرئيسية)",
        "mission": "Mission-Driven Function",
        "leadership": "Tazkiyah-Based Leadership",
        "zva": "Tazkiyah Value Added (ZVA)",
        "market": "Market Engineering",
        "monetary": "Sovereign Monetary Policy",
        "amanah": "Amanah Protocol",
        "fortification": "Sovereign Fortification"
    }
}
txt = L[st.session_state.lang]

# --- 3. القائمة الجانبية ---
st.sidebar.title(txt["sidebar_title"])
domain = st.sidebar.selectbox(txt["choose"], list(txt.values())[3:])

# --- 4. محرك المعادلات الشامل ---

# 1. الوظيفة الرسالية
if domain in [txt["mission"]]:
    st.header(txt["mission"])
    st.latex(r"P = \alpha + \beta_1 R + \beta_2 M + \beta_3 T + \beta_4 C + \epsilon")
    r = st.slider("R (Symbolic Mission)", 0, 100, 70)
    m = st.slider("M (Meaning)", 0, 100, 80)
    st.metric("Performance Impact", f"{(0.4*r + 0.3*m + 20):.2f}")

# 2. القيادة المتزكية
elif domain in [txt["leadership"]]:
    st.header(txt["leadership"])
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \beta_4 C_r + \beta_5 V_r + \beta_6 R_r + \epsilon_r")
    zr = st.slider("Zr (Tazkiyah)", 0, 100, 80)
    rr = st.slider("Rr (Embodiment)", 0, 100, 70)
    fig = go.Figure(go.Scatterpolar(r=[zr, rr, 80, 70, 90], theta=['Tazkiyah', 'Embodiment', 'Inspiration', 'Values', 'Mission'], fill='toself'))
    st.plotly_chart(fig)

# 3. القيمة التزكوية المضافة
elif domain in [txt["zva"]]:
    st.header(txt["zva"])
    st.latex(r"ZVA = EVA + \lambda Z")
    eva = st.number_input("EVA", value=50000)
    lam = st.slider("λ (Conversion)", 0.0, 2.0, 1.2)
    z = st.slider("Z (Tazkiyah Index)", 0, 100, 80)
    st.metric("Total ZVA", f"{eva + (lam * z * 100):,.2f}")

# 4. هندسة السوق
elif domain in [txt["market"]]:
    st.header(txt["market"])
    st.latex(r"V_m = \alpha (P_m + \Delta B) + \beta Q_s + \gamma J")
    pm = st.slider("Pm (Material Price)", 100, 1000, 500)
    db = st.slider("ΔB (Barakah Coeff)", 1.0, 2.0, 1.3)
    st.metric("Sovereign Market Value", f"{pm * db:.2f}")

# 5. السياسة النقدية
elif domain in [txt["monetary"]]:
    st.header(txt["monetary"])
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 W + \beta_3 S + \beta_4 G + \beta_5 F - \beta_6 C - \beta_7 V + \epsilon")
    zakat = st.slider("Z (Zakat Flow)", 0, 100, 60)
    gold = st.slider("G (Gold Cover)", 0, 100, 50)
    st.metric("Currency Stability Index", f"{(20 + 0.3*zakat + 0.4*gold):.2f}")

# 6. بروتوكول أمانة
elif domain in [txt["amanah"]]:
    st.header(txt["amanah"])
    st.latex(r"B_i = \frac{\sum (U_v \cdot S_t)}{H_w + D_i}")
    uv = st.slider("Uv (Utility)", 0, 100, 80)
    di = st.slider("Di (Debt/Hoarding)", 1, 50, 5)
    st.metric("Barakah Index (Bi)", f"{(uv * 90 / (10 + di)):.2f}")

# 7. التحصين السيادي
elif domain in [txt["fortification"]]:
    st.header(txt["fortification"])
    st.subheader("Digital Veiling (ZK-Proofs)")
    if st.button("Generate Proof"):
        st.success(txt["impact_msg"])
        st.code("Proof: 0xSovereign_Saleh_Orabi_2026", language='bash')

# --- تذييل الصفحة ---
st.sidebar.markdown("---")
st.sidebar.write(f"✍️ **Design:** Prof. Dr. Saleh Orabi (2026)")
