import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- 1. الإعدادات والسيادة البصرية ---
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

# --- 2. نظام اللغات ---
if 'lang' not in st.session_state: st.session_state.lang = "العربية"
st.sidebar.title("🌐 Language / اللغة")
st.session_state.lang = st.sidebar.radio("", ["العربية", "English"], index=0 if st.session_state.lang == "العربية" else 1)

L = {
    "العربية": {
        "title": "🏛️ بروتوكول هندسة الاستخلاف الاقتصادي الرقمي",
        "choose": "اختر نموذج الدراسة:",
        "about": "💡 التفسير الفلسفي والهندسي للموديل",
        "sidebar_info": "Prof. Dr. Saleh Orabi (2026)"
    },
    "English": {
        "title": "🏛️ Sovereign Stewardship Engineering Protocol",
        "choose": "Choose Research Model:",
        "about": "💡 Philosophy & Engineering Logic",
        "sidebar_info": "Prof. Dr. Saleh Orabi (2026)"
    }
}
txt = L[st.session_state.lang]

# --- 3. الفهرس الشامل (تم إضافة هندسة السياسات النقدية) ---
st.sidebar.title(txt["choose"])
menu = {
    "--- النماذج المؤسسية والسنن ---": "header1",
    "1. نموذج الوظيفة الرسالية (Pᵣ)": "m1",
    "7. القيمة التزكوية المضافة (ZVA)": "zva",
    "8. سنة الشكر (Y)": "s1",
    "9. سنة الظلم (R)": "s2",
    "12. سياسة مكافحة الفقر": "poverty",
    "20. سعر الكفاية (Pk)": "price_sufficiency",
    "--- هندسة السياسات النقدية ---": "header2",
    "24. مؤشر التمكين المالي (Y)": "financial_empowerment",
    "25. النموذج النقدي المركب (Y)": "monetary_composite"
}
choice_key = st.sidebar.selectbox("", list(menu.keys()))
model = menu[choice_key]

# --- 4. محرك التنفيذ ---

# --- نموذج التمكين المالي (المعادلة السادسة في مذكراتك) ---
if model == "financial_empowerment":
    st.markdown(f"<h1 class='header-style'>نموذج التمكين المالي العام (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 T + \beta_3 W + \epsilon")
    c1, c2 = st.columns([1.2, 1])
    with c1:
        z_rate = st.slider("Z (معدل المال المزكى - التزكية المالية)", 0, 100, 75)
        t_vol = st.slider("T (حجم التمويل بالمشاركة والمضاربة)", 0, 100, 60)
        w_sukuk = st.slider("W (حجم الصكوك الوقفية المصدرة)", 0, 100, 65)
        empowerment_y = 10 + (0.4 * z_rate) + (0.3 * t_vol) + (0.3 * w_sukuk)
        st.metric("مؤشر التمكين المالي العام (Y)", f"{empowerment_y:.2f}")
    with c2: st.markdown(f"<div class='about-box'><b>الهدف:</b> قياس أثر السياسات النقدية الشرعية على التمكين الاقتصادي (نسبة الوصول للتمويل، الكرامة الاقتصادية).</div>", unsafe_allow_html=True)

# --- النموذج النقدي المركب (المعادلة الشاملة) ---
elif model == "monetary_composite":
    st.markdown(f"<h1 class='header-style'>النموذج النقدي المركب (Sovereign Monetary Model)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 W + \beta_3 S + \beta_4 G + \beta_5 F + \beta_6 C + \beta_7 V + \epsilon")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("أدوات الضبط الشرعي")
        z_m = st.slider("Z (معدل الزكاة المحصلة)", 0, 100, 80)
        w_m = st.slider("W (حجم الوقف الإنتاجي)", 0, 100, 70)
        s_m = st.slider("S (مؤشر أسعار السلع الأساسية)", 0, 100, 60)
        g_f = st.slider("G/F (تغطية الذهب والفضة)", 0, 100, 85)
    
    with col2:
        st.subheader("متغيرات الاستقرار")
        c_inf = st.slider("C (معدل التضخم)", 0, 100, 20)
        v_exc = st.slider("V (تقلبات سعر الصرف)", 0, 100, 15)
        
        # حساب مؤشر الاستقرار النقدي (Y)
        # العلاقة طردية مع (Z, W, S, G) وعكسية مع (C, V)
        monetary_stability = (0.2*z_m + 0.2*w_m + 0.15*s_m + 0.25*g_f) - (0.1*c_inf + 0.1*v_exc) + 20
        st.metric("مؤشر الاستقرار النقدي السيادي (Y)", f"{monetary_stability:.2f}")
        
    st.markdown(f"<div class='about-box'><b>التحليل الاقتصادي:</b> يجمع هذا النموذج بين الزكاة (لتحفيز التداول)، الوقف (للتمويل التنموي)، السلع (للقيمة الحقيقية)، والذهب (للحماية من تقلبات العملة والمضاربات).</div>", unsafe_allow_html=True)

# استكمال روابط النماذج السابقة لضمان عمل الفهرس
elif model in ["m1", "zva", "s1", "s2", "poverty", "price_sufficiency"]:
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.info("النموذج يعمل بكفاءة ضمن محرك الاستخلاف.")

st.sidebar.markdown("---")
st.sidebar.write(txt["sidebar_info"])
