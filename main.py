import streamlit as st
import numpy as np

# --- 1. الإعدادات العامة ---
st.set_page_config(page_title="بروتوكول هندسة الاستخلاف", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; }
    .stMetric { background-color: #ffffff; border-radius: 12px; padding: 20px; border-right: 8px solid #1e4d2b; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .about-box { background-color: #e8f5e9; padding: 20px; border-radius: 12px; border-right: 10px solid #1e4d2b; line-height: 1.8; color: #11301a; margin-bottom: 20px; }
    .header-style { color: #1e4d2b; font-weight: bold; border-bottom: 2px solid #d4af37; padding-bottom: 10px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. محرك القائمة (تم تبسيط الربط لضمان العمل) ---
st.sidebar.title("🏛️ الفهرس السيادي")
st.sidebar.write("Prof. Dr. Saleh Orabi")

# قائمة النماذج (المفتاح هو الرقم لسهولة الربط)
menu_options = {
    "1. نموذج الوظيفة الرسالية (Pr)": "1",
    "7. القيمة التزكوية المضافة (ZVA)": "7",
    "12. سياسة مكافحة الفقر (ΔY)": "12",
    "13. سياسة التسعير العادل (FBi)": "13",
    "20. سعر الكفاية (Pk)": "20",
    "24. التمكين المالي العام (Y)": "24",
    "25. النموذج النقدي المركب (Y)": "25"
}

choice = st.sidebar.selectbox("اختر النموذج:", list(menu_options.keys()))
model_id = menu_options[choice]

# --- 3. محرك التنفيذ (Logic) ---

# نموذج 1: الوظيفة الرسالية
if model_id == "1":
    st.markdown("<h1 class='header-style'>نموذج الوظيفة الرسالية (Pr)</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    a = st.slider("النية الداخلية (α)", 0.0, 1.0, 0.8)
    rr = st.slider("الرسالة الرمزية (Rr)", 0, 100, 70)
    st.metric("Pᵣ Output", f"{a + (0.4*rr) + 20:.2f}")

# نموذج 7: ZVA
elif model_id == "7":
    st.markdown("<h1 class='header-style'>القيمة التزكوية المضافة (ZVA)</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    z = st.slider("مؤشر التزكية (Z)", 0, 100, 90)
    lam = st.slider("معامل التحويل (λ)", 0.5, 2.0, 1.2)
    st.metric("ZVA Result", f"{500 + (lam * z):.2f}")

# نموذج 12: مكافحة الفقر
elif model_id == "12":
    st.markdown("<h1 class='header-style'>سياسة مكافحة الفقر (ΔY)</h1>", unsafe_allow_html=True)
    st.latex(r"\Delta Y_{poor} = \alpha_1 Zd + \alpha_2 MFv + \alpha_3 BI")
    zd = st.slider("الزكاة الموزعة (Zd)", 0, 100, 70)
    mfv = st.slider("التمويل الأصغر (MFv)", 0, 100, 60)
    bi = st.slider("مؤشر البركة (BI)", 0, 100, 80)
    st.metric("ΔY poor", f"{(0.5*zd + 0.3*mfv + 0.2*bi):.2f}%")

# نموذج 13: التسعير
elif model_id == "13":
    st.markdown("<h1 class='header-style'>سياسة التسعير العادل (FBi)</h1>", unsafe_allow_html=True)
    st.latex(r"FBi = \beta_1 PCc - \beta_2 MR + \beta_3 IS")
    pcc = st.slider("ضبط الأسعار (PCc)", 0, 100, 75)
    mr = st.slider("معدل الاحتكار (MR)", 0, 100, 20)
    st.metric("FBi Result", f"{(0.4*pcc - 0.4*mr + 20):.2f}")

# نموذج 20: سعر الكفاية
elif model_id == "20":
    st.markdown("<h1 class='header-style'>سعر الكفاية (Pk)</h1>", unsafe_allow_html=True)
    st.latex(r"Pk = \delta_0 + \delta_1 C + \delta_2 Mr + \delta_3 As + \epsilon")
    c_cost = st.slider("تكلفة الإنتاج (C)", 0, 1000, 500)
    as_idx = st.slider("الكفاية الاجتماعية (As)", 0, 100, 70)
    st.metric("Pk Result", f"{c_cost + (2 * as_idx):.2f}")

# نموذج 24: التمكين المالي
elif model_id == "24":
    st.markdown("<h1 class='header-style'>التمكين المالي العام (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 T + \beta_3 W + \epsilon")
    z = st.slider("المال المزكى (Z)", 0, 100, 80)
    t = st.slider("التمويل بالمشاركة (T)", 0, 100, 70)
    st.metric("مؤشر التمكين (Y)", f"{10 + 0.5*z + 0.4*t:.2f}")

# نموذج 25: النقدي المركب
elif model_id == "25":
    st.markdown("<h1 class='header-style'>النموذج النقدي المركب (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 W + \beta_3 S + \beta_4 G + \beta_5 F + \beta_6 C + \beta_7 V + \epsilon")
    z_m = st.slider("الزكاة (Z)", 0, 100, 85)
    g_m = st.slider("الذهب (G)", 0, 100, 90)
    st.metric("الاستقرار النقدي", f"{(0.5*z_m + 0.5*g_m):.2f}")

st.sidebar.markdown("---")
st.sidebar.write("2026 © Prof. Dr. Saleh Orabi")
