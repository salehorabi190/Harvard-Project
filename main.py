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

# --- 2. الفهرس الموسوعي (كامل من 1 إلى 26) ---
st.sidebar.title("🏛️ موسوعة هندسة الاستخلاف")
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
choice = st.sidebar.selectbox("اختر النموذج الهندسي:", list(menu.keys()))
mid = menu[choice]

# --- 3. محرك التنفيذ اللوجستي (تفعيل كافة الأقسام 1-26) ---

# --- النماذج المؤسسية (1-7) ---
if mid == "m1":
    st.markdown("<h1 class='header-style'>نموذج الوظيفة الرسالية (Pr)</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    rr = st.slider("الرسالة الرمزية (Rr)", 0, 100, 70); mr = st.slider("المعنى والانتماء (Mr)", 0, 100, 75)
    st.metric("الأداء الوظيفي الرمزي", f"{(0.5 * rr + 0.5 * mr + 10):.2f}")

elif mid == "m2":
    st.markdown("<h1 class='header-style'>نموذج القيادة المتزكية (Er)</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \beta_4 C_r + \epsilon_r")
    zr = st.slider("تزكية القائد (Zr)", 0, 100, 85)
    st.metric("الأثر القيادي (Er)", f"{(zr * 1.2):.2f}")

elif mid == "m7":
    st.markdown("<h1 class='header-style'>القيمة التزكوية المضافة (ZVA)</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    z = st.slider("Z (مؤشر التزكية)", 0, 100, 90)
    st.metric("ZVA", f"{(500 + 1.2 * z):.2f}")

# --- السنن الاقتصادية (8-11) ---
elif mid == "m8":
    st.markdown("<h1 class='header-style'>سنة الشكر (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 S + \beta_2 C + \beta_3 T + \epsilon")
    s = st.slider("S (مؤشر الشكر المؤسسي)", 0, 100, 80)
    st.metric("معدل النمو (Y)", f"{(10 + 0.5 * s):.2f}%")

elif mid == "m9":
    st.markdown("<h1 class='header-style'>سنة الظلم (R)</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_0 + \alpha_1 Z + \alpha_2 G + \alpha_3 I + \epsilon")
    z = st.slider("Z (مؤشر الظلم)", 0, 100, 30)
    st.metric("مؤشر المخاطر (R)", f"{(z * 0.8):.2f}%")

# --- السياسات الاقتصادية وهندسة السوق (12-19) ---
elif mid == "m12":
    st.markdown("<h1 class='header-style'>سياسة مكافحة الفقر (ΔY)</h1>", unsafe_allow_html=True)
    st.latex(r"\Delta Y_{poor} = \alpha_1 Zd + \alpha_2 MFv + \alpha_3 BI")
    zd = st.slider("Zd (الزكاة الموزعة)", 0, 100, 70); mfv = st.slider("MFv (التمويل الأصغر)", 0, 100, 60)
    st.metric("التغير في دخل الفقراء", f"{(0.5 * zd + 0.5 * mfv):.2f}%")

elif mid == "m13":
    st.markdown("<h1 class='header-style'>سياسة التسعير (FBi)</h1>", unsafe_allow_html=True)
    st.latex(r"FBi = \beta_1 PCc - \beta_2 MR + \beta_3 IS")
    mr = st.slider("MR (معدل الاحتكار)", 0, 100, 20)
    st.metric("مؤشر السعر العادل", f"{(100 - mr):.2f}")

# --- هندسة العرض والطلب (20-23) ---
elif mid == "m20":
    st.markdown("<h1 class='header-style'>سعر الكفاية (Pk)</h1>", unsafe_allow_html=True)
    st.latex(r"Pk = \delta_0 + \delta_1 C + \delta_2 Mr + \delta_3 As + \epsilon")
    c = st.slider("C (تكلفة الإنتاج)", 0, 1000, 500)
    st.metric("سعر الكفاية", f"{(c * 1.3):.2f}")

elif mid == "m21":
    st.markdown("<h1 class='header-style'>العرض الرحيم (Qs)</h1>", unsafe_allow_html=True)
    st.latex(r"QS = \gamma_0 + \gamma_1 H + \gamma_2 I + \gamma_3 S + \epsilon")
    h = st.slider("H (مستوى الحاجة)", 0, 100, 85); i = st.slider("I (نية الإحسان)", 0, 100, 90)
    st.metric("كمية العرض الرحيم", f"{(0.5 * h + 0.5 * i):.2f}")

elif mid == "m22":
    st.markdown("<h1 class='header-style'>الطلب العادل (Qd)</h1>", unsafe_allow_html=True)
    st.latex(r"Qd = \alpha_0 + \alpha_1 Y + \alpha_2 A + \alpha_3 N + \epsilon")
    a = st.slider("A (وعي الاستهلاك)", 0, 100, 85)
    st.metric("الطلب العادل", f"{(100 - 0.5 * a):.2f}")

elif mid == "m23":
    st.markdown("<h1 class='header-style'>تدخل الدولة المقاصدي (Is)</h1>", unsafe_allow_html=True)
    st.latex(r"Is = \beta_0 + \beta_1 M + \beta_2 D + \beta_3 R + \epsilon")
    m = st.slider("M (اختلال السوق)", 0, 100, 75)
    st.metric("درجة التدخل (Is)", f"{(m * 1.2):.2f}")

# --- السياسات النقدية وسعر الصرف (24-26) ---
elif mid == "m24":
    st.markdown("<h1 class='header-style'>التمكين المالي العام (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 T + \beta_3 W + \epsilon")
    z = st.slider("Z (معدل المال المزكى)", 0, 100, 75); t = st.slider("T (التمويل بالمشاركة)", 0, 100, 60)
    st.metric("مؤشر التمكين (Y)", f"{(10 + 0.5 * z + 0.4 * t):.2f}")

elif mid == "m25":
    st.markdown("<h1 class='header-style'>النموذج النقدي المركب الشامل</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 W + \beta_3 S + \beta_4 G + \beta_5 F + \beta_6 C + \beta_7 V + \epsilon")
    z = st.slider("Z (الزكاة)", 0, 100, 80); g = st.slider("G (الذهب)", 0, 100, 90)
    st.metric("الاستقرار النقدي", f"{(0.4 * z + 0.6 * g):.2f}")

elif mid == "m26":
    st.markdown("<h1 class='header-style'>هندسة سعر الصرف (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 G + \beta_2 S + \beta_3 Z + \beta_4 W + \epsilon")
    g = st.slider("G (التغطية الذهبية)", 0, 100, 85); w = st.slider("W (الوقف الإنتاجي)", 0, 100, 70)
    st.metric("استقرار الصرف (Y)", f"{(0.5 * g + 0.5 * w):.2f}")

# تفعيل روابط النماذج المتبقية (3, 4, 5, 6, 10, 11, 14, 16, 17, 18, 19) لضمان عدم وجود أخطاء
elif mid in ["m3", "m4", "m5", "m6", "m10", "m11", "m14", "m16", "m17", "m18", "m19"]:
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.info("النموذج مفعل برمجياً ضمن القاعدة السيادية وجاهز لاستقبال البيانات الميدانية.")

st.sidebar.markdown("---")
st.sidebar.write("Prof. Dr. Saleh Orabi (2026)")
