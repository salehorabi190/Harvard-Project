import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- 1. الإعدادات والسيادة البصرية ---
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
        "usage": "📌 فيما تستخدم هذه المعادلة؟",
        "sidebar_info": "Prof. Dr. Saleh Orabi (2026)"
    },
    "English": {
        "title": "🏛️ Sovereign Stewardship Engineering Protocol",
        "choose": "Choose Research Model:",
        "about": "💡 Philosophy & Engineering Logic",
        "usage": "📌 Model Application:",
        "sidebar_info": "Prof. Dr. Saleh Orabi (2026)"
    }
}
txt = L[st.session_state.lang]

# --- 3. الفهرس (كل النماذج التي أرسلتها مفعلة الآن) ---
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
    "11. سنة التمكين (R)": "s4"
    "11. سنة التمكين (R)": "s4",
    "12. سياسة مكافحة الفقر": "poverty"  # <-- أضف هذا السطر هنا
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
        tr = st.slider("التزكية الزمنية (Tᵣ)", 0, 100, 60)
        cr = st.slider("التواصل الرمزي (Cᵣ)", 0, 100, 65)
        st.metric("Pᵣ", f"{alpha + (0.4*rr) + (0.3*mr) + (0.2*tr) + (0.1*cr):.2f}")
    with c2: st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>التمثيل الوظيفي للرسالة الرمزية للمؤسسة، بحيث تُترجم النية الروحية إلى غايات قابلة للقياس.</div>", unsafe_allow_html=True)

elif model == "m2":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \beta_4 C_r + \beta_5 V_r + \beta_6 R_r + \epsilon_r")
    zr = st.slider("تزكية القائد (Zᵣ)", 0, 100, 85)
    st.metric("Eᵣ", f"{zr * 1.25:.2f}")

elif model == "m3":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"G_r = \alpha + \beta_1 N_r + \beta_2 T_r + \beta_3 M_r + \beta_4 A_r + \epsilon_r")
    ar = st.slider("الانسجام الرمزي (Aᵣ)", 0, 100, 85)
    st.metric("Gᵣ", f"{ar * 0.95:.2f}")

elif model == "m4":
    st.header(choice_key)
    st.latex(r"R_r = \alpha + \beta_1 N_r + \beta_2 Z_r + \beta_3 S_r + \beta_4 E_r + \epsilon_r")
    zr_i = st.slider("تزكية المال (Zᵣ)", 0, 100, 90)
    st.metric("Rᵣ", f"{zr_i * 1.1:.2f}")

elif model == "m5":
    st.header(choice_key)
    st.latex(r"Q_r = \alpha + \beta_1 N_r + \beta_2 Z_r + \beta_3 M_r + \beta_4 C_r + \beta_5 F_r + \epsilon_r")
    fr = st.slider("فاعلية الروح الجماعية (Fᵣ)", 0, 100, 85)
    st.metric("Qᵣ", f"{fr * 1.05:.2f}")

elif model == "m6":
    st.header(choice_key)
    st.latex(r"V_r = \alpha + \beta_1 M_r + \beta_2 P_r + \beta_3 N_r + \beta_4 Z_r + \epsilon_r")
    mr_v = st.slider("المعنى الشخصي (Mᵣ)", 0, 100, 90)
    st.metric("Vᵣ", f"{mr_v * 0.85:.2f}")

elif model == "zva":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    z_val = st.slider("مؤشر التزكية (Z)", 0, 100, 90)
    lam = st.slider("معامل تحويل التزكية (λ)", 0.5, 2.0, 1.2)
    st.metric("ZVA", f"{500 + (lam * z_val):.2f}")

elif model == "s1":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 S + \beta_2 C + \beta_3 T + \epsilon")
    s_val = st.slider("S (مؤشر الشكر المؤسسي)", 0, 100, 80)
    st.metric("Y", f"{10 + 0.5*s_val:.2f}%")

elif model == "s2":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_0 + \alpha_1 Z + \alpha_2 G + \alpha_3 I + \epsilon")
    z_idx = st.slider("Z (مؤشر الظلم)", 0, 100, 25)
    st.metric("R", f"{10 + 0.8*z_idx:.2f}%")

elif model == "s3":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"GINI = \gamma_0 - \gamma_1 D + \gamma_2 E + \epsilon")
    d_val = st.slider("D (مؤشر التداول)", 0, 100, 75)
    st.metric("GINI", f"{60 - 0.4*d_val:.2f}")

elif model == "s4":
    st.markdown(f"<h1 class='header-style'>{choice_key}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \theta_0 + \theta_1 M + \theta_2 S + \theta_3 P + \epsilon")
    m_val = st.slider("M (مؤشر التمكين)", 0, 100, 85)
    st.metric("R (الاستقلال)", f"{m_val * 1.1:.2f}")
# --- نموذج سياسة مكافحة الفقر ---
elif model == "poverty":
    st.markdown(f"<h1 class='header-style'>سياسة مكافحة الفقر</h1>", unsafe_allow_html=True)
    st.latex(r"\Delta Y_{poor} = \alpha_1 Zd + \alpha_2 MFv + \alpha_3 BI")
    
    col1, col2 = st.columns([1.2, 1])
    with col1:
        # المؤشرات من جدول (10) الخاص بك
        zd = st.slider("الزكاة الموزعة (Zd)", 0, 100, 70)
        mfv = st.slider("حجم التمويل الأصغر (MFv)", 0, 100, 65)
        bi = st.slider("مؤشر البركة (BI)", 0, 100, 80)
        
        # حساب النتيجة بناءً على مدخلاتك
        y_poor = (0.5 * zd) + (0.3 * mfv) + (0.2 * bi)
        st.metric("التغير في دخل الفقراء (ΔY poor)", f"{y_poor:.2f}%")
        
    with col2:
        st.markdown(f"""
        <div class='about-box'>
        <b>المقصد: التمكين والرحمة</b><br>
        • Zd: الزكاة الموزعة (Zakat distributed)<br>
        • MFv: حجم التمويل الأصغر (MicroFinance volume)<br>
        • BI: مؤشر البركة (Baraka Index)
        </div>
        """, unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.write(txt["sidebar_info"])
