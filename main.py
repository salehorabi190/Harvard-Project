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

# --- 3. الفهرس الشامل (25 نموذجاً مفعلة بالكامل) ---
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
    "12. سياسة مكافحة الفقر (ΔY)": "poverty",
    "13. سياسة التسعير (FBi)": "pricing",
    "14. سياسة التمكين القيادي (ES)": "empower_policy",
    "15. سياسة الأزمات (CR)": "crisis",
    "16. العدالة في السوق (Yt)": "m_justice",
    "17. الشفافية السوقية (Yt)": "m_transparency",
    "18. منع الاحتكار (Yt)": "m_monopoly",
    "19. النية الصالحة في السوق (Yt)": "m_intention",
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

# --- النماذج الأساسية ---
if model == "m1":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    alpha = st.slider("النية الداخلية (α)", 0.0, 1.0, 0.8)
    rr = st.slider("الرسالة الرمزية (Rᵣ)", 0, 100, 70)
    st.metric("Pᵣ", f"{alpha + (0.4*rr) + 20:.2f}")

elif model == "zva":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    z_val = st.slider("مؤشر التزكية (Z)", 0, 100, 90)
    st.metric("ZVA", f"{500 + (1.2 * z_val):.2f}")

# --- هندسة السوق (تفعيل النماذج 16-19) ---
elif model == "m_justice":
    st.markdown(f"<h1 class='header-style'>العدالة في السوق</h1>", unsafe_allow_html=True)
    st.latex(r"Y_t = \beta_0 + \beta_1 Ft + \beta_2 Tt + \beta_3 At + \beta_4 Et + \epsilon_t")
    ft = st.slider("العدالة السعرية (Ft)", 0, 100, 80)
    tt = st.slider("الشفافية السوقية (Tt)", 0, 100, 75)
    st.metric("استقرار السوق (Yt)", f"{100 - (0.3*ft + 0.2*tt):.2f}")

elif model == "m_transparency":
    st.markdown(f"<h1 class='header-style'>الشفافية السوقية</h1>", unsafe_allow_html=True)
    st.latex(r"Y_t = \alpha_0 + \alpha_1 Dt + \alpha_2 Ct + \alpha_3 It + \alpha_4 AFt + \mu_t")
    dt = st.slider("الإفصاح السعري (Dt)", 0, 100, 85)
    st.metric("كفاءة السوق (Yt)", f"{dt * 0.95:.2f}")

elif model == "m_monopoly":
    st.markdown(f"<h1 class='header-style'>منع الاحتكار</h1>", unsafe_allow_html=True)
    st.latex(r"Y_t = \gamma_0 + \gamma_1 HHt + \gamma_2 ACt + \gamma_3 RIt + \gamma_4 AMt + \nu_t")
    hht = st.slider("التركز السوقي (HHt)", 0, 2500, 1500)
    st.metric("العدالة التوزيعية (Yt)", f"{2500 - hht:.2f}")

elif model == "m_intention":
    st.markdown(f"<h1 class='header-style'>النية الصالحة في السوق</h1>", unsafe_allow_html=True)
    st.latex(r"Y_t = \delta_0 + \delta_1 GIt + \delta_2 APt + \delta_3 CCt + \delta_4 NDt + \xi_t")
    gi = st.slider("النية الصالحة (GIt)", 0, 100, 90)
    st.metric("الرضا العام (Yt)", f"{gi * 1.1:.2f}")

# --- هندسة العرض والطلب (تفعيل النماذج 20-23) ---
elif model == "price_sufficiency":
    st.markdown(f"<h1 class='header-style'>سعر الكفاية (Pk)</h1>", unsafe_allow_html=True)
    st.latex(r"Pk = \delta_0 + \delta_1 C + \delta_2 Mr + \delta_3 As + \epsilon")
    c_cost = st.slider("تكلفة الإنتاج (C)", 0, 1000, 500)
    st.metric("Pk", f"{c_cost * 1.3:.2f}")

elif model == "merciful_supply":
    st.markdown(f"<h1 class='header-style'>العرض الرحيم (Qs)</h1>", unsafe_allow_html=True)
    st.latex(r"QS = \gamma_0 + \gamma_1 H + \gamma_2 I + \gamma_3 S + \epsilon")
    h_need = st.slider("الحاجة المجتمعية (H)", 0, 100, 85)
    i_bene = st.slider("نية الإحسان (I)", 0, 100, 90)
    st.metric("كمية العرض الرحيم (Qs)", f"{0.5*h_need + 0.4*i_bene + 10:.2f}")

elif model == "fair_demand":
    st.markdown(f"<h1 class='header-style'>الطلب العادل (Qd)</h1>", unsafe_allow_html=True)
    st.latex(r"Qd = \alpha_0 + \alpha_1 Y + \alpha_2 A + \alpha_3 N + \epsilon")
    a_aware = st.slider("وعي الاستهلاك (A)", 0, 100, 85)
    st.metric("الطلب العادل (Qd)", f"{100 - 0.5*a_aware:.2f}")

elif model == "state_intervention":
    st.markdown(f"<h1 class='header-style'>تدخل الدولة المقاصدي (Is)</h1>", unsafe_allow_html=True)
    st.latex(r"Is = \beta_0 + \beta_1 M + \beta_2 D + \beta_3 R + \epsilon")
    m_dist = st.slider("اختلال السوق (M)", 0, 100, 75)
    st.metric("درجة التدخل (Is)", f"{m_dist * 1.2:.2f}")

# --- السياسات النقدية (النماذج 24-25) ---
elif model == "fin_empower":
    st.markdown(f"<h1 class='header-style'>التمكين المالي العام (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 T + \beta_3 W + \epsilon")
    z_m = st.slider("Z (المال المزكى)", 0, 100, 75)
    st.metric("مؤشر التمكين (Y)", f"{10 + 0.4*z_m + 30:.2f}")

elif model == "monetary_composite":
    st.markdown(f"<h1 class='header-style'>النموذج النقدي المركب (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta
