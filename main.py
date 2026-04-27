import streamlit as st
import numpy as np

# --- 1. الإعدادات والسيادة البصرية (ابتكار أ.د. صالح عرابي) ---
st.set_page_config(page_title="SEP 2026 | ابتكار أ.د. صالح عرابي", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&family=Playfair+Display:wght@700&display=swap');
    .stApp { background-color: #f4f7f6; }
    .logo-container { text-align: center; padding: 30px; background: linear-gradient(135deg, #1e4d2b 0%, #11301a 100%); border-radius: 20px; border-bottom: 8px solid #d4af37; margin-bottom: 30px; color: white; box-shadow: 0 10px 25px rgba(0,0,0,0.3); }
    .logo-text { font-family: 'Playfair Display', serif; font-size: 50px; letter-spacing: 3px; }
    .explanation-box { background-color: #ffffff; padding: 25px; border-radius: 15px; border-right: 12px solid #2e7d32; color: #1b5e20; line-height: 1.8; margin-bottom: 25px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); font-family: 'Cairo', sans-serif; }
    .header-style { color: #1e4d2b; font-family: 'Cairo', sans-serif; font-weight: bold; border-bottom: 3px solid #d4af37; padding-bottom: 10px; margin-bottom: 25px; text-align: right; }
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

# --- 3. الفهرس الموسوعي الكامل (35 نموذجاً مفصلاً) ---
st.sidebar.header("🏛️ القائمة الهندسية الكاملة")
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

# --- 4. محرك التشغيل (الـ 35 نموذجاً مفصلاً) ---

if mid == "p1":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{it} = \alpha + \beta_1 P_{it} + \beta_2 E_{it} + \beta_3 S_{it} + \epsilon_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الفكرة:</b> تمويل مشاريع للفئات المحرومة بمشاركة متناقصة.</div>', unsafe_allow_html=True)
    p1a = st.slider("Pit (نسبة المشاركة التمكينية)", 0, 100, 80, key="p1a")
    p1b = st.slider("Eit (الأداء الإنتاجي)", 0, 100, 70, key="p1b")
    p1c = st.slider("Sit (الاستدامة الشرعية)", 0, 100, 90, key="p1c")
    st.metric("مؤشر التمكين Yit", f"{(0.4*p1a + 0.3*p1b + 0.3*p1c):.2f}")

elif mid == "p2":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Z_{it} = \gamma + \delta_1 W_{it} + \delta_2 R_{it} + \delta_3 T_{it} + \mu_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الفكرة:</b> دمج الوقف في منتجات الادخار لتمويل مشاريع تنموية.</div>', unsafe_allow_html=True)
    p2a = st.slider("Wit (نسبة الوقف من الادخار)", 0, 100, 30, key="p2a")
    p2b = st.slider("Rit (عائد الاستثمار الوقفي)", 0, 100, 60, key="p2b")
    p2c = st.slider("Tit (التفاعل الروحي)", 0, 100, 85, key="p2c")
    st.metric("مؤشر الأثر الوقفي Zit", f"{(0.5*p2a + 0.3*p2b + 0.2*p2c):.2f}")

elif mid == "p3":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"W_{it} = \theta + \lambda_1 C_{it} + \lambda_2 R_{it} + \lambda_3 I_{it} + \nu_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الفكرة:</b> صكوك وقفية ذكية؛ يشارك المستثمر في الربح ويخصص جزء للوقف.</div>', unsafe_allow_html=True)
    p3a = st.slider("Cit (قيمة الصك)", 0, 1000, 500, key="p3a")
    p3b = st.slider("Rit (العائد المخصص للوقف)", 0, 100, 20, key="p3b")
    p3c = st.slider("Iit (الأثر التنموي)", 0, 100, 80, key="p3c")
    st.metric("الأثر الوقفي Wit", f"{(p3a*0.01 + p3b*0.4 + p3c*0.5):.2f}")

elif mid == "p4":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"M_{it} = \phi + \rho_1 A_{it} + \rho_2 T_{it} + \rho_3 G_{it} + \epsilon_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الفكرة:</b> تمويل مشاريع للفقراء بصيغة مضاربة اجتماعية تمكينية.</div>', unsafe_allow_html=True)
    p4a = st.slider("Ait (رأس المال)", 0, 1000, 400, key="p4a")
    p4b = st.slider("Tit (الدعم الفني والتدريب)", 0, 100, 90, key="p4b")
    p4c = st.slider("Git (نسبة أرباح التمكين)", 0, 100, 25, key="p4c")
    st.metric("التمكين الاجتماعي Mit", f"{(p4a*0.02 + p4b*0.4 + p4c*0.4):.2f}")

elif mid == "p5":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Q_{it} = \psi + \eta_1 V_{it} + \eta_2 D_{it} + \eta_3 B_{it} + \xi_{it}")
    p5a = st.slider("Vit (قيمة التمويل)", 0, 1000, 600, key="p5a")
    p5b = st.slider("Dit (الضمان الوقفي)", 0, 100, 100, key="p5b")
    p5c = st.slider("Bit (أرباح الوقف)", 0, 100, 30, key="p5c")
    st.metric("الأثر Qit", f"{(p5a*0.02 + p5b*0.5 + p5c*0.3):.2f}")

elif mid == "p6":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"H_{it} = \omega + \sigma_1 E_{it} + \sigma_2 Q_{it} + \sigma_3 K_{it} + \varsigma_{it}")
    p6a = st.slider("Eit (الأجرة)", 0, 100, 80, key="p6a")
    p6b = st.slider("Qit (جودة المنفعة)", 0, 100, 95, key="p6b")
    p6c = st.slider("Kit (مؤشر الكرامة)", 0, 100, 100, key="p6c")
    st.metric("التمكين الوقفي Hit", f"{(0.3*p6a + 0.3*p6b + 0.4*p6c):.2f}")

elif mid == "m1":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r")
    m1_r = st.slider("Rr (الرسالة)", 0, 100, 80, key="m1a")
    m1_m = st.slider("Mr (المعنى)", 0, 100, 75, key="m1b")
    st.metric("مؤشر Pr", f"{(0.5*m1_r + 0.5*m1_m + 10):.2f}")

elif mid == "m2":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r")
    m2_z = st.slider("Zr (التزكية)", 0, 100, 85, key="m2a")
    m2_i = st.slider("Ir (الإلهام)", 0, 100, 90, key="m2b")
    st.metric("مؤشر Er", f"{(0.6*m2_z + 0.4*m2_i):.2f}")

elif mid == "m3":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"G_r = \alpha + \beta_1 N_r + \beta_2 T_r + \beta_3 M_r")
    m3_n = st.slider("Nr (النزاهة)", 0, 100, 90, key="m3a")
    m3_a = st.slider("Ar (الانسجام)", 0, 100, 85, key="m3b")
    st.metric("مؤشر Gr", f"{(0.5*m3_n + 0.5*m3_a):.2f}")

elif mid == "m4":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R_r = f(K_{spirit}, K_{social}, K_{fin})")
    m4_s = st.slider("رأس مال روحي", 0, 100, 90, key="m4a")
    m4_f = st.slider("رأس مال مادي", 0, 100, 60, key="m4b")
    st.metric("جدوى Rr", f"{(0.7*m4_s + 0.3*m4_f):.2f}")

elif mid == "m5":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Q_r = \sum Maqasid / \sum Resources")
    m5_q = st.slider("المقاصد", 0, 100, 80, key="m5a")
    m5_r = st.slider("الموارد", 1, 100, 50, key="m5b")
    st.metric("كفاءة Qr", f"{(m5_q/m5_r):.2f}")

elif mid == "m7":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    m7_e = st.slider("القيمة الاقتصادية", 0, 1000, 500, key="m7a")
    m7_z = st.slider("معامل التزكية", 0, 100, 90, key="m7b")
    st.metric("النتيجة ZVA", f"{(m7_e + 1.5*m7_z):.2f}")

elif mid == "m8":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 S + \beta_2 C")
    m8_s = st.slider("S (الشكر)", 0, 100, 90, key="m8a")
    m8_c = st.slider("C (الالتزام)", 0, 100, 80, key="m8b")
    st.metric("نماء Y", f"{(0.7*m8_s + 0.3*m8_c + 15):.2f}%")

elif mid == "m9":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_0 + \alpha_1 Z + \alpha_2 G")
    m9_z = st.slider("Z (الظلم)", 0, 100, 30, key="m9a")
    m9_g = st.slider("G (الغرور)", 0, 100, 40, key="m9b")
    st.metric("مخاطر R", f"{(0.8*m9_z + 0.2*m9_g):.2f}")

elif mid == "m10":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"GINI = \frac{1}{n} \sum (Y_i - \bar{Y}) \cdot Z")
    m10_y = st.slider("توزيع الدخل", 0, 100, 75, key="m10a")
    m10_z = st.slider("ضغط الزكاة", 0, 100, 85, key="m10b")
    st.metric("مؤشر التداول", f"{(m10_y * m10_z / 100):.2f}")

elif mid == "m11":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R_e = K_h + K_s + K_e")
    m11_h = st.slider("بشري", 0, 100, 80, key="m11a")
    m11_e = st.slider("إيماني", 0, 100, 90, key="m11b")
    st.metric("تمكين Re", f"{(m11_h + m11_e)/2:.2f}")

elif mid == "m13":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"FBi = \beta_1 PCc - \beta_2 MR")
    m13_p = st.slider("الرقابة", 0, 100, 80, key="m13a")
    m13_m = st.slider("الاحتكار", 0, 100, 20, key="m13b")
    st.metric("عدالة FBi", f"{(0.6*m13_p - 0.4*m13_m + 20):.2f}")

elif mid == "m20":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_k = C + (A_s \times 2.5\%)")
    m20_c = st.number_input("التكلفة", value=100, key="m20a")
    m20_s = st.slider("معامل الكفاية", 0, 100, 80, key="m20b")
    st.metric("سعر Pk", f"{m20_c + (m20_s * 0.025 * m20_c):.2f}")

elif mid == "m26":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{fx} = \sqrt{G \cdot S \cdot W}")
    m26_g = st.slider("ذهب", 0, 100, 90, key="m26a")
    m26_s = st.slider("سلع", 0, 100, 85, key="m26b")
    st.metric("قوة العملة", f"{(m26_g * m26_s)**0.5:.2f}")

elif mid == "m27":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_1 \pi + \alpha_2 T + \alpha_3 Z")
    m27_p = st.slider("ربح", 0, 100, 75, key="m27a")
    m27_t = st.slider("تمكين", 0, 100, 85, key="m27b")
    st.metric("معدل R %", f"{(0.5*m27_p + 0.5*m27_t):.2f}")

elif mid == "m29":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_b = 0.6 R + 0.4 Z")
    m29_r = st.slider("العائد", 0, 100, 70, key="m29a")
    m29_z = st.slider("الأخلاق", 0, 100, 25, key="m29b")
    st.metric("سعر المنتج", f"{(0.6*m29_r + 0.4*m29_z + 10):.2f}")

else:
    st.markdown(f"<h1 class='header-style'>{choice
