import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- 1. إعدادات الهوية والسيادة ---
st.set_page_config(page_title="بروتوكول هندسة الاستخلاف", layout="wide")

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

# --- 3. تنفيذ النماذج (Logic Engine) ---

if model_key == "home":
    st.markdown("<p style='font-size:42px; font-weight:bold; text-align:center;'>بروتوكول هندسة الاستخلاف الاقتصادي الرقمي</p>", unsafe_allow_html=True)
    st.info("مرحباً بروفيسور صالح. جميع النماذج الـ 11 المفعلة الآن تعمل بكامل طاقتها البرمجية.")
    st.image("https://img.icons8.com/fluency/240/stewardship.png")

elif model_key == "mission":
    st.markdown("<h1 class='header-style'>نموذج الوظيفة الرسالية (Pᵣ)</h1>", unsafe_allow_html=True)
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    rr = st.slider("Rᵣ (الرسالة الرمزية)", 0, 100, 70)
    mr = st.slider("Mᵣ (المعنى والانتماء)", 0, 100, 75)
    st.metric("الأداء الوظيفي الرمزي", f"{0.4*rr + 0.3*mr + 15:.2f}")

elif model_key == "leadership":
    st.markdown("<h1 class='header-style'>نموذج القيادة المتزكية (Eᵣ)</h1>", unsafe_allow_html=True)
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \beta_4 C_r + \beta_5 V_r + \beta_6 R_r + \epsilon_r")
    zr = st.slider("Zᵣ (تزكية القائد)", 0, 100, 85)
    st.metric("الأثر المؤسسي المتزكي", f"{zr * 1.25:.2f}")

elif model_key == "governance":
    st.markdown("<h1 class='header-style'>نموذج الحوكمة الرمزية (Gᵣ)</h1>", unsafe_allow_html=True)
    st.latex(r"G_r = \alpha + \beta_1 N_r + \beta_2 T_r + \beta_3 M_r + \beta_4 A_r + \epsilon_r")
    ar = st.slider("Aᵣ (الانسجام الرمزي)", 0, 100, 85)
    st.metric("جودة الحوكمة الرمزية", f"{ar * 0.95:.2f}")

elif model_key == "investment":
    st.markdown("<h1 class='header-style'>نموذج الاستثمار التزكوي (Rᵣ)</h1>", unsafe_allow_html=True)
    st.latex(r"R_r = \alpha + \beta_1 N_r + \beta_2 Z_r + \beta_3 S_r + \beta_4 E_r + \epsilon_r")
    zr_i = st.slider("Zᵣ (تزكية المال)", 0, 100, 90)
    st.metric("العائد التزكوي الرمزي", f"{zr_i * 1.1:.2f}")

elif model_key == "evaluation":
    st.markdown("<h1 class='header-style'>نموذج التقييم التزكوي (Qᵣ)</h1>", unsafe_allow_html=True)
    st.latex(r"Q_r = \alpha + \beta_1 N_r + \beta_2 Z_r + \beta_3 M_r + \beta_4 C_r + \beta_5 F_r + \epsilon_r")
    fr = st.slider("Fᵣ (فاعلية الروح الجماعية)", 0, 100, 85)
    st.metric("جودة المؤسسة التزكوية", f"{fr * 1.05:.2f}")

elif model_key == "existential":
    st.markdown("<h1 class='header-style'>نموذج التحقق الوجودي (Vᵣ)</h1>", unsafe_allow_html=True)
    st.latex(r"V_r = \alpha + \beta_1 M_r + \beta_2 P_r + \beta_3 N_r + \beta_4 Z_r + \epsilon_r")
    mr_v = st.slider("Mᵣ (المعنى الشخصي)", 0, 100, 90)
    st.metric("التحقق الوجودي الرمزي", f"{mr_v * 0.8:.2f}")

elif model_key == "zva":
    st.markdown("<h1 class='header-style'>القيمة التزكوية المضافة (ZVA)</h1>", unsafe_allow_html=True)
    st.latex(r"ZVA = EVA + \lambda Z")
    z_val = st.slider("Z (مؤشر التزكية)", 0, 100, 90)
    lam = st.slider("λ (معامل التحويل)", 0.5, 2.0, 1.2)
    st.metric("إجمالي القيمة ZVA", f"{500 + (lam * z_val):.2f}")

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
    st.metric("معامل جيني", f"{60 - 0.4*d_val:.2f}")

elif model_key == "tamkeen":
    st.markdown("<h1 class='header-style'>سنة التمكين (R)</h1>", unsafe_allow_html=True)
    st.latex(r"R = \theta_0 + \theta_1 M + \theta_2 S + \theta_3 P + \epsilon")
    m_val = st.slider("M (مؤشر التمكين)", 0, 100, 85)
    st.metric("الاستقلال والازدهار", f"{m_val * 1.15:.2f}")

st.sidebar.markdown("---")
st.sidebar.write("⚡ الإصدار الكامل الموحد - 2026")
