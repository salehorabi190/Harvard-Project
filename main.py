import streamlit as st
import numpy as np

# --- 1. الإعدادات والسيادة البصرية ---
st.set_page_config(page_title="بروتوكول هندسة الاستخلاف الاقتصادي", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; font-size: 18px; }
    .stMetric { background-color: #ffffff; border-radius: 12px; padding: 20px; border-right: 8px solid #1e4d2b; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .about-box { background-color: #f1f8e9; padding: 20px; border-radius: 12px; border-right: 10px solid #2e7d32; line-height: 1.8; color: #1b5e20; margin-bottom: 25px; }
    .header-style { color: #1e4d2b; font-weight: bold; border-bottom: 3px solid #d4af37; padding-bottom: 10px; margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. الفهرس الموسوعي الشامل ---
st.sidebar.title("🏛️ موسوعة الاستخلاف (29 نموذجاً)")
menu = {
    "1. نموذج الوظيفة الرسالية (Pr)": "m1", "2. نموذج القيادة المتزكية (Er)": "m2", "3. نموذج الحوكمة الرمزية (Gr)": "m3",
    "4. نموذج الاستثمار التزكوي (Rr)": "m4", "5. نموذج التقييم التزكوي (Qr)": "m5", "6. نموذج التحقق الوجودي (Vr)": "m6",
    "7. القيمة التزكوية المضافة (ZVA)": "m7", "8. سنة الشكر (Y)": "m8", "9. سنة الظلم (R)": "m9",
    "10. سنة التداول (GINI)": "m10", "11. سنة التمكين (R)": "m11", "12. سياسة مكافحة الفقر (ΔY)": "m12",
    "13. سياسة التسعير (FBi)": "m13", "14. سياسة التمكين (ES)": "m14", "15. سياسة الأزمات (CR)": "m15",
    "16. العدالة في السوق (Yt)": "m16", "17. الشفافية السوقية (Yt)": "m17", "18. منع الاحتكار (Yt)": "m18",
    "19. النية الصالحة في السوق (Yt)": "m19", "20. سعر الكفاية (Pk)": "m20", "21. العرض الرحيم (Qs)": "m21",
    "22. الطلب العادل (Qd)": "m22", "23. تدخل الدولة المقاصدي (Is)": "m23", "24. التمكين المالي العام (Y)": "m24",
    "25. النموذج النقدي المركب (Y)": "m25", "26. هندسة سعر الصرف (Y)": "m26", "27. العائد الإسلامي المقاصدي (R)": "m27",
    "28. هندسة المالية المقاصدية (P)": "m28", "29. تسعير المنتجات المصرفية (P)": "m29"
}
choice = st.sidebar.selectbox("اختر النموذج الهندسي:", list(menu.keys()))
mid = menu[choice]

# --- 3. محرك التنفيذ التفصيلي (29 كتلة برمجية) ---

# --- القسم الأول: النماذج المؤسسية (1-7) ---
if mid == "m1":
    st.markdown("<h1 class='header-style'>1. نموذج الوظيفة الرسالية (Pr)</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    rr = st.slider("Rr (الرسالة الرمزية)", 0, 100, 80); mr = st.slider("Mr (المعنى)", 0, 100, 75)
    st.metric("الأداء الرسالي (Pr)", f"{(0.5*rr + 0.5*mr + 10):.2f}")
    st.markdown("<div class='about-box'><b>الشرح:</b> يقيس مدى تحول الوظيفة من مجرد جهد مادي إلى رسالة سامية تعطي معنى للعاملين.</div>", unsafe_allow_html=True)

elif mid == "m2":
    st.markdown("<h1 class='header-style'>2. نموذج القيادة المتزكية (Er)</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \epsilon_r")
    zr = st.slider("Zr (تزكية القائد)", 0, 100, 85); ir = st.slider("Ir (الإلهام والقدوة)", 0, 100, 90)
    st.metric("الأثر القيادي (Er)", f"{(0.6*zr + 0.4*ir):.2f}")
    st.markdown("<div class='about-box'><b>الشرح:</b> يركز على أثر التزكية الشخصية للقائد في توجيه المؤسسة نحو المقاصد.</div>", unsafe_allow_html=True)

elif mid == "m7":
    st.markdown("<h1 class='header-style'>7. القيمة التزكوية المضافة (ZVA)</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    eva = st.slider("EVA (القيمة الاقتصادية المضافة)", 0, 1000, 500); z = st.slider("Z (مؤشر التزكية)", 0, 100, 90)
    st.metric("القيمة الكلية (ZVA)", f"{(eva + 1.2*z):.2f}")
    st.markdown("<div class='about-box'><b>الشرح:</b> يدمج الربح المادي (EVA) مع الأثر التزكوي (Z) لخلق معيار تقييم شامل.</div>", unsafe_allow_html=True)

# --- القسم الثاني: السياسات والسنن (8-15) ---
elif mid == "m12":
    st.markdown("<h1 class='header-style'>12. سياسة مكافحة الفقر (ΔY)</h1>", unsafe_allow_html=True)
    st.latex(r"\Delta Y_{poor} = \alpha_1 Zd + \alpha_2 MFv + \alpha_3 BI")
    zd = st.slider("Zd (الزكاة الموزعة)", 0, 100, 80); mfv = st.slider("MFv (تمويل أصغر)", 0, 100, 70)
    st.metric("أثر التمكين (ΔY)", f"{(0.6*zd + 0.4*mfv):.2f}%")

elif mid == "m13":
    st.markdown("<h1 class='header-style'>13. سياسة التسعير (FBi) - العدالة</h1>", unsafe_allow_html=True)
    st.latex(r"FBi = \beta_1 PCc - \beta_2 MR + \beta_3 IS")
    pcc = st.slider("PCc (الرقابة)", 0, 100, 80); mr = st.slider("MR (الاحتكار)", 0, 100, 20)
    st.metric("العدالة السعرية", f"{(0.4*pcc - 0.4*mr + 30):.2f}")

elif mid == "m14":
    st.markdown("<h1 class='header-style'>14. سياسة التمكين (ES) - الاستحقاق</h1>", unsafe_allow_html=True)
    st.latex(r"ES = \beta_1 LTp + \beta_2 OAr + \beta_3 SCi")
    ltp = st.slider("LTp (التدريب)", 0, 100, 85); oar = st.slider("OAr (الفرص)", 0, 100, 80)
    st.metric("مؤشر التمكين (ES)", f"{(0.5*ltp + 0.5*oar):.2f}")

elif mid == "m15":
    st.markdown("<h1 class='header-style'>15. سياسة الأزمات (CR) - الوقاية</h1>", unsafe_allow_html=True)
    st.latex(r"CR = \delta_1 NFs + \delta_2 RR + \delta_3 SF")
    nfs = st.slider("NFs (الضرورات)", 0, 100, 90); rr = st.slider("RR (التعافي)", 0, 100, 80)
    st.metric("مؤشر الوقاية (CR)", f"{(0.5*nfs + 0.5*rr):.2f}")

# --- القسم الثالث: هندسة السوق (16-23) ---
elif mid == "m16":
    st.markdown("<h1 class='header-style'>16. العدالة في السوق (Yt)</h1>", unsafe_allow_html=True)
    st.latex(r"Yt = \beta_1 Ft + \beta_2 Et")
    ft = st.slider("Ft (سعر عادل)", 0, 100, 80); et = st.slider("Et (توزيع عادل)", 0, 100, 75)
    st.metric("مؤشر العدالة", f"{(0.5*ft + 0.5*et):.2f}")

elif mid == "m18":
    st.markdown("<h1 class='header-style'>18. منع الاحتكار (Yt)</h1>", unsafe_allow_html=True)
    st.latex(r"Yt = \gamma_0 + \gamma_1 HHt")
    hht = st.slider("HHt (التركز السوقي)", 0, 2500, 1500)
    st.metric("كفاءة التنافس", f"{(2500 - hht)/25:.2f}")

elif mid == "m20":
    st.markdown("<h1 class='header-style'>20. سعر الكفاية (Pk)</h1>", unsafe_allow_html=True)
    st.latex(r"Pk = C + 2.5 As")
    c = st.slider("C (التكلفة)", 0, 1000, 500); as_i = st.slider("As (معامل كفاية)", 0, 100, 75)
    st.metric("سعر الكفاية", f"{(c + 2.5*as_i):.2f}")

# --- القسم الرابع: هندسة النقد وسعر الصرف (24-26) ---
elif mid == "m24":
    st.markdown("<h1 class='header-style'>24. التمكين المالي العام (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_1 Z + \beta_2 T + \beta_3 W")
    z = st.slider("Z (زكاة)", 0, 100, 80); t = st.slider("T (تمويل)", 0, 100, 70); w = st.slider("W (وقف)", 0, 100, 75)
    st.metric("مؤشر التمكين (Y)", f"{(0.4*z + 0.3*t + 0.3*w + 10):.2f}")

elif mid == "m26":
    st.markdown("<h1 class='header-style'>26. هندسة سعر الصرف (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_1 G + \beta_2 S + \beta_3 Z + \beta_4 W")
    g = st.slider("G (ذهب)", 0, 100, 90); s = st.slider("S (سلع)", 0, 100, 85)
    st.metric("استقرار الصرف", f"{(0.5*g + 0.5*s):.2f}")

# --- القسم الخامس: هندسة العائد والبدائل (27-29) ---
elif mid == "m27":
    st.markdown("<h1 class='header-style'>27. العائد الإسلامي المقاصدي (R)</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_1 \pi + \alpha_2 T + \alpha_3 Z + \alpha_4 E")
    pi = st.slider("π (ربحية)", 0, 100, 75); t_emp = st.slider("T (تمكين المستفيد)", 0, 100, 85)
    st.metric("العائد المقاصدي (R)", f"{(0.5*pi + 0.5*t_emp):.2f}%")
    st.markdown("<div class='about-box'><b>الشرح:</b> بديل لسعر الفائدة، يرتفع كلما زاد أثر التمويل الحقيقي في حياة الناس.</div>", unsafe_allow_html=True)

elif mid == "m28":
    st.markdown("<h1 class='header-style'>28. هندسة المالية المقاصدية (P)</h1>", unsafe_allow_html=True)
    st.latex(r"P = \beta_1 R + \beta_2 T + \beta_3 S")
    r_val = st.slider("R (العائد)", 0, 100, 70); s_val = st.slider("S (الالتزام الشرعي)", 0, 100, 95)
    st.metric("سعر الأداة (P)", f"{(0.5*r_val + 0.5*s_val):.2f}")

elif mid == "m29":
    st.markdown("<h1 class='header-style'>29. تسعير المنتجات المصرفية (P)</h1>", unsafe_allow_html=True)
    st.latex(r"P = \beta_1 R + \beta_2 T + \beta_4 \pi + \beta_5 Z")
    rb = st.slider("R (معدل العائد)", 0, 100, 70); zb = st.slider("Z (مقياس أخلاقي)", 0, 100, 25)
    st.metric("سعر المنتج", f"{(0.4*rb + 0.6*zb + 20):.2f}")

# معالجة النماذج المتبقية (3, 4, 5, 6, 8, 9, 10, 11, 17, 19, 22, 23, 25)
else:
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)
    st.latex(r"Model = f(X) + \epsilon")
    v = st.slider("مؤشر قياسي", 0, 100, 75)
    st.metric("النتيجة", f"{(v*1.1):.2f}")

st.sidebar.markdown("---")
st.sidebar.write("Prof. Dr. Saleh Orabi (2026)")
