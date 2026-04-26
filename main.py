import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- 1. إعدادات والسيادة البصرية ---
st.set_page_config(page_title="بروتوكول هندسة الاستخلاف الاقتصادي الرقمي", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; }
    .stMetric { background-color: #ffffff; border-radius: 12px; padding: 20px; border-right: 8px solid #1e4d2b; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .about-box { background-color: #e8f5e9; padding: 20px; border-radius: 12px; border-right: 10px solid #1e4d2b; line-height: 1.8; color: #11301a; margin-bottom: 20px; }
    .header-style { color: #1e4d2b; font-weight: bold; border-bottom: 2px solid #d4af37; padding-bottom: 10px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. نظام اللغات ---
if 'lang' not in st.session_state: st.session_state.lang = "العربية"
st.sidebar.title("🌐 Language / اللغة")
st.session_state.lang = st.sidebar.radio("", ["العربية", "English"], index=0 if st.session_state.lang == "العربية" else 1)

L = {
    "العربية": {
        "title": "🏛️ بروتوكول هندسة الاستخلاف الاقتصادي الرقمي",
        "choose": "اختر نموذج الدراسة:",
        "about": "💡 التفسير الفلسفي والهندسي للموديل",
        "sidebar_info": "Prof. Dr. Saleh Orabi (2026)"
    },
    "English": {
        "title": "🏛️ Sovereign Stewardship Engineering Protocol",
        "choose": "Choose Research Model:",
        "about": "💡 Philosophy & Engineering Logic",
        "sidebar_info": "Prof. Dr. Saleh Orabi (2026)"
    }
}
txt = L[st.session_state.lang]

# --- 3. الفهرس الشامل ---
st.sidebar.title(txt["choose"])
menu = {
    "1. نموذج الوظيفة الرسالية (Pᵣ)": "m1",
    "2. نموذج القيادة المتزكية (Eᵣ)": "m2",
    "3. نموذج الحوكمة الرمزية (Gᵣ)": "m3",
    "4. نموذج الاستثمار التزكوي (Rᵣ)": "m4",
    "5. نموذج التقييم التزكوي (Qᵣ)": "m5",
    "6. نموذج التحقق الوجودي (Vᵣ)": "m6",
    "7. القيمة التزكوية المضافة (ZVA)": "zva",
    "8. سنة الشكر (Y)": "s1",
    "9. سنة الظلم (R)": "s2",
    "10. سنة التداول (GINI)": "s3",
    "11. سنة التمكين (R)": "s4",
    "12. سياسة مكافحة الفقر": "poverty",
    "13. سياسة التسعير": "pricing",
    "14. سياسة التمكين القيادي": "empower_policy",
    "15. سياسة الأزمات": "crisis",
    "16. العدالة في السوق": "m_justice",
    "17. الشفافية السوقية": "m_transparency",
    "18. منع الاحتكار": "m_monopoly",
    "19. النية الصالحة في السوق": "m_intention"
}
choice_key = st.sidebar.selectbox("", list(menu.keys()))
model = menu[choice_key]

# --- 4. محرك التنفيذ ---

if model == "m1":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    c1, c2 = st.columns([1.2, 1])
    with c1:
        alpha = st.slider("النية الداخلية (α)", 0.0, 1.0, 0.8)
        rr = st.slider("الرسالة الرمزية (Rᵣ)", 0, 100, 70)
        mr = st.slider("المعنى والانتماء (Mᵣ)", 0, 100, 75)
        st.metric("Pᵣ", f"{alpha + (0.4*rr) + (0.3*mr) + 15:.2f}")
    with c2: st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>التمثيل الوظيفي للرسالة الرمزية للمؤسسة.</div>", unsafe_allow_html=True)

elif model == "m2":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \beta_4 C_r + \epsilon_r")
    zr = st.slider("تزكية القائد (Zᵣ)", 0, 100, 85)
    st.metric("Eᵣ", f"{zr * 1.25:.2f}")

elif model == "zva":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    z_val = st.slider("مؤشر التزكية (Z)", 0, 100, 90)
    st.metric("ZVA", f"{500 + (1.2 * z_val):.2f}")

elif model == "s1":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 S + \beta_2 C + \beta_3 T + \epsilon")
    s_val = st.slider("S (مؤشر الشكر المؤسسي)", 0, 100, 80)
    st.metric("Y", f"{10 + 0.5*s_val:.2f}%")

elif model == "poverty":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"\Delta Y_{poor} = \alpha_1 Zd + \alpha_2 MFv + \alpha_3 BI")
    zd = st.slider("الزكاة الموزعة (Zd)", 0, 100, 70)
    mfv = st.slider("التمويل الأصغر (MFv)", 0, 100, 65)
    bi = st.slider("مؤشر البركة (BI)", 0, 100, 80)
    st.metric("ΔY poor", f"{(0.5*zd + 0.3*mfv + 0.2*bi):.2f}%")

elif model == "pricing":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"FBi = \beta_1 PCc - \beta_2 MR + \beta_3 IS")
    pcc = st.slider("ضبط الأسعار (PCc)", 0, 100, 75)
    mr = st.slider("معدل الاحتكار (MR)", 0, 100, 20)
    is_score = st.slider("مؤشر النية (IS)", 0, 100, 85)
    st.metric("FBi", f"{(0.4*pcc - 0.4*mr + 0.2*is_score):.2f}")

elif model == "empower_policy":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"ES = \beta_1 LTp + \beta_2 OAr + \beta_3 SCi")
    ltp = st.slider("التدريب (LTp)", 0, 100, 80)
    st.metric("ES", f"{(ltp * 1.1):.2f}")

elif model == "crisis":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"CR = \delta_1 NFs + \delta_2 RR + \delta_3 SF")
    nfs = st.slider("فقه الضرورة (NFs)", 0, 100, 85)
    st.metric("CR", f"{(nfs * 1.2):.2f}")

elif model == "m_justice":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_t = \beta_0 + \beta_1 Ft + \beta_2 Tt + \beta_3 At + \beta_4 Et + \epsilon_t")
    ft = st.slider("العدالة السعرية (Ft)", 0, 100, 80)
    st.metric("Yt", f"{ft * 0.9:.2f}")

elif model == "m_transparency":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_t = \alpha_0 + \alpha_1 Dt + \alpha_2 Ct + \alpha_3 It + \alpha_4 AFt + \mu_t")
    dt = st.slider("الإفصاح السعري (Dt)", 0, 100, 85)
    st.metric("Yt", f"{dt * 0.95:.2f}")

elif model == "m_monopoly":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_t = \gamma_0 + \gamma_1 HHt + \gamma_2 ACt + \gamma_3 RIt + \gamma_4 AMt + \nu_t")
    hht = st.slider("التركز السوقي (HHt)", 0, 2500, 1500)
    st.metric("Yt", f"{2500 - hht:.2f}")

elif model == "m_intention":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"Y_t = \delta_0 + \delta_1 GIt + \delta_2 APt + \delta_3 CCt + \delta_4 NDt + \xi_t")
    gi = st.slider("النية الصالحة (GIt)", 0, 100, 90)
    st.metric("Yt", f"{gi * 1.1:.2f}")

# إضافة الحوكمة والتقييم والتحقق الوجودي والسنن لضمان عمل الفهرس بالكامل
elif model == "m3":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.metric("Gᵣ", "85.00")
elif model == "m4":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.metric("Rᵣ", "90.00")
elif model == "m5":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.metric("Qᵣ", "88.00")
elif model == "m6":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.metric("Vᵣ", "92.00")
elif model == "s2":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.metric("R", "15.00%")
elif model == "s3":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.metric("GINI", "0.35")
elif model == "s4":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.metric("R", "80.00")

st.sidebar.markdown("---")
st.sidebar.write(txt["sidebar_info"])
