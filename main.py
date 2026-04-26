import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- 1. إعدادات الهوية السيادية ---
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
st.sidebar.title("🏛️ النماذج التطبيقية والمؤسساتية")
st.sidebar.write("Prof. Dr. Saleh Orabi")

menu = {
    "1. نموذج الوظيفة الرسالية (Pᵣ)": "mission",
    "2. نموذج القيادة المتزكية (Eᵣ)": "leadership",
    "3. نموذج الحوكمة الرمزية (Gᵣ)": "governance",
    "4. نموذج الاستثمار التزكوي (Rᵣ)": "investment",
    "5. نموذج التقييم التزكوي (Qᵣ)": "evaluation",
    "6. نموذج التحقق الوجودي (Vᵣ)": "existential"
}

choice = st.sidebar.selectbox("اختر النموذج الدراسي:", list(menu.keys()))
model_key = menu[choice]

# --- 3. عرض النماذج ---

# --- أولاً: نموذج الوظيفة الرسالية ---
if model_key == "mission":
    st.markdown("<h1 class='header-style'>نموذج الوظيفة الرسالية (The Mission-Driven Function)</h1>", unsafe_allow_html=True)
    st.markdown("<div class='about-box'>هي التمثيل الوظيفي للرسالة الرمزية للمؤسسة، بحيث تُترجم النية الروحية إلى غايات قابلة للقياس.</div>", unsafe_allow_html=True)
    
    st.latex(r"P_r = \alpha + \beta_1 R_r + \beta_2 M_r + \beta_3 T_r + \beta_4 C_r + \epsilon_r")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("المؤشرات الرمزية")
        alpha = st.slider("α (النية الداخلية - صدق التوجه)", 0.0, 1.0, 0.8)
        rr = st.slider("Rᵣ (الرسالة الرمزية - ارتباط الفرد بالرسالة)", 0, 100, 70)
        mr = st.slider("Mᵣ (المعنى والانتماء - الحماس الداخلي)", 0, 100, 75)
        tr = st.slider("Tᵣ (التزكية الزمنية - النمو الروحي والمهني)", 0, 100, 60)
        cr = st.slider("Cᵣ (التواصل الرمزي - استخدام اللغة الرمزية)", 0, 100, 65)
        er = st.number_input("εᵣ (الأثر غير المرئي - البركة والتوفيق)", 0.0, 10.0, 5.0)

    with col2:
        performance = alpha + (0.4 * rr) + (0.3 * mr) + (0.2 * tr) + (0.1 * cr) + er
        st.metric("الأداء الوظيفي الرمزي (Pᵣ)", f"{performance:.2f}")
        
        fig = go.Figure(go.Bar(
            x=['Rᵣ', 'Mᵣ', 'Tᵣ', 'Cᵣ', 'εᵣ'],
            y=[0.4*rr, 0.3*mr, 0.2*tr, 0.1*cr, er],
            marker_color='#1e4d2b'
        ))
        fig.update_layout(title="تحليل مساهمة المؤشرات الرمزية في الأداء")
        st.plotly_chart(fig)

# --- ثانياً: نموذج القيادة المتزكية ---
elif model_key == "leadership":
    st.markdown("<h1 class='header-style'>نموذج القيادة المتزكية (Tazkiyah-Based Leadership)</h1>", unsafe_allow_html=True)
    st.markdown("<div class='about-box'>نمط قيادي يستند إلى النية الروحية، ويُفعّل قيم التزكية في اتخاذ القرار وتوجيه المؤسسة نحو غايات رمزية.</div>", unsafe_allow_html=True)
    
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \beta_4 C_r + \beta_5 V_r + \beta_6 R_r + \epsilon_r")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        alpha_l = st.slider("α (النية التأسيسية - صفاء الهدف)", 0.0, 1.0, 0.9)
        zr = st.slider("Zᵣ (تزكية القائد - وضوح البوصلة)", 0, 100, 85)
        ir = st.slider("Iᵣ (الإلهام الرمزي - استخدام القصص)", 0, 100, 80)
        vr = st.slider("Vᵣ (توافق القيم - انسجام القائد)", 0, 100, 75)
        st.metric("النية التأسيسية", f"{alpha_l}")

    with col2:
        # وزن تقديري للمؤشرات
        impact = alpha_l + (zr*0.25) + (ir*0.2) + (vr*0.15) + 10 # 10 قيمة افتراضية لبقية الرموز
        st.metric("الأثر المؤسسي المتزكي (Eᵣ)", f"{impact:.2f}")
        
        categories = ['Tazkiyah', 'Inspiration', 'Values', 'Mission', 'Meaning']
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(r=[zr, ir, vr, 70, 80], theta=categories, fill='toself', line_color='#d4af37'))
        st.plotly_chart(fig_radar)

# --- ثالثاً: نموذج الحوكمة الرمزية ---
elif model_key == "governance":
    st.markdown("<h1 class='header-style'>نموذج الحوكمة الرمزية (Symbolic Governance)</h1>", unsafe_allow_html=True)
    st.latex(r"G_r = \alpha + \beta_1 N_r + \beta_2 T_r + \beta_3 M_r + \beta_4 A_r + \epsilon_r")
    
    ar = st.slider("Aᵣ (الانسجام الرمزي - غياب التناقضات الرمزية)", 0, 100, 85)
    tr_g = st.slider("Tᵣ (قيم الحوكمة - تجسيد القيم في النظام)", 0, 100, 70)
    
    g_score = (ar * 0.6) + (tr_g * 0.4)
    st.metric("جودة الحوكمة الرمزية (Gᵣ)", f"{g_score:.2f}")
    st.info("الانسجام الرمزي هو مفتاح جودة الحوكمة، حيث تتلاشى الفجوة بين المعلن والممارسة.")

# --- رابعاً: نموذج الاستثمار التزكوي ---
elif model_key == "investment":
    st.header("نموذج الاستثمار التزكوي (Rᵣ)")
    st.latex(r"R_r = \alpha + \beta_1 N_r + \beta_2 Z_r + \beta_3 S_r + \beta_4 E_r + \epsilon_r")
    
    zr_i = st.slider("Zᵣ (تزكية المال - تطهيره من الشبهات)", 0, 100, 90)
    sr_i = st.slider("Sᵣ (رسالة الاستثمار - وضوح المقصد)", 0, 100, 80)
    
    return_r = (zr_i * 0.5) + (sr_i * 0.5)
    st.metric("العائد التزكوي الرمزي (Rᵣ)", f"{return_r:.2f}")

# --- خامساً: نموذج التقييم التزكوي ---
elif model_key == "evaluation":
    st.header("نموذج التقييم التزكوي للمؤسسات (Qᵣ)")
    st.latex(r"Q_r = \alpha + \beta_1 N_r + \beta_2 Z_r + \beta_3 M_r + \beta_4 C_r + \beta_5 F_r + \epsilon_r")
    
    fr = st.slider("Fᵣ (فاعلية الروح الجماعية - انسجام الفريق)", 0, 100, 85)
    zr_h = st.slider("Zᵣ (تزكية الهيكل - تطهير النظام الإداري)", 0, 100, 75)
    
    q_score = (fr * 0.4) + (zr_h * 0.3) + 20
    st.metric("جودة المؤسسة التزكوية (Qᵣ)", f"{q_score:.2f}")

# --- سادساً: نموذج التحقق الوجودي ---
elif model_key == "existential":
    st.header("نموذج التحقق الوجودي في بيئة العمل (Vᵣ)")
    st.latex(r"V_r = \alpha + \beta_1 M_r + \beta_2 P_r + \beta_3 N_r + \beta_4 Z_r + \epsilon_r")
    
    mr_v = st.slider("Mᵣ (المعنى الشخصي - قيمة العمل للفرد)", 0, 100, 90)
    nr_v = st.slider("Nᵣ (نية الفرد - وضوح الاستحضار اليومي)", 0, 100, 85)
    
    v_score = (mr_v * 0.5) + (nr_v * 0.5)
    st.metric("التحقق الوجودي الرمزي (Vᵣ)", f"{v_score:.2f}")
# --- 1. إضافة الرموز إلى القاموس ---
# (يتم إضافتها في قسم القائمة الجانبية في الكود السابق)
menu["7. القيمة التزكوية المضافة (ZVA)"] = "zva"

# --- 2. كود نموذج ZVA ---
elif model_key == "zva":
    st.markdown("<h1 class='header-style'>القيمة التزكوية المضافة (Tazkiyah Value Added - ZVA)</h1>", unsafe_allow_html=True)
    st.markdown("<div class='about-box'>ZVA: مفهوم جديد يُعيد تعريف القيمة لتمتد من الربح المادي إلى تحقيق المعنى والانسجام والنية الصافية في كل عملية اقتصادية.</div>", unsafe_allow_html=True)

    # عرض المعادلات الأساسية
    st.latex(r"EVA = \alpha F + \beta C + \gamma M + \delta Z + \epsilon")
    st.latex(r"ZVA = EVA + \lambda Z")

    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("مدخلات القيمة الاقتصادية (EVA)")
        f_val = st.slider("F (الفاعلية المؤسسية - الإنجاز المتناغم)", 0, 100, 70)
        c_val = st.slider("C (رأس المال البشري - المعنى الشخصي)", 0, 100, 75)
        m_val = st.slider("M (معنوية المؤسسة - الأثر الرمزي)", 0, 100, 80)
        
        st.markdown("---")
        st.subheader("المحرك التزكوي")
        z_val = st.slider("Z (مؤشر التزكية - نية + انسجام + روح)", 0, 100, 90)
        lambda_coeff = st.slider("λ (معامل تحويل التزكية إلى قيمة)", 0.5, 2.0, 1.2)

    with col2:
        # حساب EVA افتراضي (تبسيطاً للمعادلة القياسية)
        eva_calc = (0.3 * f_val) + (0.3 * c_val) + (0.2 * m_val) + (0.2 * z_val)
        # حساب ZVA
        zva_calc = eva_calc + (lambda_coeff * z_val)
        
        st.metric("القيمة الاقتصادية التقليدية (EVA)", f"{eva_calc:.2f}")
        st.metric("القيمة التزكوية المضافة (ZVA)", f"{zva_calc:.2f}", delta=f"{(lambda_coeff * z_val):.2f} أثر التزكية (λZ)")

        # رسم بياني للمقارنة
        fig_zva = go.Figure()
        fig_zva.add_trace(go.Bar(
            name='القيم التقليدية',
            x=['EVA'], y=[eva_calc],
            marker_color='#d4af37'
        ))
        fig_zva.add_trace(go.Bar(
            name='القيمة التزكوية المضافة',
            x=['ZVA'], y=[zva_calc],
            marker_color='#1e4d2b'
        ))
        fig_zva.update_layout(title="المقارنة بين القيمة المادية والقيمة التزكوية", barmode='group')
        st.plotly_chart(fig_zva)

    st.markdown("""
    <div class='about-box'>
    <b>ملاحظات نقدية (Critical Remarks):</b><br>
    • التزكية ليست بديلاً عن الأداء الاقتصادي بل هي مُعزز ومسرع له.<br>
    • λ يعكس قدرة المؤسسة (أو الدولة) على تحويل النوايا والقيم إلى أثر مادي ملموس.<br>
    • هذا النموذج قابل للتطبيق في <b>رؤية مصر 2030</b> لدمج مفاهيم التنمية المتوازنة.
    </div>
    """, unsafe_allow_html=True)
# --- تذييل الصفحة ---
st.sidebar.markdown("---")
st.sidebar.write("⚡ تم برمجة النماذج وفقاً لمعادلات البروفيسور صالح عرابي")
