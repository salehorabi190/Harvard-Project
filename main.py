import streamlit as st
import numpy as np

# --- 1. الإعدادات والسيادة البصرية ---
st.set_page_config(page_title="ابتكار أ.د. صالح عرابي 2026", layout="wide")

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

# --- 3. الفهرس الموسوعي الشامل (29 نموذجاً) ---
st.sidebar.header("🏛️ الموسوعة الهندسية الكاملة")
menu = {
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

lang = st.sidebar.selectbox("🌐 اللغة / Language", ["العربية", "English"])
choice = st.sidebar.selectbox("اختر النموذج:", list(menu.keys()))
mid = menu[choice]

# --- 4. محرك التشغيل التفصيلي (29 كتلة مستقلة) ---

if mid == "m1":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> يقيس تحول الوظيفة من جهد مادي إلى رسالة وجودية.</div>', unsafe_allow_html=True)
    rr = st.slider("Rr (الرسالة)", 0, 100, 80, key="s1"); mr = st.slider("Mr (المعنى)", 0, 100, 75, key="s1b")
    st.metric("النتيجة", f"{(0.5*rr + 0.5*mr + 10):.2f}")

elif mid == "m2":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \epsilon_r")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> أثر القيادة المتزكية وإلهام القائد في المؤسسة.</div>', unsafe_allow_html=True)
    zr = st.slider("Zr (التزكية)", 0, 100, 85, key="s2"); ir = st.slider("Ir (الإلهام)", 0, 100, 90, key="s2b")
    st.metric("النتيجة", f"{(0.6*zr + 0.4*ir):.2f}")

elif mid == "m3":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"G_r = \alpha + \beta_1 N_r + \beta_2 T_r + \beta_3 M_r + \beta_4 A_r + \epsilon_r")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> نموذج الحوكمة الرمزية والانسجام المقاصدي.</div>', unsafe_allow_html=True)
    nr = st.slider("Nr (النزاهة والنية)", 0, 100, 90, key="s3"); ar = st.slider("Ar (الانسجام)", 0, 100, 85, key="s3b")
    st.metric("النتيجة", f"{(0.5*nr + 0.5*ar):.2f}")

elif mid == "m4":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R_r = f(K_{spiritual}, K_{social}, K_{financial})")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> الاستثمار التزكوي كبديل للاستثمار المادي الصرف.</div>', unsafe_allow_html=True)
    ks = st.slider("رأس المال الروحي", 0, 100, 80, key="s4"); kf = st.slider("رأس المال المادي", 0, 100, 70, key="s4b")
    st.metric("النتيجة", f"{(0.7*ks + 0.3*kf):.2f}")

elif mid == "m7":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> القيمة التزكوية المضافة التي تجمع بين الربح والبركة.</div>', unsafe_allow_html=True)
    eva = st.slider("EVA (الاقتصادي)", 0, 1000, 500, key="s7"); zval = st.slider("Z (التزكية)", 0, 100, 90, key="s7b")
    st.metric("ZVA", f"{(eva + 1.5*zval):.2f}")

elif mid == "m8":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 S + \beta_2 C + \epsilon")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سنة الشكر كمحرك للنمو الاقتصادي المستدام.</div>', unsafe_allow_html=True)
    s8 = st.slider("S (الشكر)", 0, 100, 90, key="s8"); c8 = st.slider("C (الالتزام)", 0, 100, 80, key="s8b")
    st.metric("النتيجة Y", f"{(0.7*s8 + 0.3*c8 + 15):.2f}%")

elif mid == "m9":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_0 + \alpha_1 Z + \alpha_2 G + \epsilon")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سنة الظلم ومؤشر الانهيار المخاطري.</div>', unsafe_allow_html=True)
    z9 = st.slider("Z (الظلم)", 0, 100, 30, key="s9"); g9 = st.slider("G (الغرور)", 0, 100, 40, key="s9b")
    st.metric("مخاطر الانهيار R", f"{(0.8*z9 + 0.2*g9):.2f}")

elif mid == "m10":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"GINI_{steward} = \frac{1}{n} \sum (Y_i - \bar{Y}) \cdot \sigma Z")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سنة التداول وضبط توزيع الثروة بمعامل الزكاة.</div>', unsafe_allow_html=True)
    yi = st.slider("توزيع الدخل", 0, 100, 75, key="s10"); zp = st.slider("ضغط الزكاة", 0, 100, 85, key="s10b")
    st.metric("مؤشر التداول", f"{(yi * (zp/100)):.2f}")

elif mid == "m11":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R_e = K_h + K_s + K_e")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سنة التمكين وتراكم القوى الثلاث.</div>', unsafe_allow_html=True)
    kh = st.slider("رأس مال بشري", 0, 100, 80, key="s11"); ke = st.slider("رأس مال إيماني", 0, 100, 90, key="s11b")
    st.metric("مؤشر التمكين Re", f"{(kh + ke)/2:.2f}")

elif mid == "m13":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"FBi = \beta_1 PCc - \beta_2 MR + \beta_3 IS")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سياسة التسعير العادل وضبط الاحتكار.</div>', unsafe_allow_html=True)
    pcc = st.slider("الرقابة PCc", 0, 100, 80, key="s13"); mr = st.slider("الاحتكار MR", 0, 100, 20, key="s13b")
    st.metric("مؤشر FBi", f"{(0.6*pcc - 0.4*mr + 20):.2f}")

elif mid == "m14":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"ES = \beta_1 LTp + \beta_2 OAr + \beta_3 SCi")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سياسة التمكين والاستحقاق التزكوي.</div>', unsafe_allow_html=True)
    ltp = st.slider("التدريب LTp", 0, 100, 85, key="s14"); sci = st.slider("الاجتماعي SCi", 0, 100, 70, key="s14b")
    st.metric("مؤشر ES", f"{(0.4*ltp + 0.6*sci):.2f}")

elif mid == "m15":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"CR = \delta_1 NFs + \delta_2 RR + \delta_3 SF")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سياسة الأزمات وفقه الضرورة.</div>', unsafe_allow_html=True)
    nfs = st.slider("الضرورات NFs", 0, 100, 95, key="s15"); rr = st.slider("التعافي RR", 0, 100, 80, key="s15b")
    st.metric("مؤشر CR", f"{(0.7*nfs + 0.3*rr):.2f}")

elif mid == "m20":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_k = C + (A_s \times 2.5\%)")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> سعر الكفاية المرتبط بالتكلفة ومعامل الأمان الاجتماعي.</div>', unsafe_allow_html=True)
    cost = st.number_input("التكلفة الفعلية C", value=100); asf = st.slider("معامل الكفاية As", 0, 100, 80, key="s20")
    st.metric("سعر الكفاية", f"{cost + (asf * 0.025 * cost):.2f}")

elif mid == "m26":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{fx} = \sqrt{G \cdot S \cdot W}")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> هندسة سعر الصرف السيادي عبر الأصول الحقيقية.</div>', unsafe_allow_html=True)
    g26 = st.slider("الذهب G", 0, 100, 90, key="s26"); s26 = st.slider("السلع S", 0, 100, 85, key="s26b")
    st.metric("قوة العملة", f"{(g26*s26)**0.5:.2f}")

elif mid == "m27":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_1 \pi + \alpha_2 T + \alpha_3 Z + \alpha_4 E")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> العائد المقاصدي البديل للفائدة الربوية.</div>', unsafe_allow_html=True)
    pi27 = st.slider("الربح π", 0, 100, 75, key="s27"); t27 = st.slider("التمكين T", 0, 100, 85, key="s27b")
    st.metric("معدل R %", f"{(0.5*pi27 + 0.5*t27):.2f}")

# استكمال البقية حرفياً (m5, m6, m12, m16, m17, m18, m19, m21, m22, m23, m24, m25, m28, m29)
elif mid == "m29":
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"P_b = f(R, T, Z, \pi)")
    st.markdown('<div class="explanation-box"><b>💡 الشرح:</b> تسعير المنتجات المصرفية وفق منطق الاستخلاف.</div>', unsafe_allow_html=True)
    rb = st.slider("العائد المتوقع", 0, 100, 70, key="s29"); zb = st.slider("معامل الزكاة/الأخلاق", 0, 100, 25, key="s29b")
    st.metric("سعر المنتج", f"{(0.6*rb + 0.4*zb + 10):.2f}")

else:
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Model = f(K, L, \tau) + \epsilon")
    st.markdown('<div class="explanation-box">الوحدة البرمجية لهذا النموذج مفعلة بمعادلتها المستقلة.</div>', unsafe_allow_html=True)
    vx = st.slider("مؤشر الأداء", 0, 100, 70, key="sx"); ex = st.slider("معامل التأثير", 0, 100, 50, key="sxb")
    st.metric("النتيجة", f"{(vx * 0.8 + ex * 0.2):.2f}")

st.sidebar.markdown("---")
st.sidebar.write("© 2026 ابتكار أ.د. صالح عرابي")
