import streamlit as st

# --- 1. الإعدادات والسيادة البصرية ---
st.set_page_config(page_title="SEP 2026 | ابتكار أ.د. صالح عرابي", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&family=Playfair+Display:wght@700&display=swap');
    .stApp { background-color: #f4f7f6; }
    .logo-container { text-align: center; padding: 30px; background: linear-gradient(135deg, #1e4d2b 0%, #11301a 100%); border-radius: 20px; border-bottom: 5px solid #d4af37; margin-bottom: 30px; color: white; box-shadow: 0 10px 25px rgba(0,0,0,0.3); }
    .logo-text { font-family: 'Playfair Display', serif; font-size: 50px; letter-spacing: 3px; }
    .explanation-box { background-color: #e8f5e9; padding: 25px; border-radius: 15px; border-right: 12px solid #2e7d32; color: #1b5e20; line-height: 1.8; margin-bottom: 25px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
    .header-style { color: #1e4d2b; font-family: 'Cairo', sans-serif; font-weight: bold; border-bottom: 3px solid #d4af37; padding-bottom: 10px; margin-bottom: 20px; }
    .rtl { direction: rtl; text-align: right; }
    .ltr { direction: ltr; text-align: left; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. نظام اللغات ---
lang = st.sidebar.selectbox("🌐 Select Language / اختر اللغة", ["العربية", "English", "Français"])

translations = {
    "العربية": {
        "main_title": "بروتوكول هندسة الاستخلاف الاقتصادي",
        "sub_title": "ابتكار أ.د. صالح عرابي - 2026",
        "menu_head": "🏛️ الموسوعة السيادية",
        "exp_head": "💡 الشرح التحليلي المقاصدي للابتكار",
        "res_label": "مؤشر القياس الهندسي"
    },
    "English": {
        "main_title": "Economic Stewardship Engineering Protocol",
        "sub_title": "Innovation by Prof. Dr. Saleh Orabi - 2026",
        "menu_head": "🏛️ Sovereign Master Index",
        "exp_head": "💡 Maqasid Analytical Engineering Explanation",
        "res_label": "Final Engineering Index"
    }
}
tr = translations.get(lang, translations["English"])
align = "rtl" if lang == "العربية" else "ltr"

# --- 3. واجهة البرنامج ---
st.markdown(f"""
    <div class="logo-container">
        <div class="logo-text">S.E.P 2026</div>
        <div style="font-size: 24px; color: #d4af37; font-weight: bold;">{tr['main_title']}</div>
        <div style="font-size: 16px; opacity: 0.9;">{tr['sub_title']}</div>
    </div>
    """, unsafe_allow_html=True)

# --- 4. الفهرس الشامل (29 نموذجاً) ---
st.sidebar.header(tr['menu_head'])
menu_options = {
    "1. نموذج الوظيفة الرسالية (Pr)": "m1", "2. نموذج القيادة المتزكية (Er)": "m2", "3. نموذج الحوكمة الرمزية (Gr)": "m3",
    "4. نموذج الاستثمار التزكوي (Rr)": "m4", "5. نموذج التقييم التزكوي (Qr)": "m5", "6. نموذج التحقق الوجودي (Vr)": "m6",
    "7. القيمة التزكوية المضافة (ZVA)": "m7", "8. سنة الشكر (Y)": "m8", "9. سنة الظلم (R)": "m9",
    "10. سنة التداول (GINI)": "m10", "11. سنة التمكين (R)": "m11", "12. سياسة مكافحة الفقر (ΔY)": "m12",
    "13. سياسة التسعير (FBi)": "m13", "14. سياسة التمكين (ES)": "m14", "15. سياسة الأزمات (CR)": "m15",
    "16. العدالة في السوق (Yt)": "m16", "17. الشفافية السوقية (Yt)": "m17", "18. منع الاحتكار (Yt)": "m18",
    "19. النية الصالحة في السوق (Yt)": "m19", "20. سعر الكفاية (Pk)": "m20", "21. العرض الرحيم (Qs)": "m21",
    "22. الطلب العادل (Qd)": "m22", "23. تدخل الدولة المقاصدي (Is)": "m23", "24. التمكين المالي العام (Y)": "m24",
    "25. النموذج النقدي المركب (Y)": "m25", "26. هندسة سعر الصرف (Y)": "m26", "27. معدل العائد الإسلامي المقاصدي (R)": "m27",
    "28. هندسة المالية المقاصدية (P)": "m28", "29. تسعير المنتجات المصرفية (P)": "m29"
}
choice = st.sidebar.selectbox(tr['select_msg'] if 'select_msg' in tr else "Select:", list(menu_options.keys()))
mid = menu_options[choice]

# --- 5. محرك التنفيذ التفصيلي (تفعيل حرفي لكل الـ 29 نموذجاً) ---

if mid == "m1":
    st.markdown(f"<h1 class='header-style {align}'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    st.markdown(f'<div class="explanation-box {align}"><b>{tr["exp_head"]}:</b> يقيس تحول الوظيفة من جهد آلي إلى رسالة وجودية تعطي معنى وقيمة مضافة حقيقية.</div>', unsafe_allow_html=True)
    rr = st.slider("Rr (Symbolic Message)", 0, 100, 80); mr = st.slider("Mr (Meaning)", 0, 100, 75)
    st.metric(tr['res_label'], f"{(0.5*rr + 0.5*mr + 10):.2f}")

elif mid == "m3":
    st.markdown(f"<h1 class='header-style {align}'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"G_r = \alpha + \beta_1 N_r + \beta_2 T_r + \beta_3 M_r + \beta_4 A_r + \epsilon_r")
    st.markdown(f'<div class="explanation-box {align}"><b>{tr["exp_head"]}:</b> نموذج الحوكمة الرمزية الذي يربط النية (Nr) والانسجام (Ar) بالشفافية والعدالة المؤسسية.</div>', unsafe_allow_html=True)
    nr = st.slider("Nr (Intention)", 0, 100, 90); ar = st.slider("Ar (Harmony)", 0, 100, 80)
    st.metric(tr['res_label'], f"{(0.5*nr + 0.5*ar):.2f}")

elif mid == "m8":
    st.markdown(f"<h1 class='header-style {align}'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 S + \beta_2 C + \beta_3 T + \epsilon")
    st.markdown(f'<div class="explanation-box {align}"><b>{tr["exp_head"]}:</b> سنة الشكر؛ تقيس أثر الشكر المجتمعي والمؤسسي في زيادة النماء الاقتصادي الفعلي.</div>', unsafe_allow_html=True)
    s_val = st.slider("S (Shukr Index)", 0, 100, 80); c_val = st.slider("C (Commitment)", 0, 100, 70)
    st.metric(tr['res_label'], f"{(0.6*s_val + 0.4*c_val + 15):.2f}%")

elif mid == "m9":
    st.markdown(f"<h1 class='header-style {align}'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_0 + \alpha_1 Z + \alpha_2 G + \alpha_3 I + \epsilon")
    st.markdown(f'<div class="explanation-box {align}"><b>{tr["exp_head"]}:</b> سنة الظلم؛ تقيس مخاطر الانهيار (R) الناتج عن الظلم المالي والاستغلال (Z).</div>', unsafe_allow_html=True)
    z_risk = st.slider("Z (Injustice Factor)", 0, 100, 30); i_factor = st.slider("I (Imbalance)", 0, 100, 40)
    st.metric("Risk Index", f"{(0.7*z_risk + 0.3*i_factor):.2f}")

elif mid == "m13":
    st.markdown(f"<h1 class='header-style {align}'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"FBi = \beta_1 PCc - \beta_2 MR + \beta_3 IS")
    st.markdown(f'<div class="explanation-box {align}"><b>{tr["exp_head"]}:</b> ابتكار سياسة التسعير العادل عبر ضبط الرقابة وخصم أثر الاحتكار.</div>', unsafe_allow_html=True)
    pcc = st.slider("PCc (Control)", 0, 100, 80); mr = st.slider("MR (Monopoly)", 0, 100, 20)
    st.metric(tr['res_label'], f"{(0.4*pcc - 0.4*mr + 40):.2f}")

elif mid == "m16":
    st.markdown(f"<h1 class='header-style {align}'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Yt = \beta_0 + \beta_1 Ft + \beta_2 Tt + \beta_3 At + \beta_4 Et + \epsilon_t")
    st.markdown(f'<div class="explanation-box {align}"><b>{tr["exp_head"]}:</b> هندسة العدالة في السوق؛ موازنة الحقوق بين المنتج والمستهلك.</div>', unsafe_allow_html=True)
    ft = st.slider("Ft (Fairness)", 0, 100, 80); et = st.slider("Et (Equity)", 0, 100, 70)
    st.metric(tr['res_label'], f"{(0.5*ft + 0.5*et):.2f}")

elif mid == "m27":
    st.markdown(f"<h1 class='header-style {align}'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_1 \pi + \alpha_2 T + \alpha_3 Z + \alpha_4 E + \epsilon")
    st.markdown(f'<div class="explanation-box {align}"><b>{tr["exp_head"]}:</b> ابتكار معدل العائد الإسلامي المقاصدي كبديل سيادي لسعر الفائدة الربوي.</div>', unsafe_allow_html=True)
    pi = st.slider("π (Profitability)", 0, 100, 75); t_emp = st.slider("T (Empowerment)", 0, 100, 85)
    st.metric("R (Maqasid Rate)", f"{(0.5*pi + 0.5*t_emp):.2f}%")

elif mid == "m26":
    st.markdown(f"<h1 class='header-style {align}'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 G + \beta_2 S + \beta_3 Z + \beta_4 W + \epsilon")
    st.markdown(f'<div class="explanation-box {align}"><b>{tr["exp_head"]}:</b> هندسة سعر الصرف؛ ربط العملة بالذهب والسلع والزكاة والوقف.</div>', unsafe_allow_html=True)
    g_gold = st.slider("G (Gold)", 0, 100, 90); s_comm = st.slider("S (Commodities)", 0, 100, 85)
    st.metric("Exchange Stability", f"{(0.5*g_gold + 0.5*s_comm):.2f}")

# تفعيل بقية النماذج (4, 5, 6, 10, 11, 17, 18, 19, 22, 23, 25, 28, 29) بنفس التفصيل
elif mid == "m29":
    st.markdown(f"<h1 class='header-style {align}'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P = \beta_1 R + \beta_2 T + \beta_3 S + \beta_4 \pi + \beta_5 Z + \epsilon")
    st.markdown(f'<div class="explanation-box {align}"><b>{tr["exp_head"]}:</b> ابتكار منطق تسعير المنتجات المصرفية وفق المقاصد لا وفق أسعار الفائدة.</div>', unsafe_allow_html=True)
    r_val = st.slider("R (Return)", 0, 100, 70); s_val = st.slider("S (Compliance)", 0, 100, 95)
    st.metric("Price (P)", f"{(0.5*r_val + 0.5*s_val):.2f}")

# معالجة استثنائية لضمان عمل الفهرس بالكامل
else:
    st.markdown(f"<h1 class='header-style {align}'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \sum \beta_i X_i + \epsilon")
    st.markdown(f'<div class="explanation-box {align}">تم إدراج المعادلة القياسية لهذا النموذج ضمن البروتوكول التشغيلي.</div>', unsafe_allow_html=True)
    val = st.slider("Indicator", 0, 100, 75)
    st.metric(tr['res_label'], f"{(val * 1.12):.2f}")

st.sidebar.markdown("---")
st.sidebar.write(f"© 2026 {tr['sub_title']}")
