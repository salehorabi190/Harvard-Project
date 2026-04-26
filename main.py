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

# --- 3. الفهرس الموسوعي الشامل (35 نموذجاً مفصلاً) ---
st.sidebar.header("🏛️ الموسوعة الهندسية الكاملة")
menu = {
    "P1. المشاركة التمكينية المتدرجة": "p1",
    "P2. الإدخار الوقفي الذكي": "p2",
    "P3. الصكوك الوقفية التنموية الذكية": "p3",
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

choice = st.sidebar.selectbox("اختر النموذج الهندسي:", list(menu.keys()))
mid = menu[choice]

# --- 4. محرك التشغيل التفصيلي (الابتكار سطر بسطر) ---

if mid == "p1":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{it} = \alpha + \beta_1 P_{it} + \beta_2 E_{it} + \beta_3 S_{it} + \epsilon_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> تمويل مشاريع للفئات المحرومة بمشاركة متناقصة تبدأ بـ 80% للمصرف حتى يمتلك العميل المشروع بالكامل.</div>', unsafe_allow_html=True)
    p1_pit = st.slider("Pit (نسبة المشاركة التمكينية)", 0, 100, 80, key="p1_pit")
    p1_eit = st.slider("Eit (الأداء الإنتاجي)", 0, 100, 70, key="p1_eit")
    p1_sit = st.slider("Sit (الاستدامة الشرعية)", 0, 100, 85, key="p1_sit")
    st.metric("مؤشر التمكين Yit", f"{(0.4*p1_pit + 0.3*p1_eit + 0.3*p1_sit):.2f}")

elif mid == "p2":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Z_{it} = \gamma + \delta_1 W_{it} + \delta_2 R_{it} + \delta_3 T_{it} + \mu_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> دمج الوقف في منتجات الادخار لتمويل مشاريع التعليم والصحة.</div>', unsafe_allow_html=True)
    p2_wit = st.slider("Wit (نسبة الوقف)", 0, 100, 30, key="p2_wit")
    p2_rit = st.slider("Rit (العائد الوقفي)", 0, 100, 60, key="p2_rit")
    p2_tit = st.slider("Tit (التفاعل الروحي)", 0, 100, 90, key="p2_tit")
    st.metric("مؤشر الأثر Zit", f"{(0.5*p2_wit + 0.3*p2_rit + 0.2*p2_tit):.2f}")

elif mid == "p3":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"W_{it} = \theta + \lambda_1 C_{it} + \lambda_2 R_{it} + \lambda_3 I_{it} + \nu_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> صكوك وقفية ذكية؛ المستثمر يشارك في الربح وجزء من العائد مخصص للوقف الدائم.</div>', unsafe_allow_html=True)
    p3_cit = st.slider("Cit (قيمة الصك)", 0, 1000, 500, key="p3_cit")
    p3_rit = st.slider("Rit (العائد للوقف)", 0, 100, 20, key="p3_rit")
    p3_iit = st.slider("Iit (الأثر التنموي)", 0, 100, 80, key="p3_iit")
    st.metric("مؤشر الأثر Wit", f"{(0.01*p3_cit + 0.4*p3_rit + 0.5*p3_iit):.2f}")

elif mid == "p4":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"M_{it} = \phi + \rho_1 A_{it} + \rho_2 T_{it} + \rho_3 G_{it} + \epsilon_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> تمويل بمضاربة اجتماعية؛ جزء من الأرباح يخصص للتمكين (تدريب ودعم تقني).</div>', unsafe_allow_html=True)
    p4_ait = st.slider("Ait (رأس المال)", 0, 1000, 400, key="p4_ait")
    p4_tit = st.slider("Tit (التدريب والدعم)", 0, 100, 90, key="p4_tit")
    p4_git = st.slider("Git (أرباح التمكين)", 0, 100, 20, key="p4_git")
    st.metric("مؤشر التمكين Mit", f"{(0.01*p4_ait + 0.5*p4_tit + 0.4*p4_git):.2f}")

elif mid == "p5":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Q_{it} = \psi + \eta_1 V_{it} + \eta_2 D_{it} + \eta_3 B_{it} + \xi_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> صندوق وقفي مشترك يجمع أموال الوقف كضمان لتمويل الفئات المحرومة.</div>', unsafe_allow_html=True)
    p5_vit = st.slider("Vit (التمويل)", 0, 1000, 600, key="p5_vit")
    p5_dit = st.slider("Dit (الضمان الوقفي)", 0, 100, 100, key="p5_dit")
    p5_bit = st.slider("Bit (أرباح الوقف)", 0, 100, 30, key="p5_bit")
    st.metric("مؤشر الأثر Qit", f"{(0.02*p5_vit + 0.6*p5_dit + 0.3*p5_bit):.2f}")

elif mid == "p6":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"H_{it} = \omega + \sigma_1 E_{it} + \sigma_2 Q_{it} + \sigma_3 K_{it} + \varsigma_{it}")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> توفير منفعة سكنية أو تعليمية عبر أصل وقفي مع الحفاظ على الكرامة (Kit).</div>', unsafe_allow_html=True)
    p6_eit = st.slider("Eit (الأجرة)", 0, 100, 80, key="p6_eit")
    p6_qit = st.slider("Qit (جودة المنفعة)", 0, 100, 95, key="p6_qit")
    p6_kit = st.slider("Kit (مؤشر الكرامة)", 0, 100, 100, key="p6_kit")
    st.metric("مؤشر التمكين Hit", f"{(0.3*p6_eit + 0.3*p6_qit + 0.4*p6_kit):.2f}")

elif mid == "m1":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> نموذج الوظيفة الرسالية لقياس تحول العمل إلى رسالة وجودية.</div>', unsafe_allow_html=True)
    m1_rr = st.slider("Rr (الرسالة)", 0, 100, 80, key="m1_rr")
    m1_mr = st.slider("Mr (المعنى)", 0, 100, 75, key="m1_mr")
    st.metric("النتيجة", f"{(0.5*m1_rr + 0.5*m1_mr + 10):.2f}")

elif mid == "m2":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \epsilon_r")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> قياس أثر القيادة المتزكية وإلهام القائد.</div>', unsafe_allow_html=True)
    m2_zr = st.slider("Zr (التزكية)", 0, 100, 85, key="m2_zr")
    m2_ir = st.slider("Ir (الإلهام)", 0, 100, 90, key="m2_ir")
    st.metric("النتيجة", f"{(0.6*m2_zr + 0.4*m2_ir):.2f}")

elif mid == "m3":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"G_r = \alpha + \beta_1 N_r + \beta_2 T_r + \beta_3 M_r + \beta_4 A_r + \epsilon_r")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> نموذج الحوكمة الرمزية والانسجام المقاصدي.</div>', unsafe_allow_html=True)
    m3_nr = st.slider("Nr (النزاهة)", 0, 100, 90, key="m3_nr")
    m3_ar = st.slider("Ar (الانسجام)", 0, 100, 85, key="m3_ar")
    st.metric("النتيجة", f"{(0.5*m3_nr + 0.5*m3_ar):.2f}")

elif mid == "m7":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> القيمة التزكوية المضافة (الربح + البركة).</div>', unsafe_allow_html=True)
    m7_eva = st.slider("EVA (الاقتصادي)", 0, 1000, 500, key="m7_eva")
    m7_z = st.slider("Z (التزكية)", 0, 100, 90, key="m7_z")
    st.metric("ZVA", f"{(m7_eva + 1.5*m7_z):.2f}")

elif mid == "m8":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 S + \beta_2 C + \epsilon")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سنة الشكر كمحرك للنمو المستدام.</div>', unsafe_allow_html=True)
    m8_s = st.slider("S (الشكر)", 0, 100, 90, key="m8_s")
    m8_c = st.slider("C (الالتزام)", 0, 100, 80, key="m8_c")
    st.metric("معدل النماء", f"{(0.7*m8_s + 0.3*m8_c + 15):.2f}%")

elif mid == "m9":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_0 + \alpha_1 Z + \alpha_2 G + \epsilon")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سنة الظلم ومؤشر مخاطر الانهيار.</div>', unsafe_allow_html=True)
    m9_z = st.slider("Z (الظلم)", 0, 100, 30, key="m9_z")
    m9_g = st.slider("G (الغرور)", 0, 100, 40, key="m9_g")
    st.metric("مخاطر الانهيار", f"{(0.8*m9_z + 0.2*m9_g):.2f}")

elif mid == "m10":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"GINI_{steward} = \frac{1}{n} \sum (Y_i - \bar{Y}) \cdot \sigma Z")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سنة التداول لضبط توزيع الثروة بمعامل الزكاة.</div>', unsafe_allow_html=True)
    m10_yi = st.slider("توزيع الدخل", 0, 100, 75, key="m10_yi")
    m10_zp = st.slider("ضغط الزكاة", 0, 100, 85, key="m10_zp")
    st.metric("مؤشر التداول", f"{(m10_yi * (m10_zp/100)):.2f}")

elif mid == "m11":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R_e = K_h + K_s + K_e")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سنة التمكين وتراكم القوى البشرية والإيمانية.</div>', unsafe_allow_html=True)
    m11_kh = st.slider("رأس مال بشري", 0, 100, 80, key="m11_kh")
    m11_ke = st.slider("رأس مال إيماني", 0, 100, 90, key="m11_ke")
    st.metric("مؤشر التمكين", f"{(m11_kh + m11_ke)/2:.2f}")

elif mid == "m13":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"FBi = \beta_1 PCc - \beta_2 MR + \beta_3 IS")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سياسة التسعير العادل وضبط الاحتكار.</div>', unsafe_allow_html=True)
    m13_pcc = st.slider("الرقابة (PCc)", 0, 100, 80, key="m13_pcc")
    m13_mr = st.slider("الاحتكار (MR)", 0, 100, 20, key="m13_mr")
    st.metric("مؤشر FBi", f"{(0.6*m13_pcc - 0.4*m13_mr + 20):.2f}")

elif mid == "m14":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"ES = \beta_1 LTp + \beta_2 OAr + \beta_3 SCi")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سياسة التمكين والاستحقاق التزكوي.</div>', unsafe_allow_html=True)
    m14_ltp = st.slider("التدريب (LTp)", 0, 100, 85, key="m14_ltp")
    m14_sci = st.slider("رأس المال الاجتماعي", 0, 100, 70, key="m14_sci")
    st.metric("مؤشر ES", f"{(0.4*m14_ltp + 0.6*m14_sci):.2f}")

elif mid == "m15":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"CR = \delta_1 NFs + \delta_2 RR + \delta_3 SF")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سياسة الأزمات وفقه الضرورة.</div>', unsafe_allow_html=True)
    m15_nfs = st.slider("الضرورات (NFs)", 0, 100, 95, key="m15_nfs")
    m15_rr = st.slider("التعافي (RR)", 0, 100, 80, key="m15_rr")
    st.metric("مؤشر CR", f"{(0.7*m15_nfs + 0.3*m15_rr):.2f}")

elif mid == "m20":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_k = C + (A_s \times 2.5\%)")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سعر الكفاية المرتبط بالتكلفة ومعامل الأمان الاجتماعي.</div>', unsafe_allow_html=True)
    m20_c = st.number_input("التكلفة الفعلية C", value=100, key="m20_c")
    m20_as = st.slider("معامل الكفاية As", 0, 100, 80, key="m20_as")
    st.metric("سعر الكفاية", f"{m20_c + (m20_as * 0.025 * m20_c):.2f}")

elif mid == "m26":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{fx} = \sqrt{G \cdot S \cdot W}")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> هندسة سعر الصرف السيادي عبر الأصول الحقيقية.</div>', unsafe_allow_html=True)
    m26_g = st.slider("الذهب (G)", 0, 100, 90, key="m26_g")
    m26_s = st.slider("السلع (S)", 0, 100, 85, key="m26_s")
    st.metric("قوة العملة", f"{(m26_g*m26_s)**0.5:.2f}")

elif mid == "m27":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_1 \pi + \alpha_2 T + \alpha_3 Z + \alpha_4 E")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> العائد المقاصدي البديل للفائدة الربوية.</div>', unsafe_allow_html=True)
    m27_pi = st.slider("الربح (π)", 0, 100, 75, key="m27_pi")
    m27_t = st.slider("التمكين (T)", 0, 100, 85, key="m27_t")
    st.metric("معدل R %", f"{(0.5*m27_pi + 0.5*m27_t):.2f}")

elif mid == "m29":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_b = f(R, T, Z, \pi)")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> تسعير المنتجات المصرفية وفق منطق الاستخلاف.</div>', unsafe_allow_html=True)
    m29_rb = st.slider("العائد المتوقع", 0, 100, 70, key="m29_rb")
    m29_zb = st.slider("معامل الأخلاق", 0, 100, 25, key="m29_zb")
    st.metric("سعر المنتج", f"{(0.6*m29_rb + 0.4*m29_zb + 10):.2f}")

st.sidebar.markdown("---")
st.sidebar.write("© 2026 ابتكار أ.د. صالح عرابي")
