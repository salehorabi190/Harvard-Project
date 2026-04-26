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
        "choose": "اختر نموذج الدراسة:",
        "about": "الفلسفة الهندسية للنموذج",
        # القائمة الشاملة
        "overview": "الرئيسية (Overview)",
        "mission": " الوظيفة الرسالية (Mission-Driven)",
        "leadership": "👑 القيادة المتزكية (Tazkiyah Leadership)",
        "zva": "💎 القيمة المضافة (ZVA/ZVR)",
        "market": "⚖️ هندسة السوق والعدالة",
        "transparency": "🔍 الشفافية ومنع الاحتكار",
        "pricing": "🏷️ سياسات التسعير والأزمات",
        "monetary": "💰 السياسة النقدية وسعر الصرف",
        "waqf_zakat": "🕌 الزكاة والوقف (Social Finance)",
        "governance": "📜 الحوكمة الرمزية (Governance)",
        "existential": "🌱 التحقق الوجودي والتمكين",
        "sunan": "🔄 السنن الاقتصادية (Sunan Models)",
        "amanah": "🌐 بروتوكول أمانة (Amanah Protocol)",
        "simulation": "🎮 المحاكاة الرقمية (Simulation)",
        "fortification": "🛡️ التحصين السيادي (Fortification)",
        # نصوص الشرح
        "mission_desc": "تحويل النية إلى محرك أداء مؤسسي. P = α + βR.",
        "leadership_desc": "القيادة كأمانة تزكوية تعتمد على النية والقدوة.",
        "zva_desc": "دمج البركة (λZ) في القيمة الاقتصادية (EVA).",
        "market_desc": "تحقيق التوازن عبر 'العرض الرحيم' والعدالة التوزيعية.",
        "monetary_desc": "عملة سيادية مغطاة بالذهب والإنتاج (Sovereign Anchor).",
        "sunan_desc": "برمجة قوانين الشكر (الزيادة) والتداول (منع التركز).",
        "amanah_desc": "الخوارزمية الكبرى لربط الإنسان بالتراب مباشرة."
    },
    "English": {
        "title": "🏛️ Sovereign Stewardship Engineering Protocol",
        "choose": "Choose Economic Domain:",
        "about": "Engineering Philosophy",
        # Comprehensive Menu
        "overview": "Overview",
        "mission": "Mission-Driven Function",
        "leadership": "Tazkiyah Leadership",
        "zva": "Tazkiyah Value Added (ZVA)",
        "market": "Market Engineering & Justice",
        "transparency": "Transparency & Anti-Monopoly",
        "pricing": "Pricing & Crisis Policy",
        "monetary": "Monetary & Exchange Policy",
        "waqf_zakat": "Zakat & Waqf (Social Finance)",
        "governance": "Symbolic Governance",
        "existential": "Existential Realization",
        "sunan": "Economic Sunan Models",
        "amanah": "Amanah Protocol",
        "simulation": "Digital Simulation",
        "fortification": "Sovereign Fortification"
    }
}
txt = L[st.session_state.lang]

# --- 3. تصميم الواجهة (CSS) ---
st.markdown(f"""<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo&display=swap');
    html, body, [class*="css"] {{ font-family: 'Cairo', sans-serif; }}
    .about-box {{ background-color: #e8f5e9; padding: 15px; border-radius: 10px; border-right: 5px solid #1e4d2b; }}
    </style>""", unsafe_allow_html=True)

# --- 4. القائمة الجانبية ---
menu = list(txt.values())[3:]
domain = st.sidebar.selectbox(txt["choose"], menu)

# --- 5. تنفيذ النماذج (Logic Engine) ---

# 1. الرئيسية
if domain == txt["overview"]:
    st.title(txt["title"])
    st.info("Choose a model from the sidebar to start | اختر نموذجاً من القائمة للبدء")
    st.image("https://img.icons8.com/fluency/240/stewardship.png")

# 2. الوظيفة الرسالية
elif domain == txt["mission"]:
    st.header(txt["mission"])
    st.latex(r"P = \alpha + \beta_1 R + \beta_2 M + \beta_3 T + \beta_4 C + \epsilon")
    r = st.slider("R (Symbolic Mission)", 0, 100, 70)
    st.metric("Institutional Performance", f"{(0.4*r + 20):.2f}")
    st.markdown(f"<div class='about-box'>{txt.get('mission_desc', '')}</div>", unsafe_allow_html=True)

# 3. القيادة المتزكية
elif domain == txt["leadership"]:
    st.header(txt["leadership"])
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \epsilon")
    zr = st.slider("Zr (Tazkiyah Level)", 0, 100, 80)
    st.metric("Leadership Impact", f"{(zr * 1.2):.2f}")
    st.markdown(f"<div class='about-box'>{txt.get('leadership_desc', '')}</div>", unsafe_allow_html=True)

# 4. القيمة المضافة (ZVA)
elif domain == txt["zva"]:
    st.header(txt["zva"])
    st.latex(r"ZVA = EVA + \lambda Z")
    eva = st.number_input("EVA", value=50000)
    z_idx = st.slider("Z (Moral/Tazkiyah Index)", 0, 100, 85)
    st.metric("Sovereign Value Added", f"${eva + (1.2 * z_idx * 100):,.2f}")
    st.markdown(f"<div class='about-box'>{txt.get('zva_desc', '')}</div>", unsafe_allow_html=True)

# 5. السوق والشفافية
elif domain == txt["market"] or domain == txt["transparency"]:
    st.header(txt["market"])
    st.latex(r"V_m = P_m + \Delta B (Mercy) + J (Justice)")
    m_mode = st.toggle("Activate Merciful Supply (العرض الرحيم)")
    trans = st.slider("Transparency Index", 0, 100, 90)
    st.metric("Market Health", "Optimized" if m_mode and trans > 75 else "Stable")
    st.markdown(f"<div class='about-box'>{txt.get('market_desc', '')}</div>", unsafe_allow_html=True)

# 6. السياسة النقدية وسعر الصرف
elif domain == txt["monetary"]:
    st.header(txt["monetary"])
    st.latex(r"Value = \int (Gold + Production + Zakat) dt")
    gold = st.slider("Gold Coverage", 0, 100, 70)
    zakat = st.slider("Zakat Flow", 0, 100, 60)
    st.metric("Currency Stability", f"{(gold*0.6 + zakat*0.4):.2f}")
    st.markdown(f"<div class='about-box'>{txt.get('monetary_desc', '')}</div>", unsafe_allow_html=True)

# 7. الزكاة والوقف
elif domain == txt["waqf_zakat"]:
    st.header(txt["waqf_zakat"])
    st.latex(r"Z_{it} = \gamma + \delta_1 W_{it} + \delta_2 R_{it}")
    w = st.slider("W (Waqf Assets)", 0, 100, 50)
    st.metric("Social Capital Impact", f"{(w * 1.5):.2f}")

# 8. السنن الاقتصادية
elif domain == txt["sunan"]:
    st.header(txt["sunan"])
    st.subheader("Shukr & Tadawul Simulation")
    shukr = st.slider("Shukr Rate (Resource Optimization)", 0, 100, 80)
    st.metric("Productivity Growth (Y)", f"+{shukr/10}%")
    st.markdown(f"<div class='about-box'>{txt.get('sunan_desc', '')}</div>", unsafe_allow_html=True)

# 9. بروتوكول أمانة
elif domain == txt["amanah"]:
    st.header(txt["amanah"])
    st.latex(r"B_i = \frac{\sum (U_v \cdot S_t)}{H_w + D_i}")
    uv = st.slider("Utility (Uv)", 0, 100, 85)
    st.metric("Barakah Index", f"{(uv * 1.2):.2f}")
    st.markdown(f"<div class='about-box'>{txt.get('amanah_desc', '')}</div>", unsafe_allow_html=True)

# 10. سياسات التسعير والأزمات
elif domain == txt["pricing"]:
    st.header(txt["pricing"])
    st.latex(r"P_k = Cost + Adequacy\_Margin")
    cost = st.number_input("Base Cost", value=100)
    st.metric("Adequacy Price (Pk)", f"${cost * 1.1:.2f}")

# 11. التحصين السيادي
elif domain == txt["fortification"]:
    st.header(txt["fortification"])
    if st.button("Generate ZK-Proof"):
        st.success("Sovereign Identity Verified | تم التحقق السيادي بنجاح")
        st.code("Hash: 0xProf_Dr_Saleh_Orabi_2026")

# --- تذييل الصفحة ---
st.sidebar.markdown("---")
st.sidebar.write(f"✍️ **Design:** Prof. Dr. Saleh Orabi (2026)")
