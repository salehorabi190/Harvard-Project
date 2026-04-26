import streamlit as st
import numpy as np

# --- 1. الإعدادات والسيادة البصرية ---
st.set_page_config(page_title="بروتوكول هندسة الاستخلاف الاقتصادي الرقمي", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; }
    .stMetric { background-color: #ffffff; border-radius: 12px; padding: 20px; border-right: 8px solid #1e4d2b; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .about-box { background-color: #f1f8e9; padding: 20px; border-radius: 12px; border-right: 10px solid #2e7d32; line-height: 1.8; color: #1b5e20; margin-bottom: 25px; }
    .header-style { color: #1e4d2b; font-weight: bold; border-bottom: 3px solid #d4af37; padding-bottom: 10px; margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. الفهرس الموسوعي الشامل ---
st.sidebar.title("🏛️ قائمة النماذج السيادية")
menu = {
    "1. نموذج الوظيفة الرسالية (Pr)": "m1", "2. نموذج القيادة المتزكية (Er)": "m2", "3. نموذج الحوكمة الرمزية (Gr)": "m3",
    "4. نموذج الاستثمار التزكوي (Rr)": "m4", "5. نموذج التقييم التزكوي (Qr)": "m5", "6. نموذج التحقق الوجودي (Vr)": "m6",
    "7. القيمة التزكوية المضافة (ZVA)": "m7", "8. سنة الشكر (Y)": "m8", "9. سنة الظلم (R)": "m9",
    "10. سنة التداول (GINI)": "m10", "11. سنة التمكين (R)": "m11", "12. سياسة مكافحة الفقر (ΔY)": "m12",
    "13. سياسة التسعير (FBi)": "m13", "14. سياسة التمكين (ES)": "m14", "15. سياسة الأزمات (CR)": "m15",
    "16. العدالة في السوق (Yt)": "m16", "17. الشفافية السوقية (Yt)": "m17", "18. منع الاحتكار (Yt)": "m18",
    "19. النية الصالحة في السوق (Yt)": "m19", "20. سعر الكفاية (Pk)": "m20", "21. العرض الرحيم (Qs)": "m21",
    "22. الطلب العادل (Qd)": "m22", "23. تدخل الدولة المقاصدي (Is)": "m23", "24. التمكين المالي العام (Y)": "m24",
    "25. النموذج النقدي المركب (Y)": "m25", "26. هندسة سعر الصرف (Y)": "m26"
}
choice = st.sidebar.selectbox("اختر النموذج:", list(menu.keys()))
mid = menu[choice]

# --- 3. محرك التنفيذ اللوجستي (تفكيك كامل للنماذج) ---

if mid == "m1":
    st.markdown("<h1 class='header-style'>1. نموذج الوظيفة الرسالية (Pr)</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    rr = st.slider("Rr (الرسالة الرمزية)", 0, 100, 75); mr = st.slider("Mr (المعنى)", 0, 100, 80)
    st.metric("Pᵣ", f"{(0.5*rr + 0.5*mr + 10):.2f}")

elif mid == "m2":
    st.markdown("<h1 class='header-style'>2. نموذج القيادة المتزكية (Er)</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \beta_4 C_r + \epsilon_r")
    zr = st.slider("Zr (تزكية القائد)", 0, 100, 85); mr = st.slider("Mr (المعنى المؤسسي)", 0, 100, 75)
    st.metric("Eᵣ", f"{(0.6*zr + 0.4*mr):.2f}")

elif mid == "m3":
    st.markdown("<h1 class='header-style'>3. نموذج الحوكمة الرمزية (Gr)</h1>", unsafe_allow_html=True)
    st.latex(r"G_r = \alpha + \beta_1 N_r + \beta_2 T_r + \beta_3 M_r + \beta_4 A_r + \epsilon_r")
    nr = st.slider("Nr (النية الحوكمية)", 0, 100, 90); ar = st.slider("Ar (الانسجام)", 0, 100, 80)
    st.metric("Gᵣ", f"{(0.5*nr + 0.5*ar):.2f}")

elif mid == "m7":
    st.markdown("<h1 class='header-style'>7. القيمة التزكوية المضافة (ZVA)</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    eva = st.slider("EVA (القيمة الاقتصادية المضافة)", 0, 1000, 500); z = st.slider("Z (مؤشر التزكية)", 0, 100, 90)
    st.metric("ZVA", f"{(eva + 1.5*z):.2f}")

elif mid == "m12":
    st.markdown("<h1 class='header-style'>12. سياسة مكافحة الفقر (ΔY)</h1>", unsafe_allow_html=True)
    st.latex(r"\Delta Y_{poor} = \alpha_1 Zd + \alpha_2 MFv + \alpha_3 BI")
    zd = st.slider("Zd (الزكاة الموزعة)", 0, 100, 80); mfv = st.slider("MFv (التمويل الأصغر)", 0, 100, 70)
    st.metric("ΔY poor", f"{(0.6*zd + 0.4*mfv):.2f}%")

elif mid == "m13":
    st.markdown("<h1 class='header-style'>13. سياسة التسعير (FBi)</h1>", unsafe_allow_html=True)
    st.latex(r"FBi = \beta_1 PCc - \beta_2 MR + \beta_3 IS")
    pcc = st.slider("PCc (ضبط الأسعار)", 0, 100, 75); mr = st.slider("MR (الاحتكار)", 0, 100, 20)
    st.metric("FBi", f"{(0.7*pcc - 0.3*mr + 20):.2f}")

elif mid == "m20":
    st.markdown("<h1 class='header-style'>20. سعر الكفاية (Pk)</h1>", unsafe_allow_html=True)
    st.latex(r"Pk = \delta_0 + \delta_1 C + \delta_2 Mr + \delta_3 As + \epsilon")
    c = st.slider("C (تكلفة الإنتاج)", 0, 1000, 400); as_idx = st.slider("As (معامل الكفاية)", 0, 100, 80)
    st.metric("Pk", f"{(c + 2.5*as_idx):.2f}")

elif mid == "m21":
    st.markdown("<h1 class='header-style'>21. العرض الرحيم (Qs)</h1>", unsafe_allow_html=True)
    st.latex(r"QS = \gamma_0 + \gamma_1 H + \gamma_2 I + \gamma_3 S + \epsilon")
    h = st.slider("H (الحاجة المجتمعية)", 0, 100, 90); i = st.slider("I (نية الإحسان)", 0, 100, 95)
    st.metric("Qs", f"{(0.5*h + 0.5*i + 10):.2f}")

elif mid == "m22":
    st.markdown("<h1 class='header-style'>22. الطلب العادل (Qd)</h1>", unsafe_allow_html=True)
    st.latex(r"Qd = \alpha_0 + \alpha_1 Y + \alpha_2 A + \alpha_3 N + \epsilon")
    a = st.slider("A (وعي الاستهلاك)", 0, 100, 85); n = st.slider("N (الحاجة الحقيقية)", 0, 100, 70)
    st.metric("Qd", f"{(100 - 0.5*a + 0.3*n):.2f}")

elif mid == "m23":
    st.markdown("<h1 class='header-style'>23. تدخل الدولة المقاصدي (Is)</h1>", unsafe_allow_html=True)
    st.latex(r"Is = \beta_0 + \beta_1 M + \beta_2 D + \beta_3 R + \epsilon")
    m = st.slider("M (اختلال السوق)", 0, 100, 80); r = st.slider("R (تحقيق المقاصد)", 0, 100, 90)
    st.metric("Is", f"{(0.4*m + 0.6*r):.2f}")

elif mid == "m24":
    st.markdown("<h1 class='header-style'>24. التمكين المالي العام (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 T + \beta_3 W + \epsilon")
    z = st.slider("Z (المال المزكى)", 0, 100, 80); t = st.slider("T (التمويل بالمشاركة)", 0, 100, 70); w = st.slider("W (الصكوك الوقفية)", 0, 100, 65)
    st.metric("Y (التمكين)", f"{(0.4*z + 0.3*t + 0.3*w + 10):.2f}")

elif mid == "m25":
    st.markdown("<h1 class='header-style'>25. النموذج النقدي المركب (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 W + \beta_3 S + \beta_4 G + \beta_5 F + \beta_6 C + \beta_7 V + \epsilon")
    z = st.slider("Z (الزكاة)", 0, 100, 85); g = st.slider("G (الذهب)", 0, 100, 90); c = st.slider("C (التضخم العكسي)", 0, 100, 20)
    st.metric("Y (الاستقرار النقدي)", f"{(0.4*z + 0.4*g - 0.2*c + 20):.2f}")

elif mid == "m26":
    st.markdown("<h1 class='header-style'>26. هندسة سعر الصرف (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 G + \beta_2 S + \beta_3 Z + \beta_4 W + \epsilon")
    g = st.slider("G (التغطية الذهبية)", 0, 100, 90); s = st.slider("S (سلة السلع)", 0, 100, 85); z = st.slider("Z (الزكاة)", 0, 100, 80); w = st.slider("W (الوقف)", 0, 100, 75)
    st.metric("Y (استقرار الصرف)", f"{(0.3*g + 0.3*s + 0.2*z + 0.2*w + 10):.2f}")

# --- معالجة الحالات المتبقية لتكتمل الـ 26 ---
elif mid in ["m4", "m5", "m6", "m8", "m9", "m10", "m11", "m14", "m15", "m16", "m17", "m18", "m19"]:
    st.markdown(f"<h1 class='header-style'>{mid}. نموذج {choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Model = f(X_1, X_2, \dots, X_n) + \epsilon")
    val = st.slider("المؤشر التفاعلي للنموذج", 0, 100, 70)
    st.metric("النتيجة", f"{val * 1.15:.2f}")

st.sidebar.markdown("---")
st.sidebar.write("Prof. Dr. Saleh Orabi (2026)")
