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
        "amanah": "🌐 بروتوكول أمانة (Amanah Protocol)",
        "fortification": "🛡️ التحصين السيادي (Fortification)",
        "monetary": "💰 السياسات النقدية وسعر الصرف",
        "waqf_zakat": "🕌 الزكاة والوقف (Social Finance)",
        "governance": "📜 الحوكمة الرمزية (Symbolic Governance)",
        "existential": "🌱 التحقق الوجودي والتمكين",
        "sunan": "🔄 السنن الاقتصادية (Shukr & Tadawul)",
        "pricing": "🏷️ سياسات التسعير والأزمات",
        # الشروحات
        "leadership_desc": "تحويل القيادة من سلطة مادية إلى وظيفة تزكوية، حيث المحرك هو النية (α) والقدوة (Rr).",
        "zva_desc": "قياس الفائض الأخلاقي والبركة كجزء من القيمة الاقتصادية المضافة، وليس فقط الربح المادي.",
        "market_desc": "السوق هنا فضاء للعدالة؛ العرض الرحيم يتدخل في الأزمات، والشفافية تلغي الغرر آلياً.",
        "amanah_desc": "الخوارزمية الكبرى التي تربط الإنسان بالتراب مباشرة، وتلغي وساطة الديون الربوية.",
        "monetary_desc": "هندسة عملة سيادية مغطاة بالذهب والإنتاج، تتحرر من تقلبات الدولار عبر ربطها بالقيم الحقيقية.",
        "sunan_desc": "برمجة السنن الكونية؛ الشكر يزيد الإنتاج (Y)، والتداول (Tadawul) يمنع تركز الثروة آلياً."
    },
    "English": {
        "title": "🏛️ Sovereign Stewardship Engineering Protocol",
        "sidebar_title": "💎 Sovereign Models Index",
        "choose": "Choose Economic Domain:",
        "about": "Engineering Philosophy",
        "impact_msg": "Digital Veiling Proof (ZKP) Generated Successfully.",
        # Menu
        "overview": "Overview (الرئيسية)",
        "leadership": "👑 Tazkiyah Leadership",
        "zva": "💎 Value Added (ZVA/ZVR)",
        "market": "⚖️ Market Engineering & Justice",
        "amanah": "🌐 Amanah Protocol",
        "fortification": "🛡️ Sovereign Fortification",
        "monetary": "💰 Monetary & Exchange Policy",
        "waqf_zakat": "🕌 Zakat & Waqf (Social Finance)",
        "governance": "📜 Symbolic Governance",
        "existential": "🌱 Existential Realization",
        "sunan": "🔄 Economic Sunan (Shukr/Tadawul)",
        "pricing": "🏷️ Pricing & Crisis Policy",
        # Descriptions
        "leadership_desc": "Transforming leadership from material power to a Tazkiyah function driven by intention (α) and Rr.",
        "zva_desc": "Measuring moral surplus and Barakah as integral parts of economic value added beyond profit.",
        "market_desc": "A marketplace of justice; Merciful Supply intervenes in crises, and transparency erases Gharar.",
        "amanah_desc": "The grand algorithm linking humans to resources directly, eliminating interest-based mediation.",
        "monetary_desc": "Engineering a sovereign currency backed by gold and production, free from USD fluctuations.",
        "sunan_desc": "Programming cosmic laws; Shukr increases output (Y), and Tadawul prevents wealth concentration."
    }
}
txt = L[st.session_state.lang]

# --- 3. تصميم الواجهة (CSS) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] {{ font-family: 'Cairo', sans-serif; text-align: {'right' if st.session_state.lang == 'العربية' else 'left'}; }}
    .stMetric {{ background-color: #ffffff; padding: 15px; border-radius: 10px; border-left: 5px solid #d4af37; }}
    .about-box {{ background-color: #e8f5e9; padding: 20px; border-radius: 10px; border-right: 5px solid #1e4d2b; line-height: 1.6; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. القائمة الجانبية ---
st.sidebar.title(txt["sidebar_title"])
menu = [txt["overview"], txt["leadership"], txt["zva"], txt["market"], txt["monetary"], txt["waqf_zakat"], txt["governance"], txt["existential"], txt["sunan"], txt["pricing"], txt["amanah"], txt["fortification"]]
domain = st.sidebar.selectbox(txt["choose"], menu)

# --- 5. محرك النماذج ---

# --- القيادة المتزكية ---
if domain == txt["leadership"]:
    st.header(txt["leadership"])
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \epsilon")
    c1, c2 = st.columns([1, 1])
    with c1:
        zr = st.slider("Zr (Tazkiyah)", 0, 100, 85)
        st.metric("Leadership Impact", f"{(zr * 1.2):.2f}")
    with c2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>{txt['leadership_desc']}</div>", unsafe_allow_html=True)

# --- هندسة السوق والشفافية ---
elif domain == txt["market"]:
    st.header(txt["market"])
    st.latex(r"V_m = P_m + \Delta B (Mercy) + J (Justice)")
    c1, c2 = st.columns([1, 1])
    with c1:
        mercy = st.toggle("Activate Merciful Supply (العرض الرحيم)")
        transparency = st.slider("Transparency Index", 0, 100, 90)
        st.metric("Market Equilibrium", "Stable" if mercy and transparency > 70 else "Imbalanced")
    with c2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>{txt['market_desc']}</div>", unsafe_allow_html=True)

# --- السياسات النقدية وسعر الصرف ---
elif domain == txt["monetary"]:
    st.header(txt["monetary"])
    st.latex(r"Currency\_Value = \int (Gold + Production + Zakat) dt")
    c1, c2 = st.columns([1, 1])
    with c1:
        gold_cover = st.slider("Gold Coverage", 0, 100, 75)
        prod_anchor = st.slider("Real Production Anchor", 0, 100, 80)
        st.metric("Sovereign Exchange Rate", f"{(gold_cover*0.6 + prod_anchor*0.4):.2f} Index")
    with c2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>{txt['monetary_desc']}</div>", unsafe_allow_html=True)

# --- السنن الاقتصادية ---
elif domain == txt["sunan"]:
    st.header(txt["sunan"])
    st.subheader("Law of Shukr & Tadawul")
    st.latex(r"Y_{new} = Y_{old} \times (1 + Shukr\_Rate) \quad | \quad T = \frac{Wealth}{Velocity}")
    c1, c2 = st.columns([1, 1])
    with c1:
        shukr = st.slider("Shukr (Utilization of Resources)", 0, 100, 85)
        st.metric("Productivity Growth (Y)", f"+{shukr/10}%")
    with c2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>{txt['sunan_desc']}</div>", unsafe_allow_html=True)

# --- بروتوكول أمانة ---
elif domain == txt["amanah"]:
    st.header(txt["amanah"])
    st.latex(r"B_i = \frac{\sum (U_v \cdot S_t)}{H_w + D_i}")
    c1, c2 = st.columns([1, 1])
    with c1:
        uv = st.slider("Uv (Utility)", 0, 100, 80)
        di = st.slider("Di (Debt Obstruction)", 1, 50, 5)
        st.metric("Barakah Score", f"{(uv*1.5 / di):.2f}")
    with c2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>{txt['amanah_desc']}</div>", unsafe_allow_html=True)

# --- التحصين السيادي ---
elif domain == txt["fortification"]:
    st.header(txt["fortification"])
    if st.button("Generate ZK-Proof"):
        st.success(txt["impact_msg"])
        st.code("Proof_Hash: 0xProf_Dr_Saleh_Orabi_Sovereign_2026", language='bash')

# --- تذييل الصفحة ---
st.sidebar.markdown("---")
st.sidebar.write(f"✍️ **Design:** Prof. Dr. Saleh Orabi (2026)")
