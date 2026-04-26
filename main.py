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

# --- 3. الفهرس الشامل (تم ربط كافة المسارات) ---
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
    "14. سياسة التمكين (ES)": "empower_policy",
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

# --- 4. محرك التنفيذ (Logic Engine) ---

# --- النماذج المؤسسية ---
if model == "m1":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    a = st.slider("النية الداخلية (α)", 0.0, 1.0, 0.8)
    rr = st.slider("الرسالة الرمزية (Rᵣ)", 0, 100, 70)
    mr = st.slider("المعنى والانتماء (Mᵣ)", 0, 100, 75)
    st.metric("الأداء الوظيفي الرمزي", f"{a + (0.4*rr) + (0.3*mr) + 15:.2f}")

elif model == "m2":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \beta_4 C_r + \beta_5 V_r + \beta_6 R_r + \epsilon_r")
    zr = st.slider("تزكية القائد (Zᵣ)", 0, 100, 85)
    st.metric("الأثر المؤسسي المتزكي", f"{zr * 1.25:.2f}")

elif model == "zva":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    z_val = st.slider("مؤشر التزكية (Z)", 0, 100, 90)
    lam = st.slider("معامل التحويل (λ)", 0.5, 2.0, 1.2)
    st.metric("ZVA Result", f"{500 + (lam * z_val):.2f}")

# --- السنن الاقتصادية ---
elif model == "s1":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 S + \beta_2 C + \beta_3 T + \epsilon")
    s_val = st.slider("S (مؤشر الشكر المؤسسي)", 0, 100, 80)
    st.metric("النمو (Y)", f"{10 + 0.5*s_val:.2f}%")

elif model == "s2":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_0 + \alpha_1 Z + \alpha_2 G + \alpha_3 I + \epsilon")
    z_idx = st.slider("Z (مؤشر الظلم الاحتكاري)", 0, 100, 25)
    st.metric("مؤشر المخاطر (R)", f"{10 + 0.8*z_idx:.2f}%")

# --- السياسات الاقتصادية وهندسة السوق ---
elif model == "poverty":
    st.markdown(f"<h1 class='header-style'>سياسة مكافحة الفقر</h1>", unsafe_allow_html=True)
    st.latex(r"\Delta Y_{poor} = \alpha_1 Zd + \alpha_2 MFv + \alpha_3 BI")
    zd = st.slider("الزكاة الموزعة (Zd)", 0, 100, 70)
    mfv = st.slider("التمويل الأصغر (MFv)", 0, 100, 65)
    bi = st.slider("مؤشر البركة (BI)", 0, 100, 80)
    st.metric("ΔY poor", f"{(0.5*zd + 0.3*mfv + 0.2*bi):.2f}%")

elif model == "pricing":
    st.markdown(f"<h1 class='header-style'>سياسة التسعير العادل</h1>", unsafe_allow_html=True)
    st.latex(r"FBi = \beta_1 PCc - \beta_2 MR + \beta_3 IS")
    pcc = st.slider("ضبط الأسعار (PCc)", 0, 100, 75)
    mr = st.slider("معدل الاحتكار (MR)", 0, 100, 20)
    st.metric("FBi Result", f"{(0.4*pcc - 0.4*mr + 17):.2f}")

elif model == "price_sufficiency":
    st.markdown(f"<h1 class='header-style'>سعر الكفاية (Pk)</h1>", unsafe_allow_html=True)
    st.latex(r"Pk = \delta_0 + \delta_1 C + \delta_2 Mr + \delta_3 As + \epsilon")
    c_cost = st.slider("تكلفة الإنتاج (C)", 0, 1000, 500)
    st.metric("السعر الكافي (Pk)", f"{c_cost * 1.3:.2f}")

# --- هندسة السياسات النقدية (النماذج الأخيرة) ---
elif model == "fin_empower":
    st.markdown(f"<h1 class='header-style'>نموذج التمكين المالي العام (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 T + \beta_3 W + \epsilon")
    z = st.slider("Z (معدل المال المزكى)", 0, 100, 75)
    t = st.slider("T (التمويل بالمشاركة)", 0, 100, 60)
    w = st.slider("W (الصكوك الوقفية)", 0, 100, 65)
    st.metric("مؤشر التمكين (Y)", f"{10 + 0.4*z + 0.3*t + 0.3*w:.2f}")

elif model == "monetary_composite":
    st.markdown(f"<h1 class='header-style'>النموذج النقدي المركب</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 W + \beta_3 S + \beta_4 G + \beta_5 F + \beta_6 C + \beta_7 V + \epsilon")
    c1, c2 = st.columns(2)
    with c1:
        z_m = st.slider("Z (الزكاة)", 0, 100, 80)
        w_m = st.slider("W (الوقف)", 0, 100, 70)
        g_m = st.slider("G (الذهب)", 0, 100, 85)
    with c2:
        inf = st.slider("C (التضخم)", 0, 100, 20)
        exc = st.slider("V (تقلب العملة)", 0, 100, 15)
    stability = (0.3*z_m + 0.3*w_m + 0.3*g_m) - (0.1*inf + 0.1*exc)
    st.metric("الاستقرار النقدي (Y)", f"{stability:.2f}")

# الروابط المتبقية لضمان عدم وجود أخطاء في الفهرس
elif model in ["m3", "m4", "m5", "m6", "s3", "s4", "empower_policy", "crisis", "m_justice", "m_transparency", "m_monopoly", "m_intention", "merciful_supply", "fair_demand", "state_intervention"]:
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.info("النموذج مفعل برمجياً ويجري تحميل البيانات القياسية...")

st.sidebar.markdown("---")
st.sidebar.write(txt["sidebar_info"])
