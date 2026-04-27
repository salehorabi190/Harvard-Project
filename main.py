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

# --- 3. الفهرس الموسوعي ---
menu = {
    "P1. الإدخار الوقفي الذكي": "p1", "P2. المشاركة التمكينية المتدرجة": "p2", "P3. الصكوك الوقفية التنموية": "p3",
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

# --- 4. محرك التشغيل التفصيلي ---

if mid == "p1":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Z_{it} = \gamma + \delta_1 W_{it} + \delta_2 R_{it} + \delta_3 T_{it} + \mu_{it}")
    desc = "مُنْتَجُ الإِدِّخَارِ الوَقْفِيِّ الذَّكِيِّ: يتيح للعميل تخصيص نسبة من مدخراته كوقف دائم أو مؤقت، يُستثمر في مشاريع تنموية." if lang == "العربية" else "Smart Endowment Savings Product: Allows allocating a percentage of savings as an endowment for developmental projects."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("نسبة الوقف من الادخار (Wit)", value=80.0)
    v2 = st.number_input("عائد الاستثمار الوقفي (Rit)", value=70.0)
    v3 = st.number_input("مؤشر التفاعل الروحي (Tit)", value=90.0)
    st.metric(m_res, f"{(0.4*v1 + 0.3*v2 + 0.3*v3):.2f}")

elif mid == "p2":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{it} = \alpha + \beta_1 P_{it} + \beta_2 E_{it} + \beta_3 S_{it} + \epsilon_{it}")
    desc = "تمويل الفئات المحرومة بمشاركة متدرجة تتناقص فيها نسبة المصرف بنسبة 20% سنوياً حتى التملك الكامل." if lang == "العربية" else "Participatory financing with 20% annual bank-share reduction."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Pit", value=80.0); v2 = st.number_input("Eit", value=70.0); v3 = st.number_input("Sit", value=90.0)
    st.metric(m_res, f"{(0.4*v1 + 0.3*v2 + 0.3*v3):.2f}")

elif mid == "p3":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"W_{it} = \theta + \lambda_1 C_{it} + \lambda_2 R_{it} + \lambda_3 I_{it} + \nu_{it}")
    desc = "صكوك وقفية تضمن تمويلاً مستداماً للمشاريع التنموية." if lang == "العربية" else "Waqf Sukuk ensuring sustainable funding for projects."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Cit", value=500.0); v2 = st.number_input("Rit", value=20.0); v3 = st.number_input("Iit", value=80.0)
    st.metric(m_res, f"{(v1*0.01 + v2*0.4 + v3*0.5):.2f}")

elif mid == "p4":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"M_{it} = \phi + \rho_1 A_{it} + \rho_2 T_{it} + \rho_3 G_{it} + \epsilon_{it}")
    desc = "مضاربة اجتماعية لتمكين الفقراء بتمويل المصرف وإدارة العميل." if lang == "العربية" else "Social Mudaraba to empower the poor with bank financing."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Ait (Capital)", value=400.0); v2 = st.number_input("Tit (Training)", value=90.0)
    st.metric(m_res, f"{(v1*0.02 + v2*0.5):.2f}")

elif mid == "p5":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Q_{it} = \psi + \eta_1 V_{it} + \eta_2 D_{it} + \eta_3 B_{it} + \xi_{it}")
    desc = "صندوق وقفي تمكيني مشترك كضمان للمشاريع الإنتاجية." if lang == "العربية" else "Joint empowerment Waqf fund for productive projects."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Vit (Fund)", value=600.0); v2 = st.number_input("Dit (Guarantee)", value=100.0)
    st.metric(m_res, f"{(v1*0.02 + v2*0.5):.2f}")

elif mid == "p6":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"H_{it} = \omega + \sigma_1 E_{it} + \sigma_2 Q_{it} + \sigma_3 K_{it} + \varsigma_{it}")
    desc = "إجارة وقفية موصوفة لتأمين سكن أو تعليم بكرامة." if lang == "العربية" else "Forward Waqf Ijarah for dignified housing or education."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Eit (Rent)", value=80.0); v2 = st.number_input("Kit (Dignity)", value=100.0)
    st.metric(m_res, f"{(0.4*v1 + 0.6*v2):.2f}")

elif mid == "m1":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r")
    desc = "تحويل الوظيفة من كدح مادي إلى رسالة وجودية تربط الرسالة بالمعنى." if lang == "العربية" else "Transforming a job into an existential mission."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Rr", value=85.0); v2 = st.number_input("Mr", value=80.0)
    st.metric(m_res, f"{(0.5*v1 + 0.5*v2 + 10):.2f}")

elif mid == "m2":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r")
    desc = "أثر القيادة المتزكية وإلهام القائد في تحقيق الاستخلاف." if lang == "العربية" else "Impact of spiritual leadership and inspiration."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Zr", value=90.0); v2 = st.number_input("Ir", value=85.0)
    st.metric(m_res, f"{(0.6*v1 + 0.4*v2):.2f}")

elif mid == "m3":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"G_r = \alpha + \beta_1 N_r + \beta_2 T_r + \beta_3 M_r")
    desc = "الحوكمة الرمزية والانسجام المقاصدي والنزاهة المؤسسية." if lang == "العربية" else "Symbolic governance and Maqasid harmony."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Nr", value=95.0); v2 = st.number_input("Ar", value=90.0)
    st.metric(m_res, f"{(0.5*v1 + 0.5*v2):.2f}")

elif mid == "m4":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R_r = f(K_{spiritual}, K_{social}, K_{financial})")
    desc = "الاستثمار التزكوي البديل القائم على رأس المال الروحي والقيمي." if lang == "العربية" else "Alternative Tazkiyah investment based on spiritual capital."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("K Spirit", value=90.0); v2 = st.number_input("K Financial", value=60.0)
    st.metric(m_res, f"{(0.7*v1 + 0.3*v2):.2f}")

elif mid == "m5":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Q_r = \frac{\sum Maqasid}{\sum Resources}")
    desc = "التقييم التزكوي للأداء المؤسسي بناءً على كفاءة تحقيق المقاصد الشرعية." if lang == "العربية" else "Tazkiyah assessment based on Maqasid efficiency."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Maqasid", value=85.0); v2 = st.number_input("Resources", value=50.0)
    st.metric(m_res, f"{(v1/max(v2,1)):.2f}")

elif mid == "m6":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"V_r = Faith \times Impact")
    desc = "التحقق الوجودي للأثر الاقتصادي وربطه بمبادئ الاستخلاف." if lang == "العربية" else "Existential verification of economic impact."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Faith Index", value=95.0); v2 = st.number_input("Impact Index", value=80.0)
    st.metric(m_res, f"{(v1*v2/100):.2f}")

elif mid == "m7":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    desc = "القيمة التزكوية المضافة التي تدمج الربح المادي والبركة المعنوية." if lang == "العربية" else "Tazkiyah Value Added (Profit + Barakah)."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("EVA (Material)", value=500.0); v2 = st.number_input("Z factor", value=90.0)
    st.metric(m_res, f"{(v1 + 1.5*v2):.2f}")

elif mid == "m8":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 S + \beta_2 C")
    desc = "سنة الشكر والالتزام كمحرك جوهري للنماء والبركة المادية المستدامة." if lang == "العربية" else "Sunnah of Gratitude and Commitment driver."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Gratitude (S)", value=95.0); v2 = st.number_input("Commitment (C)", value=85.0)
    st.metric(m_res, f"{(0.7*v1 + 0.3*v2 + 15):.2f}")

elif mid == "m9":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_0 + \alpha_1 Z + \alpha_2 G")
    desc = "سنة الظلم والغرور ومؤشر الانهيار الاقتصادي الناتج عن غياب العدالة." if lang == "العربية" else "Sunnah of Injustice: collapse indicator."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Z (Injustice)", value=20.0); v2 = st.number_input("G (Arrogance)", value=30.0)
    st.metric(m_res, f"{(0.8*v1 + 0.2*v2):.2f}")

elif mid == "m10":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"GINI = \frac{1}{n} \sum (Y_i - \bar{Y}) \cdot Z")
    desc = "سنة التداول وضبط توزيع الثروة بمعامل الزكاة لمنع تركز المال." if lang == "العربية" else "Sunnah of Circulation via Zakat pressure."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Income Distribution", value=75.0); v2 = st.number_input("Zakat Pressure", value=85.0)
    st.metric(m_res, f"{(v1*v2/100):.2f}")

elif mid == "m11":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R_e = K_h + K_s + K_e")
    desc = "سنة التمكين وتراكم القوى البشرية والإيمانية والاجتماعية." if lang == "العربية" else "Sunnah of Empowerment: Human & Faith forces."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Human Force", value=85.0); v2 = st.number_input("Faith Force", value=90.0)
    st.metric(m_res, f"{(v1+v2)/2:.2f}")

elif mid == "m12":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"\Delta Y_{poor} = \alpha_1 Z_d + \alpha_2 MF_v")
    desc = "سياسة مكافحة الفقر عبر الزكاة المباشرة والتمويل الأصغر." if lang == "العربية" else "Poverty alleviation via Zakat and Microfinance."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Zakat Distributed", value=85.0); v2 = st.number_input("Microfinance Value", value=75.0)
    st.metric(m_res, f"{(0.6*v1 + 0.4*v2):.2f}%")

elif mid == "m13":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"FBi = \beta_1 PCc - \beta_2 MR")
    desc = "سياسة التسعير العادل وضبط الاحتكار عبر أدوات الرقابة المقاصدية." if lang == "العربية" else "Fair pricing policy and monopoly control."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Regulation (PCc)", value=80.0); v2 = st.number_input("Monopoly MR", value=15.0)
    st.metric(m_res, f"{(0.6*v1 - 0.4*v2 + 20):.2f}")

elif mid == "m14":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"ES = \beta_1 LTp + \beta_2 OAr")
    desc = "سياسة التمكين المهني وتكافؤ الفرص في سوق العمل." if lang == "العربية" else "Vocational empowerment and equal opportunities."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("LTp Training", value=85.0); v2 = st.number_input("OAr Equality", value=80.0)
    st.metric(m_res, f"{(0.5*v1 + 0.5*v2):.2f}")

elif mid == "m15":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"CR = \delta_1 NFs + \delta_2 RR")
    desc = "سياسة الأزمات وفقه الضرورة لتأمين الحاجات الأساسية (NFs)." if lang == "العربية" else "Crisis policy: Securing basic needs."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Necessities", value=95.0); v2 = st.number_input("Recovery Speed", value=80.0)
    st.metric(m_res, f"{(0.7*v1 + 0.3*v2):.2f}")

elif mid == "m16":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Yt = \beta_1 Ft + \beta_2 Et")
    desc = "هندسة العدالة السوقية بين السعر العادل (Ft) والتوزيع العادل (Et)." if lang == "العربية" else "Market justice engineering (Price vs Dist)."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Price Justice", value=80.0); v2 = st.number_input("Dist Justice", value=75.0)
    st.metric(m_res, f"{(0.5*v1 + 0.5*v2):.2f}")

elif mid == "m17":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_t = \beta_1 Info + \beta_2 Trust")
    desc = "الشفافية والتدفق المعلوماتي الموثوق في السوق." if lang == "العربية" else "Transparency and reliable info flow."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Information flow", value=90.0); v2 = st.number_input("Trust level", value=85.0)
    st.metric(m_res, f"{(0.6*v1 + 0.4*v2):.2f}")

elif mid == "m18":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{anti} = 2500 - HHI")
    desc = "هندسة منع الاحتكار وتوسيع قاعدة المنافسة العادلة." if lang == "العربية" else "Monopoly prevention engineering."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("HHI Index", value=1100.0)
    st.metric(m_res, f"{(2500-v1)/25:.2f}%")

elif mid == "m19":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{niya} = \sum GoodIntentions")
    desc = "هندسة النية الصالحة في السلوك الاقتصادي المؤسسي." if lang == "العربية" else "Good Intention engineering in behavior."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Niya Index", value=95.0)
    st.metric(m_res, f"{(v1*1.1):.2f}")

elif mid == "m20":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_k = C + (A_s \times 2.5\%)")
    desc = "سعر الكفاية لمنع الغلاء وضمان حق الفقير في السلعة." if lang == "العربية" else "Sufficiency price for basic needs."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Cost C", value=100.0); v2 = st.number_input("Security Coefficient", value=80.0)
    st.metric(m_res, f"{v1 + (v2*0.025*v1):.2f}")

elif mid == "m21":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Q_s = f(P, Z_f, B)")
    desc = "العرض الرحيم القائم على تسهيلات الزكاة والبركة." if lang == "العربية" else "Merciful Supply via Barakah logic."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Price Level", value=65.0); v2 = st.number_input("Barakah Index", value=95.0)
    st.metric(m_res, f"{(0.4*v1 + 0.6*v2):.2f}")

elif mid == "m22":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Q_d = f(P, Need, Ethics)")
    desc = "الطلب العادل المرتبط بالحاجة الحقيقية والأخلاق." if lang == "العربية" else "Fair Demand linked to real needs."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Price P", value=50.0); v2 = st.number_input("Ethics Level", value=85.0)
    st.metric(m_res, f"{(0.5*v1 + 0.5*v2):.2f}")

elif mid == "m23":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"I_s = \frac{Needs - Q_s}{Capacity}")
    desc = "معيار تدخل الدولة المقاصدي لسد فجوات السوق." if lang == "العربية" else "Maqasid State Intervention criteria."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Unmet Needs (N)", value=70.0); v2 = st.number_input("State Capacity", value=50.0)
    st.metric(m_res, f"{(v1/max(v2,1)):.2f}")

elif mid == "m24":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{pub} = \sum Financials")
    desc = "التمكين المالي العام لضمان سيولة الخدمات الأساسية." if lang == "العربية" else "Public financial empowerment."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Finance Level", value=85.0)
    st.metric(m_res, f"{(v1*1.05):.2f}")

elif mid == "m25":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{monetary} = M \cdot V + Z_{speed}")
    desc = "النظام النقدي وسرعة دوران الزكاة في تفعيل الاقتصاد." if lang == "العربية" else "Monetary system and Zakat velocity."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    v1 = st.number_input("Money Mass", value=70.0); v2 = st.number_input("Z-Velocity", value=85.0)
    st.metric(m_res, f"{(v1*0.6 + v2*0.4):.2f}")

elif mid == "m26":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    # تعريف التبويبات للنماذج الأربعة
    tab1, tab2, tab3, tab4 = st.tabs([
        "1. النموذج القيمي (الزكاة)", 
        "2. النموذج السلعي", 
        "3. النموذج الوقفي", 
        "4. النموذج الذهبي الرمزي"
    ])
    # --- أولاً: النموذج القيمي ---
    with tab1:
        st.subheader("أولاً: النموذج القيمي – ربط العملة بمؤشر الزكاة")
        st.latex(r"Y_1 = \beta_0 + \beta_1 Z + \beta_2 E - \beta_3 C - \beta_4 P + \epsilon")
        st.info("الفرضية: الزكاة تخرج المال من الاكتناز للتداول، مما يعزز الاستقرار النقدي والعدالة.")    
        col1, col2 = st.columns(2)
        with col1:
            z_val = st.number_input("معدل الزكاة المحصلة (Z)", value=2.5, key="z_val")
            e_val = st.number_input("معدل التوظيف (E)", value=90.0, key="e_val")
        with col2:
            c_val = st.number_input("معدل التضخم (C)", value=5.0, key="c_val_z")
            p_val = st.number_input("مؤشر الفقر (P)", value=15.0, key="p_val_z")  
        y1 = (0.4 * z_val + 0.3 * e_val - 0.2 * c_val - 0.1 * p_val)
        st.metric("مؤشر الاستقرار القيمي (Y1)", f"{y1:.2f}")
    # --- ثانياً: النموذج السلعي ---
    with tab2:
        st.subheader("ثانياً: النموذج السلعي – ربط العملة بسلة السلع الأساسية")
        st.latex(r"Y_2 = \beta_0 + \beta_1 S - \beta_2 I - \beta_3 V - \beta_4 P + \epsilon")
        st.info("الفرضية: ربط العملة بالقمح والزيت والتمر يحقق استقراراً حقيقياً وعدالة شرائية للفقراء.")       
        col1, col2 = st.columns(2)
        with col1:
            s_val = st.number_input("مؤشر أسعار السلع (S)", value=85.0, key="s_commodity")
            i_val = st.number_input("معدل التضخم (I)", value=4.0, key="i_commodity")
        with col2:
            v_val_c = st.number_input("تقلبات سعر الصرف (V)", value=10.0, key="v_commodity")
            p_val_c = st.number_input("مؤشر الفقر (P)", value=20.0, key="p_commodity")          
        y2 = (0.5 * s_val - 0.2 * i_val - 0.2 * v_val_c - 0.1 * p_val_c)
        st.metric("مؤشر الاستقرار السلعي (Y2)", f"{y2:.2f}")
    # --- ثالثاً: النموذج الوقفي ---
    with tab3:
        st.subheader("ثالثاً: النموذج الوقفي – ربط العملة بالوقف الإنتاجي")
        st.latex(r"Y_3 = \beta_0 + \beta_1 W + \beta_2 R - \beta_3 C - \beta_4 P + \epsilon")
        st.info("الفرضية: الوقف يوفر تمويلاً تنموياً غير ربوي، مما يقلل الاعتماد على أدوات الفائدة.")        
        col1, col2 = st.columns(2)
        with col1:
            w_val = st.number_input("حجم الوقف الإنتاجي (W)", value=30.0, key="w_waqf")
            r_val_w = st.number_input("معدل العائد الوقفي (R)", value=12.0, key="r_waqf")
        with col2:
            c_val_w = st.number_input("معدل التضخم (C)", value=3.5, key="c_waqf")
            p_val_w = st.number_input("مؤشر الفقر (P)", value=10.0, key="p_waqf")          
        y3 = (0.4 * w_val + 0.3 * r_val_w - 0.2 * c_val_w - 0.1 * p_val_w)
        st.metric("مؤشر الاستقرار الوقفي (Y3)", f"{y3:.2f}")
    # --- رابعاً: النموذج الذهبي الرمزي ---
    with tab4:
        st.subheader("رابعاً: النموذج الذهبي الرمزي – ربط العملة بالمعادن النفيسة")
        st.latex(r"Y_4 = \beta_0 + \beta_1 G + \beta_2 F - \beta_3 V - \beta_4 C + \epsilon")
        st.info("الفرضية: الذهب والفضة يمثلان قيمة حقيقية غير قابلة للتلاعب، مما يقلل أثر المضاربات.")   
        col1, col2 = st.columns(2)
        with col1:
            g_val = st.number_input("نسبة تغطية الذهب (G)", value=95.0, key="g_gold")
            f_val = st.number_input("نسبة تغطية الفضة (F)", value=80.0, key="f_gold")
        with col2:
            v_val_g = st.number_input("تقلبات سعر الصرف (V)", value=5.0, key="v_gold")
            c_val_g = st.number_input("معدل التضخم (C)", value=2.0, key="c_gold")           
        y4 = (0.4 * g_val + 0.3 * f_val - 0.2 * v_val_g - 0.1 * c_val_g)
        st.metric("مؤشر الاستقرار الذهبي (Y4)", f"{y4:.2f}")
    # --- النتيجة الإجمالية (سعر الصرف المقاصدي) ---
    st.markdown("---")
    st.subheader("🏛️ النتيجة النهائية: هندسة سعر الصرف السيادي")    
    # حساب المتوسط المرجح للنماذج الأربعة ليعطي سعر الصرف النهائي
    final_exchange_stability = (y1 + y2 + y3 + y4) / 4    
    st.metric("مؤشر سعر الصرف السيادي المجمع", f"{final_exchange_stability:.2f}")
    st.success("هذا المؤشر يمثل القيمة الحقيقية للعملة بناءً على الأصول الحقيقية والمقاصد الشرعية.")

elif mid == "m27":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.markdown("### هَنْدَسَةُ سِعْرِ الفَائِدَةِ بَيْنَ الرِّبَا وَالبَدَائِلِ الرَّمْزِيَّةِ")
    # تعريف التبويبات للنماذج الثلاثة
    tab1, tab2, tab3 = st.tabs([
        "1. معدل العائد الإسلامي المقاصدي", 
        "2. الهندسة المالية الإسلامية", 
        "3. تسعير المنتجات المصرفية"
    ])
    # --- النموذج الأول: معدل العائد الإسلامي المقاصدي ---
    with tab1:
        st.subheader("النموذج الأول: مُعَدَّلُ العَائِدِ الإِسْلَامِيُّ المَقَاصِدِيُّ")
        st.latex(r"R = \alpha_1 \pi + \alpha_2 T + \alpha_3 Z + \alpha_4 E + \epsilon")
        st.info("الهدف: بناء معدل عائد بديل للفائدة يُراعي العدالة والتمكين والحفاظ على القوة الشرائية.")       
        col1, col2 = st.columns(2)
        with col1:
            pi_1 = st.number_input("الربحية المتوقعة (π)", value=70.0, key="n1_pi")
            t_1 = st.number_input("مؤشر التمكين (T)", value=80.0, key="n1_t")
        with col2:
            z_1 = st.number_input("معدل الزكاة (Z)", value=2.5, key="n1_z")
            e_1 = st.number_input("التضخم المتوقع (E)", value=4.0, key="n1_e")       
        # حساب R (بأوزان افتراضية للمعاملات)
        r_final = (0.4 * pi_1 + 0.3 * t_1 + 0.1 * z_1 + 0.2 * e_1)
        st.metric("معدل العائد المقاصدي (R)", f"{r_final:.2f}%")
    # --- النموذج الثاني: الهندسة المالية الإسلامية المقاصدية ---
    with tab2:
        st.subheader("النموذج الثاني: نَمُوذَجُ الهَنْدَسَةِ المَالِيَّةِ الإِسْلَامِيَّةِ المَقَاصِدِيَّةِ")
        st.latex(r"P = \beta_1 R + \beta_2 T + \beta_3 S + \beta_4 \pi + \beta_5 Z + \epsilon")
        st.info("الهدف: إعادة هندسة الوظيفة المالية ليكون المال أمانة استخلافية، وتسعير الأدوات (كصكوك المشاركة).")      
        c1, c2 = st.columns(2)
        with c1:
            r_2 = st.number_input("معدل العائد المقاصدي (R)", value=r_final, key="n2_r")
            t_2 = st.number_input("مؤشر التمكين (T)", value=85.0, key="n2_t")
            s_2 = st.number_input("درجة الالتزام الشرعي (S)", value=95.0, key="n2_s")
        with c2:
            pi_2 = st.number_input("الربحية المتوقعة (π)", value=60.0, key="n2_pi")
            z_2 = st.number_input("معدل الزكاة (Z)", value=2.5, key="n2_z")      
        p_finance = (0.3 * r_2 + 0.2 * t_2 + 0.2 * s_2 + 0.2 * pi_2 + 0.1 * z_2)
        st.metric("سعر الأداة المالية (P)", f"{p_finance:.2f}")
    # --- النموذج الثالث: تسعير المنتجات المصرفية ---
    with tab3:
        st.subheader("النموذج الثالث: تَسْعِيرُ المُنْتَجَاتِ المَصْرَفِيَّةِ بالعائد المقاصدي")
        st.latex(r"P = \beta_1 R + \beta_2 T + \beta_3 S + \beta_4 \pi + \beta_5 Z + \epsilon")
        st.info("الهدف: تسعير الودائع والتمويل بناءً على المشاركة والمضاربة، والوظيفة التزكوية للمال.")       
        cc1, cc2 = st.columns(2)
        with cc1:
            r_3 = st.number_input("العائد الإسلامي (R)", value=r_final, key="n3_r")
            t_3 = st.number_input("التمكين (T)", value=75.0, key="n3_t")
            s_3 = st.number_input("الالتزام الشرعي (S)", value=100.0, key="n3_s")
        with cc2:
            pi_3 = st.number_input("الربحية المشروعة (π)", value=55.0, key="n3_pi")
            z_3 = st.number_input("معدل الزكاة (Z)", value=2.5, key="n3_z")    
        p_product = (0.25 * r_3 + 0.25 * t_3 + 0.2 * s_3 + 0.2 * pi_3 + 0.1 * z_3)
        st.metric("سعر المنتج المصرفي (P)", f"{p_product:.2f}")
    # استنتاج نهائي للمنصة
    st.markdown("---")
    st.success("تم تطبيق النماذج التطبيقية الثلاثة بنجاح، مما يعزز الاستقلال عن سعر الفائدة الربوي وتفعيل الوظيفة التمكينية للمال.")

elif mid == "m28":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    # 1. عرض المعادلة القياسية المقترحة للهندسة المالية
    st.latex(r"P = \beta_1 R + \beta_2 T + \beta_3 S + \beta_4 \pi + \beta_5 Z + \epsilon")
    # 2. شرح الفكرة العامة للنموذج (نصك الأصلي)
    desc = """نَمُوذَجُ الهَنْدَسَةِ المَالِيَّةِ الإِسْلَامِيَّةِ المَقَاصِدِيَّةِ: 
    إعادة هندسة الوظيفة المالية بحيث يُنظر للمال كأمانة لا سلعة، وربط التمويل بمقاصد العدالة والتزكية والتمكين.""" if lang == "العربية" else "Maqasid Islamic Financial Engineering: Re-engineering finance as a trust (Amanah), linking funding to justice, purification, and empowerment."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)   
    # 3. خانات إدخال الرموز (المتغيرات)
    st.write("### إدخال قيم متغيرات الهندسة المالية المقاصدية:")   
    col1, col2 = st.columns(2)
    with col1:
        v1 = st.number_input("معدل العائد الإسلامي المقاصدي (R)", value=75.0, key="m28_v1")
        v2 = st.number_input("مؤشر التمكين (T)", value=80.0, key="m28_v2")
        v3 = st.number_input("درجة الالتزام الشرعي (S)", value=90.0, key="m28_v3")
    with col2:
        v4 = st.number_input("الربحية المتوقعة (π)", value=65.0, key="m28_v4")
        v5 = st.number_input("معدل الزكاة كمقياس أخلاقي (Z)", value=2.5, key="m28_v5")
    # 4. حساب الناتج النهائي (P: سعر الأداة المالية)
    # تم توزيع معاملات الانحدار (Beta) لتعكس التأثير الطردي للتمكين والالتزام والربحية
    p_financial = (0.3*v1 + 0.2*v2 + 0.25*v3 + 0.15*v4 + 0.1*v5)
    # 5. ظهور الناتج النهائي
    st.metric("سعر الأداة المالية الإسلامية (P)", f"{p_financial:.2f}")

elif mid == "m29":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    # 1. عرض المعادلة القياسية المقترحة
    st.latex(r"P = \beta_1 R + \beta_2 T + \beta_3 S + \beta_4 \pi + \beta_5 Z + \epsilon")
    # 2. شرح الفكرة العامة والنموذج (نصك الأصلي)
    desc = """تَسْعِيرُ المُنْتَجَاتِ المَصْرَفِيَّةِ بِالعَائِدِ الإِسْلَامِيِّ المَقَاصِدِيِّ: 
    نموذج يُعيد تعريف التسعير على أساس التمكين والتزكية والالتزام الشرعي، بعيداً عن سعر الفائدة التقليدي.""" if lang == "العربية" else "Pricing banking products based on Maqasid return, empowerment, and Sharia compliance, independent of interest rates."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    # 3. خانات إدخال الرموز (المتغيرات) بناءً على عناصر النموذج
    st.write("### إدخال قيم متغيرات التسعير المقاصدي:")
    col1, col2 = st.columns(2)
    with col1:
        v1 = st.number_input("معدل العائد الإسلامي المقاصدي (R)", value=70.0)
        v2 = st.number_input("مؤشر التمكين (T)", value=85.0)
        v3 = st.number_input("درجة الالتزام الشرعي (S)", value=95.0)
    with col2:
        v4 = st.number_input("الربحية المتوقعة (π)", value=60.0)
        v5 = st.number_input("معدل الزكاة كمقياس أخلاقي (Z)", value=2.5)
    # 4. حساب الناتج النهائي (P: سعر المنتج)
    # ملاحظة: تم استخدام أوزان نسبية (Beta coefficients) لتفعيل المعادلة حسابياً
    # الأوزان: R=0.3, T=0.2, S=0.2, π=0.2, Z=0.1
    p_price = (0.3*v1 + 0.2*v2 + 0.2*v3 + 0.2*v4 + 0.1*v5)
    # 5. ظهور الناتج النهائي
    st.metric("سعر المنتج المصرفي الإسلامي (P)", f"{p_price:.2f}")
