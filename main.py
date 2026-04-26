import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- 1. إعدادات الهوية السيادية ---
st.set_page_config(page_title="بروتوكول هندسة الاستخلاف الاقتصادي الرقمي", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; }
    .stMetric { background-color: #ffffff; border-radius: 12px; padding: 20px; border-right: 8px solid #1e4d2b; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .about-box { background-color: #e8f5e9; padding: 20px; border-radius: 12px; border-right: 10px solid #1e4d2b; line-height: 1.8; color: #11301a; margin-bottom: 20px; }
    .header-style { color: #1e4d2b; font-weight: bold; border-bottom: 2px solid #d4af37; padding-bottom: 10px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. محرك الفهرس الرقمي ---
st.sidebar.title("🏛️ النماذج التطبيقية والمؤسساتية")
st.sidebar.write("Prof. Dr. Saleh Orabi")

menu = {
    "1. نموذج الوظيفة الرسالية (Pᵣ)": "mission",
    "2. نموذج القيادة المتزكية (Eᵣ)": "leadership",
    "3. نموذج الحوكمة الرمزية (Gᵣ)": "governance",
    "4. نموذج الاستثمار التزكوي (Rᵣ)": "investment",
    "5. نموذج التقييم التزكوي (Qᵣ)": "evaluation",
    "6. نموذج التحقق الوجودي (Vᵣ)": "existential",
    "7. القيمة التزكوية المضافة (ZVA)": "zva"
}

choice = st.sidebar.selectbox("اختر النموذج الدراسي:", list(menu.keys()))
model_key = menu[choice]

# --- 3. عرض النماذج ---

if model_key == "mission":
    st.markdown("<h1 class='header-style'>نموذج الوظيفة الرسالية (The Mission-Driven Function)</h1>", unsafe_allow_html=True)
    st.markdown("<div class='about-box'>التمثيل الوظيفي للرسالة الرمزية للمؤسسة، حيث تُترجم النية الروحية إلى غايات قابلة للقياس.</div>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    
    col1, col2 = st.columns(2)
    with col1:
        alpha = st.slider("α (النية الداخلية)", 0.0, 1.0, 0.8)
        rr = st.slider("Rᵣ (الرسالة الرمزية)", 0, 100, 70)
        performance = alpha + (0.4 * rr) + 15 
        st.metric("الأداء الوظيفي الرمزي (Pᵣ)", f"{performance:.2f}")

elif model_key == "leadership":
    st.markdown("<h1 class='header-style'>نموذج القيادة المتزكية (Tazkiyah-Based Leadership)</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \beta_4 C_r + \beta_5 V_r + \beta_6 R_r + \epsilon_r")
    zr = st.slider("Zᵣ (تزكية القائد)", 0, 100, 85)
    st.metric("الأثر المؤسسي المتزكي (Eᵣ)", f"{zr * 1.2:.2f}")

elif model_key == "zva":
    st.markdown("<h1 class='header-style'>القيمة التزكوية المضافة (Tazkiyah Value Added - ZVA)</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    col1, col2 = st.columns(2)
    with col1:
        eva = st.slider("EVA (القيمة الاقتصادية التقليدية)", 0, 1000, 500)
        z = st.slider("Z (مؤشر التزكية)", 0, 100, 80)
        lam = st.slider("λ (معامل التحويل)", 0.5, 2.0, 1.2)
    with col2:
        zva = eva + (lam * z)
        st.metric("إجمالي القيمة التزكوية (ZVA)", f"{zva:.2f}", delta=f"{lam*z:.2f} (أثر البركة)")

# يمكنك إضافة بقية الـ elif هنا بنفس النمط

# --- تذييل الصفحة ---
st.sidebar.markdown("---")
st.sidebar.write("⚡ تم برمجة النماذج وفقاً لمعادلات البروفيسور صالح عرابي")
