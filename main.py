import streamlit as st
import numpy as np

# --- 1. الإعدادات والسيادة البصرية (ابتكار أ.د. صالح عرابي 2026) ---
st.set_page_config(page_title="S.E.P 2026 | Prof. Dr. Saleh Orabi", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&family=Playfair+Display:wght@700&display=swap');
    .stApp { background-color: #f4f7f6; }
    .logo-container { text-align: center; padding: 45px; background: linear-gradient(135deg, #1e4d2b 0%, #11301a 100%); border-radius: 30px; border-bottom: 12px solid #d4af37; margin-bottom: 40px; color: white; box-shadow: 0 20px 40px rgba(0,0,0,0.4); }
    .logo-text { font-family: 'Playfair Display', serif; font-size: 70px; letter-spacing: 5px; }
    .explanation-box { background-color: #ffffff; padding: 35px; border-radius: 20px; border-right: 20px solid #2e7d32; color: #1b5e20; line-height: 2.2; margin-bottom: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); font-family: 'Cairo', sans-serif; font-size: 18px; }
    .header-style { color: #1e4d2b; font-family: 'Cairo', sans-serif; font-weight: bold; border-bottom: 8px solid #d4af37; padding-bottom: 20px; margin-bottom: 40px; text-align: right; }
    .stMetric { background: #ffffff; padding: 30px; border-radius: 25px; border: 2px solid #e0e0e0; box-shadow: 0 8px 20px rgba(0,0,0,0.03); }
    </style>
    """, unsafe_allow_html=True)

# --- 2. نظام اللغات والتحكم ---
lang = st.sidebar.selectbox("🌐 اختر اللغة / Select Language", ["العربية", "English"])

# تم تعريف الاسم كمتغير نصي ثابت لتجنب أخطاء السنتكس
AUTHOR_NAME = "Prof. Dr. Saleh Orabi" if lang == "English" else "أ.د. صالح عرابي"

if lang == "العربية":
    m_res, m_auth, m_title = "النتيجة النهائية", f"إعداد وتطوير: {AUTHOR_NAME} - 2026", "بروتوكول هندسة الاستخلاف الاقتصادي"
    sidebar_head, select_msg = "🏛️ القائمة الهندسية الكاملة", "اختر النموذج الهندسي المطلوب:"
else:
    m_res, m_auth, m_title = "Final Result", f"Developed by: {AUTHOR_NAME} - 2026", "Economic Stewardship Engineering Protocol"
    sidebar_head, select_msg = "🏛️ Full Engineering List", "Select the required Engineering Model:"

st.markdown(f"""
    <div class="logo-container">
        <div class="logo-text">S.E.P 2026</div>
        <div style="font-size: 32px; color: #d4af37; font-weight: bold; margin-top:15px;">{m_title}</div>
        <div style="font-size: 20px; opacity: 0.9;">{m_auth}</div>
    </div>
    """, unsafe_allow_html=True)

# --- 3. الفهرس الموسوعي الشامل (35 نموذجاً مستقلاً حرفياً) ---
menu = {
    "P1. المشاركة التمكينية المتدرجة": "p1", "P2. الإدخار الوقفي الذكي": "p2", "P3. الصكوك الوقفية التنموية": "p3",
    "P4. المضاربة الاجتماعية التمكينية": "p4", "P5. صندوق الوقف التمكيني المشترك": "p5", "P6. الإجارة الوقفية الموصوفة": "p6",
    "1. نموذج الوظيفة الرسالية (Pr)": "m1", "2. نموذج القيادة المتزكية (Er)": "m2", "3. نموذج الحوكمة الرمزية (Gr)": "m3",
    "4. نموذج الاستثمار التزكوي (Rr)": "m4", "5. نموذج التقييم التزكوي (Qr)": "m5", "6. نموذج التحقق الوجودي (Vr)": "m6",
    "7. القيمة التزكوية المضافة (ZVA)": "m7", "8. سنة الشكر (Y)": "m8", "9. سنة الظلم (R)": "m9",
    "10. سنة التداول (GINI)": "m10", "11. سنة التمكين (R_e)": "m11", "12. سياسة مكافحة الفقر (ΔY)": "m12",
    "13. سياسة التسعير (FBi)": "m13", "14. سياسة التمكين (ES)": "m14", "15. سياسة الأزمات (CR)": "m15",
    "16. العدالة في السوق (Yt)": "m16", "17. الشفافية السوقية (Yt)": "m17", "18. منع الاحتكار (Yt)": "m18",
    "19. النية الصالحة في السوق (Yt)": "m19", "20. سعر الكفاية (Pk)": "m20", "21. العرض الرحيم (Qs)": "m21",
    "22. الطلب العادل (Qd)": "m22", "23. تدخل الدولة المقاصدي (Is)": "m23", "24. التمكين المالي العام (Y)": "m24",
    "25. النموذج النقدي المركب (Y)": "m25", "26. هندسة سعر الصرف (Y_fx)": "m26", "27. معدل العائد المقاصدي (R)": "m27",
    "28. هندسة المالية المقاصدية (P)": "m28", "29. تسعير المنتجات المصرفية (P_b)": "m29"
}

st.sidebar.header(sidebar_head)
choice = st.sidebar.selectbox(select_msg, list(menu.keys()))
mid = menu[choice]

# --- 4. محرك التشغيل التفصيلي (الـ 35 كتلة سطر بسطر) ---

if mid == "p1":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{it} = \alpha + \beta_1 P_{it} + \beta_2 E_{it} + \beta_3 S_{it} + \epsilon_{it}")
    desc = "تمويل الفئات المحرومة بمشاركة متدرجة تتناقص فيها نسبة المصرف بنسبة 20% سنوياً حتى التملك الكامل." if lang == "العربية" else "Participatory financing with 20% annual bank-share reduction."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Pit", 0, 100, 80); v2 = st.slider("Eit", 0, 100, 70); v3 = st.slider("Sit", 0, 100, 90)
    st.metric(m_res, f"{(0.4*v1 + 0.3*v2 + 0.3*v3):.2f}")

elif mid == "p2":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Z_{it} = \gamma + \delta_1 W_{it} + \delta_2 R_{it} + \delta_3 T_{it} + \mu_{it}")
    desc = "دمج الوقف في المدخرات لتحقيق استدامة تنموية وتفاعل روحي." if lang == "العربية" else "Integrating Waqf in savings for developmental sustainability."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Wit", 0, 100, 30); v2 = st.slider("Rit", 0, 100, 60); v3 = st.slider("Tit", 0, 100, 85)
    st.metric(m_res, f"{(0.5*v1 + 0.3*v2 + 0.2*v3):.2f}")

elif mid == "p3":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"W_{it} = \theta + \lambda_1 C_{it} + \lambda_2 R_{it} + \lambda_3 I_{it} + \nu_{it}")
    desc = "صكوك وقفية تضمن تمويلاً مستداماً للمشاريع التنموية." if lang == "العربية" else "Waqf Sukuk ensuring sustainable funding for projects."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Cit", 0, 1000, 500); v2 = st.slider("Rit", 0, 100, 20); v3 = st.slider("Iit", 0, 100, 80)
    st.metric(m_res, f"{(v1*0.01 + v2*0.4 + v3*0.5):.2f}")

elif mid == "p4":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"M_{it} = \phi + \rho_1 A_{it} + \rho_2 T_{it} + \rho_3 G_{it} + \epsilon_{it}")
    desc = "مضاربة اجتماعية لتمكين الفقراء بتمويل المصرف وإدارة العميل." if lang == "العربية" else "Social Mudaraba to empower the poor with bank financing."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Ait (Capital)", 0, 1000, 400); v2 = st.slider("Tit (Training)", 0, 100, 90)
    st.metric(m_res, f"{(v1*0.02 + v2*0.5):.2f}")

elif mid == "p5":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Q_{it} = \psi + \eta_1 V_{it} + \eta_2 D_{it} + \eta_3 B_{it} + \xi_{it}")
    desc = "صندوق وقفي تمكيني مشترك كضمان للمشاريع الإنتاجية." if lang == "العربية" else "Joint empowerment Waqf fund for productive projects."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Vit (Fund)", 0, 1000, 600); v2 = st.slider("Dit (Guarantee)", 0, 100, 100)
    st.metric(m_res, f"{(v1*0.02 + v2*0.5):.2f}")

elif mid == "p6":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"H_{it} = \omega + \sigma_1 E_{it} + \sigma_2 Q_{it} + \sigma_3 K_{it} + \varsigma_{it}")
    desc = "إجارة وقفية موصوفة لتأمين سكن أو تعليم بكرامة." if lang == "العربية" else "Forward Waqf Ijarah for dignified housing or education."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Eit (Rent)", 0, 100, 80); v2 = st.slider("Kit (Dignity)", 0, 100, 100)
    st.metric(m_res, f"{(0.4*v1 + 0.6*v2):.2f}")

elif mid == "m1":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r")
    desc = "تحويل الوظيفة من كدح مادي إلى رسالة وجودية تربط الرسالة بالمعنى." if lang == "العربية" else "Transforming a job into an existential mission."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Rr", 0, 100, 85); v2 = st.slider("Mr", 0, 100, 80)
    st.metric(m_res, f"{(0.5*v1 + 0.5*v2 + 10):.2f}")

elif mid == "m2":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r")
    desc = "أثر القيادة المتزكية وإلهام القائد في تحقيق الاستخلاف." if lang == "العربية" else "Impact of spiritual leadership and inspiration."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Zr", 0, 100, 90); v2 = st.slider("Ir", 0, 100, 85)
    st.metric(m_res, f"{(0.6*v1 + 0.4*v2):.2f}")

elif mid == "m3":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"G_r = \alpha + \beta_1 N_r + \beta_2 T_r + \beta_3 M_r")
    desc = "الحوكمة الرمزية والانسجام المقاصدي والنزاهة المؤسسية." if lang == "العربية" else "Symbolic governance and Maqasid harmony."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Nr", 0, 100, 95); v2 = st.slider("Ar", 0, 100, 90)
    st.metric(m_res, f"{(0.5*v1 + 0.5*v2):.2f}")

elif mid == "m4":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R_r = f(K_{spiritual}, K_{social}, K_{financial})")
    desc = "الاستثمار التزكوي البديل القائم على رأس المال الروحي والقيمي." if lang == "العربية" else "Alternative Tazkiyah investment based on spiritual capital."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("K Spirit", 0, 100, 90); v2 = st.slider("K Financial", 0, 100, 60)
    st.metric(m_res, f"{(0.7*v1 + 0.3*v2):.2f}")

elif mid == "m5":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Q_r = \frac{\sum Maqasid}{\sum Resources}")
    desc = "التقييم التزكوي للأداء المؤسسي بناءً على كفاءة تحقيق المقاصد الشرعية." if lang == "العربية" else "Tazkiyah assessment based on Maqasid efficiency."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Maqasid", 0, 100, 85); v2 = st.slider("Resources", 1, 100, 50)
    st.metric(m_res, f"{(v1/v2):.2f}")

elif mid == "m6":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"V_r = Faith \times Impact")
    desc = "التحقق الوجودي للأثر الاقتصادي وربطه بمبادئ الاستخلاف." if lang == "العربية" else "Existential verification of economic impact."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Faith Index", 0, 100, 95); v2 = st.slider("Impact Index", 0, 100, 80)
    st.metric(m_res, f"{(v1*v2/100):.2f}")

elif mid == "m7":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    desc = "القيمة التزكوية المضافة التي تدمج الربح المادي والبركة المعنوية." if lang == "العربية" else "Tazkiyah Value Added (Profit + Barakah)."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("EVA (Material)", 0, 1000, 500); v2 = st.slider("Z factor", 0, 100, 90)
    st.metric(m_res, f"{(v1 + 1.5*v2):.2f}")

elif mid == "m8":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 S + \beta_2 C")
    desc = "سنة الشكر والالتزام كمحرك جوهري للنماء والبركة المادية المستدامة." if lang == "العربية" else "Sunnah of Gratitude and Commitment driver."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Gratitude (S)", 0, 100, 95); v2 = st.slider("Commitment (C)", 0, 100, 85)
    st.metric(m_res, f"{(0.7*v1 + 0.3*v2 + 15):.2f}")

elif mid == "m9":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_0 + \alpha_1 Z + \alpha_2 G")
    desc = "سنة الظلم والغرور ومؤشر الانهيار الاقتصادي الناتج عن غياب العدالة." if lang == "العربية" else "Sunnah of Injustice: collapse indicator."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Z (Injustice)", 0, 100, 20); v2 = st.slider("G (Arrogance)", 0, 100, 30)
    st.metric(m_res, f"{(0.8*v1 + 0.2*v2):.2f}")

elif mid == "m10":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"GINI = \frac{1}{n} \sum (Y_i - \bar{Y}) \cdot Z")
    desc = "سنة التداول وضبط توزيع الثروة بمعامل الزكاة لمنع تركز المال." if lang == "العربية" else "Sunnah of Circulation via Zakat pressure."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Income Distribution", 0, 100, 75); v2 = st.slider("Zakat Pressure", 0, 100, 85)
    st.metric(m_res, f"{(v1*v2/100):.2f}")

elif mid == "m11":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R_e = K_h + K_s + K_e")
    desc = "سنة التمكين وتراكم القوى البشرية والإيمانية والاجتماعية." if lang == "العربية" else "Sunnah of Empowerment: Human & Faith forces."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Human Force", 0, 100, 85); v2 = st.slider("Faith Force", 0, 100, 90)
    st.metric(m_res, f"{(v1+v2)/2:.2f}")

elif mid == "m12":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"\Delta Y_{poor} = \alpha_1 Z_d + \alpha_2 MF_v")
    desc = "سياسة مكافحة الفقر عبر الزكاة المباشرة والتمويل الأصغر." if lang == "العربية" else "Poverty alleviation via Zakat and Microfinance."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Zakat Distributed", 0, 100, 85); v2 = st.slider("Microfinance Value", 0, 100, 75)
    st.metric(m_res, f"{(0.6*v1 + 0.4*v2):.2f}%")

elif mid == "m13":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"FBi = \beta_1 PCc - \beta_2 MR")
    desc = "سياسة التسعير العادل وضبط الاحتكار عبر أدوات الرقابة المقاصدية." if lang == "العربية" else "Fair pricing policy and monopoly control."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Regulation (PCc)", 0, 100, 80); v2 = st.slider("Monopoly MR", 0, 100, 15)
    st.metric(m_res, f"{(0.6*v1 - 0.4*v2 + 20):.2f}")

elif mid == "m14":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"ES = \beta_1 LTp + \beta_2 OAr")
    desc = "سياسة التمكين المهني وتكافؤ الفرص في سوق العمل." if lang == "العربية" else "Vocational empowerment and equal opportunities."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("LTp Training", 0, 100, 85); v2 = st.slider("OAr Equality", 0, 100, 80)
    st.metric(m_res, f"{(0.5*v1 + 0.5*v2):.2f}")

elif mid == "m15":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"CR = \delta_1 NFs + \delta_2 RR")
    desc = "سياسة الأزمات وفقه الضرورة لتأمين الحاجات الأساسية (NFs)." if lang == "العربية" else "Crisis policy: Securing basic needs."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Necessities", 0, 100, 95); v2 = st.slider("Recovery Speed", 0, 100, 80)
    st.metric(m_res, f"{(0.7*v1 + 0.3*v2):.2f}")

elif mid == "m16":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Yt = \beta_1 Ft + \beta_2 Et")
    desc = "هندسة العدالة السوقية بين السعر العادل (Ft) والتوزيع العادل (Et)." if lang == "العربية" else "Market justice engineering (Price vs Dist)."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Price Justice", 0, 100, 80); v2 = st.slider("Dist Justice", 0, 100, 75)
    st.metric(m_res, f"{(0.5*v1 + 0.5*v2):.2f}")

elif mid == "m17":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_t = \beta_1 Info + \beta_2 Trust")
    desc = "الشفافية والتدفق المعلوماتي الموثوق في السوق." if lang == "العربية" else "Transparency and reliable info flow."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Information flow", 0, 100, 90); v2 = st.slider("Trust level", 0, 100, 85)
    st.metric(m_res, f"{(0.6*v1 + 0.4*v2):.2f}")

elif mid == "m18":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{anti} = 2500 - HHI")
    desc = "هندسة منع الاحتكار وتوسيع قاعدة المنافسة العادلة." if lang == "العربية" else "Monopoly prevention engineering."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("HHI Index", 0, 2500, 1100)
    st.metric(m_res, f"{(2500-v1)/25:.2f}%")

elif mid == "m19":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{niya} = \sum GoodIntentions")
    desc = "هندسة النية الصالحة في السلوك الاقتصادي المؤسسي." if lang == "العربية" else "Good Intention engineering in behavior."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Niya Index", 0, 100, 95)
    st.metric(m_res, f"{(v1*1.1):.2f}")

elif mid == "m20":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_k = C + (A_s \times 2.5\%)")
    desc = "سعر الكفاية لمنع الغلاء وضمان حق الفقير في السلعة." if lang == "العربية" else "Sufficiency price for basic needs."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Cost C", value=100); v2 = st.slider("Security Coefficient", 0, 100, 80)
    st.metric(m_res, f"{v1 + (v2*0.025*v1):.2f}")

elif mid == "m21":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Q_s = f(P, Z_f, B)")
    desc = "العرض الرحيم القائم على تسهيلات الزكاة والبركة." if lang == "العربية" else "Merciful Supply via Barakah logic."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Price Level", 0, 100, 65); v2 = st.slider("Barakah Index", 0, 100, 95)
    st.metric(m_res, f"{(0.4*v1 + 0.6*v2):.2f}")

elif mid == "m22":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Q_d = f(P, Need, Ethics)")
    desc = "الطلب العادل المرتبط بالحاجة الحقيقية والأخلاق." if lang == "العربية" else "Fair Demand linked to real needs."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Price P", 0, 100, 50); v2 = st.slider("Ethics Level", 0, 100, 85)
    st.metric(m_res, f"{(0.5*v1 + 0.5*v2):.2f}")

elif mid == "m23":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"I_s = \frac{Needs - Q_s}{Capacity}")
    desc = "معيار تدخل الدولة المقاصدي لسد فجوات السوق." if lang == "العربية" else "Maqasid State Intervention criteria."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Unmet Needs (N)", 0, 100, 70); v2 = st.slider("State Capacity", 1, 100, 50)
    st.metric(m_res, f"{(v1/v2):.2f}")

elif mid == "m24":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{pub} = \sum Financials")
    desc = "التمكين المالي العام لضمان سيولة الخدمات الأساسية." if lang == "العربية" else "Public financial empowerment."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Finance Level", 0, 100, 85)
    st.metric(m_res, f"{(v1*1.05):.2f}")

elif mid == "m25":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{monetary} = M \cdot V + Z_{speed}")
    desc = "النظام النقدي وسرعة دوران الزكاة في تفعيل الاقتصاد." if lang == "العربية" else "Monetary system and Zakat velocity."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Money Mass", 0, 100, 70); v2 = st.slider("Z-Velocity", 0, 100, 85)
    st.metric(m_res, f"{(v1*0.6 + v2*0.4):.2f}")

elif mid == "m26":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{fx} = \sqrt{G \cdot S \cdot W}")
    desc = "هندسة سعر الصرف السيادي المعتمد على الأصول الحقيقية." if lang == "العربية" else "Sovereign exchange rate via real assets."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Gold G", 0, 100, 95); v2 = st.slider("Assets S", 0, 100, 85)
    st.metric(m_res, f"{(v1*v2)**0.5:.2f}")

elif mid == "m27":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_1 \pi + \alpha_2 T + \alpha_3 Z")
    desc = "العائد المقاصدي البديل للفائدة الربوية." if lang == "العربية" else "Maqasid Return: alternative to usury."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Profit π", 0, 100, 80); v2 = st.slider("Empowerment T", 0, 100, 85)
    st.metric(m_res, f"{(0.5*v1 + 0.5*v2):.2f}")

elif mid == "m28":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_{fin} = \frac{R + T}{Risk}")
    desc = "هندسة المالية المقاصدية وإدارة مخاطر المشاركة." if lang == "العربية" else "Maqasid Finance: risk-sharing management."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Expected Return", 0, 100, 75); v2 = st.slider("Risk Coeff", 1, 100, 50)
    st.metric(m_res, f"{(v1/v2)*10:.2f}")

elif mid == "m29":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_b = 0.6 R + 0.4 Z")
    desc = "تسعير المنتجات المصرفية الأخلاقية بناءً على العائد والزكاة." if lang == "العربية" else "Ethical banking product pricing."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.slider("Profitability R", 0, 100, 75); v2 = st.slider("Ethics Index Z", 0, 100, 30)
    st.metric(m_res, f"{(0.6*v1 + 0.4*v2 + 10):.2f}")

# --- 5. التذييل والسيادة الختامية ---
st.sidebar.markdown("---")
# كتابة الاسم بشكل نصي ثابت لضمان عدم حدوث خطأ برمجي
st.sidebar.write(f"© 2026 Developed by: {AUTHOR_NAME}")
