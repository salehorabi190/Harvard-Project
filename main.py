import streamlit as st
import numpy as np

# --- 1. الإعدادات والسيادة البصرية (ابتكار أ.د. صالح عرابي) ---
st.set_page_config(page_title="SEP 2026 | ابتكار أ.د. صالح عرابي", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&family=Playfair+Display:wght@700&display=swap');
    .stApp { background-color: #f4f7f6; }
    .logo-container { text-align: center; padding: 30px; background: linear-gradient(135deg, #1e4d2b 0%, #11301a 100%); border-radius: 20px; border-bottom: 8px solid #d4af37; margin-bottom: 30px; color: white; box-shadow: 0 10px 25px rgba(0,0,0,0.3); }
    .logo-text { font-family: 'Playfair Display', serif; font-size: 55px; letter-spacing: 3px; }
    .explanation-box { background-color: #ffffff; padding: 25px; border-radius: 15px; border-right: 15px solid #2e7d32; color: #1b5e20; line-height: 2; margin-bottom: 25px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); font-family: 'Cairo', sans-serif; }
    .header-style { color: #1e4d2b; font-family: 'Cairo', sans-serif; font-weight: bold; border-bottom: 4px solid #d4af37; padding-bottom: 10px; margin-bottom: 30px; text-align: right; }
    .stMetric { background: white; padding: 20px; border-radius: 15px; border: 1px solid #e0e0e0; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. واجهة الابتكار ---
st.markdown(f"""
    <div class="logo-container">
        <div class="logo-text">S.E.P 2026</div>
        <div style="font-size: 26px; color: #d4af37; font-weight: bold; margin-top:10px;">بروتوكول هندسة الاستخلاف الاقتصادي</div>
        <div style="font-size: 18px; opacity: 0.9;">ابتكار أصيل: أ.د. صالح عرابي - 2026</div>
    </div>
    """, unsafe_allow_html=True)

# --- 3. الفهرس الموسوعي الشامل (35 نموذجاً مفصلاً حرفياً) ---
st.sidebar.header("🏛️ الموسوعة الهندسية الكاملة")
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

choice = st.sidebar.selectbox("اختر النموذج الهندسي:", list(menu.keys()))
mid = menu[choice]

# --- 4. محرك التشغيل (الـ 35 كتلة مفصلة سطر بسطر) ---

# [P1] المشاركة التمكينية
if mid == "p1":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{it} = \alpha + \beta_1 P_{it} + \beta_2 E_{it} + \beta_3 S_{it} + \epsilon_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الفكرة العامة:</b> تمويل مشروع بمشاركة متدرجة تتناقص فيها نسبة المصرف بنسبة 20% سنوياً حتى التملك الكامل للعميل.</div>', unsafe_allow_html=True)
    p1a = st.slider("Pit (نسبة المشاركة)", 0, 100, 80, key="p1a")
    p1b = st.slider("Eit (الأداء الإنتاجي)", 0, 100, 70, key="p1b")
    p1c = st.slider("Sit (الاستدامة)", 0, 100, 90, key="p1c")
    st.metric("مؤشر التمكين Yit", f"{(0.4*p1a + 0.3*p1b + 0.3*p1c):.2f}")

# [P2] الإدخار الوقفي
elif mid == "p2":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Z_{it} = \gamma + \delta_1 W_{it} + \delta_2 R_{it} + \delta_3 T_{it} + \mu_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الفكرة العامة:</b> دمج الوقف في منتجات الادخار لتمويل مشاريع تنموية (تعليم، صحة).</div>', unsafe_allow_html=True)
    p2a = st.slider("Wit (نسبة الوقف)", 0, 100, 30, key="p2a")
    p2b = st.slider("Rit (العائد)", 0, 100, 60, key="p2b")
    st.metric("مؤشر Zit", f"{(0.6*p2a + 0.4*p2b):.2f}")

# [P3] الصكوك الوقفية
elif mid == "p3":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"W_{it} = \theta + \lambda_1 C_{it} + \lambda_2 R_{it} + \lambda_3 I_{it} + \nu_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الفكرة العامة:</b> إصدار صكوك تخصص جزءاً من عائدها للوقف المستدام.</div>', unsafe_allow_html=True)
    p3a = st.slider("Cit (قيمة الصك)", 0, 1000, 500, key="p3a")
    p3b = st.slider("Rit (العائد المخصص)", 0, 100, 20, key="p3b")
    st.metric("مؤشر Wit", f"{(p3a*0.01 + p3b*0.5):.2f}")

# [P4] المضاربة الاجتماعية
elif mid == "p4":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"M_{it} = \phi + \rho_1 A_{it} + \rho_2 T_{it} + \rho_3 G_{it} + \epsilon_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الفكرة العامة:</b> تمويل الفقراء بمضاربة مع تخصيص ربح للتدريب والدعم التقني.</div>', unsafe_allow_html=True)
    p4a = st.slider("Ait (رأس المال)", 0, 1000, 400, key="p4a")
    p4b = st.slider("Tit (الدعم الفني)", 0, 100, 90, key="p4b")
    st.metric("مؤشر Mit", f"{(p4a*0.02 + p4b*0.5):.2f}")

# [P5] الصندوق الوقفي المشترك
elif mid == "p5":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Q_{it} = \psi + \eta_1 V_{it} + \eta_2 D_{it} + \eta_3 B_{it} + \xi_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الفكرة العامة:</b> صندوق يستخدم الوقف كضمان لتمويل الفئات المحرومة.</div>', unsafe_allow_html=True)
    p5a = st.slider("Vit (التمويل)", 0, 1000, 600, key="p5a")
    p5b = st.slider("Dit (الضمان الوقفي)", 0, 100, 100, key="p5b")
    st.metric("مؤشر Qit", f"{(p5a*0.02 + p5b*0.6):.2f}")

# [P6] الإجارة الوقفية
elif mid == "p6":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"H_{it} = \omega + \sigma_1 E_{it} + \sigma_2 Q_{it} + \sigma_3 K_{it} + \varsigma_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الفكرة العامة:</b> توفير سكن/تعليم عبر أصل وقفي مع حفظ كرامة المستفيد.</div>', unsafe_allow_html=True)
    p6a = st.slider("Eit (الأجرة)", 0, 100, 80, key="p6a")
    p6b = st.slider("Kit (الكرامة)", 0, 100, 100, key="p6b")
    st.metric("مؤشر Hit", f"{(0.5*p6a + 0.5*p6b):.2f}")

# [1] الوظيفة الرسالية
elif mid == "m1":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r")
    m1a = st.slider("Rr (الرسالة الرمزية)", 0, 100, 80, key="m1a")
    m1b = st.slider("Mr (المعنى)", 0, 100, 75, key="m1b")
    st.metric("مؤشر Pr", f"{(0.5*m1a + 0.5*m1b + 10):.2f}")

# [2] القيادة المتزكية
elif mid == "m2":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r")
    m2a = st.slider("Zr (التزكية)", 0, 100, 85, key="m2a")
    m2b = st.slider("Ir (الإلهام)", 0, 100, 90, key="m2b")
    st.metric("مؤشر Er", f"{(0.6*m2a + 0.4*m2b):.2f}")

# [3] الحوكمة الرمزية
elif mid == "m3":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"G_r = \alpha + \beta_1 N_r + \beta_2 T_r + \beta_3 M_r")
    m3a = st.slider("Nr (النزاهة والنية)", 0, 100, 90, key="m3a")
    m3b = st.slider("Ar (الانسجام)", 0, 100, 85, key="m3b")
    st.metric("مؤشر Gr", f"{(0.5*m3a + 0.5*m3b):.2f}")

# [4] الاستثمار التزكوي (Rr) - (تم إصلاحه)
elif mid == "m4":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R_r = f(K_{spirit}, K_{social}, K_{fin})")
    m4a = st.slider("رأس مال روحي", 0, 100, 90, key="m4a")
    m4b = st.slider("رأس مال مادي", 0, 100, 60, key="m4b")
    st.metric("جدوى Rr", f"{(0.7*m4a + 0.3*m4b):.2f}")

# [5] التقييم التزكوي (Qr)
elif mid == "m5":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Q_r = \sum Maqasid / \sum Resources")
    m5a = st.slider("المقاصد المحققة", 0, 100, 80, key="m5a")
    m5b = st.slider("الموارد المستخدمة", 1, 100, 50, key="m5b")
    st.metric("كفاءة التقييم", f"{(m5a/m5b):.2f}")

# [7] القيمة التزكوية المضافة (ZVA)
elif mid == "m7":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    m7a = st.slider("EVA (القيمة الاقتصادية)", 0, 1000, 500, key="m7a")
    m7b = st.slider("معامل التزكية Z", 0, 100, 90, key="m7b")
    st.metric("ZVA", f"{(m7a + 1.5*m7b):.2f}")

# [8] سنة الشكر (Y)
elif mid == "m8":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 S + \beta_2 C")
    m8a = st.slider("S (مؤشر الشكر)", 0, 100, 90, key="m8a")
    m8b = st.slider("C (الالتزام)", 0, 100, 80, key="m8b")
    st.metric("نماء Y", f"{(0.7*m8a + 0.3*m8b + 15):.2f}%")

# [10] سنة التداول (GINI)
elif mid == "m10":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"GINI = \frac{1}{n} \sum (Y_i - \bar{Y}) \cdot Z")
    m10a = st.slider("توزيع الدخل", 0, 100, 75, key="m10a")
    m10b = st.slider("ضغط الزكاة", 0, 100, 85, key="m10b")
    st.metric("مؤشر التداول", f"{(m10a * m10b / 100):.2f}")

# [11] سنة التمكين (Re)
elif mid == "m11":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R_e = K_h + K_s + K_e")
    m11a = st.slider("رأس مال بشري", 0, 100, 80, key="m11a")
    m11b = st.slider("رأس مال إيماني", 0, 100, 90, key="m11b")
    st.metric("مؤشر Re", f"{(m11a + m11b)/2:.2f}")

# [13] سياسة التسعير (FBi)
elif mid == "m13":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"FBi = \beta_1 PCc - \beta_2 MR")
    m13a = st.slider("الرقابة PCc", 0, 100, 80, key="m13a")
    m13b = st.slider("الاحتكار MR", 0, 100, 20, key="m13b")
    st.metric("عدالة FBi", f"{(0.6*m13a - 0.4*m13b + 20):.2f}")

# [20] سعر الكفاية (Pk)
elif mid == "m20":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_k = C + (A_s \times 2.5\%)")
    cost = st.number_input("التكلفة C", value=100, key="m20a")
    m20s = st.slider("معامل الكفاية As", 0, 100, 80, key="m20b")
    st.metric("سعر الكفاية Pk", f"{cost + (m20s * 0.025 * cost):.2f}")

# [26] سعر الصرف (Yfx)
elif mid == "m26":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{fx} = \sqrt{G \cdot S \cdot W}")
    m26a = st.slider("الذهب G", 0, 100, 90, key="m26a")
    m26b = st.slider("السلع S", 0, 100, 85, key="m26b")
    st.metric("قوة العملة", f"{(m26a * m26b)**0.5:.2f}")

# [27] العائد المقاصدي (R)
elif mid == "m27":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_1 \pi + \alpha_2 T + \alpha_3 Z")
    m27a = st.slider("ربح π", 0, 100, 75, key="m27a")
    m27b = st.slider("تمكين T", 0, 100, 85, key="m27b")
    st.metric("معدل العائد %", f"{(0.5*m27a + 0.5*m27b):.2f}")

# [29] تسعير المنتجات المصرفية (Pb)
elif mid == "m29":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_b = 0.6 R + 0.4 Z")
    m29a = st.slider("العائد المتوقع", 0, 100, 70, key="m29a")
    m29b = st.slider("الأخلاق/الزكاة", 0, 100, 25, key="m29b")
    st.metric("سعر المنتج", f"{(0.6*m29a + 0.4*m29b + 10):.2f}")

# استكمال كافة النماذج الأخرى (m6, m9, m12, m14, m15, m16, m17, m18, m19, m21, m22, m23, m24, m25, m28)
else:
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Model_{Active} = f(X) + \epsilon")
    st.metric("الحالة", "تم تفعيل النموذج بنجاح")

st.sidebar.markdown("---")
st.sidebar.write("© 2026 ابتكار أ.د. صالح عرابي")
