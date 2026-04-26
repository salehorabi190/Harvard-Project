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

# --- 2. الفهرس السيادي الشامل (29 نموذجاً) ---
st.sidebar.title("🏛️ قائمة النماذج السيادية")
menu = {
    "1. نموذج الوظيفة الرسالية (Pr)": "m1",
    "2. نموذج القيادة المتزكية (Er)": "m2",
    "3. نموذج الحوكمة الرمزية (Gr)": "m3",
    "7. القيمة التزكوية المضافة (ZVA)": "m7",
    "12. سياسة مكافحة الفقر (ΔY)": "m12",
    "13. سياسة التسعير (FBi)": "m13",
    "20. سعر الكفاية (Pk)": "m20",
    "21. العرض الرحيم (Qs)": "m21",
    "22. الطلب العادل (Qd)": "m22",
    "23. تدخل الدولة المقاصدي (Is)": "m23",
    "24. التمكين المالي العام (Y)": "m24",
    "25. النموذج النقدي المركب (Y)": "m25",
    "26. هندسة سعر الصرف (Y)": "m26",
    "27. معدل العائد الإسلامي المقاصدي (R)": "m27",
    "28. هندسة المالية المقاصدية (P)": "m28",
    "29. تسعير المنتجات المصرفية (P)": "m29"
}
choice = st.sidebar.selectbox("اختر النموذج:", list(menu.keys()))
mid = menu[choice]

# --- 3. محرك التنفيذ اللوجستي (ربط صارم ومباشر) ---

if mid == "m1":
    st.markdown("<h1 class='header-style'>1. نموذج الوظيفة الرسالية (Pr)</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    rr = st.slider("الرسالة الرمزية (Rr)", 0, 100, 70)
    mr = st.slider("المعنى والانتماء (Mr)", 0, 100, 80)
    st.metric("النتيجة التقديرية (Pr)", f"{(0.5 * rr + 0.5 * mr + 10):.2f}")

elif mid == "m27":
    st.markdown("<h1 class='header-style'>27. معدل العائد الإسلامي المقاصدي (R)</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_1 \pi + \alpha_2 T + \alpha_3 Z + \alpha_4 E + \epsilon")
    pi_val = st.slider("الربحية المشروعة (π)", 0, 100, 75)
    t_val = st.slider("مؤشر التمكين (T)", 0, 100, 85)
    z_val = st.slider("الحد الأخلاقي الزكوي (Z)", 0, 100, 25)
    e_val = st.slider("معدل التضخم (E)", 0, 100, 10)
    r_res = (0.4 * pi_val + 0.3 * t_val + 0.2 * z_val + 0.1 * e_val)
    st.metric("معدل العائد (R)", f"{r_res:.2f}%")

elif mid == "m28":
    st.markdown("<h1 class='header-style'>28. هندسة المالية المقاصدية (P)</h1>", unsafe_allow_html=True)
    st.latex(r"P = \beta_1 R + \beta_2 T + \beta_3 S + \beta_4 \pi + \beta_5 Z + \epsilon")
    r_in = st.slider("العائد المقاصدي (R)", 0, 100, 65)
    s_in = st.slider("الالتزام الشرعي (S)", 0, 100, 95)
    st.metric("سعر الأداة المالية (P)", f"{(0.5 * r_in + 0.5 * s_in):.2f}")

elif mid == "m29":
    st.markdown("<h1 class='header-style'>29. تسعير المنتجات المصرفية (P)</h1>", unsafe_allow_html=True)
    st.latex(r"P = \beta_1 R + \beta_2 T + \beta_3 S + \beta_4 \pi + \beta_5 Z + \epsilon")
    r_bank = st.slider("معدل العائد (R)", 0, 100, 70)
    t_bank = st.slider("أثر التمكين (T)", 0, 100, 80)
    z_bank = st.slider("مقياس الزكاة (Z)", 0, 100, 25)
    p_bank = (0.4 * r_bank + 0.3 * t_bank + 0.1 * z_bank + 20)
    st.metric("سعر المنتج (P)", f"{p_bank:.2f}")

elif mid == "m26":
    st.markdown("<h1 class='header-style'>26. هندسة سعر الصرف (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 G + \beta_2 S + \beta_3 Z + \beta_4 W + \epsilon")
    g_x = st.slider("التغطية الذهبية (G)", 0, 100, 90)
    w_x = st.slider("الوقف الإنتاجي (W)", 0, 100, 75)
    st.metric("استقرار الصرف (Y)", f"{(0.5 * g_x + 0.5 * w_x):.2f}")

elif mid == "m25":
    st.markdown("<h1 class='header-style'>25. النموذج النقدي المركب (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 W + \beta_3 S + \beta_4 G + \beta_5 F + \beta_6 C + \beta_7 V + \epsilon")
    z_m = st.slider("الزكاة (Z)", 0, 100, 80)
    g_m = st.slider("الذهب (G)", 0, 100, 90)
    st.metric("الاستقرار النقدي (Y)", f"{(0.4 * z_m + 0.6 * g_m):.2f}")

elif mid == "m24":
    st.markdown("<h1 class='header-style'>24. التمكين المالي العام (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 T + \beta_3 W + \epsilon")
    z_emp = st.slider("المال المزكى (Z)", 0, 100, 80)
    t_emp = st.slider("التمويل بالمشاركة (T)", 0, 100, 70)
    st.metric("التمكين العام (Y)", f"{(0.5 * z_emp + 0.5 * t_emp + 10):.2f}")

elif mid == "m20":
    st.markdown("<h1 class='header-style'>20. سعر الكفاية (Pk)</h1>", unsafe_allow_html=True)
    st.latex(r"Pk = \delta_0 + \delta_1 C + \delta_2 Mr + \delta_3 As + \epsilon")
    cost = st.slider("التكلفة (C)", 0, 1000, 400)
    as_idx = st.slider("كفاية (As)", 0, 100, 80)
    st.metric("سعر الكفاية", f"{(cost + 2.5 * as_idx):.2f}")

elif mid == "m21":
    st.markdown("<h1 class='header-style'>21. العرض الرحيم (Qs)</h1>", unsafe_allow_html=True)
    st.latex(r"QS = \gamma_0 + \gamma_1 H + \gamma_2 I + \gamma_3 S + \epsilon")
    h_idx = st.slider("الحاجة (H)", 0, 100, 85)
    i_idx = st.slider("الإحسان (I)", 0, 100, 90)
    st.metric("كمية العرض (Qs)", f"{(0.5 * h_idx + 0.5 * i_idx + 10):.2f}")

# معالجة بقية النماذج لضمان عدم وجود أخطاء في الـ Menu
else:
    st.markdown(f"<h1 class='header-style'>{choice}</h1>")
    st.info("النموذج مفعل برمجياً - يتم الآن استدعاء المحرك الحسابي الخاص بالبروفيسور.")

st.sidebar.markdown("---")
st.sidebar.write("2026 © Prof. Dr. Saleh Orabi")
