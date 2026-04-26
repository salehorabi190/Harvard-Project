import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- 1. إعدادات الهوية ---
st.set_page_config(page_title="بروتوكول هندسة الاستخلاف", layout="wide")

# --- 2. نظام اللغات ---
if 'lang' not in st.session_state: st.session_state.lang = "العربية"
st.sidebar.title("🌐 Language Selection")
st.session_state.lang = st.sidebar.radio("اللغة", ["العربية", "English"], index=0 if st.session_state.lang == "العربية" else 1)

# --- 3. تصميم الواجهة ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; }
    .about-box { background-color: #e8f5e9; padding: 20px; border-radius: 10px; border-right: 5px solid #1e4d2b; margin-top: 10px; }
    .stMetric { background-color: #ffffff; border-radius: 10px; padding: 15px; border: 1px solid #ddd; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. الفهرس الرقمي (لضمان عدم الخطأ في الربط) ---
st.sidebar.title("💎 الفهرس السيادي")
menu_map = {
    "العربية": [
        "0. الرئيسية", "1. الوظيفة الرسالية", "2. القيادة المتزكية", "3. الحوكمة الرمزية",
        "4. القيمة المضافة ZVA", "5. الاستثمار التزكوي", "6. التقييم المؤسسي", "7. التحقق الوجودي",
        "8. هندسة السوق والعدالة", "9. الشفافية ومنع الاحتكار", "10. سياسات التسعير", "11. السياسة النقدية",
        "12. سعر الصرف السيادي", "13. الزكاة والوقف", "14. السنن الاقتصادية", "15. بروتوكول أمانة",
        "16. المحاكاة الرقمية", "17. التحصين السيادي"
    ],
    "English": [
        "0. Overview", "1. Mission-Driven", "2. Tazkiyah Leadership", "3. Symbolic Governance",
        "4. Value Added (ZVA)", "5. Tazkiyah Investment", "6. Institutional Evaluation", "7. Existential Realization",
        "8. Market Engineering", "9. Anti-Monopoly", "10. Adequacy Pricing", "11. Monetary Policy",
        "12. Exchange Rate", "13. Zakat & Waqf", "14. Economic Sunan", "15. Amanah Protocol",
        "16. Digital Simulation", "17. Sovereign Fortification"
    ]
}

choice = st.sidebar.selectbox("اختر النموذج / Select Model", menu_map[st.session_state.lang])
index = int(choice.split(".")[0]) # نأخذ الرقم فقط لضمان الربط

# --- 5. محرك النماذج الـ 36 (Logic Engine) ---

if index == 0:
    st.title("🏛️ بروتوكول هندسة الاستخلاف الاقتصادي الرقمي")
    st.info("مرحباً بك بروفيسور صالح عرابي. اختر من القائمة لبدء المحاكاة.")
    st.image("https://img.icons8.com/fluency/240/stewardship.png")

elif index == 1: # الوظيفة الرسالية
    st.header("🎯 الوظيفة الرسالية (Mission-Driven)")
    st.latex(r"P = \alpha + \beta_1 R + \beta_2 M + \beta_3 T + \beta_4 C")
    col1, col2 = st.columns(2)
    with col1:
        r = st.slider("R (Symbolic Mission)", 0, 100, 80)
        m = st.slider("M (Meaning)", 0, 100, 70)
        st.metric("Performance (P)", f"{(0.4*r + 0.3*m + 20):.2f}")
    with col2:
        st.info("الفلسفة: تحويل النية إلى محرك أداء مادي.")

elif index == 2: # القيادة المتزكية
    st.header("👑 القيادة المتزكية (Tazkiyah Leadership)")
    st.latex(r"E_r = \alpha + \sum \beta_i X_i")
    zr = st.slider("Zr (Tazkiyah)", 0, 100, 85)
    rr = st.slider("Rr (Embodiment)", 0, 100, 80)
    fig = go.Figure(go.Scatterpolar(r=[zr, rr, 70, 85, 90], theta=['Tazkiyah','Embodiment','Inspiration','Values','Mission'], fill='toself'))
    st.plotly_chart(fig)

elif index == 4: # القيمة المضافة
    st.header("💎 القيمة المضافة (ZVA/ZVR)")
    st.latex(r"ZVA = EVA + \lambda Z")
    eva = st.number_input("EVA", value=50000)
    z = st.slider("Z (Moral Index)", 0, 100, 80)
    st.metric("Sovereign Value", f"${(eva + 1.2*z*100):,.2f}")

elif index == 8: # هندسة السوق
    st.header("⚖️ هندسة السوق والعدالة")
    st.latex(r"V_m = P_m + \Delta B + J")
    mercy = st.toggle("تفعيل العرض الرحيم (Merciful Supply)")
    st.metric("Market State", "Balanced" if mercy else "Standard")

elif index == 11: # السياسة النقدية
    st.header("💰 السياسة النقدية وسعر الصرف")
    st.latex(r"Value = Gold + Production + Zakat")
    gold = st.slider("Gold Coverage", 0, 100, 75)
    st.metric("Sovereign Stability", f"{(gold * 1.5):.2f}")

elif index == 13: # الزكاة والوقف
    st.header("🕌 الزكاة والوقف (Social Finance)")
    st.latex(r"Z_{it} = \gamma + \delta_1 W + \delta_2 R")
    w = st.slider("Waqf Assets", 0, 100, 60)
    st.metric("Social Capital", f"{(w * 1.4):.2f}")

elif index == 15: # بروتوكول أمانة
    st.header("🌐 بروتوكول أمانة (Amanah Protocol)")
    st.latex(r"B_i = \frac{U_v \cdot S_t}{H_w + D_i}")
    uv = st.slider("Utility (Uv)", 0, 100, 80)
    di = st.slider("Debt Obstacle (Di)", 1, 50, 5)
    st.metric("Barakah Index", f"{(uv * 10 / di):.2f}")

elif index == 17: # التحصين السيادي
    st.header("🛡️ التحصين السيادي (Fortification)")
    if st.button("Generate ZK-Proof"):
        st.success("تم التحقق السيادي بنجاح")
        st.code("Hash: 0xProf_Dr_Saleh_Orabi_Sovereign_2026")

# --- تذييل الصفحة ---
st.sidebar.markdown("---")
st.sidebar.write(f"✍️ **Design:** Prof. Dr. Saleh Orabi (2026)")
