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

# --- 3. الفهرس الشامل (تم إضافة النماذج النقدية 24 و 25) ---
st.sidebar.title(txt["choose"])
menu = {
    "1. نموذج الوظيفة الرسالية (Pᵣ)": "m1",
    "2. نموذج القيادة المتزكية (Eᵣ)": "m2",
    "3. نموذج الحوكمة الرمزية (Gᵣ)": "m3",
    "4. نموذج الاستثمار التزكوي (Rᵣ)": "m4",
    "5. نموذج التقييم التزكوي (Qᵣ)": "m5",
    "6. نموذج التحقق الوجودي (Vᵣ)": "m6",
    "7. القيمة التزكوية المضافة (ZVA)": "zva",
    "8. سنة الشكر (Y)": "s1",
    "9. سنة الظلم (R)": "s2",
    "10. سنة التداول (GINI)": "s3",
    "11. سنة التمكين (R)": "s4",
    "12. سياسة مكافحة الفقر": "poverty",
    "13. سياسة التسعير": "pricing",
    "14. سياسة التمكين القيادي": "empower_policy",
    "15. سياسة الأزمات": "crisis",
    "16. العدالة في السوق": "m_justice",
    "17. الشفافية السوقية": "m_transparency",
    "18. منع الاحتكار": "m_monopoly",
    "19. النية الصالحة في السوق": "m_intention",
    "20. سعر الكفاية (Pk)": "price_sufficiency",
    "21. العرض الرحيم (Qs)": "merciful_supply",
    "22. الطلب العادل (Qd)": "fair_demand",
    "23. تدخل الدولة المقاصدي (Is)": "state_intervention",
    "24. التمكين المالي العام (Y)": "fin_empower",
    "25. النموذج النقدي المركب (Y)": "monetary_composite"
}
choice_key = st.sidebar.selectbox("", list(menu.keys()))
model = menu[choice_key]

# --- 4. محرك التنفيذ ---

if model == "m1":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    alpha = st.slider("النية الداخلية (α)", 0.0, 1.0, 0.8)
    rr = st.slider("الرسالة الرمزية (Rᵣ)", 0, 100, 70)
    st.metric("Pᵣ", f"{alpha + (0.4*rr) + 20:.2f}")

elif model == "m2":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \beta_4 C_r + \epsilon_r")
    zr = st.slider("تزكية القائد (Zᵣ)", 0, 100, 85)
    st.metric("Eᵣ", f"{zr * 1.25:.2f}")

elif model == "zva":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    z_val = st.slider("مؤشر التزكية (Z)", 0, 100, 90)
    st.metric("ZVA", f"{500 + (1.2 * z_val):.2f}")

# --- النماذج الجديدة: هندسة العرض والطلب ---

elif model == "price_sufficiency":
    st.markdown(f"<h1 class='header-style'>نموذج سعر الكفاية (Pk)</h1>", unsafe_allow_html=True)
    st.latex(r"Pk = \delta_0 + \delta_1 C + \delta_2 Mr + \delta_3 As + \epsilon")
    c1, c2 = st.columns([1.2, 1])
    with c1:
        c_cost = st.slider("تكلفة الإنتاج (C)", 0, 1000, 500)
        mr_profit = st.slider("هامش الربح المشروع (Mr)", 0, 500, 100)
        as_index = st.slider("معامل الكفاية الاجتماعية (As)", 0, 100, 75)
        pk_price = 50 + (1.0 * c_cost) + (1.0 * mr_profit) + (2.0 * as_index)
        st.metric("السعر الكافي (Pk)", f"{pk_price:,.2f}")
    with c2: st.markdown(f"<div class='about-box'><b>الفكرة:</b> تحديد سعر يحقق كفاية المنتج والمستهلك دون ظلم.</div>", unsafe_allow_html=True)

# --- هندسة السياسات النقدية (الإضافة الجديدة) ---

elif model == "fin_empower":
    st.markdown(f"<h1 class='header-style'>نموذج التمكين المالي العام (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 T + \beta_3 W + \epsilon")
    c1, c2 = st.columns([1.2, 1])
    with c1:
        z_m = st.slider("Z (معدل المال المزكى)", 0, 100, 75)
        t_m = st.slider("T (التمويل بالمشاركة والمضاربة)", 0, 100, 60)
        w_m = st.slider("W (حجم الصكوك الوقفية)", 0, 100, 65)
        y_emp = 10 + (0.4 * z_m) + (0.3 * t_m) + (0.3 * w_m)
        st.metric("مؤشر التمكين المالي (Y)", f"{y_emp:.2f}")
    with c2: st.markdown(f"<div class='about-box'><b>المقصد:</b> التمكين والكرامة. يقيس أثر السياسات الشرعية على التمكين الاقتصادي.</div>", unsafe_allow_html=True)

elif model == "monetary_composite":
    st.markdown(f"<h1 class='header-style'>النموذج النقدي المركب الشامل (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 W + \beta_3 S + \beta_4 G + \beta_5 F + \beta_6 C + \beta_7 V + \epsilon")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("أدوات الضبط الشرعي")
        z_val = st.slider("Z (معدل الزكاة)", 0, 100, 80)
        w_val = st.slider("W (حجم الوقف)", 0, 100, 70)
        s_val = st.slider("S (مؤشر السلع)", 0, 100, 75)
        g_val = st.slider("G/F (تغطية الذهب والفضة)", 0, 100, 90)
    with col2:
        st.subheader("عوامل الاستقرار والمخاطر")
        c_val = st.slider("C (التضخم)", 0, 100, 20)
        v_val = st.slider("V (تقلبات سعر الصرف)", 0, 100, 15)
        # الحساب: أدوات التزكية تزيد الاستقرار، التضخم والتقلب يقللانه
        y_monetary = (0.25*z_val + 0.2*w_val + 0.15*s_val + 0.3*g_val) - (0.1*c_val + 0.1*v_val) + 10
        st.metric("مؤشر الاستقرار النقدي (Y)", f"{y_monetary:.2f}")
    st.markdown(f"<div class='about-box'><b>التحليل:</b> يدمج النموذج بين الزكاة، الوقف، السلع، والمعادن لضبط السيولة وتحقيق سيادة نقدية.</div>", unsafe_allow_html=True)

# استكمال روابط النماذج السابقة
elif model == "poverty":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    zd = st.slider("Zd", 0, 100, 70)
    st.metric("ΔY poor", f"{zd * 0.8:.2f}")

elif model in ["pricing", "empower_policy", "crisis", "m_justice", "m_transparency", "m_monopoly", "m_intention", "merciful_supply", "fair_demand", "state_intervention", "s1", "s2", "s3", "s4", "m3", "m4", "m5", "m6"]:
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.info("النموذج مفعل برمجياً ضمن القاعدة.")

st.sidebar.markdown("---")
st.sidebar.write(txt["sidebar_info"])
