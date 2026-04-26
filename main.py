import streamlit as st
import numpy as np

# --- 1. الإعدادات العامة والسيادة البصرية ---
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

# --- 2. محرك الفهرس الشامل (25 نموذجاً) ---
st.sidebar.title("🏛️ الفهرس السيادي الشامل")
st.sidebar.write("Prof. Dr. Saleh Orabi")

menu_options = {
    "1. نموذج الوظيفة الرسالية (Pr)": "1",
    "2. نموذج القيادة المتزكية (Er)": "2",
    "3. نموذج الحوكمة الرمزية (Gr)": "3",
    "4. نموذج الاستثمار التزكوي (Rr)": "4",
    "5. نموذج التقييم التزكوي (Qr)": "5",
    "6. نموذج التحقق الوجودي (Vr)": "6",
    "7. القيمة التزكوية المضافة (ZVA)": "7",
    "8. سنة الشكر (Y)": "8",
    "9. سنة الظلم (R)": "9",
    "10. سنة التداول (GINI)": "10",
    "11. سنة التمكين (R)": "11",
    "12. سياسة مكافحة الفقر (ΔY)": "12",
    "13. سياسة التسعير العادل (FBi)": "13",
    "14. سياسة التمكين القيادي (ES)": "14",
    "15. سياسة الأزمات (CR)": "15",
    "16. العدالة في السوق (Yt)": "16",
    "17. الشفافية السوقية (Yt)": "17",
    "18. منع الاحتكار (Yt)": "18",
    "19. النية الصالحة في السوق (Yt)": "19",
    "20. سعر الكفاية (Pk)": "20",
    "21. العرض الرحيم (Qs)": "21",
    "22. الطلب العادل (Qd)": "22",
    "23. تدخل الدولة المقاصدي (Is)": "23",
    "24. التمكين المالي العام (Y)": "24",
    "25. النموذج النقدي المركب (Y)": "25"
}

choice = st.sidebar.selectbox("اختر النموذج المطلوب تنفيذه:", list(menu_options.keys()))
mid = menu_options[choice]

# --- 3. محرك التنفيذ اللوجستي ---

if mid == "1":
    st.markdown("<h1 class='header-style'>نموذج الوظيفة الرسالية (Pr)</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    rr = st.slider("الرسالة الرمزية (Rr)", 0, 100, 70); mr = st.slider("المعنى والانتماء (Mr)", 0, 100, 75)
    st.metric("الأداء الوظيفي (Pr)", f"{0.5*rr + 0.5*mr:.2f}")

elif mid == "2":
    st.markdown("<h1 class='header-style'>نموذج القيادة المتزكية (Er)</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \beta_4 C_r + \epsilon_r")
    zr = st.slider("تزكية القائد (Zr)", 0, 100, 85)
    st.metric("الأثر المؤسسي (Er)", f"{zr * 1.25:.2f}")

elif mid == "3":
    st.markdown("<h1 class='header-style'>نموذج الحوكمة الرمزية (Gr)</h1>", unsafe_allow_html=True)
    st.latex(r"G_r = \alpha + \beta_1 N_r + \beta_2 T_r + \beta_3 M_r + \beta_4 A_r + \epsilon_r")
    ar = st.slider("الانسجام الرمزي (Ar)", 0, 100, 90)
    st.metric("جودة الحوكمة (Gr)", f"{ar * 0.95:.2f}")

elif mid == "8":
    st.markdown("<h1 class='header-style'>سنة الشكر (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 S + \beta_2 C + \beta_3 T + \epsilon")
    s = st.slider("مؤشر الشكر (S)", 0, 100, 80)
    st.metric("معدل النمو (Y)", f"{10 + 0.5*s:.2f}%")

elif mid == "9":
    st.markdown("<h1 class='header-style'>سنة الظلم (R)</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_0 + \alpha_1 Z + \alpha_2 G + \alpha_3 I + \epsilon")
    z = st.slider("مؤشر الظلم الاحتكاري (Z)", 0, 100, 30)
    st.metric("مؤشر المخاطر (R)", f"{z * 0.8:.2f}%")

elif mid == "13":
    st.markdown("<h1 class='header-style'>سياسة التسعير العادل (FBi)</h1>", unsafe_allow_html=True)
    st.latex(r"FBi = \beta_1 PCc - \beta_2 MR + \beta_3 IS")
    pcc = st.slider("ضبط الأسعار (PCc)", 0, 100, 70); mr = st.slider("معدل الاحتكار (MR)", 0, 100, 20)
    st.metric("مؤشر السعر العادل", f"{0.5*pcc - 0.5*mr + 20:.2f}")

elif mid == "15":
    st.markdown("<h1 class='header-style'>سياسة الأزمات (CR)</h1>", unsafe_allow_html=True)
    st.latex(r"CR = \delta_1 NFs + \delta_2 RR + \delta_3 SF")
    nfs = st.slider("فقه الضرورة (NFs)", 0, 100, 85)
    st.metric("التصدي للأزمات (CR)", f"{nfs * 1.15:.2f}")

elif mid == "21":
    st.markdown("<h1 class='header-style'>نموذج العرض الرحيم (Qs)</h1>", unsafe_allow_html=True)
    st.latex(r"QS = \gamma_0 + \gamma_1 H + \gamma_2 I + \gamma_3 S + \epsilon")
    h = st.slider("الحاجة المجتمعية (H)", 0, 100, 80); i = st.slider("نية الإحسان (I)", 0, 100, 90)
    st.metric("كمية العرض الرحيم (Qs)", f"{0.6*h + 0.4*i:.2f}")

elif mid == "22":
    st.markdown("<h1 class='header-style'>نموذج الطلب العادل (Qd)</h1>", unsafe_allow_html=True)
    st.latex(r"Qd = \alpha_0 + \alpha_1 Y + \alpha_2 A + \alpha_3 N + \epsilon")
    a_idx = st.slider("وعي الاستهلاك (A)", 0, 100, 85); n_idx = st.slider("الحاجة الحقيقية (N)", 0, 100, 70)
    st.metric("كمية الطلب العادل (Qd)", f"{100 - (0.5*a_idx) + (0.5*n_idx):.2f}")

elif mid == "25":
    st.markdown("<h1 class='header-style'>النموذج النقدي المركب (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 W + \beta_3 S + \beta_4 G + \beta_5 F + \beta_6 C + \beta_7 V + \epsilon")
    z_m = st.slider("معدل الزكاة (Z)", 0, 100, 85); g_m = st.slider("تغطية الذهب (G)", 0, 100, 90)
    st.metric("الاستقرار النقدي (Y)", f"{(0.4*z_m + 0.6*g_m):.2f}")

# إضافة باقي الـ elif للنماذج المفقودة بنفس النمط (7, 10, 11, 12, 14, 16, 17, 18, 19, 20, 23, 24)
else:
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.info("النموذج قيد التفعيل الرياضي بناءً على معطيات البروفيسور.")

st.sidebar.markdown("---")
st.sidebar.write("2026 © Prof. Dr. Saleh Orabi")
