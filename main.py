import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- 1. إعدادات الهوية البصرية ---
st.set_page_config(page_title="بروتوكول هندسة الاستخلاف", page_icon="⚖️", layout="wide")

# --- 2. نظام اللغات (Session State) ---
if 'lang' not in st.session_state: st.session_state.lang = "العربية"
selected_lang = st.sidebar.radio("Language / اللغة", ["العربية", "English"], index=0 if st.session_state.lang == "العربية" else 1)
st.session_state.lang = selected_lang

L = {
    "العربية": {
        "title": "🏛️ بروتوكول هندسة الاستخلاف الاقتصادي الرقمي",
        "sidebar_title": "💎 فهرس النماذج السيادية",
        "choose": "اختر نموذج الدراسة:",
        "about": "الفلسفة الهندسية للنموذج",
        "impact_msg": "تم إصدار برهان الستر الرقمي (ZKP) بنجاح.",
        # القائمة
        "overview": "الرئيسية (Overview)",
        "leadership": "👑 القيادة المتزكية (Tazkiyah Leadership)",
        "zva": "💎 القيمة المضافة (ZVA/ZVR)",
        "market": "⚖️ هندسة السوق (العدالة والشفافية)",
        "waqf_zakat": "🕌 الزكاة والوقف (Social Finance)",
        "governance": "📜 الحوكمة الرمزية (Symbolic Governance)",
        "existential": "🌱 التحقق الوجودي والتمكين",
        "pricing": "🏷️ سياسات التسعير والأزمات",
        "amanah": "🌐 بروتوكول أمانة (Amanah Protocol)",
        "fortification": "🛡️ التحصين السيادي (Fortification)",
        # الشروحات
        "zva_desc": "قياس الفائض الأخلاقي والبركة كجزء من القيمة الاقتصادية المضافة (ZVA = EVA + λZ). هذا النموذج يثبت أن الالتزام القيمي يرفع الجدارة الائتمانية.",
        "waqf_desc": "تحويل الزكاة والوقف من 'تبرع' إلى 'رأس مال تنموي' مستدام. (Z_it) هو مؤشر الأثر الوقفي التراكمي.",
        "governance_desc": "حوكمة قائمة على 'الانسجام الرمزي' (Ar) وليس فقط القوانين الجافة. الشفافية هنا هي تعبير عن التسامي الأخلاقي.",
        "existential_desc": "تحليل مدى تحقيق الفرد لذاته (Vr) داخل المنظومة. العمل هنا ليس مجرد وظيفة، بل هو 'تحقق وجودي' واستخلاف.",
        "pricing_desc": "هندسة 'سعر الكفاية' (Pk) الذي يضمن حق المنتج وكرامة المستهلك، مع تفعيل 'العرض الرحيم' في الأزمات."
    },
    "English": {
        "title": "🏛️ Sovereign Stewardship Engineering Protocol",
        "sidebar_title": "💎 Sovereign Models Index",
        "choose": "Choose Economic Domain:",
        "about": "Engineering Philosophy",
        "impact_msg": "Digital Veiling Proof (ZKP) Generated Successfully.",
        # Menu
        "overview": "Overview",
        "leadership": "👑 Tazkiyah Leadership",
        "zva": "💎 Value Added (ZVA/ZVR)",
        "market": "⚖️ Market Engineering & Justice",
        "waqf_zakat": "🕌 Zakat & Waqf (Social Finance)",
        "governance": "📜 Symbolic Governance",
        "existential": "🌱 Existential Realization",
        "pricing": "🏷️ Pricing & Crisis Policy",
        "amanah": "🌐 Amanah Protocol",
        "fortification": "🛡️ Sovereign Fortification",
        # Descriptions
        "zva_desc": "Measuring moral surplus and Barakah as part of economic value added (ZVA = EVA + λZ). It proves that value-alignment raises credit merit.",
        "waqf_desc": "Transforming Zakat and Waqf from 'charity' to sustainable 'developmental capital'. (Z_it) is the cumulative impact index.",
        "governance_desc": "Governance based on 'Symbolic Alignment' (Ar). Transparency is an expression of ethical transcendence.",
        "existential_desc": "Analyzing individual self-realization (Vr) within the system. Work is a mission of stewardship, not just a job.",
        "pricing_desc": "Engineering the 'Adequacy Price' (Pk) to ensure producer rights and consumer dignity, activating 'Merciful Supply' during crises."
    }
}
txt = L[st.session_state.lang]

# --- 3. القائمة الجانبية ---
st.sidebar.title(txt["sidebar_title"])
menu_options = [txt["overview"], txt["leadership"], txt["zva"], txt["market"], 
                txt["waqf_zakat"], txt["governance"], txt["existential"], 
                txt["pricing"], txt["amanah"], txt["fortification"]]
domain = st.sidebar.selectbox(txt["choose"], menu_options)

# --- 4. تنفيذ النماذج (Logic Engine) ---

# --- القيمة المضافة ZVA ---
if domain == txt["zva"]:
    st.header(txt["zva"])
    st.latex(r"ZVA = EVA + \lambda Z")
    c1, c2 = st.columns([1, 1])
    with c1:
        eva = st.number_input("EVA (Economic Value Added)", value=50000)
        z_score = st.slider("Z (Tazkiyah/Moral Index)", 0, 100, 80)
        lam = 1.2
        total_zva = eva + (lam * z_score * 100)
        st.metric("Total Sovereign Value", f"${total_zva:,.2f}", delta=f"{z_score}% Moral Gain")
    with c2:
        st.markdown(f"<div style='background-color:#e8f5e9; padding:20px; border-radius:10px;'><b>{txt['about']}</b><br>{txt['zva_desc']}</div>", unsafe_allow_html=True)

# --- الزكاة والوقف ---
elif domain == txt["waqf_zakat"]:
    st.header(txt["waqf_zakat"])
    st.latex(r"Z_{it} = \gamma + \delta_1 W_{it} + \delta_2 R_{it} + \delta_3 T_{it}")
    c1, c2 = st.columns([1, 1])
    with c1:
        waqf_vol = st.slider("W (Waqf Assets Volume)", 0, 100, 60)
        return_rate = st.slider("R (Social Return Rate)", 0, 100, 75)
        st.metric("Social Impact Index", f"{(waqf_vol*0.6 + return_rate*0.4):.2f}")
    with c2:
        st.markdown(f"<div style='background-color:#e8f5e9; padding:20px; border-radius:10px;'><b>{txt['about']}</b><br>{txt['waqf_desc']}</div>", unsafe_allow_html=True)

# --- الحوكمة الرمزية ---
elif domain == txt["governance"]:
    st.header(txt["governance"])
    st.latex(r"G_r = \alpha + \beta_1 N_r + \beta_2 T_r + \beta_3 M_r + \beta_4 A_r")
    c1, c2 = st.columns([1, 1])
    with c1:
        alignment = st.slider("Ar (Symbolic Alignment Index)", 0, 100, 85)
        transparency = st.slider("Tr (Transparency Level)", 0, 100, 90)
        st.metric("Governance Quality", f"{(alignment*0.7 + transparency*0.3):.2f}")
    with c2:
        st.markdown(f"<div style='background-color:#e8f5e9; padding:20px; border-radius:10px;'><b>{txt['about']}</b><br>{txt['governance_desc']}</div>", unsafe_allow_html=True)

# --- التحقق الوجودي ---
elif domain == txt["existential"]:
    st.header(txt["existential"])
    st.latex(r"V_r = \alpha + \beta_1 M_r + \beta_2 P_r + \beta_3 N_r + \beta_4 Z_r")
    c1, c2 = st.columns([1, 1])
    with c1:
        meaning = st.slider("Mr (Personal Meaning Index)", 0, 100, 80)
        participation = st.slider("Pr (Symbolic Participation)", 0, 100, 70)
        st.metric("Existential Realization Score", f"{(meaning*0.5 + participation*0.5):.2f}")
    with c2:
        st.markdown(f"<div style='background-color:#e8f5e9; padding:20px; border-radius:10px;'><b>{txt['about']}</b><br>{txt['existential_desc']}</div>", unsafe_allow_html=True)

# --- سياسات التسعير ---
elif domain == txt["pricing"]:
    st.header(txt["pricing"])
    st.latex(r"P_k = \delta_0 + \delta_1 C + \delta_2 M_r + \delta_3 A_s")
    c1, c2 = st.columns([1, 1])
    with c1:
        cost = st.number_input("C (Production Cost)", value=100)
        mercy_mode = st.toggle("Enable Merciful Pricing (سعر الكفاية)")
        price = (cost * 1.2) if not mercy_mode else (cost * 1.05)
        st.metric("Current Market Price", f"${price:.2f}", delta="-15% Mercy Discount" if mercy_mode else None)
    with c2:
        st.markdown(f"<div style='background-color:#e8f5e9; padding:20px; border-radius:10px;'><b>{txt['about']}</b><br>{txt['pricing_desc']}</div>", unsafe_allow_html=True)

# --- الرئيسية وغيرها ---
elif domain == txt["overview"]:
    st.title(txt["title"])
    st.info("Choose a model from the sidebar to start | اختر نموذجاً من القائمة للبدء")

# --- تذييل الصفحة ---
st.sidebar.markdown("---")
st.sidebar.write(f"✍️ **Design:** Prof. Dr. Saleh Orabi (2026)")
