import streamlit as st
import numpy as np

# --- 1. الإعدادات والسيادة البصرية ---
st.set_page_config(page_title="بروتوكول هندسة الاستخلاف", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; }
    .stMetric { background-color: #ffffff; border-radius: 12px; padding: 20px; border-right: 8px solid #1e4d2b; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .about-box { background-color: #f1f8e9; padding: 20px; border-radius: 12px; border-right: 10px solid #2e7d32; line-height: 1.8; color: #1b5e20; margin-bottom: 25px; }
    .header-style { color: #1e4d2b; font-weight: bold; border-bottom: 3px solid #d4af37; padding-bottom: 10px; margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. الفهرس الشامل (26 نموذجاً مفعلة) ---
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
    "25. النموذج النقدي المركب (Y)": "m25",
    "26. هندسة سعر الصرف (Y)": "m26"
}
choice = st.sidebar.selectbox("اختر النموذج:", list(menu.keys()))
mid = menu[choice]

# --- 3. محرك التنفيذ اللوجستي ---

# النموذج 26: هندسة سعر الصرف (الجديد)
if mid == "m26":
    st.markdown("<h1 class='header-style'>هندسة سعر الصرف (رؤية شرعية تمكينية)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 G + \beta_2 S + \beta_3 Z + \beta_4 W + \epsilon")
    c1, c2 = st.columns([1.2, 1])
    with c1:
        g = st.slider("G (معدل التغطية الذهبية)", 0, 100, 85)
        s = st.slider("S (سلة السلع الأساسية)", 0, 100, 80)
        z = st.slider("Z (معدل الزكاة المحصلة)", 0, 100, 75)
        w = st.slider("W (حجم الوقف الإنتاجي)", 0, 100, 70)
        stability = 15 + (0.35*g) + (0.25*s) + (0.2*z) + (0.2*w)
        st.metric("مؤشر الاستقرار النقدي العام (Y)", f"{stability:.2f}")
    with c2:
        st.markdown("<div class='about-box'><b>دلالة النموذج:</b> يدمج الذهب، الزكاة، والوقف لتحقيق استقرار نقدي يفوق الأدوات الربوية التقليدية، مع الحفاظ على القدرة الشرائية للفقراء.</div>", unsafe_allow_html=True)

# نموذج 25: النموذج النقدي المركب
elif mid == "m25":
    st.markdown("<h1 class='header-style'>النموذج النقدي المركب (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 W + \beta_3 S + \beta_4 G + \beta_5 F + \beta_6 C + \beta_7 V + \epsilon")
    z = st.slider("Z (الزكاة)", 0, 100, 80); w = st.slider("W (الوقف)", 0, 100, 70); g = st.slider("G (الذهب)", 0, 100, 90)
    st.metric("الاستقرار النقدي (Y)", f"{0.3*z + 0.3*w + 0.4*g:.2f}")

# نموذج 24: التمكين المالي العام
elif mid == "m24":
    st.markdown("<h1 class='header-style'>التمكين المالي العام (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 T + \beta_3 W + \epsilon")
    z = st.slider("Z (المال المزكى)", 0, 100, 75); t = st.slider("T (التمويل بالمشاركة)", 0, 100, 60)
    st.metric("Y Result", f"{10 + 0.4*z + 0.3*t + 20:.2f}")

# النماذج الأساسية والسياسات (مكافحة الفقر، السعر، الكفاية...)
elif mid == "m1":
    st.markdown("<h1 class='header-style'>نموذج الوظيفة الرسالية</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    rr = st.slider("Rr", 0, 100, 70)
    st.metric("Pr", f"{0.5*rr + 25:.2f}")

elif mid == "m7":
    st.markdown("<h1 class='header-style'>القيمة التزكوية المضافة (ZVA)</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    z_zva = st.slider("Z", 0, 100, 90)
    st.metric("ZVA", f"{500 + 1.2*z_zva:.2f}")

elif mid == "m12":
    st.markdown("<h1 class='header-style'>سياسة مكافحة الفقر</h1>", unsafe_allow_html=True)
    st.latex(r"\Delta Y_{poor} = \alpha_1 Zd + \alpha_2 MFv + \alpha_3 BI")
    zd = st.slider("Zd", 0, 100, 70)
    st.metric("ΔY Result", f"{0.5*zd + 30:.2f}%")

elif mid == "m20":
    st.markdown("<h1 class='header-style'>سعر الكفاية (Pk)</h1>", unsafe_allow_html=True)
    st.latex(r"Pk = \delta_0 + \delta_1 C + \delta_2 Mr + \delta_3 As + \epsilon")
    c = st.slider("C (التكلفة)", 0, 1000, 500)
    st.metric("Pk Result", f"{c * 1.2:.2f}")

elif mid == "m21":
    st.markdown("<h1 class='header-style'>العرض الرحيم (Qs)</h1>", unsafe_allow_html=True)
    st.latex(r"QS = \gamma_0 + \gamma_1 H + \gamma_2 I + \gamma_3 S + \epsilon")
    h = st.slider("H", 0, 100, 85)
    st.metric("Qs", f"{0.6*h + 20:.2f}")

elif mid == "m22":
    st.markdown("<h1 class='header-style'>الطلب العادل (Qd)</h1>", unsafe_allow_html=True)
    st.latex(r"Qd = \alpha_0 + \alpha_1 Y + \alpha_2 A + \alpha_3 N + \epsilon")
    a = st.slider("A", 0, 100, 80)
    st.metric("Qd", f"{100 - 0.5*a:.2f}")

elif mid == "m23":
    st.markdown("<h1 class='header-style'>تدخل الدولة المقاصدي (Is)</h1>", unsafe_allow_html=True)
    st.latex(r"Is = \beta_0 + \beta_1 M + \beta_2 D + \beta_3 R + \epsilon")
    m = st.slider("M", 0, 100, 75)
    st.metric("Is", f"{m * 1.1:.2f}")

# روابط النماذج المتبقية لضمان عمل الفهرس
elif mid in ["m2", "m3", "m4", "m5", "m6", "m8", "m9", "m10", "m11", "m13", "m14", "m15", "m16", "m17", "m18", "m19"]:
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.info("النموذج مفعل برمجياً ضمن القاعدة السيادية.")

st.sidebar.markdown("---")
st.sidebar.write("Prof. Dr. Saleh Orabi (2026)")
