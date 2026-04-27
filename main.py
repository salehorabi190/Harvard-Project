import streamlit as st
import numpy as np

# --- 1. الإعدادات والسيادة البصرية المبدعة (ابتكار أ.د. صالح عرابي 2026) ---
st.set_page_config(page_title="S.E.P 2026 | Prof. Dr. Saleh Orabi", layout="wide")

# تصميم CSS متقدم يدمج الزخرفة الإسلامية بالواجهة الرقمية الحديثة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&family=Amiri:wght@700&family=Playfair+Display:wght@700&display=swap');
    
    /* خلفية التطبيق مع لمسة زخرفية خفيفة */
    .stApp {
        background-color: #f8faf9;
        background-image: url("https://www.transparenttextures.com/patterns/islamic-art.png");
    }
    
    /* حاوية الشعار الرئيسية - نمط المحراب الرقمي */
    .logo-container {
        text-align: center;
        padding: 60px;
        background: linear-gradient(135deg, #1e4d2b 0%, #0d2b16 100%);
        border-radius: 0 0 50px 50px;
        border-bottom: 15px solid #d4af37;
        margin-bottom: 50px;
        color: white;
        box-shadow: 0 25px 50px rgba(0,0,0,0.3);
        position: relative;
    }
    
    .logo-text { font-family: 'Playfair Display', serif; font-size: 85px; letter-spacing: 8px; text-shadow: 3px 3px 10px rgba(0,0,0,0.5); }
    
    /* تصميم الأزرار التفاعلية للنماذج */
    .model-card {
        background: white;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        border: 2px solid #e0e0e0;
        transition: all 0.4s ease;
        cursor: pointer;
        height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    }
    
    .model-card:hover {
        transform: translateY(-10px);
        border-color: #d4af37;
        background: #f1f8f3;
        box-shadow: 0 15px 30px rgba(30, 77, 43, 0.2);
    }
    
    .model-icon { font-size: 40px; margin-bottom: 15px; }
    .model-name { font-family: 'Cairo', sans-serif; font-weight: bold; color: #1e4d2b; font-size: 16px; }

    /* صندوق الشرح المقاصدي */
    .explanation-box {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 25px;
        border-right: 15px solid #d4af37;
        border-left: 2px solid #e0e0e0;
        color: #1b5e20;
        line-height: 2.4;
        margin-bottom: 40px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.08);
        font-family: 'Cairo', sans-serif;
        font-size: 20px;
        text-align: justify;
    }

    .header-style { 
        color: #1e4d2b; font-family: 'Amiri', serif; font-size: 45px;
        border-bottom: 5px solid #d4af37; display: inline-block; margin-bottom: 30px;
    }
    
    /* إخفاء القائمة الجانبية الأصلية للتركيز على واجهة الأزرار */
    [data-testid="stSidebar"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. نظام اللغات والبيانات الأساسية ---
# تم وضع اللغة في أعلى الصفحة كجزء من الواجهة بدلاً من الجانب
lang = st.radio("🌐 Language / اللغة", ["العربية", "English"], horizontal=True)

AUTHOR_NAME = "Prof. Dr. Saleh Orabi" if lang == "English" else "أ.د. صالح عرابي"

if lang == "العربية":
    m_res, m_auth, m_title = "النتيجة النهائية", f"إعداد وتطوير: {AUTHOR_NAME} - 2026", "بـروتوكـول هـنـدسـة الاسـتـخـلاف الاقـتـصـادي"
    main_head = "🏛️ مـركـز قـيادة الـنـمـاذج الـهـنـدسيـة"
else:
    m_res, m_auth, m_title = "Final Result", f"Developed by: {AUTHOR_NAME} - 2026", "Economic Stewardship Engineering Protocol"
    main_head = "🏛️ Engineering Models Command Center"

# عرض الهوية البصرية السيادية
st.markdown(f"""
    <div class="logo-container">
        <div class="logo-text">S.E.P 2026</div>
        <div style="font-size: 38px; color: #d4af37; font-family: 'Amiri', serif; font-weight: bold; margin-top:15px;">{m_title}</div>
        <div style="font-size: 22px; opacity: 0.9; font-family: 'Cairo';">{m_auth}</div>
    </div>
    """, unsafe_allow_html=True)

# --- 3. الفهرس الموسوعي المبوب (Tabs) لتقسيم النماذج ---
st.markdown(f"<h2 style='text-align:center; color:#1e4d2b; font-family:Cairo;'>{main_head}</h2>", unsafe_allow_html=True)

# تقسيم النماذج إلى قطاعات هندسية كبرى
tab_main, tab_sharia, tab_market, tab_advanced = st.tabs([
    "📂 المنتجات الوقفية والتمكينية", 
    "📊 نماذج التزكية والمقاصد", 
    "📈 هندسة السياسات والسوق", 
    "🔐 الأنظمة السيادية والذكاء"
])

# وظيفة مساعدة لرسم الأزرار
def draw_model_button(col, label, key, icon):
    with col:
        if st.button(f"{icon}\n{label}", key=key, use_container_width=True):
            st.session_state.selected_model = key

# تعريف الحالة الافتراضية
if 'selected_model' not in st.session_state:
    st.session_state.selected_model = None

# --- توزيع الأزرار داخل التبويبات ---

with tab_main:
    c1, c2, c3 = st.columns(3)
    draw_model_button(c1, "P1. الإدخار الوقفي الذكي", "p1", "🌙")
    draw_model_button(c2, "P2. المشاركة التمكينية المتدرجة", "p2", "🪜")
    draw_model_button(c3, "P3. الصكوك الوقفية التنموية", "p3", "📜")
    c4, c5, c6 = st.columns(3)
    draw_model_button(c4, "P4. المضاربة الاجتماعية التمكينية", "p4", "🤝")
    draw_model_button(c5, "P5. صندوق الوقف التمكيني المشترك", "p5", "🏦")
    draw_model_button(c6, "P6. الإجارة الوقفية الموصوفة", "p6", "🏠")

with tab_sharia:
    c1, c2, c3 = st.columns(3)
    draw_model_button(c1, "1. الأثر الرمزي (Pr)", "m1", "✨")
    draw_model_button(c2, "2. القيادة المتزكية (Er)", "m2", "👑")
    draw_model_button(c3, "3. الحوكمة الرمزية (Gr)", "m3", "🛡️")
    c4, c5, c6 = st.columns(3)
    draw_model_button(c4, "4. الاستثمار التزكوي (Rr)", "m4", "💎")
    draw_model_button(c5, "5. التقييم التزكوي للمؤسسات (Qr)", "m5", "🏛️")
    draw_model_button(c6, "6. التحقق الوجودي (Vr)", "m6", "🧬")

with tab_market:
    c1, c2 = st.columns(2)
    draw_model_button(c1, "السُّنَنِ فِي السِّيَاسَاتِ الِاقْتِصَادِيَّةِ", "m8_m11", "📖")
    draw_model_button(c2, "تطبيق السياسات الاقتصادية السننية", "m12_m15", "⚖️")
    c3, c4 = st.columns(2)
    draw_model_button(c3, "هَنْدَسَةِ السُّوقِ: مِنَ التَّبَادُلِ إِلَى التَّزْكِيَةِ", "m16_m19", "📉")
    draw_model_button(c4, "هَنْدَسَةِ العَرْضِ والطَّلَبِ المَقاصِدِيَّةِ", "m20_m23", "⚖️")

with tab_advanced:
    c1, c2, c3 = st.columns(3)
    draw_model_button(c1, "30. خوارزمية التقييم الشرعي التنبؤية", "m30", "🤖")
    draw_model_button(c2, "31. مؤشر الأمان الشرعي (SSI)", "m31", "🔐")
    draw_model_button(c3, "32. بروتوكول الإشراف (SCS)", "m32", "📑")
    c4, c5, c6 = st.columns(3)
    draw_model_button(c4, "33. بروتوكول أمانة (مؤشر البركة Bi)", "m33", "🌿")
    draw_model_button(c5, "7. القيمة التزكوية المضافة (ZVA)", "m7", "➕")
    draw_model_button(c6, "27. هندسة سعر الفائدة والبدائل", "m27", "📊")

# --- 4. محرك التشغيل التفصيلي (بناءً على اختيار الزر) ---
if st.session_state.selected_model:
    mid = st.session_state.selected_model
    st.markdown("---")
    
    # مثال لتنفيذ m33 (بروتوكول أمانة) كمثال للتطبيق داخل الواجهة الجديدة
    if mid == "m33":
        st.markdown(f"<h1 class='header-style'>بروتوكول 'أمانة' السيادي: المحاكاة الرقمية الشاملة</h1>", unsafe_allow_html=True)
        st.latex(r"Bi = \frac{\sum (U_v \cdot S_t)}{H_w + D_i}")
        # ... باقي كود m33 كما تم برمجته سابقاً ...
        st.success("تم تفعيل بروتوكول أمانة بنجاح.")

    # (هنا يتم وضع بقية الـ elif لجميع النماذج p1-m33 التي برمجناها سابقاً)
    else:
        st.info(f"تم اختيار النموذج: {mid} - جاري تحميل البيئة الهندسية...")

# إضافة لمسة جمالية في ذيل الصفحة
st.markdown(f"""
    <div style="text-align: center; color: #1e4d2b; padding: 50px; font-family: Cairo;">
        <hr style="border-top: 3px solid #d4af37; width: 50%; margin: auto;">
        <br>
        جميع الحقوق محفوظة © {AUTHOR_NAME} 2026<br>
        <b>نحو اقتصاد استخلافي سيادي</b>
    </div>
    """, unsafe_allow_html=True)

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
    # 1. المعادلة الرمزية الأساسية للتحقق الوجودي
    st.latex(r"V_r = \alpha + \beta_1 M_r + \beta_2 P_r + \beta_3 N_r + \beta_4 Z_r + \epsilon_r")    
    desc = "التحقق الوجودي الرمزي: يقيس مدى شعور الفرد بأن وجوده داخل المؤسسة له معنى ورسالة وأثر يتجاوز المهام الوظيفية التقليدية." if lang == "العربية" else "Symbolic Existential Validation: Measures the individual's sense of meaning, mission, and impact within the organization."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    # 2. استبانة الأثر الرمزي في التحقق الوجودي
    st.markdown("### 🧬 استبانة التحقق الوجودي في بيئة العمل")
    st.info("يرجى تقييم المحاور التالية (من 1 إلى 5) بناءً على شعورك الشخصي وتجربتك داخل المؤسسة")
    # استخدام التبويبات لتنظيم المحاور الستة
    tabs = st.tabs([
        "النية المؤسسية (α)", "المعنى الشخصي (Mr)", "المشاركة الرمزية (Pr)", 
        "نية الفرد (Nr)", "التزكية الذاتية (Zr)", "الأثر غير المرئي (ε)"
    ])
    with tabs[0]:
        st.subheader("النية التأسيسية للمؤسسة (α)")
        a1 = st.number_input("تأسست المؤسسة على نية واضحة تتجاوز الربح المادي", 1, 5, 5, key="a1_m6")
        a2 = st.number_input("تُستخدم النية كمرجعية في التقييم والتطوير المؤسسي", 1, 5, 4, key="a2_m6")
        alpha = (a1 + a2) / 2
    with tabs[1]:
        st.subheader("المعنى الشخصي (Mr)")
        m1 = st.number_input("أشعر أن عملي يحمل قيمة ومعنى يتجاوز تنفيذ المهام", 1, 5, 5, key="m1_m6")
        m2 = st.number_input("أجد فرصة للتعبير عن قناعاتي وقيمي الشخصية في عملي", 1, 5, 4, key="m2_m6")
        Mr = (m1 + m2) / 2
    with tabs[2]:
        st.subheader("المشاركة الرمزية (Pr)")
        p1 = st.number_input("أشارك بفعالية في طقوس وقرارات جماعية ذات بعد رمزي", 1, 5, 4, key="p1_m6")
        p2 = st.number_input("أشعر أن صوتي مسموع في السياقات المعنوية والرمزية", 1, 5, 4, key="p2_m6")
        Pr = (p1 + p2) / 2
    with tabs[3]:
        st.subheader("نية الفرد (Nr)")
        n1 = st.number_input("لدي نية واضحة وموثقة لأهدافي من العمل هنا", 1, 5, 4, key="n1_m6")
        n2 = st.number_input("أراجع نواياي دورياً لضمان ترجمتها إلى أثر حقيقي", 1, 5, 5, key="n2_m6")
        Nr = (n1 + n2) / 2
    with tabs[4]:
        st.subheader("التزكية الذاتية (Zr)")
        z1 = st.number_input("بيئة العمل تساعدني على النمو الروحي والتطهير الذاتي", 1, 5, 3, key="z1_m6")
        z2 = st.number_input("أشعر أن العمل يزكّي نفسي ولا يرهق قيمها الأخلاقية", 1, 5, 4, key="z2_m6")
        Zr = (z1 + z2) / 2
    with tabs[5]:
        st.subheader("الأثر غير المرئي (ε)")
        epsilon = st.number_input("أستشعر بركة وتوفيقاً وانجاماً غير مفسر في نتائجي", 1, 5, 5, key="eps_m6")
    # 3. حساب التحقق الوجودي الرمزي Vr
    # تم توزيع الأوزان لتعكس قوة تأثير المعنى والنية والتزكية
    Vr = alpha + (0.25 * Mr) + (0.2 * Pr) + (0.2 * Nr) + (0.15 * Zr) + (0.1 * epsilon)
    st.markdown("---")
    st.subheader("📊 تحليل مؤشر التحقق الوجودي النهائي")    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.metric("مؤشر التحقق الوجودي (Vr)", f"{Vr:.2f}")
    with col_res2:
        # تقييم درجة التحقق الوجودي
        status = "تحقق وجودي كامل (رسالي)" if Vr > 4.2 else "تحقق وجودي جزئي (باحث)" if Vr > 3.5 else "وجود إجرائي (مادي)"
        st.write(f"**الحالة الوجودية في العمل:** {status}")
    st.success("تم التقييم بناءً على استنطاق المعاني العميقة للانتماء والنمو الروحي وفق نموذج السيادة التزكوية.")

elif mid == "m7":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.markdown("### نَمُوذَجُ القِيمَةِ التَّزْكِيَّةِ المُضَافَةِ (ZVA)")
    # 1. المعادلات الرياضية للنموذج
    st.latex(r"ZVA = EVA + \lambda Z")
    st.latex(r"Z = \theta N + \mu A + \nu R")    
    desc = "نموذج ZVA لتقييم التزكية الصناعية: يُعيد تعريف الأداء المؤسسي عبر دمج البعد التزكوي (النية، المعنى، الانسجام) مع المؤشرات التقليدية وقياس أثرها على الإنتاجية." if lang == "العربية" else "ZVA Model: Redefining industrial performance by integrating Tazkiyah (Intention, Meaning, Harmony) with traditional indicators."
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    # 2. إدخال المؤشرات التقليدية (EVA)
    st.subheader("أولاً: مؤشر القيمة الاقتصادية المضافة (التقليدي)")
    col_eva1, col_eva2 = st.columns(2)
    with col_eva1:
        eva_val = st.number_input("القيمة الاقتصادية المضافة (EVA)", value=500.0, key="eva_input")
    with col_eva2:
        lambda_val = st.number_input("معامل التحويل (λ) - قدرة المؤسسة على تحويل القيم لأثر", value=1.5, key="lambda_input")
    # 3. استبانة مؤشر التزكية المركب (Z)
    st.subheader("ثانياً: قياس مؤشر التزكية المركب (Z)")
    st.info("يرجى تقييم الأبعاد التزكوية التالية في المؤسسة (من 1 إلى 100)")    
    tab_n, tab_a, tab_r = st.tabs(["النية (N)", "الانسجام (A)", "الالتزام (R)"])    
    with tab_n:
        st.write("**مؤشر النية المؤسسية (N):** وضوح الرسالة، الهدف غير الربحي، النية في المشاريع.")
        n_val = st.number_input("درجة النية المؤسسية", 0.0, 100.0, 85.0, key="n_zva")
        theta = 0.4 # معامل ترجيح النية
    with tab_a:
        st.write("**الانسجام الداخلي (A):** رضا العاملين، الانتماء، غياب التناقضات الرمزية.")
        a_val = st.number_input("درجة الانسجام الداخلي", 0.0, 100.0, 80.0, key="a_zva")
        mu = 0.3 # معامل ترجيح الانسجام
    with tab_r:
        st.write("**الالتزام الروحي (R):** القرارات الأخلاقية، العدالة الداخلية، الأثر الرمزي.")
        r_val = st.number_input("درجة الالتزام الروحي", 0.0, 100.0, 90.0, key="r_zva")
        nu = 0.3 # معامل ترجيح الالتزام
    # 4. الحسابات البرمجية
    # حساب مؤشر التزكية المركب Z
    Z_composite = (theta * n_val) + (mu * a_val) + (nu * r_val)
    
    # حساب القيمة التزكوية المضافة ZVA
    zva_result = eva_val + (lambda_val * Z_composite)
    # 5. عرض النتائج والتحليل الصناعي
    st.markdown("---")
    st.subheader("📊 تحليل القيمة التزكوية المضافة النهائية")    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.metric("القيمة التزكوية المضافة (ZVA)", f"{zva_result:.2f}")
    with col_res2:
        st.metric("مؤشر التزكية المركب (Z)", f"{Z_composite:.2f}")
    # مصفوفة الأثر (ارتباط التزكية بالمؤشرات التقليدية)
    st.write("### 📉 أثر التزكية المتوقع على المؤشرات التقليدية:")
    st.table({
        "المؤشر الاقتصادي": ["العائد على الأصول (ROA)", "الإنتاجية الفردية", "معدل دوران الموظفين"],
        "العلاقة مع التزكية": ["ارتفاع (بفعل الانسجام)", "تحسن (بفعل المعنى)", "انخفاض (بفعل النية الصافية)"],
        "القيمة المتوقعة": [f"{zva_result*0.02:.2f}%", "مرتفعة", "منخفضة جداً"]
    })
    st.success("تم تحليل الأداء الصناعي وفق نموذج ZVA لدمج الربح المادي بالبركة المعنوية.")

elif mid == "m8_m11":
    st.markdown(f"<h1 class='header-style'>السُّنَنِ فِي السِّيَاسَاتِ الِاقْتِصَادِيَّةِ</h1>", unsafe_allow_html=True)    
    # تعريف التبويبات للسنن الأربعة
    tab1, tab2, tab3, tab4 = st.tabs([
        "1. سنة الشكر", 
        "2. سنة الظلم", 
        "3. سنة التداول", 
        "4. سنة التمكين"
    ])
    # --- سنة الشكر (نموذج التحفيز بالتنمية) ---
    with tab1:
        st.subheader("سُنَّةُ الشُّكْرِ: نموذج التحفيز التنموي بالامتنان")
        st.latex(r"Y = \beta_0 + \beta_1 S + \beta_2 C + \beta_3 T + \epsilon")
        st.info("الفرضية: زيادة الشكر المؤسسي (التقدير والعدالة) تؤدي لزيادة الإنتاجية والنمو.")        
        c1, c2 = st.columns(2)
        with c1:
            s_shukr = st.number_input("مؤشر الشكر المؤسسي (S)", value=85.0, key="s_shukr")
            c_shukr = st.number_input("رأس المال البشري (C)", value=80.0, key="c_shukr")
        with c2:
            t_shukr = st.number_input("مستوى التكنولوجيا (T)", value=70.0, key="t_shukr")       
        y_shukr = (0.5 * s_shukr + 0.3 * c_shukr + 0.2 * t_shukr)
        st.metric("معدل النمو / الإنتاجية (Y)", f"{y_shukr:.2f}")
    # --- سنة الظلم (نموذج الإنذار المبكر) ---
    with tab2:
        st.subheader("سُنَّةُ الظُّلمِ: نموذج الإنذار المبكر للانهيار")
        st.latex(r"R = \alpha_0 + \alpha_1 Z + \alpha_2 G + \alpha_3 I + \epsilon")
        st.warning("الفرضية: ارتفاع الظلم الاقتصادي (الاحتكار والفساد) يزيد من مخاطر الانهيار.")       
        c1, c2 = st.columns(2)
        with c1:
            z_zulm = st.number_input("مؤشر الظلم الاقتصادي (Z)", value=30.0, key="z_zulm")
            g_zulm = st.number_input("الإنفاق الحكومي (G)", value=60.0, key="g_zulm")
        with c2:
            i_zulm = st.number_input("الاستثمار العام (I)", value=50.0, key="i_zulm")         
        r_risk = (0.7 * z_zulm + 0.2 * g_zulm + 0.1 * i_zulm)
        st.metric("مؤشر المخاطر الاقتصادية (R)", f"{r_risk:.2f}")
    # --- سنة التداول (نموذج إعادة توزيع الثروة) ---
    with tab3:
        st.subheader("سُنَّةُ التَّدَاوُلِ: نموذج منع تركز الثروة")
        st.latex(r"GINI = \gamma_0 - \gamma_1 D + \gamma_2 E + \epsilon")
        st.latex(r"Y = \alpha_0 + \alpha_1 D + \alpha_2 E + \epsilon")
        st.info("الفرضية: زيادة أدوات التداول (زكاة، وقف) تقلل الفجوة الاقتصادية وتحفز النمو.")        
        c1, c2 = st.columns(2)
        with c1:
            d_tadawul = st.number_input("مؤشر تداول الثروة (D)", value=75.0, key="d_tadawul")
        with c2:
            e_employment = st.number_input("معدل التوظيف (E)", value=80.0, key="e_employment")            
        gini_res = (100 - 0.6 * d_tadawul + 0.2 * e_employment) / 100
        y_growth = (0.6 * d_tadawul + 0.4 * e_employment)        
        st.metric("معامل جيني المتوقع (GINI)", f"{gini_res:.3f}")
        st.metric("معدل النمو الاقتصادي (Y)", f"{y_growth:.2f}")
    # --- سنة التمكين (نموذج بناء القدرة) ---
    with tab4:
        st.subheader("سُنَّةُ التَّمْكِينِ: نموذج بناء القدرة الاقتصادية")
        st.latex(r"R = \theta_0 + \theta_1 M + \theta_2 S + \theta_3 P + \epsilon")
        st.info("الفرضية: التمكين عبر التعليم والملكية يؤدي إلى استقلال اقتصادي وازدهار مستدام.")      
        c1, c2 = st.columns(2)
        with c1:
            m_empower = st.number_input("مؤشر التمكين (M)", value=85.0, key="m_empower")
            s_indep = st.number_input("مؤشر الاستقلال المالي (S)", value=70.0, key="s_indep")
        with c2:
            p_participation = st.number_input("مؤشر المشاركة الاقتصادية (P)", value=75.0, key="p_participation")           
        r_empower_res = (0.4 * m_empower + 0.3 * s_indep + 0.3 * p_participation)
        st.metric("مؤشر الاستقلال والازدهار (R)", f"{r_empower_res:.2f}")
    st.markdown("---")
    st.success("تم دمج وتحليل السنن الاقتصادية الأربعة كإطار مرجعي للسياسات الاقتصادية المقاصدية.")

elif mid == "m12_m15":
    st.markdown(f"<h1 class='header-style'>تطبيق السياسات الاقتصادية السننية</h1>", unsafe_allow_html=True)    
    # تعريف التبويبات للسياسات الأربعة
    tab_poverty, tab_pricing, tab_empower, tab_crisis = st.tabs([
        "🍎 سياسة مكافحة الفقر", 
        "⚖️ سياسة التسعير", 
        "🚀 سياسة التمكين", 
        "🛡️ سياسة الأزمات"
    ])
    # --- 1. سياسة مكافحة الفقر (التمكين والرحمة) ---
    with tab_poverty:
        st.subheader("سِيَاسَةُ مُكَافَحَةِ الْفَقْرِ")
        st.latex(r"\Delta Y_{poor} = \alpha_1 Z_d + \alpha_2 MF_v + \alpha_3 BI")
        st.info("المقصد: التمكين والرحمة عبر الزكاة والتمويل الأصغر ومؤشر البركة.")        
        col1, col2 = st.columns(2)
        with col1:
            zd_val = st.number_input("الزكاة الموزعة (Zd)", value=85.0, key="poverty_zd")
            mfv_val = st.number_input("حجم التمويل الأصغر (MFv)", value=75.0, key="poverty_mfv")
        with col2:
            bi_val = st.number_input("مؤشر البركة (BI)", value=90.0, key="poverty_bi")            
        y_poor = (0.5 * zd_val + 0.3 * mfv_val + 0.2 * bi_val)
        st.metric("تغير دخل الفقراء (ΔY poor)", f"{y_poor:.2f}%")
    # --- 2. سياسة التسعير (العدالة) ---
    with tab_pricing:
        st.subheader("سِيَاسَةُ التَّسْعِيرِ")
        st.latex(r"FBi = \beta_1 PCc - \beta_2 MR + \beta_3 IS")
        st.info("المقصد: العدالة وضبط الاحتكار عبر الرقابة والنية المقاصدية.")        
        col1, col2 = st.columns(2)
        with col1:
            pcc_val = st.number_input("نطاق ضبط الأسعار (PCc)", value=80.0, key="price_pcc")
            mr_val = st.number_input("معدل الاحتكار (MR)", value=15.0, key="price_mr")
        with col2:
            is_val = st.number_input("مؤشر النية (IS)", value=85.0, key="price_is")            
        fbi_res = (0.5 * pcc_val - 0.3 * mr_val + 0.2 * is_val + 20)
        st.metric("مؤشر السعر العادل (FBi)", f"{fbi_res:.2f}")
    # --- 3. سياسة التمكين (الاستحقاق والتزكية) ---
    with tab_empower:
        st.subheader("سِيَاسَةُ التَّمْكِينِ")
        st.latex(r"ES = \gamma_1 LTp + \gamma_2 OAr + \gamma_3 SCi")
        st.info("المقصد: الاستحقاق والتزكية عبر التدريب القيادي ومراعاة السنن.")        
        col1, col2 = st.columns(2)
        with col1:
            ltp_val = st.number_input("التدريب القيادي (LTp)", value=85.0, key="emp_ltp")
            oar_val = st.number_input("الوصول للفرص (OAr)", value=80.0, key="emp_oar")
        with col2:
            sci_val = st.number_input("مؤشر مراعاة السنن (SCi)", value=90.0, key="emp_sci")            
        es_res = (0.4 * ltp_val + 0.3 * oar_val + 0.3 * sci_val)
        st.metric("مؤشر التمكين (ES)", f"{es_res:.2f}")
    # --- 4. سياسة الأزمات (الوقاية والنجاة) ---
    with tab_crisis:
        st.subheader("سِيَاسَةُ الْأَزْمَاتِ")
        st.latex(r"CR = \delta_1 NFs + \delta_2 RR + \delta_3 SF")
        st.warning("المقصد: الوقاية والنجاة عبر فقه الضرورة ومرونة تعليق الأحكام.")       
        col1, col2 = st.columns(2)
        with col1:
            nfs_val = st.number_input("مؤشر فقه الضرورة (NFs)", value=95.0, key="crisis_nfs")
            rr_val = st.number_input("معدل إعادة التوزيع (RR)", value=80.0, key="crisis_rr")
        with col2:
            sf_val = st.number_input("مرونة تعليق الأحكام (SF)", value=85.0, key="crisis_sf")            
        cr_res = (0.5 * nfs_val + 0.3 * rr_val + 0.2 * sf_val)
        st.metric("التصدي للأزمات (CR)", f"{cr_res:.2f}")
    st.markdown("---")
    st.success("تم تفعيل بروتوكول السياسات الاقتصادية السننية لتعزيز الاستقرار وتحقيق العدالة المقاصدية.")

elif mid == "m16_m19":
    st.markdown(f"<h1 class='header-style'>النَّمَاذِجُ التَّطْبِيقِيَّةُ لِهَنْدَسَةِ السُّوقِ: مِنَ التَّبَادُلِ إِلَى التَّزْكِيَةِ</h1>", unsafe_allow_html=True)    
    # تعريف التبويبات للنماذج الأربعة
    tab_justice, tab_transparency, tab_monopoly, tab_niya = st.tabs([
        "⚖️ العدالة السوقية", 
        "🔍 الشفافية", 
        "🚫 منع الاحتكار", 
        "💎 النية الصالحة"
    ])
    # --- 1. الْعَدَالَةُ فِي السُّوقِ (Yt) ---
    with tab_justice:
        st.subheader("الْعَدَالَةُ فِي السُّوقِ: نموذج الاستقرار التزكوي")
        st.latex(r"Y_t = \beta_0 + \beta_1 Ft + \beta_2 Tt + \beta_3 At + \beta_4 Et + \epsilon_t")
        st.info("الفرضية: زيادة العدالة السوقية تقلل تقلبات الأسعار وتزيد الاستقرار الاقتصادي.")        
        col1, col2 = st.columns(2)
        with col1:
            ft_val = st.number_input("مؤشر العدالة السعرية (Ft)", 0.0, 100.0, 80.0, key="m16_ft")
            tt_val = st.number_input("مؤشر الشفافية السوقية (Tt)", 0.0, 100.0, 75.0, key="m16_tt")
        with col2:
            at_val = st.number_input("مؤشر منع الاحتكار (At)", 0.0, 100.0, 85.0, key="m16_at")
            et_val = st.number_input("مؤشر الإنصاف في التوزيع (Et)", 0.0, 100.0, 70.0, key="m16_et")        
        # حساب النتيجة (استخدام أوزان لتمثيل العلاقة العكسية مع التقلبات)
        y_justice = (100 - (0.3*ft_val + 0.2*tt_val + 0.3*at_val + 0.2*et_val))
        st.metric("مؤشر تقلبات الأسعار (Yt)", f"{y_justice:.2f}")
    # --- 2. الشَّفَافِيَّةُ فِي السُّوقِ (Yt) ---
    with tab_transparency:
        st.subheader("الشَّفَافِيَّةُ فِي السُّوقِ: نموذج رفع الجهالة والغرر")
        st.latex(r"Y_t = \alpha_0 + \alpha_1 Dt + \alpha_2 Ct + \alpha_3 It + \alpha_4 AFt + \mu_t")
        st.info("الفرضية: كلما زادت الشفافية، زادت الكفاءة وانخفضت التقلبات السوقية.")        
        col1, col2 = st.columns(2)
        with col1:
            dt_val = st.number_input("مؤشر الإفصاح السعري (Dt)", 0.0, 100.0, 90.0, key="m17_dt")
            ct_val = st.number_input("مؤشر وضوح العقود (Ct)", 0.0, 100.0, 85.0, key="m17_ct")
        with col2:
            it_val = st.number_input("مؤشر توفر المعلومات (It)", 0.0, 100.0, 80.0, key="m17_it")
            aft_val = st.number_input("مؤشر مكافحة الغش (AFt)", 0.0, 100.0, 95.0, key="m17_aft")          
        y_trans = (0.4*dt_val + 0.2*ct_val + 0.2*it_val + 0.2*aft_val)
        st.metric("مؤشر كفاءة السوق (Yt)", f"{y_trans:.2f}")
    # --- 3. مَنْعُ الِاحْتِكَارِ فِي السُّوقِ (Yt) ---
    with tab_monopoly:
        st.subheader("مَنْعُ الِاحْتِكَارِ فِي السُّوقِ: نموذج التزكية عبر التنافسية")
        st.latex(r"Y_t = \gamma_0 + \gamma_1 HHt + \gamma_2 ACt + \gamma_3 RIt + \gamma_4 AMt + \nu_t")
        st.info("الفرضية: انخفاض التركز السوقي (HHI) وتدخل الدولة الفعال يعزز العدالة التوزيعية.")      
        col1, col2 = st.columns(2)
        with col1:
            hh_val = st.number_input("مؤشر التركز السوقي (HHt)", 0.0, 10000.0, 1500.0, key="m18_hh")
            ac_val = st.number_input("عدد المنافسين الفاعلين (ACt)", 1.0, 100.0, 10.0, key="m18_ac")
        with col2:
            ri_val = st.number_input("مؤشر تدخل الدولة (RIt)", 0.0, 100.0, 75.0, key="m18_ri")
            am_val = st.number_input("مؤشر الشكاوى الاحتكارية (AMt)", 0.0, 100.0, 20.0, key="m18_am")          
        # نموذج حساب العدالة التوزيعية (HHI يؤثر سلباً)
        y_monop = ((10000 - hh_val)/100 + 0.3*ac_val + 0.4*ri_val - 0.2*am_val)
        st.metric("مؤشر العدالة التوزيعية (Yt)", f"{y_monop:.2f}")
    # --- 4. النِّيَّةُ الصَّالِحَةُ فِي السُّوقِ (Yt) ---
    with tab_niya:
        st.subheader("النِّيَّةُ الصَّالِحَةُ فِي السُّوقِ: نموذج الاقتصاد السلوكي التزكوي")
        st.latex(r"Y_t = \delta_0 + \delta_1 GIt + \delta_2 APt + \delta_3 CCt + \delta_4 NDt + \xi_t")
        st.info("الفرضية: النية الصالحة والإيثار في التسعير يزيدان من رضا المجتمع ويقللان الفجوة التوزيعية.")        
        col1, col2 = st.columns(2)
        with col1:
            gi_val = st.number_input("مؤشر النية الصالحة (GIt)", 0.0, 100.0, 95.0, key="m19_gi")
            ap_val = st.number_input("مؤشر الإيثار في التسعير (APt)", 0.0, 100.0, 80.0, key="m19_ap")
        with col2:
            cc_val = st.number_input("مؤشر المبادرات المجتمعية (CCt)", 0.0, 100.0, 85.0, key="m19_cc")
            nd_val = st.number_input("مؤشر الامتناع عن الغش (NDt)", 0.0, 100.0, 98.0, key="m19_nd")            
        y_niya = (0.4*gi_val + 0.2*ap_val + 0.2*cc_val + 0.2*nd_val)
        st.metric("مؤشر الرضا العام والعدالة (Yt)", f"{y_niya:.2f}")
    st.markdown("---")
    st.success("تم تفعيل بروتوكول هندسة السوق التزكوية لضبط كفاءة التبادل وتحقيق المقاصد الشرعية.")

elif mid == "m20_m23":
    st.markdown(f"<h1 class='header-style'>نَماذِجُ تَطْبِيقِيَّةٌ لِهَنْدَسَةِ العَرْضِ والطَّلَبِ في ضَوْءِ المَقاصِدِ</h1>", unsafe_allow_html=True)    
    # تعريف التبويبات للنماذج الأربعة
    tab_suff, tab_mercy, tab_fair, tab_state = st.tabs([
        "⚖️ سعر الكفاية", 
        "🤍 العرض الرحيم", 
        "🛒 الطلب العادل", 
        "🏛️ التدخل المقاصدي"
    ])
    # --- 1. سِعْرُ الكِفايَةِ (Pk) ---
    with tab_suff:
        st.subheader("سِعْرُ الكِفايَةِ: توازن الحقوق والكرامة")
        st.latex(r"P_k = \delta_0 + \delta_1 C + \delta_2 Mr + \delta_3 As + \epsilon")
        st.info("الفرضية: السعر العادل هو الذي يحقق الكفاية للمنتج والمستهلك معاً دون إخلال بالتوازن.")        
        col1, col2 = st.columns(2)
        with col1:
            c_cost = st.number_input("تكلفة الإنتاج (C)", min_value=0.0, value=100.0, key="m20_c")
            mr_profit = st.number_input("هامش الربح المشروع (Mr)", min_value=0.0, value=15.0, key="m20_mr")
        with col2:
            as_index = st.number_input("معامل الكفاية الاجتماعية (As)", 0.0, 100.0, 80.0, key="m20_as")            
        # حساب سعر الكفاية بناءً على الأوزان الهندسية
        pk_res = (1.0 * c_cost + 1.0 * mr_profit + 0.5 * as_index)
        st.metric("سعر الكفاية المقترح (Pk)", f"{pk_res:.2f}")
        st.write("**الأثر المتوقع:** تقليل الفقر ومنع الاحتكار واستقرار السوق.")
    # --- 2. العَرْضُ الرَّحِيمُ (QS) ---
    with tab_mercy:
        st.subheader("العَرْضُ الرَّحِيمُ: العطاء في زمن الأزمات")
        st.latex(r"QS = \gamma_0 + \gamma_1 H + \gamma_2 I + \gamma_3 S + \epsilon")
        st.info("الفرضية: العرض الرحيم يرتفع في الأزمات لتقليل التقلبات وزيادة الثقة المجتمعية.")        
        col1, col2 = st.columns(2)
        with col1:
            h_need = st.number_input("مستوى الحاجة المجتمعية (H)", 0.0, 100.0, 90.0, key="m21_h")
            i_intent = st.number_input("نية الإحسان والمبادرات (I)", 0.0, 100.0, 85.0, key="m21_i")
        with col2:
            s_avail = st.number_input("وفرة السلعة والمخزون (S)", 0.0, 100.0, 70.0, key="m21_s")           
        qs_res = (0.4 * h_need + 0.4 * i_intent + 0.2 * s_avail)
        st.metric("كمية العرض الرحيم (QS)", f"{qs_res:.2f}")
    # --- 3. الطَّلَبُ العَادِلُ (Qd) ---
    with tab_fair:
        st.subheader("الطَّلَبُ العَادِلُ: ترشيد الاستهلاك")
        st.latex(r"Q_d = \alpha_0 + \alpha_1 Y + \alpha_2 A + \alpha_3 N + \epsilon")
        st.info("الفرضية: زيادة الوعي الاستهلاكي تقلل الهدر وتحقق التوازن السوقي.")        
        col1, col2 = st.columns(2)
        with col1:
            y_income = st.number_input("دخل الفرد (Y)", min_value=0.0, value=5000.0, key="m22_y")
            a_awareness = st.number_input("وعي الاستهلاك (A)", 0.0, 100.0, 75.0, key="m22_a")
        with col2:
            n_real_need = st.number_input("الحاجة الحقيقية (N)", 0.0, 100.0, 85.0, key="m22_n")            
        # نموذج الطلب العادل (الوعي A يقلل من الطلب المفرط)
        qd_res = (0.01 * y_income - 0.2 * a_awareness + 0.5 * n_real_need + 30)
        st.metric("كمية الطلب العادل (Qd)", f"{qd_res:.2f}")
    # --- 4. تَدَخُّلُ الدَّوْلَةِ المَقاصِدِيُّ (Is) ---
    with tab_state:
        st.subheader("تَدَخُّلُ الدَّوْلَةِ المَقاصِدِيُّ: ضبط الموازين")
        st.latex(r"Is = \beta_0 + \beta_1 M + \beta_2 D + \beta_3 R + \epsilon")
        st.warning("الفرضية: تدخل الدولة ضروري عند اختلال السوق لتحقيق مقاصد العدل والرحمة.")        
        col1, col2 = st.columns(2)
        with col1:
            m_imbalance = st.number_input("مستوى اختلال السوق (M)", 0.0, 100.0, 60.0, key="m23_m")
            d_tools = st.number_input("أدوات التدخل والرقابة (D)", 0.0, 100.0, 70.0, key="m23_d")
        with col2:
            r_maqasid = st.number_input("تحقيق المقاصد الشرعية (R)", 0.0, 100.0, 90.0, key="m23_r")            
        is_res = (0.4 * m_imbalance + 0.3 * d_tools + 0.3 * r_maqasid)
        st.metric("درجة التدخل المقاصدي (Is)", f"{is_res:.2f}")
    st.markdown("---")
    st.success("تم دمج نماذج هندسة العرض والطلب بنجاح لضمان كفاية المجتمع واستقرار الأسواق.")
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

elif mid == "m30":
    st.markdown(f"<h1 class='header-style'>خوارزمية التقييم الشرعي التنبؤية (المدينة المقاصدية)</h1>", unsafe_allow_html=True)    
    # 1. دالة التقييم الشرعي التنبؤية
    st.latex(r"M_{impact} = \sum_{i=1}^{5} (\omega_i \cdot P_i) + \epsilon")    
    desc = """خوارزمية التقييم الشرعي التنبؤية: خوارزمية رقمية تُحاكي أثر السياسات الحضرية والاقتصادية على المقاصد الشرعية الخمسة 
    لترشيد القرارات الوقفية والبلدية قبل تنفيذها في المدينة الذكية.""" if lang == "العربية" else "Predictive Sharia Assessment Algorithm: Simulates the impact of urban policies on the five Sharia objectives (Maqasid) to guide decision-making."    
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    # 2. مدخلات الخوارزمية (السياسات المقترحة)
    st.write("### 🛠️ مدخلات سياسات المحاكاة:")
    col_in1, col_in2, col_in3 = st.columns(3)    
    with col_in1:
        policy_waqf = st.number_input("حجم الاستثمار الوقفي (Wp)", 0.0, 1000.0, 500.0, key="m30_waqf")
        policy_zakat = st.number_input("معدل توزيع الزكاة (Zd)", 0.0, 1000.0, 300.0, key="m30_zakat")
    with col_in2:
        policy_infra = st.number_input("تطوير البنية التحتية (In)", 0.0, 1000.0, 400.0, key="m30_infra")
        policy_edu = st.number_input("الإنفاق التعليمي/الصحي (Ed)", 0.0, 1000.0, 450.0, key="m30_edu")
    with col_in3:
        policy_security = st.number_input("مؤشر الأمن والرقابة (Se)", 0.0, 1000.0, 600.0, key="m30_sec")
    # 3. خريطة المقاصد الشرعية (المخرجات التنبؤية)
    st.markdown("---")
    st.write("### 📊 نتائج المحاكاة ولائحة الأثر المقاصدي:")    
    # حساب الأثر التنبؤي لكل مقصد (بناءً على معاملات التأثير التقديرية)
    m_religion = (0.4 * policy_waqf + 0.2 * policy_edu) / 10
    m_life = (0.3 * policy_infra + 0.5 * policy_edu + 0.2 * policy_security) / 10
    m_intellect = (0.7 * policy_edu + 0.3 * policy_waqf) / 10
    m_progeny = (0.4 * policy_zakat + 0.4 * policy_infra + 0.2 * policy_edu) / 10
    m_wealth = (0.5 * policy_zakat + 0.3 * policy_waqf + 0.2 * policy_infra) / 10
    # عرض النتائج في بطاقات ذكية
    res_col1, res_col2, res_col3, res_col4, res_col5 = st.columns(5)    
    with res_col1:
        st.metric("حفظ الدين", f"{m_religion:.1f}", delta="إيجابي" if m_religion > 50 else "ضعيف")
    with res_col2:
        st.metric("حفظ النفس", f"{m_life:.1f}", delta="إيجابي" if m_life > 50 else "ضعيف")
    with res_col3:
        st.metric("حفظ العقل", f"{m_intellect:.1f}", delta="إيجابي" if m_intellect > 50 else "ضعيف")
    with res_col4:
        st.metric("حفظ النسل", f"{m_progeny:.1f}", delta="إيجابي" if m_progeny > 50 else "ضعيف")
    with res_col5:
        st.metric("حفظ المال", f"{m_wealth:.1f}", delta="إيجابي" if m_wealth > 50 else "ضعيف")
    # 4. تحليل النتائج داخل بيئة المحاكاة
    st.markdown("---")
    total_impact = (m_religion + m_life + m_intellect + m_progeny + m_wealth) / 5
    if total_impact >= 75:
        st.success(f"✅ السياسة المقترحة مطابقة للمقاصد العليا (مؤشر الاستخلاف: {total_impact:.2f})")
    elif total_impact >= 50:
        st.warning(f"⚠️ السياسة تحتاج إلى ضبط لتحسين الأثر المقاصدي (مؤشر الاستخلاف: {total_impact:.2f})")
    else:
        st.error(f"🚨 السياسة قد تؤدي إلى خلل في التوازن المقاصدي (مؤشر الاستخلاف: {total_impact:.2f})")
    # 5. المنظومة الرمزية (الابتكار)
    st.info("💡 **الابتكار الرمزي:** يتم ربط هذه النتائج بلحظة محاكاة بصرية داخل المدينة الذكية لتوجيه الهيئات الشرعية والمؤسسات الوقفية بلغة رقمية.")

elif mid == "m31":
    st.markdown(f"<h1 class='header-style'>مُؤَشِّرُ الأَمَانِ الشَّرْعِيِّ فِي الاِقْتِصَادِ الرَّمْزِيِّ</h1>", unsafe_allow_html=True)    
    # 1. المعادلة المركبة للمؤشر
    st.latex(r"SSI = \sum (\omega_i \cdot S_i)")    
    desc = """مؤشر الأمان الشرعي (SSI): أداة تحليلية مركبة تُقيِّم الرموز الرقمية والأصول الذكية من حيث التزامها بالقواعد الفقهية والمقاصد والحوكمة الإسلامية، 
    مما يمنح المستثمر درجة أمان رقمية موثوقة.""" if lang == "العربية" else "Sharia Safety Index (SSI): A composite tool assessing digital tokens and smart assets based on Fiqh rules, Maqasid, and Islamic governance."    
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    # 2. إدخال المؤشرات الفرعية (التقييم الرقمي)
    st.write("### 🔍 تقييم أبعاد الأمان الشرعي للرمز الرقمي:")    
    col_eval1, col_eval2 = st.columns(2)    
    with col_eval1:
        s1 = st.number_input("التوافق الفقهي (فتوى، خلو من الربا) - %", 0, 100, 90, key="m31_s1")
        s2 = st.number_input("المقاصد الشرعية (أثر اجتماعي وتنموي) - %", 0, 100, 85, key="m31_s2")
        s3 = st.number_input("الشفافية الشرعية (توثيق النية والعقود) - %", 0, 100, 80, key="m31_s3")    
    with col_eval2:
        s4 = st.number_input("الحوكمة الإسلامية (هيئة رقابة ومراجعة) - %", 0, 100, 75, key="m31_s4")
        s5 = st.number_input("قابلية التتبع الشرعي (سجل البلوك تشين) - %", 0, 100, 95, key="m31_s5")
        w_factor = st.slider("معامل الأولوية الشرعية (الوزن المعياري)", 0.5, 1.5, 1.0)
    # 3. الحسابات الرقمية للمؤشر
    # الأوزان المعيارية المقترحة: الفقهي 30%، المقاصد 20%، الشفافية 20%، الحوكمة 15%، التتبع 15%
    ssi_score = ( (0.30 * s1) + (0.20 * s2) + (0.20 * s3) + (0.15 * s4) + (0.15 * s5) ) / 100
    ssi_final = ssi_score * w_factor
    # 4. عرض النتائج والتصنيف الشرعي
    st.markdown("---")
    col_res1, col_res2 = st.columns([1, 2])    
    with col_res1:
        st.metric("درجة الأمان الشرعي (SSI)", f"{ssi_final:.2f}")    
    with col_res2:
        if ssi_final >= 0.80:
            st.success("✅ الفئة: آمن شرعيًّا | التوصية: صالح للاستثمار والتمويل")
        elif ssi_final >= 0.50:
            st.warning("⚠️ الفئة: متوسط الأمان | التوصية: يُوصى بالمراجعة الشرعية وتعديل العقود")
        else:
            st.error("🚨 الفئة: منخفض الأمان | التوصية: يُوصى بالامتناع أو إعادة الهيكلة الشاملة")
    # 5. الاستخدامات التطبيقية
    with st.expander("📚 الاستخدامات التطبيقية للمؤشر"):
        st.write("""
        * **توجيه المستثمرين:** نحو الرموز الرقمية الأكثر امتثالاً ومصداقية.
        * **دعم الأوقاف:** في اختيار الصكوك والرموز الوقفية لتمويل المشاريع.
        * **الشفافية:** ربط المؤشر بسجل البلوك تشين (Blockchain) لضمان عدم التلاعب بالبيانات الشرعية.
        * **التحفيز:** دفع المشاريع الناشئة لتبني معايير (AAOIFI) للحصول على تصنيف مرتفع.
        """)
    st.markdown("---")
    st.caption(f"تم تطوير هذا المؤشر بناءً على معايير الأمان الشرعي الذكي - {AUTHOR_NAME} 2026")

elif mid == "m32":
    st.markdown(f"<h1 class='header-style'>بروتوكول الإشراف الرقمي وتصنيف الأصول الرمزية</h1>", unsafe_allow_html=True)
    
    # 1. الإطار المفاهيمي للهيئة الشرعية الرقمية
    st.latex(r"SCS = \sum_{i=1}^{n} (\omega_i \cdot C_i)")
    
    desc = """بروتوكول الإشراف الرقمي (m32): منظومة ذكية متكاملة لإدارة الأصول الرمزية (Tokens)، 
    تجمع بين تصنيف الالتزام الشرعي (SCS)، وإدارة العقود الذكية الوقفية، ومنصة الزكاة الرمزية لضمان سيادة المقاصد في الاقتصاد الرقمي."""
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)

    # إنشاء التبويبات الثلاثة للمنظومة
    tab_class, tab_smart_contract, tab_zakat_platform = st.tabs([
        "🛡️ تصنيف الأصول الرمزية", 
        "📜 العقود الذكية الوقفية", 
        "💰 منصة الزكاة الرمزية"
    ])
    # --- التبويب الأول: تصنيف الأصول الرمزية (SCS) ---
    with tab_class:
        st.subheader("وحدة التصنيف الشرعي للأصول الرمزية")
        st.info("قم بإدخال درجات الالتزام (من 0 إلى 1) بناءً على معايير الهيئة الرقمية")        
        c1, c2 = st.columns(2)
        with c1:
            fiqh_c = st.slider("الضوابط الفقهية (الربا، الغرر)", 0.0, 1.0, 0.95, key="scs_fiqh")
            maqasid_c = st.slider("المقاصد الشرعية (حفظ الضرورات)", 0.0, 1.0, 0.90, key="scs_maq")
            trans_c = st.slider("الشفافية والتوثيق (Blockchain)", 0.0, 1.0, 0.85, key="scs_trans")
        with c2:
            gov_c = st.slider("الحوكمة الشرعية (هيئة الرقابة)", 0.0, 1.0, 0.75, key="scs_gov")
            social_c = st.slider("الأثر الاجتماعي (تمكين، عدالة)", 0.0, 1.0, 0.80, key="scs_social")        
        # حساب النتيجة بناءً على الأوزان المعيارية (30%، 25%، 20%، 15%، 10%)
        scs_score = (0.30*fiqh_c + 0.25*maqasid_c + 0.20*trans_c + 0.15*gov_c + 0.10*social_c)       
        st.markdown(f"### مؤشر الامتثال الشرعي (SCS): **{scs_score:.2f}**")
        if scs_score >= 0.80:
            st.success("✅ متوافق شرعيًّا (Shariah-Compliant): صالح للاستثمار والتمويل")
        elif scs_score >= 0.50:
            st.warning("⚠️ متوافق جزئيًّا (Review Required): يحتاج مراجعة فنية فقهية")
        else:
            st.error("❌ غير متوافق (Non-Compliant): يُوصى بالامتناع أو التعديل الجذري")
    # --- التبويب الثاني: العقود الذكية الوقفية ---
    with tab_smart_contract:
        st.subheader("محاكي العقود الذكية الوقفية (Smart Waqf)")
        st.write("تحويل شروط الواقف إلى أكواد قابلة للتنفيذ الذاتي:")       
        asset_id = st.text_input("معرف الأصل الوقفي", "Waqf-Asset-2026")
        intent_signed = st.checkbox("توثيق نية الواقف (النية الوقفية الرقمية)")        
        st.code(f"""
        if (asset_verified == True and intent_signed == {intent_signed}):
            execute_waqf_transfer(asset_id)
            log_to_blockchain("Waqf_Execution_Success")
        else:
            stop_transaction("Incomplete_Sharia_Conditions")
        """, language="python")       
        if intent_signed:
            st.success("🔒 تم تسجيل شرط النفاذ الشرعي في سلسلة الكتلة.")
    # --- التبويب الثالث: منصة الزكاة الرمزية ---
    with tab_zakat_platform:
        st.subheader("منصة الزكاة الرمزية: تحويل النية إلى أصول مقاصدية")
        st.latex(r"Z_{token} = f(Niya, Value, Maqasid\_Map)")       
        z_value = st.number_input("قيمة الزكاة المراد ترميزها (Z_value)", min_value=0.0, value=1000.0)
        target_maqsad = st.selectbox("توجيه المصرف (الخوارزمية المقاصدية)", ["حفظ النفس (صحة)", "حفظ العقل (تعليم)", "حفظ المال (تمويل إنتاجي)"])        
        if st.button("إصدار رمز الزكاة (Z-Token)"):
            st.balloons()
            st.info(f"تم إصدار الرمز بنجاح وتوجيهه إلى مصرف: {target_maqsad}")
            st.table({
                "مؤشر الأداء الشرعي": ["نسبة تحقق النية", "كفاءة التوزيع", "الشفافية"],
                "النسبة الحالية": ["100%", "94%", "98%"]
            })
    
elif mid == "m33":
    st.markdown(f"<h1 class='header-style'>بروتوكول 'أمانة' السيادي: المحاكاة الرقمية الشاملة</h1>", unsafe_allow_html=True)    
    # 1. المعادلات الحاكمة للمحرك (البركة والتداول)
    st.latex(r"Bi = \frac{\sum (U_v \cdot S_t)}{H_w + D_i} \quad , \quad W_c = \frac{V_{zakat}}{S_{stagnation}}")    
    desc = """بروتوكول أمانة: نظام ائتماني سيادي يعتمد 'براهين الجدارة' بدلاً من الفائدة. 
    يستخدم 'بصمة الستر الرقمي' لحماية الخصوصية، و'القيد البرمجي' لمنع الاحتكار والربا آلياً."""
    st.markdown(f'<div class="explanation-box"><b>💡 {desc}</b></div>', unsafe_allow_html=True)
    # إنشاء التبويبات لمحاكاة المنظومة
    tab_dash, tab_shock, tab_logic, tab_sovereign = st.tabs([
        "🖥️ لوحة تحكم الاستخلاف", 
        "📉 منحنى امتصاص الصدمات", 
        "⚙️ البوابات المنطقية (PC)", 
        "🛡️ درع التحصين السيادي"
    ])
    # --- التبويب الأول: لوحة تحكم الذكاء الاستخلافي ومدخلات النظام ---
    with tab_dash:
        st.subheader("لوحة تحكم الذكاء الاستخلافي (Control Dashboard)")        
        # مدخلات المشروع الأساسية
        col_in1, col_in2 = st.columns(2)
        with col_in1:
            project_value = st.number_input("قيمة المشروع العينية", value=1000000.0, step=10000.0, key="m33_p_val")
            uv_val = st.number_input("النفع المتعدي (Utility Value)", 0.0, 100.0, 85.0, key="m33_uv_val")
        with col_in2:
            work_share = st.slider("نسبة مشاركة الجهد (المنتج)", 0, 100, 40, key="m33_w_s")
            st_val = st.number_input("استدامة الأثر (Sustainability)", 0.0, 1.0, 0.9, key="m33_st_val")            
        st.markdown("---")        
        # حساب المؤشرات اللحظية (تفاعل حي)
        hw_val, di_val = 10.0, 5.0
        bi_score = (uv_val * st_val) / (hw_val + di_val)        
        col_m1, col_m2, col_m3, col_m4 = st.columns(4)
        with col_m1:
            st.metric("معامل التداول (Wc)", f"{bi_score * 0.12:.2f}", delta="30% vs Trad")
        with col_m2:
            st.metric("انقباض الآمال (Ei)", f"{100 - (bi_score * 10):.2f}", delta="-15%", delta_color="inverse")
        with col_m3:
            st.metric("رصيد الزكاة (Tazkiyah)", "25,000 $", delta="جاهز")
        with col_m4:
            st.metric("مؤشر البركة (Bi)", f"{bi_score:.2f}", delta="ممتاز")
        st.info("💡 الإجراء البرمجي: تم تفعيل 'حسبة ابن تيمية السيبرانية' لمراقبة الأسعار لحظياً.")
    # --- التبويب الثاني: منحنى امتصاص الصدمات ---
    with tab_shock:
        st.subheader("محاكاة صمود العمران vs الانهيار التقليدي")
        chart_data = {
            "الأزمة": [0, 1, 2, 3, 4, 5],
            "النظام التقليدي (القرض)": [1.0, 0.80, 0.45, 0.15, 0.05, 0.0],
            "بروتوكول أمانة (المشاركة)": [1.0, 0.92, 0.82, 0.70, 0.62, 0.55]
        }
        st.line_chart(chart_data, x="الأزمة")
        st.success("النتيجة: المشاركة في الخسارة تخفف العبء عن الأصول وتمنع الإفلاس القسري.")
    # --- التبويب الثالث: البوابات المنطقية والقيد البرمجي ---
    with tab_logic:
        st.subheader("محرك التشغيل: البوابات المنطقية (Logic Gates)")
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            st.write("**🛡️ فلتر الغزالي (بوابة القصد)**")
            flow = st.radio("نوع المعاملة:", ["عمارة حقيقية", "مضاربة وهمية"], key="gate_m33")
            if flow == "عمارة حقيقية":
                st.success("✅ [Access Granted]: مسارات السيولة مفتوحة.")
            else:
                st.error("❌ [Access Denied]: قيد برمجـي يمنع الفقاعات.")
        with col_p2:
            st.write("**🔄 خوارزمية مكافحة الركود**")
            stagnation = st.slider("سكون المال (شهور):", 0, 24, 13, key="stagn_m33")
            if stagnation >= 12:
                st.warning("🚨 بلوغ الحول الرقمي: تفعيل بوابة التزكية الآلية.")
    # --- التبويب الرابع: درع التحصين السيادي ---
    with tab_sovereign:
        st.subheader("السيادة الرقمية وبصمة الستر")
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            st.write("**🔒 بصمة الستر الرقمي**")
            if st.button("إصدار صك جدارة مستور", key="ssi_btn"):
                st.info("تم توثيق أثرك العمراني (Zero-Knowledge) مع بقاء هويتك مستورة.")
        with col_s2:
            st.write("**🌍 التوأمة الرقمية للموارد (RWA)**")
            st.code("Constraint: Property_Transfer ONLY IF (Added_Value > 0)", language="python")
    st.markdown("---")
    st.write("### 🏛️ حوكمة الهيئة الشرعية الرقمية")
    st.table({
        "الوحدة": ["الفتوى الذكية", "التتبع الشرعي", "التقرير الرقمي"],
        "التقنية": ["AI-NLP", "Smart Monitoring", "Blockchain Ledger"],
        "الحالة": ["نشط", "مراقب", "جاهز"]
    })
    
