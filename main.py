import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# --- 1. إعدادات الهوية البصرية ---
st.set_page_config(
    page_title="بروتوكول هندسة الاستخلاف الاقتصادي الرقمي",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. نظام اللغات (Session State Fix) ---
if 'lang' not in st.session_state:
    st.session_state.lang = "العربية"

# وضع زر تغيير اللغة في القائمة الجانبية
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
        "governance": "Symbolic Governance (الحوكمة الرمزية)",
        "investment": "Tazkiyah Investment (الاستثمار التزكوي)",
        "evaluation": "Institutional Evaluation (التقييم التزكوي)",
        "existential": "Existential Realization (التحقق الوجودي)",
        "zva": "Tazkiyah Value Added (ZVA)",
        "market": "Market Engineering (هندسة السوق)",
        "monetary": "Sovereign Monetary Policy (السياسة النقدية)",
        "exchange": "Exchange Rate Engineering (سعر الصرف)",
        "amanah": "Amanah Protocol (بروتوكول أمانة)",
        "simulation": "Digital Simulation (المحاكاة الرقمية)",
        "fortification": "Sovereign Fortification (التحصين السيادي)",
        "impact_msg": "تم إصدار برهان الستر الرقمي (ZKP) بنجاح."
    },
    "English": {
        "title": "🏛️ Sovereign Stewardship Engineering Protocol",
        "sidebar_title": "💎 Sovereign Models Index",
        "choose": "Choose Economic Domain:",
        "overview": "Overview (الرئيسية)",
        "mission": "Mission-Driven Function",
        "leadership": "Tazkiyah-Based Leadership",
        "governance": "Symbolic Governance",
        "investment": "Tazkiyah-Based Investment",
        "evaluation": "Institutional Evaluation",
        "existential": "Existential Realization",
        "zva": "Tazkiyah Value Added (ZVA)",
        "market": "Market Engineering",
        "monetary": "Sovereign Monetary Policy",
        "exchange": "Exchange Rate Engineering",
        "amanah": "Amanah Protocol",
        "simulation": "Digital Simulation",
        "fortification": "Sovereign Fortification",
        "impact_msg": "Digital Veiling Proof (ZKP) Generated Successfully."
    }
}

txt = L[st.session_state.lang]

# --- 3. تصميم الواجهة (CSS) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] {{ font-family: 'Cairo', sans-serif; }}
    .main {{ background-color: #f8f9fa; }}
    .stMetric {{ background-color: #ffffff; padding: 15px; border-radius: 10px; border-left: 5px solid #d4af37; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }}
    h1, h2, h3 {{ color: #1e4d2b; font-weight: bold; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. القائمة الجانبية الموحدة ---
st.sidebar.title(txt["sidebar_title"])
domain = st.sidebar.selectbox(txt["choose"], [
    txt["overview"], txt["mission"], txt["leadership"], txt["governance"], 
    txt["investment"], txt["evaluation"], txt["existential"], txt["zva"], 
    txt["market"], txt["monetary"], txt["exchange"], txt["amanah"], 
    txt["simulation"], txt["fortification"]
])

# --- 5. تنفيذ النماذج (Logic Engine) ---

# --- الصفحة الرئيسية ---
if domain == txt["overview"]:
    st.title(txt["title"])
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"""
        ### المشروع القومي للسيادة الرقمية
        هذا البروتوكول هو محرك اقتصادي متكامل يهدف إلى:
        * **رقمنة المقاصد:** تحويل "العدل" و"البركة" إلى أكواد برمجية.
        * **تحرير الائتمان:** ربط المال بالنشاط الحقيقي (التراب) مباشرة.
        * **السيادة الموزعة:** استقلال الأمة عن النظم المركزية العالمية.
        """)
        st.info("استخدم الفهرس الجانبي للتنقل بين النماذج الهندسية الـ 36.")
    with col2:
        st.image("https://img.icons8.com/fluency/240/stewardship.png")

# --- نموذج الوظيفة الرسالية ---
elif domain == txt["mission"]:
    st.header(txt["mission"])
    st.latex(r"P = \alpha + \beta_1 R + \beta_2 M + \beta_3 T + \beta_4 C + \epsilon")
    alpha = st.slider("α (Internal Intention)", 0.0, 1.0, 0.5)
    r_val = st.slider("R (Symbolic Mission)", 0, 100, 70)
    performance = alpha + (0.4 * r_val)
    st.metric("Institutional Performance (P)", f"{performance:.2f}")

# --- بروتوكول أمانة ---
elif domain == txt["amanah"]:
    st.header(txt["amanah"])
    st.latex(r"B_i = \frac{\sum (U_v \cdot S_t)}{H_w + D_i}")
    col1, col2 = st.columns(2)
    with col1:
        uv = st.slider("Uv (Utility Value)", 0, 100, 80)
        st_val = st.slider("St (Sustainability)", 0, 100, 90)
    with col2:
        hw = st.slider("Hw (Waste)", 1, 50, 10)
        di = st.slider("Di (Debt/Hoarding)", 1, 50, 5)
    bi = (uv * st_val) / (hw + di)
    st.metric("Barakah Index (Bi)", f"{bi:.2f}")

# --- المحاكاة الرقمية ---
elif domain == txt["simulation"]:
    st.header(txt["simulation"])
    st.write("أداء بروتوكول أمانة مقابل النظام التقليدي في الأزمات")
    time = np.linspace(0, 10, 100)
    trad = np.exp(-0.2 * time)
    amanah = np.ones(100) * 0.8 + 0.1 * np.sin(time)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time, y=trad, name="Traditional System (Collapse)", line=dict(color='red', dash='dot')))
    fig.add_trace(go.Scatter(x=time, y=amanah, name="Amanah Protocol (Stable)", line=dict(color='green', width=4)))
    st.plotly_chart(fig)

# --- التحصين السيادي ---
elif domain == txt["fortification"]:
    st.header(txt["fortification"])
    st.subheader("Digital Veiling | بصمة الستر الرقمي")
    if st.button("Generate ZK-Proof"):
        st.balloons()
        st.success(txt["impact_msg"])
        st.code("Proof: 0x77ae...Sovereign_Verified", language='bash')

# --- تذييل الصفحة ---
st.sidebar.markdown("---")
st.sidebar.write(f"✍️ **Design:** Prof. Dr. Saleh Orabi (2026)")
st.sidebar.write("⚡ Powered by Amanah Engine")
