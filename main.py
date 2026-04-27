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
    "P4. المضاربة الاجتماعية التمكينية": "p4", "P5. صندوق الوقف التمكيني المشترك": "p5", "P6. الإِجَارَةُ الوَقْفِيَّةُ المَوْصُوفَةُ فِي الذِّمَّةِ": "p6",
    "1. نموذج الأثر الرمزي في الأداء الوظيفي (Pr)": "m1", "2. نموذج القيادة المتزكية (Er)": "m2", "3. نموذج الحوكمة الرمزية (Gr)": "m3",
    "4. نموذج الاستثمار التزكوي (Rr)": "m4", "5. نموذج التقييم التزكوي للمؤسسات (Qr)": "m5", "6. نموذج التحقق الوجودي (Vr)": "m6",
    "7. القيمة التزكوية المضافة (ZVA)": "m7", "8. سنة الشكر (Y)": "m8", "9. سنة الظلم (R)": "m9",
    "10. سنة التداول (GINI)": "m10", "11. سنة التمكين (R_e)": "m11", "12. سياسة مكافحة الفقر (ΔY)": "m12",
    "13. سياسة التسعير (FBi)": "m13", "14. سياسة التمكين (ES)": "m14", "15. سياسة الأزمات (CR)": "m15",
    "16. العدالة في السوق (Yt)": "m16", "17. الشفافية السوقية (Yt)": "m17", "18. منع الاحتكار (Yt)": "m18",
    "19. النية الصالحة في السوق (Yt)": "m19", "20. سعر الكفاية (Pk)": "m20", "21. العرض الرحيم (Qs)": "m21",
    "22. الطلب العادل (Qd)": "m22", "23. تدخل الدولة المقاصدي (Is)": "m23", "24. التمكين المالي العام (Y)": "m24",
    "25. النموذج النقدي المركب (Y)": "m25", "26. هندسة سعر الصرف (Y_fx)": "m26", "27. هَنْدَسَةُ سِعْرِ الفَائِدَةِ بَيْنَ الرِّبَا وَالبَدَائِلِ الرَّمْزِيَّةِ": "m27",
    "28. هندسة المالية المقاصدية (P)": "m28", "29. تسعير المنتجات المصرفية (P_b)": "m29"
}

st.sidebar.header(sidebar_head)
choice = st.sidebar.selectbox(select_msg, list(menu.keys()))
mid = menu[choice]

# --- 4. محرك التشغيل التفصيلي ---

if mid == "p1":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)    
    # 1. المعادلة الرياضية القياسية للإدخار الوقفي الذكي
    st.latex(r"Z_{it} = \gamma + \delta_1 W_{it} + \delta_2 R_{it} + \delta_3 T_{it} + \mu_{it}")    
    # 2. شرح الفكرة العامة والفرضية
    desc = "مُنْتَجُ الإِدِّخَارِ الوَقْفِيِّ الذَّكِيِّ: يتيح للعميل تخصيص نسبة من مدخراته كوقف يُستثمر في مشاريع تنموية (تعليم، صحة، تدريب) لتعزيز الاستدامة والتفاعل الروحي." if lang == "العربية" else "Smart Endowment Savings Product: Integrates waqf into savings to achieve developmental sustainability and enhance spiritual and economic interaction."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)    
    # 3. خانات إدخال الرموز (المتغيرات) بناءً على عناصر النموذج
    st.write("### إدخال قيم متغيرات النموذج الوقفي:")    
    col1, col2, col3 = st.columns(3)    
    with col1:
        v1 = st.number_input("نسبة الوقف من الادخار (Wit)", min_value=0.0, max_value=100.0, value=80.0, key="wit_p1")
    with col2:
        v2 = st.number_input("عائد الاستثمار الوقفي (Rit)", min_value=0.0, max_value=100.0, value=70.0, key="rit_p1")
    with col3:
        v3 = st.number_input("مؤشر التفاعل الروحي (Tit)", min_value=0.0, max_value=100.0, value=90.0, key="tit_p1")    
    # 4. حساب الناتج النهائي (Zit: مؤشر الأثر الوقفي)
    # الأوزان الافتراضية للمعاملات لضمان عمل المعادلة حسابياً
    z_impact = (0.4 * v1 + 0.3 * v2 + 0.3 * v3)    
    # 5. ظهور الناتج النهائي
    st.metric("مؤشر الأثر الوقفي النهائي (Zit)", f"{z_impact:.2f}")
    # إضافة ملاحظة حول النتائج المتوقعة
    if lang == "العربية":
        st.info("النتائج المتوقعة: زيادة المشاريع الوقفية، تعزيز التكافل، ورفع مستوى التفاعل الروحي والاقتصادي.")

elif mid == "p2":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)    
    # 1. عرض المعادلة الرياضية القياسية للمشاركة التمكينية المتدرجة
    st.latex(r"Y_{it} = \alpha + \beta_1 P_{it} + \beta_2 E_{it} + \beta_3 S_{it} + \epsilon_{it}")    
    # 2. شرح الفكرة العامة والفرضية الأساسية
    desc = "مُنْتَجُ ٱلْمُشَارَكَةِ ٱلتَّمْكِينِيَّةِ ٱلْمُتَدَرِّجَةِ: تمويل الفئات المحرومة بمشاركة متدرجة تتناقص فيها نسبة المصرف بنسبة 20% سنوياً لتمكين العميل من التملك الكامل وتحقيق العدالة التوزيعية." if lang == "العربية" else "Progressive Empowerment Participation: Financing for vulnerable groups through a decreasing bank-share (20% annually) to achieve full ownership and distributive justice."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)    
    # 3. خانات إدخال الرموز (المتغيرات) بناءً على عناصر النموذج
    st.write("### إدخال قيم متغيرات مؤشر التمكين:")    
    col1, col2, col3 = st.columns(3)    
    with col1:
        v1 = st.number_input("نسبة المشاركة التمكينية (Pit)", min_value=0.0, max_value=100.0, value=80.0, key="pit_p2")
    with col2:
        v2 = st.number_input("مؤشر الأداء الإنتاجي (Eit)", min_value=0.0, max_value=100.0, value=70.0, key="eit_p2")
    with col3:
        v3 = st.number_input("مؤشر الاستدامة الشرعية (Sit)", min_value=0.0, max_value=100.0, value=90.0, key="sit_p2")    
    # 4. حساب الناتج النهائي (Yit: مؤشر التمكين الاقتصادي)
    # استخدام الأوزان القياسية المتوافقة مع النموذج
    y_empowerment = (0.4 * v1 + 0.3 * v2 + 0.3 * v3)    
    # 5. ظهور الناتج النهائي
    st.metric("مؤشر التمكين الاقتصادي النهائي (Yit)", f"{y_empowerment:.2f}")
    # إضافة ملاحظة حول النتائج المتوقعة وآلية التناقص
    if lang == "العربية":
        st.info("الآلية: يبدأ المصرف بنسبة 80% وتتناقص سنوياً بنسبة 20% حتى التملك الكامل للعميل، مما يعزز الشمول المالي الشرعي.")

elif mid == "p3":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)    
    # 1. عرض المعادلة الرياضية القياسية للصكوك الوقفية الذكية
    st.latex(r"W_{it} = \theta + \lambda_1 C_{it} + \lambda_2 R_{it} + \lambda_3 I_{it} + \nu_{it}")    
    # 2. شرح الفكرة العامة والفرضية (نصك الأصلي)
    desc = "الصُّكُوكُ الوَقْفِيَّةُ التَّنْمَوِيَّةُ الذَّكِيَّةُ: إصدار صكوك لتمويل مشاريع تنموية مستدامة، تجمع بين ربح المستثمر وتخصيص عائد للوقف لضمان التكافل والتمكين." if lang == "العربية" else "Smart Developmental Waqf Sukuk: Issuing sukuk to fund sustainable projects, combining investor profit with waqf-allocated returns for community empowerment."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)    
    # 3. خانات إدخال الرموز (المتغيرات) بناءً على عناصر النموذج
    st.write("### إدخال قيم متغيرات مؤشر الأثر الوقفي:")    
    col1, col2, col3 = st.columns(3)    
    with col1:
        v1 = st.number_input("قيمة الصك الوقفي المُصدر (Cit)", min_value=0.0, value=500.0, key="cit_p3")
    with col2:
        v2 = st.number_input("نسبة العائد المخصص للوقف (Rit)", min_value=0.0, max_value=100.0, value=20.0, key="rit_p3")
    with col3:
        v3 = st.number_input("مؤشر الأثر التنموي (Iit)", min_value=0.0, max_value=100.0, value=80.0, key="iit_p3")   
    # 4. حساب الناتج النهائي (Wit: مؤشر الأثر الوقفي للمشروع)
    # تم استخدام الأوزان القياسية لتفعيل المعادلة حسابياً
    w_impact = (0.01 * v1 + 0.4 * v2 + 0.5 * v3)    
    # 5. ظهور الناتج النهائي
    st.metric("مؤشر الأثر الوقفي للمشروع (Wit)", f"{w_impact:.2f}")
    # إضافة ملاحظة حول آلية الذكاء المالي والنتائج
    if lang == "العربية":
        st.info("النتائج المتوقعة: تمويل مستدام للمشاريع التنموية، تعزيز ثقافة الاستثمار الوقفي، ورفع مستوى الشفافية والامتثال الشرعي.")

elif mid == "p4":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)    
    # 1. عرض المعادلة الرياضية القياسية للمشاركة التمكينية
    st.latex(r"Y_{it} = \alpha + \beta_1 P_{it} + \beta_2 E_{it} + \beta_3 S_{it} + \epsilon_{it}")    
    # 2. شرح الفكرة العامة والفرضية (نفس النص الذي أرسلته)
    desc = "مُنْتَجُ ٱلْمُشَارَكَةِ ٱلتَّمْكِينِيَّةِ ٱلْمُتَدَرِّجَةِ: تمويل مشروع لفئة محرومة عبر مشاركة متدرجة تتناقص فيها حصة المصرف سنوياً بنسبة 20% لتمكين العميل من التملك الكامل." if lang == "العربية" else "Progressive Empowerment Participation: Financing projects for vulnerable groups through a decreasing bank-share model (20% annual reduction) to achieve full ownership."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)    
    # 3. خانات إدخال الرموز (المتغيرات)
    st.write("### إدخال قيم متغيرات نموذج التمكين:")    
    col1, col2, col3 = st.columns(3)    
    with col1:
        v1 = st.number_input("نسبة المشاركة التمكينية (Pit)", min_value=0.0, max_value=100.0, value=80.0, key="pit_p4")
    with col2:
        v2 = st.number_input("مؤشر الأداء الإنتاجي (Eit)", min_value=0.0, max_value=100.0, value=75.0, key="eit_p4")
    with col3:
        v3 = st.number_input("مؤشر الاستدامة الشرعية (Sit)", min_value=0.0, max_value=100.0, value=90.0, key="sit_p4")    
    # 4. حساب الناتج النهائي (Yit: مؤشر التمكين الاقتصادي)
    # ملاحظة: تم استخدام أوزان لتعكس تأثير المشاركة والأداء والاستدامة
    y_empowerment = (0.4 * v1 + 0.3 * v2 + 0.3 * v3)    
    # 5. ظهور الناتج النهائي
    st.metric("مؤشر التمكين الاقتصادي للعميل (Yit)", f"{y_empowerment:.2f}")
    # إضافة ملاحظة حول آلية التناقص
    st.info("⚠️ ملاحظة: وفقاً لآلية النموذج، تتناقص نسبة المصرف سنوياً بمعدل 20% لصالح ملكية العميل.")
    
elif mid == "p5":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)    
    # 1. عرض المعادلة الرياضية القياسية لصندوق الوقف التمكيني
    st.latex(r"Q_{it} = \psi + \eta_1 V_{it} + \eta_2 D_{it} + \eta_3 B_{it} + \xi_{it}")    
    # 2. شرح الفكرة العامة والفرضية (نصك الأصلي)
    desc = "صُنْدُوقُ الوَقْفِ التَّمْكِينِيِّ المُشْتَرَكِ: يجمع بين أموال الوقف كضمان وأموال المستثمرين لتمويل مشاريع إنتاجية للفئات المحرومة وفق حوكمة شرعية مستقلة." if lang == "العربية" else "Joint Empowerment Waqf Fund: Combines waqf assets as guarantees with investor funds to finance productive projects for vulnerable groups under Sharia governance."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)    
    # 3. خانات إدخال الرموز (المتغيرات) بناءً على عناصر النموذج
    st.write("### إدخال قيم متغيرات مؤشر الأثر التمكيني:")    
    col1, col2, col3 = st.columns(3)    
    with col1:
        v1 = st.number_input("قيمة التمويل المقدم (Vit)", min_value=0.0, value=600.0, key="vit_p5")
    with col2:
        v2 = st.number_input("نسبة الضمان الوقفي (Dit)", min_value=0.0, max_value=100.0, value=100.0, key="dit_p5")
    with col3:
        v3 = st.number_input("نسبة الأرباح المخصصة للتمكين (Bit)", min_value=0.0, max_value=100.0, value=15.0, key="bit_p5")    
    # 4. حساب الناتج النهائي (Qit: مؤشر الأثر التمكيني)
    # تم استخدام أوزان لتعكس تأثير التمويل والضمان والتدوير الربحي للوقف
    q_empowerment = (0.02 * v1 + 0.5 * v2 + 0.3 * v3)    
    # 5. ظهور الناتج النهائي
    st.metric("مؤشر الأثر التمكيني للمشروع (Qit)", f"{q_empowerment:.2f}")
    # إضافة ملاحظة حول التفسير والنتائج المتوقعة
    if lang == "العربية":
        st.info("النتائج المتوقعة: تمويل المشاريع الصغيرة دون ضمانات تقليدية، تعزيز ثقافة الوقف الإنتاجي، وتحسين مؤشرات العدالة التوزيعية.")

elif mid == "p6":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)    
    # 1. عرض المعادلة الرياضية القياسية للإجارة الوقفية الموصوفة
    st.latex(r"H_{it} = \omega + \sigma_1 E_{it} + \sigma_2 Q_{it} + \sigma_3 K_{it} + \varsigma_{it}")    
    # 2. شرح الفكرة العامة والفرضية (نصك الأصلي)
    desc = "الإِجَارَةُ الوَقْفِيَّةُ المَوْصُوفَةُ فِي الذِّمَّةِ: تمويل سكن أو تعليم أو علاج للفقراء عبر أصل وقفي، حيث تُدفع الأجرة من جهة مانحة لضمان الاستدامة والحفاظ على كرامة المستفيد." if lang == "العربية" else "Forward Waqf Ijarah: Financing housing, education, or healthcare through waqf assets, where rent is covered by a donor to ensure sustainability and preserve beneficiary dignity."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)    
    # 3. خانات إدخال الرموز (المتغيرات) بناءً على عناصر النموذج
    st.write("### إدخال قيم متغيرات مؤشر التمكين الوقفي:")    
    col1, col2, col3 = st.columns(3)    
    with col1:
        v1 = st.number_input("قيمة الأجرة المدفوعة (Eit)", min_value=0.0, value=80.0, key="eit_p6")
    with col2:
        v2 = st.number_input("جودة المنفعة المقدمة (Qit)", min_value=0.0, max_value=100.0, value=85.0, key="qit_p6")
    with col3:
        v3 = st.number_input("مؤشر الكرامة (Kit)", min_value=0.0, max_value=100.0, value=100.0, key="kit_p6")    
    # 4. حساب الناتج النهائي (Hit: مؤشر التمكين الوقفي)
    # تم توزيع الأوزان لتعكس أهمية الجودة والكرامة في تحقيق الأثر
    h_empowerment = (0.3 * v1 + 0.3 * v2 + 0.4 * v3)    
    # 5. ظهور الناتج النهائي
    st.metric("مؤشر التمكين الوقفي النهائي (Hit)", f"{h_empowerment:.2f}")
    # إضافة ملاحظة حول النتائج المتوقعة
    if lang == "العربية":
        st.info("النتائج المتوقعة: توفير الخدمات الأساسية للفئات المحرومة دون ديون، تعزيز ثقافة الوقف، وتحسين مؤشرات الكرامة والخصوصية.")

elif mid == "m1":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)   
    # 1. المعادلة الرمزية الأساسية
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")    
    desc = "نموذج الأثر الرمزي: يربط بين الرسالة الرمزية والأداء الوظيفي، محولاً الوظيفة من كدح مادي إلى رسالة وجودية." if lang == "العربية" else "Symbolic Impact Model: Linking symbolic mission to performance, transforming a job into an existential message."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    # 2. الاستبانة الرمزية المبتكرة (محاور القياس)
    st.markdown("### 📋 استبانة الأثر الرمزي في الأداء الوظيفي")
    st.info("قم بتقييم البنود التالية من (1 إلى 5) بناءً على درجة التجسيد الرمزي في عملك")
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "1. الرسالة (Rr)", 
        "2. المعنى (Mr)", 
        "3. التزكية (Tr)", 
        "4. التواصل (Cr)",
        "5. النية والأثر (α & ε)"
    ])
    with tab1:
        st.subheader("وضوح الرسالة الرمزية (Rr)")
        r1 = st.number_input("لدي رسالة شخصية واضحة أستحضرها يومياً", 1, 5, 4, key="r1")
        r2 = st.number_input("عملي اليومي يعبّر عن رسالتي في الحياة", 1, 5, 4, key="r2")
        r3 = st.number_input("أساهم في تحقيق رسالة المؤسسة من منطلق قيمي", 1, 5, 4, key="r3")
        Rr = (r1 + r2 + r3) / 3
    with tab2:
        st.subheader("المعنى والانتماء (Mr)")
        m1 = st.number_input("عملي يحمل معنى يتجاوز الإنجاز المادي", 1, 5, 5, key="m1_val")
        m2 = st.number_input("أنتمي لفريق العمل من منطلق قيمي مشترك", 1, 5, 4, key="m2_val")
        m3 = st.number_input("أتحمس للمهام التي تعكس قيمًا أؤمن بها", 1, 5, 5, key="m3_val")
        Mr = (m1 + m2 + m3) / 3
    with tab3:
        st.subheader("التزكية الزمنية (Tr)")
        t1 = st.number_input("أخصص وقتًا للتأمل أو التزكية الذاتية مهنياً", 1, 5, 3, key="t1")
        t2 = st.number_input("أدمج التعلم الروحي في تطويري المهني", 1, 5, 3, key="t2")
        t3 = st.number_input("أوازن بين الإنجاز والتأمل في سياق العمل", 1, 5, 4, key="t3")
        Tr = (t1 + t2 + t3) / 3
    with tab4:
        st.subheader("التواصل الرمزي (Cr)")
        c1 = st.number_input("أستخدم لغة رمزية تعكس القيم مع الزملاء", 1, 5, 3, key="c1")
        c2 = st.number_input("أشارك في قيم مؤسسية تعزز الانتماء والمعنى", 1, 5, 4, key="c2")
        c3 = st.number_input("أساهم في خلق بيئة عمل تحمل إشارات رمزية", 1, 5, 4, key="c3")
        Cr = (c1 + c2 + c3) / 3
    with tab5:
        st.subheader("النية الداخلية والأثر غير المرئي")
        alpha = st.number_input("النية الداخلية (α): استحضار نية صافية", 1, 5, 5, key="alpha")
        epsilon = st.number_input("الأثر غير المرئي (ε): الشعور بالبركة والتوفيق", 1, 5, 5, key="epsilon")
    # 3. حساب الأداء الوظيفي الرمزي Pr
    # تم استخدام معاملات الانحدار (Betas) بناءً على الأهمية النسبية في النموذج الرمزي
    Pr = alpha + (0.3 * Rr) + (0.25 * Mr) + (0.2 * Tr) + (0.15 * Cr) + (0.1 * epsilon)
    st.markdown("---")
    st.subheader("📊 تحليل الأداء الوظيفي الرمزي النهائي")    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.metric("مؤشر الأداء الرمزي (Pr)", f"{Pr:.2f}")
    with col_res2:
        # تقييم وصفي بناءً على النتيجة
        status = "رسالي بامتياز" if Pr > 4 else "قيد التحول الرمزي" if Pr > 3 else "كدح مادي"
        st.write(f"**الحالة الرمزية:** {status}")
    st.success("تم تحليل الأداء بناءً على استنطاق المعاني العميقة خلف السلوك الوظيفي.")

elif mid == "m2":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)    
    # 1. المعادلة الرمزية الأساسية للقيادة المتزكية
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \beta_4 C_r + \beta_5 V_r + \beta_6 R_r + \epsilon_r")   
    desc = "القيادة المتزكية: نموذج رمزي عالمي يقيس أثر تزكية القائد وإلهامه في جودة الأداء المؤسسي وتحقيق الاستخلاف." if lang == "العربية" else "Tazkiyah-Based Leadership: A symbolic model measuring the impact of a leader's purification and inspiration on institutional performance."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    # 2. استبانة الأثر الرمزي في القيادة المتزكية
    st.markdown("### 🏛️ استبانة قياس الأثر القيادي المتزكي")
    st.info("يرجى تقييم المحاور التالية (من 1 إلى 5) بناءً على الممارسة القيادية الفعلية")
    # استخدام التبويبات لتنظيم المحاور الثمانية
    tabs = st.tabs([
        "تزكية الذات (Zr)", "المعنى (Mr)", "الإلهام (Ir)", "التواصل (Cr)", 
        "التوافق (Vr)", "الرسالة (Rr)", "النية (α)", "الأثر (ε)"
    ])
    with tabs[0]:
        st.subheader("تزكية القائد (Zr)")
        z1 = st.number_input("أمارس التأمل أو مراجعة النية بانتظام", 1, 5, 4, key="z1_m2")
        z2 = st.number_input("أمتلك خطة شخصية للنمو الروحي والسلوكي", 1, 5, 3, key="z2_m2")
        z3 = st.number_input("أحرص على ضبط الأنا في المواقف القيادية", 1, 5, 4, key="z3_m2")
        Zr = (z1 + z2 + z3) / 3
    with tabs[1]:
        st.subheader("المعنى والانتماء (Mr)")
        m1 = st.number_input("أشعر أن عملي يحمل رسالة تتجاوز المادة", 1, 5, 5, key="m1_m2")
        m2 = st.number_input("أساهم في بناء روابط معنوية داخل الفريق", 1, 5, 4, key="m2_m2")
        m3 = st.number_input("أحتفي بالمعاني لا فقط بالنتائج", 1, 5, 4, key="m3_m2")
        Mr = (m1 + m2 + m3) / 3
    with tabs[2]:
        st.subheader("الإلهام الرمزي (Ir)")
        i1 = st.number_input("أستخدم القصص الرمزية في التحفيز والتوجيه", 1, 5, 4, key="i1_m2")
        i2 = st.number_input("أبتكر قيم روحية تعزز الحافز الداخلي", 1, 5, 4, key="i2_m2")
        Ir = (i1 + i2) / 2
    with tabs[3]:
        st.subheader("التواصل الرمزي (Cr)")
        c1 = st.number_input("أستخدم لغة رمزية تعكس القيم في الاجتماعات", 1, 5, 3, key="c1_m2")
        c2 = st.number_input("أوظّف إشارات بصرية وسلوكية تُجسّد الرسالة", 1, 5, 4, key="c2_m2")
        Cr = (c1 + c2) / 2
    with tabs[4]:
        st.subheader("توافق القيم (Vr)")
        v1 = st.number_input("أجد توافقًا بين قيمي الشخصية ورسالة المؤسسة", 1, 5, 5, key="v1_m2")
        v2 = st.number_input("أساهم في تطوير ثقافة مؤسسية رمزية", 1, 5, 4, key="v2_m2")
        Vr = (v1 + v2) / 2
    with tabs[5]:
        st.subheader("تجسيد الرسالة (Rr)")
        r1 = st.number_input("أحوّل رسالة المؤسسة إلى خطوات عملية رمزية", 1, 5, 4, key="r1_m2")
        r2 = st.number_input("أستخدم الرسالة كمرجعية في التوجيه والتقييم", 1, 5, 5, key="r2_m2")
        Rr = (r1 + r2) / 2
    with tabs[6]:
        st.subheader("النية التأسيسية (α)")
        alpha = st.number_input("أراجع نيتي قبل اتخاذ القرارات الكبرى", 1, 5, 5, key="alpha_m2")
    with tabs[7]:
        st.subheader("الأثر غير المرئي (ε)")
        epsilon = st.number_input("أستشعر البركة في القرارات التي تنبع من الرسالة", 1, 5, 5, key="eps_m2")
    # 3. حساب الأثر المؤسسي المتزكي Er
    # تم توزيع الأوزان بناءً على أهمية تزكية القائد والإلهام وتجسيد الرسالة
    Er = alpha + (0.2 * Zr) + (0.15 * Mr) + (0.15 * Ir) + (0.1 * Cr) + (0.15 * Vr) + (0.15 * Rr) + (0.1 * epsilon)
    st.markdown("---")
    st.subheader("📊 تحليل الأثر القيادي المتزكي النهائي")    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.metric("مؤشر الأثر المؤسسي (Er)", f"{Er:.2f}")
    with col_res2:
        # تقييم المستوى القيادي
        status = "قائد متزكٍ (ملهم)" if Er > 4.2 else "قائد في مرحلة التزكية" if Er > 3.5 else "قائد إجرائي (مادي)"
        st.write(f"**التصنيف القيادي الرمزي:** {status}")
    st.success("تم تحليل الأداء القيادي بناءً على نموذج السيادة التزكوية والمقاصدية.")

elif mid == "m3":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)    
    # 1. المعادلة الرمزية الأساسية للحوكمة الرمزية
    st.latex(r"G_r = \alpha + \beta_1 N_r + \beta_2 T_r + \beta_3 M_r + \beta_4 A_r + \epsilon_r")    
    desc = "الحوكمة الرمزية: إطار مفاهيمي يربط بين المعنى الداخلي والنظام المؤسسي، لتحويل الحوكمة من مجرد إجراءات إلى ممارسة تزكوية." if lang == "العربية" else "Symbolic Governance: A framework bridging inner meaning and institutional order, transforming governance into a Tazkiyah practice."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    # 2. استبانة الأثر الرمزي في الحوكمة الرمزية
    st.markdown("### 🏛️ استبانة قياس أثر الحوكمة الرمزية")
    st.info("يرجى تقييم المحاور التالية (من 1 إلى 5) بناءً على الواقع التنظيمي للمؤسسة")
    # استخدام التبويبات لتنظيم المحاور الستة
    tabs = st.tabs([
        "النمط القيادي (Nr)", "قيم الحوكمة (Tr)", "المعنى المؤسسي (Mr)", 
        "الانسجام الرمزي (Ar)", "النية (α)", "الأثر (ε)"
    ])
    with tabs[0]:
        st.subheader("النمط القيادي الرمزي (Nr)")
        n1 = st.number_input("يُمارس القادة سلطتهم بأسلوب تشاركي يستحضر الرسالة", 1, 5, 4, key="n1_m3")
        n2 = st.number_input("يُستخدم الخطاب الرمزي في التوجيه والتحفيز", 1, 5, 4, key="n2_m3")
        n3 = st.number_input("يُنظر إلى القائد كرمز للقيم وليس مجرد مدير", 1, 5, 5, key="n3_m3")
        Nr = (n1 + n2 + n3) / 3
    with tabs[1]:
        st.subheader("قيم الحوكمة (Tr)")
        t1 = st.number_input("تُمارس الاجتماعات بطريقة رمزية (تأمل، مراجعة نيات)", 1, 5, 3, key="t1_m3")
        t2 = st.number_input("تُحتفى بالقيم عبر لحظات جماعية رمزية", 1, 5, 4, key="t2_m3")
        t3 = st.number_input("تُستخدم إشارات بصرية وسلوكية تعكس الرسالة", 1, 5, 4, key="t3_m3")
        Tr = (t1 + t2 + t3) / 3
    with tabs[2]:
        st.subheader("المعنى المؤسسي (Mr)")
        m1 = st.number_input("الهيكل التنظيمي يُجسّد رسالة المؤسسة", 1, 5, 4, key="m1_m3")
        m2 = st.number_input("السياسات واللوائح تحمل لغة رمزية تعكس القيم", 1, 5, 3, key="m2_m3")
        m3 = st.number_input("القرارات تُربط بالرسالة لا فقط بالأهداف الكمية", 1, 5, 4, key="m3_m3")
        Mr = (m1 + m2 + m3) / 3
    with tabs[3]:
        st.subheader("الانسجام الرمزي (Ar)")
        a1 = st.number_input("العاملون يشعرون بانسجام داخلي مع ثقافة المؤسسة", 1, 5, 4, key="a1_m3")
        a2 = st.number_input("تُحلّ التناقضات الرمزية بسرعة ووعي", 1, 5, 3, key="a2_m3")
        a3 = st.number_input("تُحترم القيم الشخصية في بيئة العمل", 1, 5, 5, key="a3_m3")
        Ar = (a1 + a2 + a3) / 3
    with tabs[4]:
        st.subheader("النية التأسيسية (α)")
        alpha = st.number_input("تُراجع النية دوريًا في القرارات الكبرى وتُوثّق", 1, 5, 5, key="alpha_m3")
    with tabs[5]:
        st.subheader("الأثر غير المرئي (ε)")
        epsilon = st.number_input("تظهر نتائج إيجابية غير مفسرة بالمنطق الإداري (بركة وتوفيق)", 1, 5, 5, key="eps_m3")
    # 3. حساب أثر الحوكمة الرمزية Gr
    # توزيع الأوزان لتعكس تأثير النمط القيادي، القيم، والمعنى والانسجام
    Gr = alpha + (0.25 * Nr) + (0.2 * Tr) + (0.2 * Mr) + (0.15 * Ar) + (0.1 * epsilon)
    st.markdown("---")
    st.subheader("📊 تحليل مؤشر الحوكمة الرمزية النهائي")    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.metric("مؤشر جودة التنظيم (Gr)", f"{Gr:.2f}")
    with col_res2:
        # تقييم مستوى الحوكمة
        status = "حوكمة رسالية (متناغمة)" if Gr > 4.2 else "حوكمة إجرائية (في طور التحول)" if Gr > 3.5 else "حوكمة جافة (مادية)"
        st.write(f"**الحالة التنظيمية الرمزية:** {status}")
    st.success("تم تقييم عمق الحوكمة في تجسيد الرسالة وتفعيل المعنى بناءً على نموذج السيادة التزكوية.")

elif mid == "m4":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)    
    # 1. المعادلة الرمزية الأساسية للاستثمار التزكوي
    st.latex(r"R_r = \alpha + \beta_1 N_r + \beta_2 Z_r + \beta_3 S_r + \beta_4 E_r + \epsilon_r")    
    desc = "الاستثمار التزكوي: دليل رمزي يُعيد تعريف الاستثمار بوصفه فعلاً يحمل نية وتزكية ورسالة، لا مجرد عائد مادي." if lang == "العربية" else "Tazkiyah-based Investment: A symbolic guide redefining investment as an act of intention, purification, and mission."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    # 2. استبانة الأثر الرمزي في الاستثمار التزكوي
    st.markdown("### 📊 استبانة قياس أثر الاستثمار التزكوي")
    st.info("يرجى تقييم المحاور التالية (من 1 إلى 5) بناءً على واقع المشروع الاستثماري")
    # استخدام التبويبات لتنظيم المحاور الستة
    tabs = st.tabs([
        "النية التأسيسية (α)", "نية المستثمر (Nr)", "تزكية المال (Zr)", 
        "رسالة الاستثمار (Sr)", "الأثر الرمزي (Er)", "الأثر غير المرئي (ε)"
    ])
    with tabs[0]:
        st.subheader("النية التأسيسية (α)")
        a1 = st.number_input("تم توثيق نية واضحة ومقاصد تزكوية عند التأسيس", 1, 5, 5, key="a1_p4")
        a2 = st.number_input("تُراجع النية دورياً في القرارات الكبرى والتقييم", 1, 5, 4, key="a2_p4")
        alpha = (a1 + a2) / 2
    with tabs[1]:
        st.subheader("نية المستثمر (Nr)")
        n1 = st.number_input("الاستثمار وسيلة لتحقيق رسالة شخصية عليا", 1, 5, 4, key="n1_p4")
        n2 = st.number_input("تُستحضر النية عند تقييم النجاح والتوسع", 1, 5, 4, key="n2_p4")
        Nr = (n1 + n2) / 2
    with tabs[2]:
        st.subheader("تزكية المال (Zr)")
        z1 = st.number_input("مصدر المال نزيه ويُخصّص جزء من الأرباح لأغراض تزكوية", 1, 5, 5, key="z1_p4")
        z2 = st.number_input("يُراجع أثر المال على النفس والمجتمع دورياً", 1, 5, 4, key="z2_p4")
        Zr = (z1 + z2) / 2
    with tabs[3]:
        st.subheader("رسالة الاستثمار (Sr)")
        s1 = st.number_input("للمشروع رسالة معلنة تتجاوز الربح وتُجسّد يومياً", 1, 5, 5, key="s1_p4")
        s2 = st.number_input("يُستخدم بيان الرسالة كمرجعية في التوجيه والتقييم", 1, 5, 4, key="s2_p4")
        Sr = (s1 + s2) / 2
    with tabs[4]:
        st.subheader("الأثر الرمزي (Er)")
        e1 = st.number_input("يُنتج المشروع أثرًا معنويًا يُغيّر حياة المستفيدين", 1, 5, 4, key="e1_p4")
        e2 = st.number_input("يُحتفى بالقيم والرموز التي تعزز المعنى لا فقط الأرباح", 1, 5, 4, key="e2_p4")
        Er_val = (e1 + e2) / 2
    with tabs[5]:
        st.subheader("الأثر غير المرئي (ε)")
        epsilon = st.number_input("تظهر نتائج إيجابية وبركة غير مفسرة ماليًا", 1, 5, 5, key="eps_p4")
    # 3. حساب العائد التزكوي الرمزي Rr
    # توزيع الأوزان لتعكس النية والرسالة وتزكية المال
    Rr = alpha + (0.25 * Nr) + (0.2 * Zr) + (0.2 * Sr) + (0.15 * Er_val) + (0.1 * epsilon)
    st.markdown("---")
    st.subheader("🏛️ تحليل مؤشر العائد التزكوي النهائي")    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.metric("مؤشر العائد التزكوي (Rr)", f"{Rr:.2f}")
    with col_res2:
        # تقييم درجة التزكية الاستثمارية
        status = "استثمار رسالي (مبارك)" if Rr > 4.2 else "استثمار قيمي (ناشئ)" if Rr > 3.5 else "استثمار تجاري (مادي)"
        st.write(f"**تصنيف الاستثمار الرمزي:** {status}")
    st.success("تم تحليل الاستثمار بناءً على معايير التزكية والرسالة وعمق الأثر المعنوي.")

elif mid == "m5":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)    
    # 1. المعادلة الرمزية الأساسية للتقييم التزكوي
    st.latex(r"Q_r = \alpha + \beta_1 N_r + \beta_2 Z_r + \beta_3 M_r + \beta_4 C_r + \beta_5 F_r + \epsilon_r")   
    desc = "التقييم التزكوي للمؤسسات: نموذج يُعيد تعريف جودة المؤسسة من منظور تزكوي ومعنوي، مستنداً إلى النية والمعنى والروح الجماعية." if lang == "العربية" else "Tazkiyah-Based Institutional Evaluation: A model redefining institutional quality through intention, meaning, and collective spirit."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    # 2. استبانة الأثر الرمزي في التقييم التزكوي
    st.markdown("### 🏛️ استبانة جودة المؤسسة التزكوية")
    st.info("يرجى تقييم المحاور التالية (من 1 إلى 5) بناءً على الواقع التشغيلي والقيمي للمؤسسة")
    # استخدام التبويبات لتنظيم المحاور السبعة
    tabs = st.tabs([
        "النية (α)", "نية القيادة (Nr)", "تزكية الهيكل (Zr)", 
        "المعنى (Mr)", "التواصل (Cr)", "الروح الجماعية (Fr)", "الأثر (ε)"
    ])
    with tabs[0]:
        st.subheader("النية التأسيسية (α)")
        a1 = st.number_input("تأسست المؤسسة على نية واضحة ومقاصد تزكوية", 1, 5, 5, key="a1_m5")
        a2 = st.number_input("تُراجع النية دورياً في القرارات الكبرى والتقييم", 1, 5, 4, key="a2_m5")
        alpha = (a1 + a2) / 2
    with tabs[1]:
        st.subheader("نية القيادة (Nr)")
        n1 = st.number_input("يوثق القادة نواياهم الشخصية ويستحضرونها قبل الفعل", 1, 5, 4, key="n1_m5")
        n2 = st.number_input("يشعر الفريق أن القيادة تحمل رسالة لا مجرد سلطة", 1, 5, 5, key="n2_m5")
        Nr = (n1 + n2) / 2
    with tabs[2]:
        st.subheader("تزكية الهيكل (Zr)")
        z1 = st.number_input("الهيكل الإداري خالٍ من التناقضات الرمزية والشبهات", 1, 5, 4, key="z1_m5")
        z2 = st.number_input("يُجسّد النظام القيم الأخلاقية لا مجرد الإجراءات", 1, 5, 4, key="z2_m5")
        Zr = (z1 + z2) / 2
    with tabs[3]:
        st.subheader("المعنى المؤسسي (Mr)")
        m1 = st.number_input("للمؤسسة رسالة واضحة تتجاوز الربح وتُجسّد في القرارات", 1, 5, 5, key="m1_m5")
        m2 = st.number_input("يشعر العاملون أن عملهم يحمل معنى وقيمة وجودية", 1, 5, 4, key="m2_m5")
        Mr = (m1 + m2) / 2
    with tabs[4]:
        st.subheader("التواصل الرمزي (Cr)")
        c1 = st.number_input("تُستخدم لغة ورموز تعكس القيم في الخطاب الداخلي", 1, 5, 3, key="c1_m5")
        c2 = st.number_input("توجد طقوس جماعية (تأمل، مراجعة) تعزز الانتماء", 1, 5, 4, key="c2_m5")
        Cr = (c1 + c2) / 2
    with tabs[5]:
        st.subheader("فاعلية الروح الجماعية (Fr)")
        f1 = st.number_input("يشعر الفريق بانسجام داخلي عميق حول الرسالة", 1, 5, 4, key="f1_m5")
        f2 = st.number_input("يُحتفى بالنجاح كفعل جماعي وبركة مشتركة", 1, 5, 5, key="f2_m5")
        Fr = (f1 + f2) / 2
    with tabs[6]:
        st.subheader("الأثر غير المرئي (ε)")
        epsilon = st.number_input("ظهور نتائج إيجابية وبركة غير مفسرة بالمنطق الإداري", 1, 5, 5, key="eps_m5")
    # 3. حساب جودة المؤسسة التزكوية Qr
    # توزيع الأوزان لتعكس النية والهيكل والروح الجماعية
    Qr = alpha + (0.2 * Nr) + (0.15 * Zr) + (0.2 * Mr) + (0.15 * Cr) + (0.2 * Fr) + (0.1 * epsilon)
    st.markdown("---")
    st.subheader("📊 تحليل مؤشر الجودة التزكوية النهائي")    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.metric("مؤشر جودة المؤسسة (Qr)", f"{Qr:.2f}")
    with col_res2:
        # تقييم المستوى المؤسسي
        status = "مؤسسة رسالية (مباركة)" if Qr > 4.2 else "مؤسسة قيمية (في طور التزكية)" if Qr > 3.5 else "مؤسسة إجرائية (مادية)"
        st.write(f"**تصنيف المؤسسة الرمزي:** {status}")
    st.success("تم التقييم بناءً على استنطاق المعاني العميقة والنية المؤسسية وفق نموذج السيادة التزكوية.")

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
    # --- معدل العائد الإسلامي المقاصدي ---
    with tab1:
        st.subheader("مُعَدَّلُ العَائِدِ الإِسْلَامِيُّ المَقَاصِدِيُّ")
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
    # --- الهندسة المالية الإسلامية المقاصدية ---
    with tab2:
        st.subheader("نَمُوذَجُ الهَنْدَسَةِ المَالِيَّةِ الإِسْلَامِيَّةِ المَقَاصِدِيَّةِ")
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
    # --- تسعير المنتجات المصرفية ---
    with tab3:
        st.subheader("تَسْعِيرُ المُنْتَجَاتِ المَصْرَفِيَّةِ بالعائد المقاصدي")
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
