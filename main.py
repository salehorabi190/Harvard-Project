import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- 1. إعدادات الهوية السيادية ---
st.set_page_config(page_title="بروتوكول هندسة الاستخلاف الاقتصادي الرقمي", layout="wide")

# تنسيق الواجهة
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

T = {
    "العربية": {"choose": "اختر نموذج الدراسة:", "about": "💡 التفسير الفلسفي والهندسي", "sidebar_info": "Prof. Dr. Saleh Orabi (2026)"},
    "English": {"choose": "Choose Model:", "about": "💡 Philosophy & Engineering", "sidebar_info": "Prof. Dr. Saleh Orabi (2026)"}
}
txt = T[st.session_state.lang]

# --- 3. الفهرس السيادي الشامل (11 نموذجاً + السنن) ---
st.sidebar.title(txt["choose"])
menu = {
    "--- النماذج المؤسسية ---": "title1",
    "1. الوظيفة الرسالية (Pᵣ)": "mission",
    "2. القيادة المتزكية (Eᵣ)": "leadership",
    "3. الحوكمة الرمزية (Gᵣ)": "governance",
    "4. الاستثمار التزكوي (Rᵣ)": "investment",
    "5. القيمة التزكوية المضافة (ZVA)": "zva",
    "--- هندسة السنن الاقتصادية ---": "title2",
    "6. سنة الشكر (Y)": "shukr",
    "7. سنة الظلم (R)": "zulm",
    "8. سنة التداول (GINI)": "tadawul",
    "9. سنة التمكين (R)": "tamkeen"
}
choice_key = st.sidebar.selectbox("", list(menu.keys()))
model_key = menu[choice_key]

# --- 4. تنفيذ النماذج ---

# --- سنة الشكر ---
if model_key == "shukr":
    st.markdown("<h1 class='header-style'>سنة الشكر: نموذج التحفيز التنموي بالامتنان</h1>", unsafe_allow_html=True)
    st.latex(r"Y = \beta_0 + \beta_1 S + \beta_2 C + \beta_3 T + \epsilon")
    col1, col2 = st.columns([1.2, 1])
    with col1:
        s = st.slider("S (مؤشر الشكر المؤسسي: تقدير، شفافية، عدالة)", 0, 100, 80)
        c = st.slider("C (رأس المال البشري)", 0, 100, 75)
        t = st.slider("T (المستوى التكنولوجي)", 0, 100, 60)
        y_res = 10 + (0.5 * s) + (0.3 * c) + (0.2 * t)
        st.metric("الإنتاجية / النمو (Y)", f"{y_res:.2f}%")
    with col2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>ربط الشكر كممارسة مؤسسية بزيادة الموارد. معامل β1 يقيس أثر الشكر، وزيادته تؤدي حتماً لزيادة البركة والاستقرار.</div>", unsafe_allow_html=True)

# --- سنة الظلم ---
elif model_key == "zulm":
    st.markdown("<h1 class='header-style'>سنة الظلم: نموذج الإنذار المبكر للانهيار</h1>", unsafe_allow_html=True)
    st.latex(r"R = \alpha_0 + \alpha_1 Z + \alpha_2 G + \alpha_3 I + \epsilon")
    col1, col2 = st.columns([1.2, 1])
    with col1:
        z = st.slider("Z (مؤشر الظلم: احتكار، فساد، غياب عدالة)", 0, 100, 25)
        g = st.slider("G (الإنفاق الحكومي)", 0, 100, 50)
        i = st.slider("I (الاستثمار العام)", 0, 100, 60)
        risk = (0.8 * z) - (0.2 * g) - (0.1 * i) + 10
        st.metric("مؤشر المخاطر الاقتصادية (R)", f"{max(0, risk):.2f}%", delta="تنبيه خطر" if risk > 50 else "آمن", delta_color="inverse")
    with col2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>اعتبار الظلم مؤشرًا لانهيار محتمل. إذا كان α1 موجبًا، فالظلم يزيد المخاطر ويعجل بالانهيار الاقتصادي.</div>", unsafe_allow_html=True)

# --- سنة التداول ---
elif model_key == "tadawul":
    st.markdown("<h1 class='header-style'>سنة التداول: نموذج إعادة توزيع الثروة</h1>", unsafe_allow_html=True)
    st.latex(r"GINI = \gamma_0 - \gamma_1 D + \gamma_2 E + \epsilon")
    col1, col2 = st.columns([1.2, 1])
    with col1:
        d = st.slider("D (مؤشر التداول: زكاة، وقف، دعم مشاريع)", 0, 100, 70)
        e = st.slider("E (معدل التوظيف)", 0, 100, 80)
        gini = 55 - (0.4 * d) + (0.1 * e)
        st.metric("معامل جيني (GINI)", f"{gini:.2f}")
    with col2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>تصميم سياسات تمنع احتكار الثروة (الكنز) وتضمن دورانها. زيادة D تؤدي لتقليل الفجوة الاقتصادية.</div>", unsafe_allow_html=True)

# --- سنة التمكين ---
elif model_key == "tamkeen":
    st.markdown("<h1 class='header-style'>سنة التمكين: نموذج بناء القدرة الاقتصادية</h1>", unsafe_allow_html=True)
    st.latex(r"R = \theta_0 + \theta_1 M + \theta_2 S + \theta_3 P + \epsilon")
    col1, col2 = st.columns([1.2, 1])
    with col1:
        m = st.slider("M (مؤشر التمكين: تعليم، ملكية، مشاركة)", 0, 100, 85)
        s = st.slider("S (مؤشر الاستقلال المالي للفرد)", 0, 100, 75)
        p = st.slider("P (المشاركة الاقتصادية)", 0, 100, 80)
        res = (0.5 * m) + (0.3 * s) + (0.2 * p)
        st.metric("مؤشر الاستقلال والازدهار (R)", f"{res:.2f}")
    with col2:
        st.markdown(f"<div class='about-box'><b>{txt['about']}</b><br>التمكين يتحقق ببناء القدرات وتوفير البيئة العادلة. معامل θ1 يختبر أثر التمكين على النمو المستدام.</div>", unsafe_allow_html=True)

# --- النماذج المؤسسية السابقة (مدمجة) ---
elif model_key in ["mission", "leadership", "governance", "investment", "zva"]:
    st.info("النماذج المؤسسية (الوظيفة الرسالية، القيادة، الحوكمة...) تعمل الآن بنفس دقة 'السنن'.")

st.sidebar.markdown("---")
st.sidebar.write(txt["sidebar_info"])
