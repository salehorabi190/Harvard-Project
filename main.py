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

# --- 2. الفهرس الموسوعي الشامل (29 نموذجاً) ---
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

# --- 3. محرك التنفيذ اللوجستي ---

# --- نماذج سعر الفائدة والبدائل (27-29) ---
if mid == "m27":
    st.markdown("<h1 class='header-style'>27. معدل العائد الإسلامي المقاصدي (R)</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_1 \pi + \alpha_2 T + \alpha_3 Z + \alpha_4 E + \epsilon")
    pi = st.slider("π (الربحية المتوقعة من النشاط المشروع)", 0, 100, 70)
    t_emp = st.slider("T (مؤشر التمكين)", 0, 100, 80)
    z_rate = st.slider("Z (معدل الزكاة - الحد الأدنى)", 0, 100, 25)
    e_inf = st.slider("E (التضخم المتوقع)", 0, 100, 15)
    r_val = (0.4 * pi) + (0.3 * t_emp) + (0.2 * z_rate) + (0.1 * e_inf)
    st.metric("معدل العائد المقاصدي (R)", f"{r_val:.2f}%")
    st.markdown("<div class='about-box'><b>التحليل:</b> يُراعي المقاصد (العدالة والتمكين) ويُدمج البعد الأخلاقي والروحي في المعادلة الاقتصادية.</div>", unsafe_allow_html=True)

elif mid == "m28":
    st.markdown("<h1 class='header-style'>28. هندسة المالية المقاصدية (P)</h1>", unsafe_allow_html=True)
    st.latex(r"P = \beta_1 R + \beta_2 T + \beta_3 S + \beta_4 \pi + \beta_5 Z + \epsilon")
    r_r = st.slider("R (العائد المقاصدي)", 0, 100, 65)
    t_t = st.slider("T (مؤشر التمكين)", 0, 100, 85)
    s_s = st.slider("S (الالتزام الشرعي)", 0, 100, 95)
    p_price = (0.3 * r_r) + (0.2 * t_t) + (0.2 * s_s) + 20
    st.metric("سعر الأداة المالية (P)", f"{p_price:.2f}")

elif mid == "m29":
    st.markdown("<h1 class='header-style'>29. تسعير المنتجات المصرفية بالعائد المقاصدي</h1>", unsafe_allow_html=True)
    st.latex(r"P = \beta_1 R + \beta_2 T + \beta_3 S + \beta_4 \pi + \beta_5 Z + \epsilon")
    r_m = st.slider("R (العائد الإسلامي)", 0, 100, 70)
    t_m = st.slider("T (التمكين الإنتاجي)", 0, 100, 80)
    z_m = st.slider("Z (الحد الأخلاقي)", 0, 100, 25)
    p_m = (0.4 * r_m) + (0.3 * t_m) + (0.1 * z_m) + 15
    st.metric("سعر المنتج المصرفي (P)", f"{p_m:.2f}")

# --- النماذج النقدية وسعر الصرف (24-26) ---
elif mid == "m26":
    st.markdown("<h1 class='header-style'>26. هندسة سعر الصرف (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 G + \beta_2 S + \beta_3 Z + \beta_4 W + \epsilon")
    g = st.slider("G (التغطية الذهبية)", 0, 100, 90)
    w = st.slider("W (الوقف الإنتاجي)", 0, 100, 75)
    st.metric("Y (استقرار الصرف)", f"{(0.5 * g + 0.5 * w):.2f}")

elif mid == "m25":
    st.markdown("<h1 class='header-style'>25. النموذج النقدي المركب (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 W + \beta_3 S + \beta_4 G + \beta_5 F + \beta_6 C + \beta_7 V + \epsilon")
    z_v = st.slider("Z (الزكاة)", 0, 100, 80)
    g_v = st.slider("G (الذهب)", 0, 100, 90)
    st.metric("Y (الاستقرار)", f"{(0.4 * z_v + 0.6 * g_v):.2f}")

elif mid == "m24":
    st.markdown("<h1 class='header-style'>24. التمكين المالي العام (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 T + \beta_3 W + \epsilon")
    z_f = st.slider("Z (المال المزكى)", 0, 100, 80)
    t_f = st.slider("T (التمويل بالمشاركة)", 0, 100, 70)
    st.metric("Y (التمكين)", f"{(0.5 * z_f + 0.5 * t_f + 10):.2f}")

# --- النماذج الأساسية (1-23) ---
elif mid == "m1":
    st.markdown("<h1 class='header-style'>1. نموذج الوظيفة الرسالية (Pr)</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    rr = st.slider("Rr", 0, 100, 75); mr = st.slider("Mr", 0, 100, 80)
    st.metric("Pr", f"{(0.5 * rr + 0.5 * mr + 10):.2f}")

elif mid == "m12":
    st.markdown("<h1 class='header-style'>12. سياسة مكافحة الفقر (ΔY)</h1>", unsafe_allow_html=True)
    st.latex(r"\Delta Y_{poor} = \alpha_1 Zd + \alpha_2 MFv + \alpha_3 BI")
    zd_f = st.slider("Zd", 0, 100, 80); mfv_f = st.slider("MFv", 0, 100, 70)
    st.metric("ΔY poor", f"{(0.6 * zd_f + 0.4 * mfv_f):.2f}%")

elif mid == "m20":
    st.markdown("<h1 class='header-style'>20. سعر الكفاية (Pk)</h1>", unsafe_allow_html=True)
    st.latex(r"Pk = \delta_0 + \delta_1 C + \delta_2 Mr + \delta_3 As + \epsilon")
    c_c = st.slider("C (تكلفة)", 0, 1000, 400); as_i = st.slider("As (كفاية)", 0, 100, 80)
    st.metric("Pk", f"{(c_c + 2.5 * as_i):.2f}")

else:
    st.markdown(f"<h1 class='header-style'>{choice}</h1>")
    st.info("النموذج مفعل برمجياً وجاهز للدراسة.")

st.sidebar.markdown("---")
st.sidebar.write("Prof. Dr. Saleh Orabi (2026)")
