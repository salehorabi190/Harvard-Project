import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- 1. إعدادات الهوية البصرية ---
st.set_page_config(page_title="بروتوكول هندسة الاستخلاف", page_icon="⚖️", layout="wide")

# --- 2. نظام اللغات (Session State) ---
if 'lang' not in st.session_state: 
    st.session_state.lang = "العربية"

selected_lang = st.sidebar.radio("Language / اللغة", ["العربية", "English"], 
                                 index=0 if st.session_state.lang == "العربية" else 1)
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
        "fortification": "Sovereign Fortification (التحصين السيادي)",
        "impact_msg": "تم إصدار برهان الستر الرقمي (ZKP) بنجاح.",
        "about": "الفلسفة الهندسية للنموذج",
        "mission_desc": "هذا النموذج يحول 'النية' من مفهوم مجرد إلى محرك أداء. نحن نفترض أن المؤسسة تزداد إنتاجيتها كلما ارتبط الموظف برسالة رمزية معنوية.",
        "monetary_desc": "هنا نلغي الاعتماد على الديون؛ قوة العملة تُشتق من (الزكاة، الذهب، والإنتاج الوقفي). الاستقرار هو نتيجة حتمية للارتباط بالأصول الحقيقي."
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
        "fortification": "Sovereign Fortification",
        "impact_msg": "Digital Veiling Proof (ZKP) Generated Successfully.",
        "about": "Engineering Philosophy",
        "mission_desc": "This model transforms 'Intention' into a performance driver. Productivity increases as employees align with a symbolic mission.",
        "monetary_desc": "Eliminating debt reliance; currency strength is derived from Zakat, Gold, and Waqf production. Stability is a result of real-asset anchoring."
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
    .about-box {{ background-color: #e8f5e9; padding: 20px; border-radius: 10px; border-right: 5px solid #1e4d2b; margin-top: 20px; }}
    h1, h2, h3 {{ color: #1e4d2b; font-weight: bold; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. القائمة الجانبية ---
st.sidebar.title(txt["sidebar_title"])
menu_options = [txt["overview"], txt["mission"], txt["leadership"], txt["zva"], 
                txt["market"], txt["monetary"], txt["amanah"], txt["fortification"]]
domain = st.sidebar.selectbox(txt["choose"], menu_options)

# --- 5. تنفيذ النماذج ---

# الرئيسية
if domain == txt["overview"]:
    st.title(txt["title"])
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"""
        ### أمانة: السيادة عبر الكود
        هذه المنصة هي محاكاة تفاعلية للـ **36 نموذجاً قياسياً** التي تمثل العمود الفقري لهندسة الاستخلاف. 
        نحن هنا لا نعرض بيانات تاريخية، بل نصمم **خوارزميات مستقبلية** لإدارة الموارد والائتمان والعدالة.
        """)
        st.info("Choose a model from the sidebar to begin the simulation | اختر نموذجاً من القائمة لبدء المحاكاة")
    with col2:
        st.image("https://img.icons8.com/fluency/240/stewardship.png")

# 1. الوظيفة الرسالية
elif domain == txt["mission"]:
    st.header(txt["mission"])
    st.latex(r"P = \alpha + \beta_1 R + \beta_2 M + \beta_3 T + \beta_4 C + \epsilon")
    col1, col2 = st.columns([1, 1])
    with col1:
        r = st.slider("R (Symbolic Mission)", 0, 100, 70)
        m = st.slider("M (Meaning)", 0, 100, 80)
        st.metric("Performance Impact (P)", f"{(0.4*r + 0.3*m + 20):.2f}")
    with col2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>{txt['mission_desc']}</div>", unsafe_allow_html=True)

# 5. السياسة النقدية
elif domain == txt["monetary"]:
    st.header(txt["monetary"])
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 W + \beta_3 S + \beta_4 G + \beta_5 F - \beta_6 C - \beta_7 V + \epsilon")
    col1, col2 = st.columns([1, 1])
    with col1:
        zakat = st.slider("Z (Zakat Flow)", 0, 100, 60)
        gold = st.slider("G (Gold Cover)", 0, 100, 50)
        st.metric("Currency Stability Index", f"{(20 + 0.3*zakat + 0.4*gold):.2f}")
    with col2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>{txt['monetary_desc']}</div>", unsafe_allow_html=True)

# (ملاحظة: يتم تكرار نفس النمط لبقية النماذج لضمان وجود الشرح تحت كل قسم)

# --- تذييل الصفحة ---
st.sidebar.markdown("---")
st.sidebar.write(f"✍️ **Design:** Prof. Dr. Saleh Orabi (2026)")
st.sidebar.write("⚡ Powered by Amanah Engine")
