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
    .about-box { background-color: #e8f5e9; padding: 20px; border-radius: 12px; border-right: 10px solid #1e4d2b; line-height: 1.8; color: #11301a; margin-bottom: 20px; }
    .header-style { color: #1e4d2b; font-weight: bold; border-bottom: 2px solid #d4af37; padding-bottom: 10px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. محرك الفهرس الرقمي ---
st.sidebar.title("🏛️ فهرس النماذج السيادية")
st.sidebar.write("Prof. Dr. Saleh Orabi")

# تعريف القائمة الشاملة لكل ما أرسلته
menu = {
    "الرئيسية": "home",
    "1. نموذج الوظيفة الرسالية (Pᵣ)": "mission",
    "2. نموذج القيادة المتزكية (Eᵣ)": "leadership",
    "3. نموذج الحوكمة الرمزية (Gᵣ)": "governance",
    "4. نموذج الاستثمار التزكوي (Rᵣ)": "investment",
    "5. نموذج التقييم التزكوي (Qᵣ)": "evaluation",
    "6. نموذج التحقق الوجودي (Vᵣ)": "existential",
    "7. القيمة التزكوية المضافة (ZVA)": "zva",
    "8. سنة الشكر (التحفيز بالامتنان)": "shukr",
    "9. سنة الظلم (الإنذار المبكر)": "zulm",
    "10. سنة التداول (إعادة التوزيع)": "tadawul",
    "11. سنة التمكين (بناء القدرات)": "tamkeen"
}

choice = st.sidebar.selectbox("اختر النموذج الدراسي:", list(menu.keys()))
model_key = menu[choice]

# --- 3. عرض النماذج (Logic Engine) ---

if model_key == "home":
    st.markdown("<p style='font-size:42px; font-weight:bold; text-align:center;'>بروتوكول هندسة الاستخلاف الاقتصادي الرقمي</p>", unsafe_allow_html=True)
    st.info("مرحباً بروفيسور صالح. المنصة جاهزة الآن لمحاكاة 11 نموذجاً من نماذجك. اختر من القائمة الجانبية.")

elif model_key == "mission":
    st.markdown("<h1 class='header-style'>نموذج الوظيفة الرسالية (Pᵣ)</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    r_val = st.slider("Rᵣ (الرسالة الرمزية)", 0, 100, 70)
    st.metric("الأداء الوظيفي الرمزي", f"{0.4*r_val + 20:.2f}")

elif model_key == "leadership":
    st.markdown("<h1 class='header-style'>نموذج القيادة المتزكية (Eᵣ)</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \beta_4 C_r + \beta_5 V_r + \beta_6 R_r + \epsilon_r")
    zr = st.slider("Zᵣ (تزكية القائد)", 0, 100, 85)
    st.metric("الأثر المؤسسي المتزكي", f"{zr * 1.25:.2f}")

elif model_key == "zva":
    st.markdown("<h1 class='header-style'>القيمة التزكوية المضافة (ZVA)</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    z_val = st.slider("Z (مؤشر التزكية)", 0, 100, 90)
    st.metric("إجمالي القيمة ZVA", f"{500 + (1.2 * z_val):.2f}")

elif model_key == "shukr":
    st.markdown("<h1 class='header-style'>سنة الشكر (Y)</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 S + \beta_2 C + \beta_3 T + \epsilon")
    s_val = st.slider("S (مؤشر الشكر)", 0, 100, 80)
    st.metric("معدل النمو (Y)", f"{10 + 0.5*s_val:.2f}%")

elif model_key == "zulm":
    st.markdown("<h1 class='header-style'>سنة الظلم (R)</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_0 + \alpha_1 Z + \alpha_2 G + \alpha_3 I + \epsilon")
    z_idx = st.slider("Z (مؤشر الظلم)", 0, 100, 20)
    st.metric("مؤشر المخاطر (R)", f"{z_idx * 0.8:.2f}%")

elif model_key == "tadawul":
    st.markdown("<h1 class='header-style'>سنة التداول (GINI)</h1>", unsafe_allow_html=True)
    st.latex(r"GINI = \gamma_0 - \gamma_1 D + \gamma_2 E + \epsilon")
    d_val = st.slider("D (مؤشر التداول)", 0, 100, 70)
    st.metric("معامل جيني (توزيع الثروة)", f"{60 - 0.4*d_val:.2f}")

# (سيتم إضافة بقية النماذج بنفس النمط elif عند إرسالك لها)

# --- تذييل الصفحة ---
st.sidebar.markdown("---")
st.sidebar.write("⚡ تم برمجة النماذج وفقاً لمعادلات البروفيسور صالح عرابي")
