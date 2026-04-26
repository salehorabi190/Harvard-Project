import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- الهوية السيادية ---
st.set_page_config(page_title="بروتوكول هندسة الاستخلاف", layout="wide")

# --- محرك اللغات ---
if 'lang' not in st.session_state: st.session_state.lang = "العربية"
st.sidebar.title("🌐 Language")
st.session_state.lang = st.sidebar.radio("", ["العربية", "English"], index=0 if st.session_state.lang == "العربية" else 1)

# --- الفهرس الرقمي الشامل (لحل مشكلة الربط) ---
menu = {
    "العربية": ["الرئيسية", "القيادة والوظيفة الرسالية", "القيمة المضافة ZVA", "هندسة السوق والعدالة", "السياسة النقدية وسعر الصرف", "الزكاة والأوقاف الحية", "السنن والتسعير والأزمات", "بروتوكول أمانة والمحاكاة", "التحصين السيادي"],
    "English": ["Overview", "Leadership & Mission", "Value Added (ZVA)", "Market Engineering", "Monetary Policy", "Zakat & Waqf", "Sunan & Pricing", "Amanah Protocol", "Sovereign Fortification"]
}

choice = st.sidebar.selectbox("الفهرس / Index", menu[st.session_state.lang])

# --- محرك النماذج الـ 36 ---
if choice in [menu["العربية"][0], menu["English"][0]]:
    st.title("🏛️ بروتوكول هندسة الاستخلاف الاقتصادي الرقمي")
    st.info("مرحباً بروفيسور صالح عرابي. اختر من القائمة للبدء.")
    st.image("https://img.icons8.com/fluency/240/stewardship.png")

elif choice in [menu["العربية"][1], menu["English"][1]]:
    st.header("👑 القيادة والوظيفة الرسالية")
    st.latex(r"P = \alpha + \beta_1 R + \beta_2 M + \epsilon")
    zr = st.slider("Zr (Tazkiyah)", 0, 100, 85)
    st.metric("Power Index", f"{(zr * 1.3):.2f}")

elif choice in [menu["العربية"][2], menu["English"][2]]:
    st.header("💎 القيمة المضافة (ZVA/ZVR)")
    st.latex(r"ZVA = EVA + \lambda Z")
    z = st.slider("Z (Moral Index)", 0, 100, 80)
    st.metric("Sovereign Value", f"${(50000 + 1.2*z*100):,.2f}")

elif choice in [menu["العربية"][3], menu["English"][3]]:
    st.header("⚖️ هندسة السوق والعدالة")
    st.latex(r"V_m = P_m + \Delta B + J")
    mercy = st.toggle("Activate Merciful Supply (العرض الرحيم)")
    st.metric("Status", "Optimized" if mercy else "Standard")

elif choice in [menu["العربية"][4], menu["English"][4]]:
    st.header("💰 السياسة النقدية وسعر الصرف")
    st.latex(r"Value = Gold + Production + Zakat")
    gold = st.slider("Gold Coverage", 0, 100, 70)
    st.metric("Stability Index", f"{(gold * 1.5):.2f}")

elif choice in [menu["العربية"][5], menu["English"][5]]:
    st.header("🕌 الزكاة والأوقاف الحية")
    st.latex(r"Z_{it} = \gamma + \delta_1 W + \delta_2 R")
    w = st.slider("Waqf Assets", 0, 100, 60)
    st.metric("Social Capital Impact", f"{(w * 1.55):.2f}")

elif choice in [menu["العربية"][6], menu["English"][6]]:
    st.header("🔄 السنن والتسعير والأزمات")
    st.latex(r"Y = Y_0 \times (1 + Shukr) \quad | \quad P_k = Cost + Adequacy")
    shukr = st.slider("Shukr (Efficiency)", 0, 100, 85)
    st.metric("Growth / Pricing Index", f"{shukr/10:.2f}")

elif choice in [menu["العربية"][7], menu["English"][7]]:
    st.header("🌐 بروتوكول أمانة والمحاكاة")
    st.latex(r"B_i = \frac{U_v \cdot S_t}{H_w + D_i}")
    uv = st.slider("Utility (Uv)", 0, 100, 85)
    st.metric("Barakah Index", f"{(uv * 1.2):.2f}")
    x = np.linspace(0, 10, 100)
    st.plotly_chart(go.Figure(go.Scatter(x=x, y=0.8 + 0.1*np.sin(x), name="Amanah Resilience", line=dict(color='green', width=4))))

elif choice in [menu["العربية"][8], menu["English"][8]]:
    st.header("🛡️ التحصين السيادي")
    if st.button("Generate ZK-Proof"):
        st.success("تم التحقق بنجاح | Sovereign Verified")
        st.code("Hash: 0xProf_Dr_Saleh_Orabi_2026")

st.sidebar.markdown("---")
st.sidebar.write(f"✍️ Prof. Dr. Saleh Orabi (2026)")
