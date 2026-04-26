import streamlit as st
import numpy as np

# --- 1. الإعدادات والسيادة البصرية ---
st.set_page_config(page_title="SEP 2026 | ابتكار أ.د. صالح عرابي", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&family=Playfair+Display:wght@700&display=swap');
    .stApp { background-color: #f4f7f6; }
    .logo-container { text-align: center; padding: 30px; background: linear-gradient(135deg, #1e4d2b 0%, #11301a 100%); border-radius: 20px; border-bottom: 8px solid #d4af37; margin-bottom: 30px; color: white; box-shadow: 0 10px 25px rgba(0,0,0,0.3); }
    .logo-text { font-family: 'Playfair Display', serif; font-size: 50px; letter-spacing: 3px; }
    .explanation-box { background-color: #ffffff; padding: 25px; border-radius: 15px; border-right: 12px solid #2e7d32; color: #1b5e20; line-height: 1.8; margin-bottom: 25px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); font-family: 'Cairo', sans-serif; }
    .header-style { color: #1e4d2b; font-family: 'Cairo', sans-serif; font-weight: bold; border-bottom: 3px solid #d4af37; padding-bottom: 10px; margin-bottom: 20px; text-align: right; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. واجهة الابتكار ---
st.markdown(f"""
    <div class="logo-container">
        <div class="logo-text">S.E.P 2026</div>
        <div style="font-size: 24px; color: #d4af37; font-weight: bold;">بروتوكول هندسة الاستخلاف الاقتصادي</div>
        <div style="font-size: 16px;">ابتكار أصيل: أ.د. صالح عرابي - 2026</div>
    </div>
    """, unsafe_allow_html=True)

# --- 3. الفهرس الموسوعي (35 نموذجاً) ---
st.sidebar.header("🏛️ الموسوعة الهندسية الكاملة")
menu = {
    # النماذج التطبيقية
    "P1. المشاركة التمكينية المتدرجة": "p1", "P2. الإدخار الوقفي الذكي": "p2", "P3. الصكوك الوقفية التنموية": "p3",
    "P4. المضاربة الاجتماعية التمكينية": "p4", "P5. صندوق الوقف التمكيني المشترك": "p5", "P6. الإجارة الوقفية الموصوفة": "p6",
    # النماذج القياسية والسنن والسياسات
    "1. نموذج الوظيفة الرسالية (Pr)": "m1", "2. نموذج القيادة المتزكية (Er)": "m2", "3. نموذج الحوكمة الرمزية (Gr)": "m3",
    "4. نموذج الاستثمار التزكوي (Rr)": "m4", "7. القيمة التزكوية المضافة (ZVA)": "m7", "8. سنة الشكر (Y)": "m8",
    "9. سنة الظلم (R)": "m9", "10. سنة التداول (GINI)": "m10", "11. سنة التمكين (R_e)": "m11",
    "12. سياسة مكافحة الفقر (ΔY)": "m12", "13. سياسة التسعير (FBi)": "m13", "14. سياسة التمكين (ES)": "m14",
    "15. سياسة الأزمات (CR)": "m15", "20. سعر الكفاية (Pk)": "m20", "21. العرض الرحيم (Qs)": "m21",
    "23. تدخل الدولة المقاصدي (Is)": "m23", "25. النموذج النقدي المركب (Y)": "m25", "26. هندسة سعر الصرف (Y_fx)": "m26",
    "27. معدل العائد المقاصدي (R)": "m27", "28. هندسة المالية المقاصدية (P)": "m28", "29. تسعير المنتجات المصرفية (P_b)": "m29"
}

choice = st.sidebar.selectbox("اختر النموذج الهندسي:", list(menu.keys()))
mid = menu[choice]

# --- 4. محرك التشغيل (الـ 35 نموذجاً سطر بسطر) ---

# [P1] المشاركة التمكينية
if mid == "p1":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{it} = \alpha + \beta_1 P_{it} + \beta_2 E_{it} + \beta_3 S_{it} + \epsilon_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> تمويل مشاريع بمشاركة متناقصة حتى التملك الكامل للعميل.</div>', unsafe_allow_html=True)
    p1_a = st.slider("Pit (نسبة المشاركة)", 0, 100, 80, key="p1_a")
    p1_b = st.slider("Eit (الأداء الإنتاجي)", 0, 100, 70, key="p1_b")
    st.metric("مؤشر التمكين Yit", f"{(0.5*p1_a + 0.5*p1_b):.2f}")

# [P2] الإدخار الوقفي
elif mid == "p2":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Z_{it} = \gamma + \delta_1 W_{it} + \delta_2 R_{it} + \delta_3 T_{it} + \mu_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> دمج الوقف في منتجات الادخار لتمويل مشاريع تنموية.</div>', unsafe_allow_html=True)
    p2_a = st.slider("Wit (نسبة الوقف)", 0, 100, 30, key="p2_a")
    p2_b = st.slider("Rit (العائد الوقفي)", 0, 100, 60, key="p2_b")
    st.metric("مؤشر الأثر Zit", f"{(0.6*p2_a + 0.4*p2_b):.2f}")

# [P3] الصكوك الوقفية
elif mid == "p3":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"W_{it} = \theta + \lambda_1 C_{it} + \lambda_2 R_{it} + \lambda_3 I_{it} + \nu_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> صكوك تخصص جزءاً من عائدها للوقف المستدام.</div>', unsafe_allow_html=True)
    p3_a = st.slider("Cit (قيمة الصك)", 0, 1000, 500, key="p3_a")
    p3_b = st.slider("Rit (العائد المخصص)", 0, 100, 20, key="p3_b")
    st.metric("مؤشر Wit", f"{(p3_a*0.01 + p3_b*0.5):.2f}")

# [P4] المضاربة الاجتماعية
elif mid == "p4":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"M_{it} = \phi + \rho_1 A_{it} + \rho_2 T_{it} + \rho_3 G_{it} + \epsilon_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> تمويل مشاريع بمضاربة مع تخصيص ربح للتمكين المجتمعي.</div>', unsafe_allow_html=True)
    p4_a = st.slider("Ait (رأس المال)", 0, 1000, 400, key="p4_a")
    p4_b = st.slider("Tit (التدريب)", 0, 100, 90, key="p4_b")
    st.metric("مؤشر Mit", f"{(p4_a*0.01 + p4_b*0.5):.2f}")

# [P5] الصندوق المشترك
elif mid == "p5":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Q_{it} = \psi + \eta_1 V_{it} + \eta_2 D_{it} + \eta_3 B_{it} + \xi_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> صندوق وقفي تمكيني يستخدم الوقف كضمان.</div>', unsafe_allow_html=True)
    p5_a = st.slider("Vit (التمويل)", 0, 1000, 600, key="p5_a")
    p5_b = st.slider("Dit (الضمان)", 0, 100, 100, key="p5_b")
    st.metric("مؤشر Qit", f"{(p5_a*0.02 + p5_b*0.6):.2f}")

# [P6] الإجارة الوقفية
elif mid == "p6":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"H_{it} = \omega + \sigma_1 E_{it} + \sigma_2 Q_{it} + \sigma_3 K_{it} + \varsigma_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> توفير سكن/تعليم عبر أصل وقفي مع حفظ الكرامة.</div>', unsafe_allow_html=True)
    p6_a = st.slider("Eit (الأجرة)", 0, 100, 80, key="p6_a")
    p6_b = st.slider("Kit (الكرامة)", 0, 100, 100, key="p6_b")
    st.metric("مؤشر Hit", f"{(0.5*p6_a + 0.5*p6_b):.2f}")

# [1] الوظيفة الرسالية
elif mid == "m1":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r")
    rr = st.slider("Rr (الرسالة)", 0, 100, 80, key="m1_rr")
    mr = st.slider("Mr (المعنى)", 0, 100, 75, key="m1_mr")
    st.metric("النتيجة", f"{(0.5*rr + 0.5*mr + 10):.2f}")

# [2] القيادة المتزكية
elif mid == "m2":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r")
    zr = st.slider("Zr (التزكية)", 0, 100, 85, key="m2_zr")
    ir = st.slider("Ir (الإلهام)", 0, 100, 90, key="m2_ir")
    st.metric("النتيجة", f"{(0.6*zr + 0.4*ir):.2f}")

# [3] الحوكمة الرمزية
elif mid == "m3":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"G_r = \alpha + \beta_1 N_r + \beta_2 T_r + \beta_3 M_r")
    nr = st.slider("Nr (النزاهة)", 0, 100, 90, key="m3_nr")
    ar = st.slider("Ar (الانسجام)", 0, 100, 85, key="m3_ar")
    st.metric("النتيجة", f"{(0.5*nr + 0.5*ar):.2f}")

# [8] سنة الشكر
elif mid == "m8":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 S + \beta_2 C")
    s8 = st.slider("S (الشكر)", 0, 100, 90, key="m8_s")
    c8 = st.slider("C (الالتزام)", 0, 100, 80, key="m8_c")
    st.metric("معدل النماء", f"{(0.7*s8 + 0.3*c8 + 15):.2f}%")

# [10] سنة التداول
elif mid == "m10":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"GINI_{steward} = \frac{1}{n} \sum (Y_i - \bar{Y}) \cdot \sigma Z")
    yi = st.slider("توزيع الدخل", 0, 100, 75, key="m10_yi")
    zp = st.slider("ضغط الزكاة", 0, 100, 85, key="m10_zp")
    st.metric("مؤشر التداول", f"{(yi * (zp/100)):.2f}")

# [13] سياسة التسعير
elif mid == "m13":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"FBi = \beta_1 PCc - \beta_2 MR + \beta_3 IS")
    pcc = st.slider("الرقابة (PCc)", 0, 100, 80, key="m13_pcc")
    mr = st.slider("الاحتكار (MR)", 0, 100, 20, key="m13_mr")
    st.metric("مؤشر FBi", f"{(0.6*pcc - 0.4*mr + 20):.2f}")

# [26] سعر الصرف
elif mid == "m26":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{fx} = \sqrt{G \cdot S \cdot W}")
    g = st.slider("G (الذهب)", 0, 100, 90, key="m26_g")
    s = st.slider("S (السلع)", 0, 100, 85, key="m26_s")
    st.metric("قوة العملة", f"{(g*s)**0.5:.2f}")

# [27] العائد المقاصدي
elif mid == "m27":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_1 \pi + \alpha_2 T + \alpha_3 Z")
    pi = st.slider("الربح (π)", 0, 100, 75, key="m27_pi")
    t = st.slider("التمكين (T)", 0, 100, 85, key="m27_t")
    st.metric("معدل R %", f"{(0.5*pi + 0.5*t):.2f}")

# [29] تسعير المنتجات
elif mid == "m29":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_b = f(R, T, Z, \pi)")
    rb = st.slider("العائد", 0, 100, 70, key="m29_rb")
    zb = st.slider("معامل الأخلاق", 0, 100, 25, key="m29_zb")
    st.metric("سعر المنتج", f"{(0.6*rb + 0.4*zb + 10):.2f}")

# تذييل
st.sidebar.markdown("---")
st.sidebar.write("© 2026 ابتكار أ.د. صالح عرابي")
