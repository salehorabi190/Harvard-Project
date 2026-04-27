import streamlit as st
import numpy as np

# --- 1. الإعدادات والسيادة البصرية (ابتكار أ.د. صالح عرابي 2026) ---
st.set_page_config(page_title="SEP 2026 | Prof. Dr. Saleh Orrabi", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&family=Playfair+Display:wght@700&display=swap');
    .stApp { background-color: #f4f7f6; }
    .logo-container { text-align: center; padding: 45px; background: linear-gradient(135deg, #1e4d2b 0%, #11301a 100%); border-radius: 30px; border-bottom: 12px solid #d4af37; margin-bottom: 40px; color: white; box-shadow: 0 20px 40px rgba(0,0,0,0.4); }
    .logo-text { font-family: 'Playfair Display', serif; font-size: 70px; letter-spacing: 5px; }
    .explanation-box { background-color: #ffffff; padding: 35px; border-radius: 20px; border-right: 20px solid #2e7d32; color: #1b5e20; line-height: 2.2; margin-bottom: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); font-family: 'Cairo', sans-serif; font-size: 18px; }
    .header-style { color: #1e4d2b; font-family: 'Cairo', sans-serif; font-weight: bold; border-bottom: 6px solid #d4af37; padding-bottom: 20px; margin-bottom: 40px; text-align: right; }
    .stMetric { background: #ffffff; padding: 30px; border-radius: 25px; border: 2px solid #e0e0e0; box-shadow: 0 8px 20px rgba(0,0,0,0.03); }
    </style>
    """, unsafe_allow_html=True)

# --- 2. نظام اللغات والواجهة ---
lang = st.sidebar.selectbox("🌐 اختر اللغة / Select Language", ["العربية", "English"])

# تعريف اسم صاحب الابتكار كمتغير نصي لتجنب أخطاء السنتكس
author_name = "Prof. Dr. Saleh Orrabi" if lang == "English" else "أ.د. صالح عرابي"

if lang == "العربية":
    m_res = "النتيجة النهائية"
    m_auth = f"إعداد وتطوير: {author_name} - 2026"
    m_title = "بروتوكول هندسة الاستخلاف الاقتصادي"
    sidebar_head = "🏛️ القائمة الهندسية الكاملة"
    select_msg = "اختر النموذج الهندسي المطلوب:"
else:
    m_res = "Final Result"
    m_auth = f"Developed by: {author_name} - 2026"
    m_title = "Economic Stewardship Engineering Protocol"
    sidebar_head = "🏛️ Full Engineering List"
    select_msg = "Select the required Engineering Model:"

st.markdown(f"""
    <div class="logo-container">
        <div class="logo-text">S.E.P 2026</div>
        <div style="font-size: 32px; color: #d4af37; font-weight: bold; margin-top:15px;">{m_title}</div>
        <div style="font-size: 20px; opacity: 0.9;">{m_auth}</div>
    </div>
    """, unsafe_allow_html=True)

# --- 3. الفهرس الموسوعي الشامل (35 نموذجاً مفصلاً حرفياً) ---
st.sidebar.header(sidebar_head)
menu = {
    "P1. المشاركة التمكينية المتدرجة": "p1",
    "P2. الإدخار الوقفي الذكي": "p2",
    "P3. الصكوك الوقفية التنموية": "p3",
    "P4. المضاربة الاجتماعية التمكينية": "p4",
    "P5. صندوق الوقف التمكيني المشترك": "p5",
    "P6. الإجارة الوقفية الموصوفة": "p6",
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
    "11. سنة التمكين (R_e)": "m11",
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
    "26. هندسة سعر الصرف (Y_fx)": "m26",
    "27. معدل العائد المقاصدي (R)": "m27",
    "28. هندسة المالية المقاصدية (P)": "m28",
    "29. تسعير المنتجات المصرفية (P_b)": "m29"
}

choice = st.sidebar.selectbox(select_msg, list(menu.keys()))
mid = menu[choice]

# --- 4. محرك التشغيل (الـ 35 كتلة سطر بسطر) ---

if mid == "p1":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{it} = \alpha + \beta_1 P_{it} + \beta_2 E_{it} + \beta_3 S_{it} + \epsilon_{it}")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> تمويل الفئات المحرومة بمشاركة متدرجة تتناقص فيها نسبة المصرف بنسبة 20% سنوياً حتى التملك الكامل.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Financing for disadvantaged groups through progressive participation with the bank share decreasing by 20% annually.</div>', unsafe_allow_html=True)
    p1a = st.slider("Pit", 0, 100, 80); p1b = st.slider("Eit", 0, 100, 70); p1c = st.slider("Sit", 0, 100, 90)
    st.metric(m_res, f"{(0.4*p1a + 0.3*p1b + 0.3*p1c):.2f}")

elif mid == "p2":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Z_{it} = \gamma + \delta_1 W_{it} + \delta_2 R_{it} + \delta_3 T_{it} + \mu_{it}")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> دمج الوقف في منتجات الادخار لتحقيق استدامة تنموية وتفاعلاً روحياً.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Integrating Waqf in savings products to achieve developmental sustainability and spiritual engagement.</div>', unsafe_allow_html=True)
    p2a = st.slider("Wit", 0, 100, 30); p2b = st.slider("Rit", 0, 100, 60); p2c = st.slider("Tit", 0, 100, 85)
    st.metric(m_res, f"{(0.5*p2a + 0.3*p2b + 0.2*p2c):.2f}")

elif mid == "p3":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"W_{it} = \theta + \lambda_1 C_{it} + \lambda_2 R_{it} + \lambda_3 I_{it} + \nu_{it}")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> صكوك وقفية تمول مشاريع تنموية وتخصص جزءاً من العائد للوقف الدائم.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Waqf Sukuk funding developmental projects with partial returns dedicated to permanent endowment.</div>', unsafe_allow_html=True)
    p3a = st.slider("Cit", 0, 1000, 500); p3b = st.slider("Rit", 0, 100, 20); p3c = st.slider("Iit", 0, 100, 80)
    st.metric(m_res, f"{(p3a*0.01 + p3b*0.4 + p3c*0.5):.2f}")

elif mid == "p4":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"M_{it} = \phi + \rho_1 A_{it} + \rho_2 T_{it} + \rho_3 G_{it} + \epsilon_{it}")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> مضاربة اجتماعية لتمكين الفقراء بتمويل المصرف وإدارة العميل مع دعم تقني.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Social Mudaraba for empowering the poor with bank capital and client management plus technical support.</div>', unsafe_allow_html=True)
    p4a = st.slider("Ait", 0, 1000, 400); p4b = st.slider("Tit", 0, 100, 90); p4c = st.slider("Git", 0, 100, 25)
    st.metric(m_res, f"{(p4a*0.02 + p4b*0.4 + p4c*0.4):.2f}")

elif mid == "p5":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Q_{it} = \psi + \eta_1 V_{it} + \eta_2 D_{it} + \eta_3 B_{it} + \xi_{it}")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> صندوق وقفي تمكيني مشترك يستخدم الوقف كضمان للتمويل الإنتاجي.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Joint Empowerment Waqf Fund using Waqf assets as collateral for productive financing.</div>', unsafe_allow_html=True)
    p5a = st.slider("Vit", 0, 1000, 600); p5b = st.slider("Dit", 0, 100, 100); p5c = st.slider("Bit", 0, 100, 30)
    st.metric(m_res, f"{(p5a*0.02 + p5b*0.5 + p5c*0.3):.2f}")

elif mid == "p6":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"H_{it} = \omega + \sigma_1 E_{it} + \sigma_2 Q_{it} + \sigma_3 K_{it} + \varsigma_{it}")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> إجارة وقفية موصوفة لتأمين سكن أو تعليم مع حفظ الكرامة.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Forward Waqf Ijarah for securing dignified housing or education.</div>', unsafe_allow_html=True)
    p6a = st.slider("Eit", 0, 100, 80); p6b = st.slider("Qit", 0, 100, 95); p6c = st.slider("Kit", 0, 100, 100)
    st.metric(m_res, f"{(0.3*p6a + 0.3*p6b + 0.4*p6c):.2f}")

elif mid == "m1":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> تحويل الوظيفة من كدح مادي إلى رسالة وجودية تربط الرسالة بالمعنى.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Transforming a job from material toil into an existential mission linking mission to meaning.</div>', unsafe_allow_html=True)
    m1r = st.slider("Rr", 0, 100, 85); m1m = st.slider("Mr", 0, 100, 80)
    st.metric(m_res, f"{(0.5*m1r + 0.5*m1m + 10):.2f}")

elif mid == "m2":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> قياس أثر القيادة المتزكية وإلهام القائد في تحقيق الاستخلاف.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Measuring the impact of spiritual leadership and inspiration in achieving stewardship.</div>', unsafe_allow_html=True)
    m2z = st.slider("Zr", 0, 100, 90); m2i = st.slider("Ir", 0, 100, 85)
    st.metric(m_res, f"{(0.6*m2z + 0.4*m2i):.2f}")

elif mid == "m3":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"G_r = \alpha + \beta_1 N_r + \beta_2 T_r + \beta_3 M_r")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> الحوكمة الرمزية والانسجام المقاصدي والنزاهة المؤسسية.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Symbolic Governance, Maqasid Harmony, and Institutional Integrity.</div>', unsafe_allow_html=True)
    m3n = st.slider("Nr", 0, 100, 95); m3a = st.slider("Ar", 0, 100, 90)
    st.metric(m_res, f"{(0.5*m3n + 0.5*m3a):.2f}")

elif mid == "m4":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R_r = f(K_{spiritual}, K_{social}, K_{financial})")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> الاستثمار التزكوي البديل القائم على رأس المال الروحي والقيمي.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Alternative Tazkiyah Investment based on spiritual and value-based capital.</div>', unsafe_allow_html=True)
    m4s = st.slider("K spirit", 0, 100, 90); m4f = st.slider("K fin", 0, 100, 60)
    st.metric(m_res, f"{(0.7*m4s + 0.3*m4f):.2f}")

elif mid == "m5":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Q_r = \sum Maqasid / \sum Resources")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> التقييم التزكوي للأداء المؤسسي بناءً على كفاءة المقاصد.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Tazkiyah assessment of institutional performance based on Maqasid efficiency.</div>', unsafe_allow_html=True)
    m5m = st.slider("Maqasid", 0, 100, 85); m5r = st.slider("Resources", 1, 100, 50)
    st.metric(m_res, f"{(m5m/m5r):.2f}")

elif mid == "m6":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"V_r = Faith \times Impact")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> التحقق الوجودي للأثر الاقتصادي وربطه بمبادئ الاستخلاف.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Existential verification of economic impact linked to Stewardship principles.</div>', unsafe_allow_html=True)
    m6a = st.slider("Faith", 0, 100, 95); m6b = st.slider("Impact", 0, 100, 80)
    st.metric(m_res, f"{(m6a*m6b/100):.2f}")

elif mid == "m7":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> القيمة التزكوية المضافة التي تدمج الربح المادي والبركة المعنوية.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Tazkiyah Value Added integrating material profit and spiritual blessing.</div>', unsafe_allow_html=True)
    m7e = st.slider("EVA", 0, 1000, 500); m7z = st.slider("Z factor", 0, 100, 90)
    st.metric(m_res, f"{(m7e + 1.5*m7z):.2f}")

elif mid == "m8":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 S + \beta_2 C")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سنة الشكر والالتزام كمحرك جوهري للنماء والبركة المادية.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> The Sunnah of Gratitude and Commitment as a driver for growth and blessing.</div>', unsafe_allow_html=True)
    m8s = st.slider("S (Gratitude)", 0, 100, 95); m8c = st.slider("C (Commitment)", 0, 100, 85)
    st.metric(m_res, f"{(0.7*m8s + 0.3*m8c + 15):.2f}%")

elif mid == "m9":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_0 + \alpha_1 Z + \alpha_2 G")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سنة الظلم والغرور ومؤشر الانهيار الاقتصادي.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> The Sunnah of Injustice and Arrogance as an economic collapse indicator.</div>', unsafe_allow_html=True)
    m9z = st.slider("Z (Injustice)", 0, 100, 20); m9g = st.slider("G (Arrogance)", 0, 100, 30)
    st.metric(m_res, f"{(0.8*m9z + 0.2*m9g):.2f}")

elif mid == "m10":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"GINI = \frac{1}{n} \sum (Y_i - \bar{Y}) \cdot Z")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سنة التداول وضغط الزكاة لإعادة تدوير الثروة.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> The Sunnah of Circulation and Zakat pressure for wealth recycling.</div>', unsafe_allow_html=True)
    m10a = st.slider("Income Dist", 0, 100, 75); m10b = st.slider("Zakat Press", 0, 100, 85)
    st.metric(m_res, f"{(m10a*m10b/100):.2f}")

elif mid == "m11":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R_e = K_h + K_s + K_e")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سنة التمكين وتراكم القوى البشرية والإيمانية والاجتماعية.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> The Sunnah of Empowerment and accumulation of human, spiritual, and social forces.</div>', unsafe_allow_html=True)
    m11h = st.slider("Human K", 0, 100, 85); m11e = st.slider("Faith K", 0, 100, 90)
    st.metric(m_res, f"{(m11h + m11e)/2:.2f}")

elif mid == "m12":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"\Delta Y_{poor} = \alpha_1 Z_d + \alpha_2 MF_v")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سياسة مكافحة الفقر عبر الزكاة المباشرة والتمويل الأصغر.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Poverty alleviation policy via direct Zakat and microfinance.</div>', unsafe_allow_html=True)
    m12z = st.slider("Zakat Dist", 0, 100, 85); m12m = st.slider("Microfinance", 0, 100, 75)
    st.metric(m_res, f"{(0.6*m12z + 0.4*m12m):.2f}%")

elif mid == "m13":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"FBi = \beta_1 PCc - \beta_2 MR")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سياسة التسعير العادل وضبط الاحتكار عبر الرقابة المقاصدية.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Fair Pricing policy and monopoly control via Maqasid monitoring.</div>', unsafe_allow_html=True)
    m13p = st.slider("Regulation", 0, 100, 80); m13m = st.slider("Monopoly", 0, 100, 15)
    st.metric(m_res, f"{(0.6*m13p - 0.4*m13m + 20):.2f}")

elif mid == "m14":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"ES = \beta_1 LTp + \beta_2 OAr")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سياسة التمكين المهني وتكافؤ الفرص في سوق العمل.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Vocational empowerment policy and equal opportunity in the labor market.</div>', unsafe_allow_html=True)
    m14l = st.slider("Training", 0, 100, 85); m14o = st.slider("Equality", 0, 100, 80)
    st.metric(m_res, f"{(0.5*m14l + 0.5*m14o):.2f}")

elif mid == "m15":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"CR = \delta_1 NFs + \delta_2 RR")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سياسة الأزمات وفقه الضرورة لتأمين الحاجات الأساسية.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Crisis policy and Jurisprudence of Necessity for securing basic needs.</div>', unsafe_allow_html=True)
    m15n = st.slider("Necessities", 0, 100, 95); m15r = st.slider("Recovery Speed", 0, 100, 80)
    st.metric(m_res, f"{(0.7*m15n + 0.3*m15r):.2f}")

elif mid == "m16":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Yt = \beta_1 Ft + \beta_2 Et")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> هندسة العدالة السوقية بين السعر والتوزيع.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Market justice engineering between price and distribution.</div>', unsafe_allow_html=True)
    m16f = st.slider("Fair Price", 0, 100, 80); m16e = st.slider("Fair Dist", 0, 100, 75)
    st.metric(m_res, f"{(0.5*m16f + 0.5*m16e):.2f}")

elif mid == "m17":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_t = \beta_1 Info + \beta_2 Trust")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> الشفافية والتدفق المعلوماتي الموثوق في السوق.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Transparency and reliable information flow in the market.</div>', unsafe_allow_html=True)
    m17i = st.slider("Info Flow", 0, 100, 90); m17t = st.slider("Trust Index", 0, 100, 85)
    st.metric(m_res, f"{(0.6*m17i + 0.4*m17t):.2f}")

elif mid == "m18":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{anti} = 2500 - HHI")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> هندسة منع الاحتكار وتوسيع قاعدة المنافسة العادلة.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Monopoly prevention engineering and expanding fair competition base.</div>', unsafe_allow_html=True)
    m18h = st.slider("HHI Index", 0, 2500, 1100)
    st.metric(m_res, f"{(2500-m18h)/25:.2f}%")

elif mid == "m19":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{niya} = \sum GoodIntentions")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> هندسة النية الصالحة في السلوك الاقتصادي المؤسسي.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Good Intention engineering in institutional economic behavior.</div>', unsafe_allow_html=True)
    m19n = st.slider("Intention Index", 0, 100, 95)
    st.metric(m_res, f"{(m19n*1.1):.2f}")

elif mid == "m20":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_k = C + (A_s \times 2.5\%)")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سعر الكفاية لمنع الغلاء وضمان حق الفقير في السلعة.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Sufficiency price for preventing inflation and ensuring the poor\'s right to goods.</div>', unsafe_allow_html=True)
    m20c = st.number_input("Cost C", value=100); m20a = st.slider("As (Security)", 0, 100, 80)
    st.metric(m_res, f"{m20c + (m20a*0.025*m20c):.2f}")

elif mid == "m21":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Q_s = f(P, Z_f, B)")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> العرض الرحيم القائم على تسهيلات الزكاة والبركة.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Merciful Supply based on Zakat facilities and Barakah.</div>', unsafe_allow_html=True)
    m21p = st.slider("Price P", 0, 100, 65); m21b = st.slider("Barakah B", 0, 100, 95)
    st.metric(m_res, f"{(0.4*m21p + 0.6*m21b):.2f}")

elif mid == "m22":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Q_d = f(P, Need, Ethics)")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> الطلب العادل المرتبط بالحاجة الحقيقية والأخلاق الاقتصادية.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Fair Demand linked to real needs and economic ethics.</div>', unsafe_allow_html=True)
    m22p = st.slider("Price", 0, 100, 50); m22e = st.slider("Ethics", 0, 100, 85)
    st.metric(m_res, f"{(0.5*m22p + 0.5*m22e):.2f}")

elif mid == "m23":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"I_s = \frac{Needs - Q_s}{Capacity}")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> معيار تدخل الدولة المقاصدي لسد فجوات السوق.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Maqasid State Intervention criteria for closing market gaps.</div>', unsafe_allow_html=True)
    m23n = st.slider("Unmet Needs", 0, 100, 70); m23c = st.slider("Capacity", 1, 100, 50)
    st.metric(m_res, f"{(m23n/m23c):.2f}")

elif mid == "m24":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{pub} = \sum Financials")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> التمكين المالي العام لضمان سيولة الخدمات الأساسية.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Public financial empowerment to ensure liquidity for basic services.</div>', unsafe_allow_html=True)
    m24f = st.slider("Public Finance", 0, 100, 85)
    st.metric(m_res, f"{(m24f*1.05):.2f}")

elif mid == "m25":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{monetary} = M \cdot V + Z_{speed}")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> النظام النقدي وسرعة دوران الزكاة في تفعيل الاقتصاد.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Monetary system and Zakat velocity in activating the economy.</div>', unsafe_allow_html=True)
    m25m = st.slider("Money M", 0, 100, 70); m25z = st.slider("Velocity Z", 0, 100, 85)
    st.metric(m_res, f"{(m25m*0.6 + m25z*0.4):.2f}")

elif mid == "m26":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{fx} = \sqrt{G \cdot S \cdot W}")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> هندسة سعر الصرف السيادي المعتمد على الأصول الحقيقية.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Sovereign exchange rate engineering based on real assets.</div>', unsafe_allow_html=True)
    m26g = st.slider("Gold G", 0, 100, 95); m26s = st.slider("Commodities S", 0, 100, 85)
    st.metric(m_res, f"{(m26g*m26s)**0.5:.2f}")

elif mid == "m27":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_1 \pi + \alpha_2 T + \alpha_3 Z")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> العائد المقاصدي البديل للفائدة الربوية.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Maqasid Return as an alternative to Usury.</div>', unsafe_allow_html=True)
    m27p = st.slider("Profit pi", 0, 100, 80); m27t = st.slider("Empowerment T", 0, 100, 85)
    st.metric(m_res, f"{(0.5*m27p + 0.5*m27t):.2f}")

elif mid == "m28":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_{fin} = \frac{R + T}{Risk}")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> هندسة المالية المقاصدية وإدارة مخاطر المشاركة.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Maqasid Finance engineering and risk-sharing management.</div>', unsafe_allow_html=True)
    m28r = st.slider("Return R", 0, 100, 75); m28k = st.slider("Risk Coeff", 1, 100, 50)
    st.metric(m_res, f"{(m28r/m28k)*10:.2f}")

elif mid == "m29":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_b = 0.6 R + 0.4 Z")
    if lang == "العربية":
        st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> تسعير المنتجات المصرفية الأخلاقية بناءً على العائد والزكاة.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="explanation-box"><b>💡 Concept:</b> Ethical banking product pricing based on return and Zakat.</div>', unsafe_allow_html=True)
    m29r = st.slider("Yield", 0, 100, 75); m29z = st.slider("Ethics", 0, 100, 30)
    st.metric(m_res, f"{(0.6*m29r + 0.4*m29z + 10):.2f}")

st.sidebar.markdown("---")
# تصحيح اسم صاحب الابتكار في السطر الأخير بدقة
st.sidebar.write(f"© 2026 Developed by: {Prof.Dr. Saleh Orabi}")
