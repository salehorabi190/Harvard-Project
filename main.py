import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- 1. إعدادات الهوية والسيادة ---
st.set_page_config(page_title="Stewardship Engineering | هندسة الاستخلاف", layout="wide")

# --- 2. نظام اللغات (Bilingual Logic) ---
if 'lang' not in st.session_state:
    st.session_state.lang = "العربية"

st.sidebar.title("🌐 Language / اللغة")
selected_lang = st.sidebar.radio("", ["العربية", "English"], index=0 if st.session_state.lang == "العربية" else 1)
st.session_state.lang = selected_lang

T = {
    "العربية": {
        "title": "🏛️ بروتوكول هندسة الاستخلاف الاقتصادي الرقمي",
        "choose": "اختر نموذج الدراسة:",
        "about": "💡 التفسير الفلسفي والهندسي للموديل",
        "usage": "📌 فيما تستخدم هذه المعادلة؟",
        "sidebar_info": "تصميم: أ.د. صالح عرابي (2026)",
        "mission_desc": "هذه المعادلة تحول 'النية' إلى محرك أداء مادي. تستخدم لتقليل تكاليف الرقابة عبر رفع الوازع القيمي والرسالة.",
        "leadership_desc": "تستخدم لقياس جودة القيادة التزكوية وأثرها في استقرار المؤسسة، حيث البركة نتاج لصفاء النية والقدوة.",
    },
    "English": {
        "title": "🏛️ Sovereign Stewardship Engineering Protocol",
        "choose": "Choose Research Model:",
        "about": "💡 Philosophy & Engineering Logic",
        "usage": "📌 Model Application:",
        "sidebar_info": "Designed by: Prof. Saleh Orabi (2026)",
        "mission_desc": "This equation transforms 'Intention' into a performance driver. Used to reduce monitoring costs by enhancing Mission and Meaning.",
        "leadership_desc": "Used to measure Tazkiyah-based leadership quality and its impact on stability.",
    }
}
txt = T[st.session_state.lang]

# --- 3. تصميم الواجهة (CSS) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] {{ font-family: 'Cairo', sans-serif; text-align: {'right' if st.session_state.lang == "العربية" else 'left'}; }}
    .stMetric {{ background-color: #ffffff; border-radius: 12px; padding: 20px; border-right: 8px solid #1e4d2b; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }}
    .about-box {{ background-color: #e8f5e9; padding: 20px; border-radius: 12px; border-{'right' if st.session_state.lang == "العربية" else 'left'}: 10px solid #1e4d2b; line-height: 1.8; color: #11301a; margin-bottom: 20px; }}
    .header-style {{ color: #1e4d2b; font-weight: bold; border-bottom: 2px solid #d4af37; padding-bottom: 10px; margin-bottom: 20px; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. القائمة الجانبية ---
st.sidebar.title(txt["choose"])
menu = {
    "1. نموذج الوظيفة الرسالية (Pᵣ)": "mission",
    "2. نموذج القيادة المتزكية (Eᵣ)": "leadership",
    "3. نموذج القيمة المضافة (ZVA)": "zva",
}
choice_key = st.sidebar.selectbox("", list(menu.keys()))
model_key = menu[choice_key]

# --- 5. تنفيذ النماذج مع الأسماء العربية للمؤشرات ---

if model_key == "mission":
    st.markdown(f"<h1 class='header-style'>نموذج الوظيفة الرسالية - Mission-Driven Function</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    
    col1, col2 = st.columns([1.2, 1])
    with col1:
        a = st.slider("النية الداخلية (α)", 0.0, 1.0, 0.8)
        rr = st.slider("الرسالة الرمزية (Rᵣ)", 0, 100, 70)
        mr = st.slider("المعنى والانتماء (Mᵣ)", 0, 100, 75)
        tr = st.slider("التزكية الزمنية (Tᵣ)", 0, 100, 60)
        cr = st.slider("التواصل الرمزي (Cᵣ)", 0, 100, 65)
        st.metric("الأداء الوظيفي الرمزي (Pᵣ)", f"{a + (0.4*rr) + (0.3*mr) + (0.2*tr) + (0.1*cr):.2f}")
    with col2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>{txt['mission_desc']}</div>", unsafe_allow_html=True)

elif model_key == "leadership":
    st.markdown(f"<h1 class='header-style'>نموذج القيادة المتزكية - Tazkiyah Leadership</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \beta_4 C_r + \beta_5 V_r + \beta_6 R_r + \epsilon_r")
    
    col1, col2 = st.columns([1.2, 1])
    with col1:
        zr = st.slider("تزكية القائد (Zᵣ)", 0, 100, 85)
        ir = st.slider("الإلهام الرمزي (Iᵣ)", 0, 100, 80)
        vr = st.slider("توافق القيم (Vᵣ)", 0, 100, 75)
        rr_l = st.slider("تجسيد الرسالة (Rᵣ)", 0, 100, 90)
        st.metric("الأثر المؤسسي المتزكي (Eᵣ)", f"{(zr*0.4 + ir*0.3 + vr*0.1 + rr_l*0.2):.2f}")
    with col2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>{txt['leadership_desc']}</div>", unsafe_allow_html=True)

elif model_key == "zva":
    st.markdown(f"<h1 class='header-style'>نموذج القيمة التزكوية المضافة - ZVA</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    
    col1, col2 = st.columns([1.2, 1])
    with col1:
        eva = st.number_input("القيمة الاقتصادية التقليدية (EVA)", value=50000)
        z = st.slider("مؤشر التزكية (Z)", 0, 100, 90)
        lam = st.slider("معامل تحويل التزكية (λ)", 0.5, 2.0, 1.2)
        st.metric("إجمالي القيمة المضافة (ZVA)", f"{eva + (lam * z * 100):,.2f}")
    with col2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>{T['العربية']['zva_desc']}</div>", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.write(txt["sidebar_info"])
