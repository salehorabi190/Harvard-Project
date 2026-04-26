import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- 1. إعدادات الهوية السيادية ---
st.set_page_config(page_title="بروتوكول هندسة الاستخلاف الاقتصادي الرقمي", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; }
    .stMetric { background-color: #ffffff; border-radius: 12px; padding: 20px; border-right: 8px solid #1e4d2b; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .about-box { background-color: #f1f8e9; padding: 20px; border-radius: 12px; border-right: 10px solid #2e7d32; line-height: 1.8; color: #1b5e20; margin-bottom: 20px; }
    .header-style { color: #1b5e20; font-weight: bold; border-bottom: 2px solid #d4af37; padding-bottom: 10px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. نظام اللغات ---
if 'lang' not in st.session_state: st.session_state.lang = "العربية"
st.sidebar.title("🌐 Language / اللغة")
st.session_state.lang = st.sidebar.radio("", ["العربية", "English"], index=0 if st.session_state.lang == "العربية" else 1)

L = {
    "العربية": {
        "choose": "اختر مجال الدراسة:",
        "about": "💡 التفسير الفلسفي والهندسي",
        "sidebar_info": "Prof. Dr. Saleh Orabi (2026)",
        "mission": "1. الوظيفة الرسالية (Pᵣ)",
        "leadership": "2. القيادة المتزكية (Eᵣ)",
        "zva": "3. القيمة التزكوية المضافة (ZVA)",
        "shukr": "4. سنة الشكر (التحفيز)",
        "zulm": "5. سنة الظلم (الإنذار المبكر)",
        "tadawul": "6. سنة التداول (إعادة التوزيع)",
        "tamkeen": "7. سنة التمكين (بناء القدرة)"
    },
    "English": {
        "choose": "Choose Model:",
        "about": "💡 Philosophy & Engineering",
        "sidebar_info": "Prof. Dr. Saleh Orabi (2026)",
        "mission": "1. Mission-Driven Function (Pᵣ)",
        "leadership": "2. Tazkiyah Leadership (Eᵣ)",
        "zva": "3. Tazkiyah Value Added (ZVA)",
        "shukr": "4. Law of Shukr (Growth)",
        "zulm": "5. Law of Zulm (Risk)",
        "tadawul": "6. Law of Circulation (Tadawul)",
        "tamkeen": "7. Law of Empowerment (Tamkeen)"
    }
}
txt = L[st.session_state.lang]

# --- 3. الفهرس السيادي ---
st.sidebar.title(txt["choose"])
menu_options = [txt["mission"], txt["leadership"], txt["zva"], txt["shukr"], txt["zulm"], txt["tadawul"], txt["tamkeen"]]
choice = st.sidebar.selectbox("", menu_options)

# --- 4. محرك النماذج (Logic Engine) ---

# 1. الوظيفة الرسالية
if choice == txt["mission"]:
    st.markdown(f"<h1 class='header-style'>{txt['mission']}</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    col1, col2 = st.columns([1.2, 1])
    with col1:
        rr = st.slider("الرسالة الرمزية (Rᵣ)", 0, 100, 70)
        mr = st.slider("المعنى والانتماء (Mᵣ)", 0, 100, 75)
        st.metric("الأداء الوظيفي الرمزي", f"{0.4*rr + 0.3*mr + 15:.2f}")
    with col2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>تستخدم لتقليل تكاليف الرقابة عبر رفع الوازع القيمي والرسالة.</div>", unsafe_allow_html=True)

# 2. القيادة المتزكية
elif choice == txt["leadership"]:
    st.markdown(f"<h1 class='header-style'>{txt['leadership']}</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \beta_4 C_r + \epsilon_r")
    zr = st.slider("تزكية القائد (Zᵣ)", 0, 100, 85)
    st.metric("الأثر المؤسسي المتزكي", f"{zr * 1.25:.2f}")

# 3. القيمة المضافة (ZVA)
elif choice == txt["zva"]:
    st.markdown(f"<h1 class='header-style'>{txt['zva']}</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    z_val = st.slider("مؤشر التزكية (Z)", 0, 100, 90)
    st.metric("إجمالي القيمة ZVA", f"{500 + (1.2 * z_val):.2f}")

# 4. سنة الشكر
elif choice == txt["shukr"]:
    st.markdown(f"<h1 class='header-style'>{txt['shukr']}</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 S + \beta_2 C + \beta_3 T + \epsilon")
    s_val = st.slider("S (مؤشر الشكر المؤسسي)", 0, 100, 80)
    st.metric("الإنتاجية / النمو (Y)", f"{10 + 0.5*s_val:.2f}%")
    st.markdown(f"<div class='about-box'>تحفيز تنموي بالامتنان؛ زيادة الشكر تؤدي لزيادة الموارد.</div>", unsafe_allow_html=True)

# 5. سنة الظلم
elif choice == txt["zulm"]:
    st.markdown(f"<h1 class='header-style'>{txt['zulm']}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_0 + \alpha_1 Z + \alpha_2 G + \alpha_3 I + \epsilon")
    z_idx = st.slider("Z (مؤشر الظلم - احتكار وفساد)", 0, 100, 25)
    risk = (0.8 * z_idx) + 10
    st.metric("مؤشر المخاطر والانهيار (R)", f"{risk:.2f}%", delta="تنبيه" if risk > 50 else "آمن", delta_color="inverse")
    st.markdown(f"<div class='about-box'>الإنذار المبكر؛ الظلم الاقتصادي هو المحرك الأول للانهيار.</div>", unsafe_allow_html=True)

# 6. سنة التداول
elif choice == txt["tadawul"]:
    st.markdown(f"<h1 class='header-style'>{txt['tadawul']}</h1>", unsafe_allow_html=True)
    st.latex(r"GINI = \gamma_0 - \gamma_1 D + \gamma_2 E + \epsilon")
    d_val = st.slider("D (مؤشر التداول - زكاة وأوقاف)", 0, 100, 75)
    st.metric("معامل جيني (توزيع الثروة)", f"{60 - 0.4*d_val:.2f}")

# 7. سنة التمكين
elif choice == txt["tamkeen"]:
    st.markdown(f"<h1 class='header-style'>{txt['tamkeen']}</h1>", unsafe_allow_html=True)
    st.latex(r"R = \theta_0 + \theta_1 M + \theta_2 S + \theta_3 P + \epsilon")
    m_val = st.slider("M (مؤشر التمكين - تعليم وملكية)", 0, 100, 85)
    st.metric("الاستقلال والازدهار", f"{m_val * 1.15:.2f}")

st.sidebar.markdown("---")
st.sidebar.write(txt["sidebar_info"])
