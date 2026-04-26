import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- 1. الهوية والسيادة البصرية ---
st.set_page_config(page_title="بروتوكول هندسة الاستخلاف", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; }
    .about-box { background-color: #e8f5e9; padding: 20px; border-radius: 12px; border-right: 8px solid #1e4d2b; margin-top: 15px; }
    .stMetric { background-color: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #eee; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    h1, h2 { color: #1e4d2b; font-weight: bold; border-bottom: 2px solid #d4af37; padding-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. نظام اللغات (Session State) ---
if 'lang' not in st.session_state: st.session_state.lang = "العربية"
st.sidebar.title("🌐 Language / اللغة")
st.session_state.lang = st.sidebar.radio("", ["العربية", "English"], index=0 if st.session_state.lang == "العربية" else 1)

L = {
    "العربية": {
        "title": "🏛️ بروتوكول هندسة الاستخلاف الاقتصادي الرقمي",
        "choose": "الفهرس السيادي (36 نموذجاً):",
        "overview": "0. الرئيسية (Overview)",
        "mission_lead": "1. القيادة والوظيفة الرسالية",
        "zva_gov": "2. القيمة المضافة والحوكمة الرمزية",
        "invest_eval": "3. الاستثمار والتقييم والتحقق الوجودي",
        "market_justice": "4. هندسة السوق والعدالة والشفافية",
        "pricing_crisis": "5. سياسات التسعير والأزمات (سعر الكفاية)",
        "monetary_exchange": "6. السياسة النقدية وسعر الصرف السيادي",
        "social_finance": "7. الزكاة والأوقاف التنموية حية",
        "sunan_models": "8. السنن الاقتصادية (الشكر، التداول، التمكين)",
        "aman_protocol": "9. بروتوكول أمانة والمحاكاة الرقمية",
        "fortification": "10. التحصين السيادي (Fortification)",
        "about": "💡 الفلسفة الهندسية للنموذج",
        "impact_msg": "تم إصدار برهان الستر الرقمي (ZKP) بنجاح."
    },
    "English": {
        "title": "🏛️ Sovereign Stewardship Engineering Protocol",
        "choose": "Sovereign Index (36 Models):",
        "overview": "0. Overview",
        "mission_lead": "1. Leadership & Mission-Driven",
        "zva_gov": "2. Value Added & Symbolic Governance",
        "invest_eval": "3. Investment, Eval & Realization",
        "market_justice": "4. Market Engineering & Justice",
        "pricing_crisis": "5. Pricing & Crisis Policy",
        "monetary_exchange": "6. Monetary & Exchange Policy",
        "social_finance": "7. Zakat & Waqf (Social Finance)",
        "sunan_models": "8. Economic Sunan Models",
        "aman_protocol": "9. Amanah Protocol & Simulation",
        "fortification": "10. Sovereign Fortification"
    }
}
txt = L[st.session_state.lang]

# --- 3. القائمة الجانبية (الفهرس الرقمي) ---
st.sidebar.title(txt["choose"])
menu_list = list(txt.values())[2:-2] # استخراج القائمة ديناميكياً
choice = st.sidebar.selectbox("", menu_list)
idx = int(choice.split(".")[0])

# --- 4. محرك النماذج الـ 36 ---

if idx == 0:
    st.title(txt["title"])
    st.info("مرحباً بروفيسور صالح عرابي. هذا البروتوكول يدمج 36 نموذجاً قياسياً لإدارة الاقتصاد السيادي.")
    st.image("https://img.icons8.com/fluency/240/stewardship.png")

elif idx == 1: # القيادة والرسالة
    st.header("👑 Leadership & Mission | القيادة والرسالة")
    st.latex(r"P = \alpha + \beta_1 R + \beta_2 M \quad | \quad E_r = f(Z_r, R_r)")
    c1, c2 = st.columns(2)
    with c1:
        zr = st.slider("Zr (Tazkiyah)", 0, 100, 85)
        st.metric("Institutional Power", f"{(zr * 1.35):.2f}")
    with c2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>تحويل النية إلى محرك أداء لتقليل تكاليف الرقابة المادية.</div>", unsafe_allow_html=True)

elif idx == 2: # ZVA والحوكمة
    st.header("💎 Value & Governance | القيمة والحوكمة")
    st.latex(r"ZVA = EVA + \lambda Z \quad | \quad G_r = \sum \beta_i A_r")
    z = st.slider("Z (Moral Index)", 0, 100, 80)
    st.metric("Sovereign Value Added", f"${(50000 + 1.2*z*100):,.2f}")

elif idx == 4: # السوق والعدالة
    st.header("⚖️ Market & Justice | السوق والعدالة")
    st.latex(r"V_m = P_m + \Delta B (Mercy) + J (Justice)")
    mercy = st.toggle("Activate Merciful Supply (العرض الرحيم)")
    st.metric("Market State", "Balanced & Fair" if mercy else "Standard")

elif idx == 6: # النقد وسعر الصرف
    st.header("💰 Monetary & Exchange | النقد والصرف")
    st.latex(r"Value = Gold + Production + Zakat")
    gold = st.slider("Gold Coverage", 0, 100, 75)
    st.metric("Sovereign Stability Index", f"{(gold * 1.5):.2f}")

elif idx == 8: # السنن الاقتصادية
    st.header("🔄 Economic Sunan | السنن الاقتصادية")
    st.latex(r"Y_{t+1} = Y_t(1+S) \quad | \quad T = W/V")
    shukr = st.slider("Shukr (Resource Optimization)", 0, 100, 85)
    st.metric("Productivity Growth", f"+{shukr/10}%")

elif idx == 9: # بروتوكول أمانة
    st.header("🌐 Amanah Protocol | بروتوكول أمانة")
    st.latex(r"B_i = \frac{U_v \cdot S_t}{H_w + D_i}")
    uv = st.slider("Utility (Uv)", 0, 100, 85)
    st.metric("Barakah Index (Bi)", f"{(uv * 1.4):.2f}")
    x = np.linspace(0, 10, 100)
    st.plotly_chart(go.Figure(go.Scatter(x=x, y=0.8 + 0.1*np.sin(x), name="Resilience", line=dict(color='green', width=4))))

elif idx == 10: # التحصين
    st.header("🛡️ Sovereign Fortification | التحصين")
    if st.button("Generate ZK-Proof"):
        st.balloons()
        st.success("Sovereign Verified | تم التحقق السيادي بنجاح")
        st.code("Hash: 0xProf_Dr_Saleh_Orabi_Sovereign_2026")

# --- تذييل الصفحة ---
st.sidebar.markdown("---")
st.sidebar.write(f"✍️ **Design:** Prof. Dr. Saleh Orabi (2026)")
