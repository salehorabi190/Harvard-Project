import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- 1. إعدادات الهوية والسيادة ---
st.set_page_config(page_title="Stewardship Engineering | هندسة الاستخلاف", layout="wide")

# --- 2. نظام اللغات (Bilingual Logic) ---
if 'lang' not in st.session_state:
    st.session_state.lang = "العربية"

st.sidebar.title("🌐 Language / اللغة")
selected_lang = st.sidebar.radio("", ["العربية", "English"], 
                                 index=0 if st.session_state.lang == "العربية" else 1)
st.session_state.lang = selected_lang

# قاموس النصوص (Translation Dictionary)
T = {
    "العربية": {
        "title": "🏛️ بروتوكول هندسة الاستخلاف الاقتصادي الرقمي",
        "choose": "اختر نموذج الدراسة:",
        "about": "💡 التفسير الفلسفي والهندسي للموديل",
        "usage": "📌 فيما تستخدم هذه المعادلة؟",
        "sidebar_info": "تصميم: أ.د. صالح عرابي (2026)",
        "mission_desc": "هذه المعادلة تحول 'النية' إلى محرك أداء مادي. تستخدم لتقليل تكاليف الرقابة عبر رفع الوازع القيمي (R) والمعنى (M).",
        "leadership_desc": "تستخدم لقياس جودة القيادة التزكوية وأثرها في استقرار المؤسسة، حيث البركة (ε) نتاج لصفاء النية (α).",
        "zva_desc": "تستخدم كبديل سيادي لمؤشر EVA التقليدي، لدمج القيمة الأخلاقية (λZ) في تقييم المشاريع القومية.",
    },
    "English": {
        "title": "🏛️ Sovereign Stewardship Engineering Protocol",
        "choose": "Choose Research Model:",
        "about": "💡 Philosophy & Engineering Logic",
        "usage": "📌 Model Application:",
        "sidebar_info": "Designed by: Prof. Saleh Orabi (2026)",
        "mission_desc": "This equation transforms 'Intention' into a material performance driver. Used to reduce monitoring costs by enhancing Mission (R) and Meaning (M).",
        "leadership_desc": "Used to measure Tazkiyah-based leadership quality and its impact on stability, where Barakah (ε) is a result of Intention (α).",
        "zva_desc": "Used as a sovereign alternative to traditional EVA, integrating ethical value (λZ) into project evaluation.",
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
    "1. Mission-Driven (Pᵣ)": "mission",
    "2. Leadership (Eᵣ)": "leadership",
    "3. ZVA Value": "zva",
    "4. Governance (Gᵣ)": "governance",
}
choice_key = st.sidebar.selectbox("", list(menu.keys()))
model_key = menu[choice_key]

# --- 5. تنفيذ النماذج مع الشرح ---

# نموذج الوظيفة الرسالية
if model_key == "mission":
    st.markdown(f"<h1 class='header-style'>{txt['title']} - Pᵣ</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    
    col1, col2 = st.columns([1, 1.2])
    with col1:
        rr = st.slider("Rᵣ (Mission/الرسالة)", 0, 100, 70)
        mr = st.slider("Mᵣ (Meaning/المعنى)", 0, 100, 75)
        st.metric("Pᵣ Output", f"{0.4*rr + 0.3*mr + 15:.2f}")
    with col2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>{txt['mission_desc']}</div>", unsafe_allow_html=True)

# نموذج القيادة المتزكية
elif model_key == "leadership":
    st.markdown(f"<h1 class='header-style'>{txt['title']} - Eᵣ</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \beta_4 C_r + \epsilon_r")
    
    col1, col2 = st.columns([1, 1.2])
    with col1:
        zr = st.slider("Zᵣ (Tazkiyah/التزكية)", 0, 100, 85)
        st.metric("Eᵣ Impact", f"{zr * 1.25:.2f}")
    with col2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>{txt['leadership_desc']}</div>", unsafe_allow_html=True)

# نموذج ZVA
elif model_key == "zva":
    st.markdown(f"<h1 class='header-style'>{txt['title']} - ZVA</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    
    col1, col2 = st.columns([1, 1.2])
    with col1:
        z_val = st.slider("Z (Moral/التزكية)", 0, 100, 90)
        lam = st.slider("λ (Conversion/معامل التحويل)", 0.5, 2.0, 1.2)
        st.metric("ZVA Result", f"{500 + (lam * z_val):.2f}")
    with col2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>{txt['zva_desc']}</div>", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.write(txt["sidebar_info"])
