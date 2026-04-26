import streamlit as st
import numpy as np

# --- 1. الإعدادات والسيادة البصرية ---
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

# --- 2. الفهرس الشامل لكل ما أرسلته ---
st.sidebar.title("🏛️ الموسوعة الاقتصادية السيادية")
menu = {
    "1. نموذج الوظيفة الرسالية (Pr)": "m1",
    "2. نموذج القيادة المتزكية (Er)": "m2",
    "3. نموذج الحوكمة الرمزية (Gr)": "m3",
    "4. نموذج الاستثمار التزكوي (Rr)": "m4",
    "5. نموذج التقييم التزكوي (Qr)": "m5",
    "6. نموذج التحقق الوجودي (Vr)": "m6",
    "7. القيمة التزكوية المضافة (ZVA)": "m7",
    "8. سنة الشكر (Y)": "m8",
    "9. سنة الظلم (R)": "m9",
    "10. سنة التداول (GINI)": "m10",
    "11. سنة التمكين (R)": "m11",
    "12. سياسة مكافحة الفقر (ΔY)": "m12",
    "13. سياسة التسعير (FBi)": "m13",
    "14. سياسة التمكين (ES)": "m14",
    "15. سياسة الأزمات (CR)": "m15",
    "16. العدالة في السوق (Yt)": "m16",
    "17. الشفافية السوقية (Yt)": "m17",
    "18. منع الاحتكار (Yt)": "m18",
    "19. النية الصالحة في السوق (Yt)": "m19",
    "20. سعر الكفاية (Pk)": "m20",
    "21. العرض الرحيم (Qs)": "m21",
    "22. الطلب العادل (Qd)": "m22",
    "23. تدخل الدولة المقاصدي (Is)": "m23",
    "24. التمكين المالي العام (Y)": "m24",
    "25. النموذج النقدي المركب (Y)": "m25"
}
choice = st.sidebar.selectbox("اختر النموذج:", list(menu.keys()))
mid = menu[choice]

# --- 3. محرك التنفيذ الكامل ---

if mid == "m1":
    st.markdown("<h1 class='header-style'>نموذج الوظيفة الرسالية</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    rr = st.slider("Rr (الرسالة الرمزية)", 0, 100, 70)
    st.metric("Pr Result", f"{0.5*rr + 25:.2f}")

elif mid == "m7":
    st.markdown("<h1 class='header-style'>القيمة التزكوية المضافة (ZVA)</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    z = st.slider("Z (مؤشر التزكية)", 0, 100, 90)
    st.metric("ZVA Result", f"{500 + 1.2*z:.2f}")

elif mid == "m12":
    st.markdown("<h1 class='header-style'>سياسة مكافحة الفقر (ΔY poor)</h1>", unsafe_allow_html=True)
    st.latex(r"\Delta Y_{poor} = \alpha_1 Zd + \alpha_2 MFv + \alpha_3 BI")
    zd = st.slider("Zd (الزكاة الموزعة)", 0, 100, 70)
    mfv = st.slider("MFv (التمويل الأصغر)", 0, 100, 60)
    bi = st.slider("BI (مؤشر البركة)", 0, 100, 80)
    st.metric("ΔY Result", f"{0.5*zd + 0.3*mfv + 0.2*bi:.2f}%")

elif mid == "m13":
    st.markdown("<h1 class='header-style'>سياسة التسعير (FBi)</h1>", unsafe_allow_html=True)
    st.latex(r"FBi = \beta_1 PCc - \beta_2 MR + \beta_3 IS")
    pcc = st.slider("PCc (ضبط الأسعار)", 0, 100, 75)
    mr = st.slider("MR (معدل الاحتكار)", 0, 100, 20)
    st.metric("FBi Result", f"{0.4*pcc - 0.4*mr + 20:.2f}")

elif mid == "m20":
    st.markdown("<h1 class='header-style'>سعر الكفاية (Pk)</h1>", unsafe_allow_html=True)
    st.latex(r"Pk = \delta_0 + \delta_1 C + \delta_2 Mr + \delta_3 As + \epsilon")
    c = st.slider("C (التكلفة)", 0, 1000, 500)
    as_idx = st.slider("As (الكفاية الاجتماعية)", 0, 100, 75)
    st.metric("Pk Result", f"{c + 2*as_idx:.2f}")

elif mid == "m21":
    st.markdown("<h1 class='header-style'>العرض الرحيم (Qs)</h1>", unsafe_allow_html=True)
    st.latex(r"QS = \gamma_0 + \gamma_1 H + \gamma_2 I + \gamma_3 S + \epsilon")
    h = st.slider("H (مستوى الحاجة)", 0, 100, 85)
    i = st.slider("I (نية الإحسان)", 0, 100, 90)
    st.metric("Qs Result", f"{0.5*h + 0.4*i + 10:.2f}")

elif mid == "m22":
    st.markdown("<h1 class='header-style'>الطلب العادل (Qd)</h1>", unsafe_allow_html=True)
    st.latex(r"Qd = \alpha_0 + \alpha_1 Y + \alpha_2 A + \alpha_3 N + \epsilon")
    a = st.slider("A (وعي الاستهلاك)", 0, 100, 80)
    n = st.slider("N (الحاجة الحقيقية)", 0, 100, 70)
    st.metric("Qd Result", f"{100 - 0.5*a + 0.3*n:.2f}")

elif mid == "m23":
    st.markdown("<h1 class='header-style'>تدخل الدولة المقاصدي (Is)</h1>", unsafe_allow_html=True)
    st.latex(r"Is = \beta_0 + \beta_1 M + \beta_2 D + \beta_3 R + \epsilon")
    m = st.slider("M (اختلال السوق)", 0, 100, 75)
    r = st.slider("R (تحقيق المقاصد)", 0, 100, 90)
    st.metric("Is Result", f"{0.4*m + 0.3*r + 15:.2f}")

elif mid == "m24":
    st.markdown("<h1 class='header-style'>التمكين المالي العام (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 T + \beta_3 W + \epsilon")
    z = st.slider("Z (المال المزكى)", 0, 100, 75)
    t = st.slider("T (التمويل بالمشاركة)", 0, 100, 60)
    w = st.slider("W (الصكوك الوقفية)", 0, 100, 65)
    st.metric("Y Result", f"{10 + 0.4*z + 0.3*t + 0.3*w:.2f}")

elif mid == "m25":
    st.markdown("<h1 class='header-style'>النموذج النقدي المركب (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 W + \beta_3 S + \beta_4 G + \beta_5 F + \beta_6 C + \beta_7 V + \epsilon")
    z = st.slider("Z (الزكاة)", 0, 100, 80)
    w = st.slider("W (الوقف)", 0, 100, 70)
    g = st.slider("G (الذهب)", 0, 100, 90)
    st.metric("الاستقرار النقدي (Y)", f"{0.3*z + 0.3*w + 0.4*g:.2f}")

else:
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.info("النموذج قيد التفعيل الرياضي...")

st.sidebar.markdown("---")
st.sidebar.write("Prof. Dr. Saleh Orabi (2026)")
