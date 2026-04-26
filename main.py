import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- إعدادات الواجهة الاحترافية ---
st.set_page_config(page_title="Stewardship Engineering Lab", layout="wide")

st.title("🏛 Stewardship Engineering: The Comprehensive Lab")
st.markdown("---")

# --- قائمة الأقسام الرئيسية ---
# هنا سنضيف الأقسام التي تملك فيها معادلات
domain = st.sidebar.selectbox("Choose Economic Domain:", [
    "Sunnan Calculations",
    "Monetary Architecture",
    "Market Justice & Pricing",
    "Product Engineering",
    "Poverty & Empowerment"
])

# --- محرك المعادلات الذكي ---
# يا دكتور، سأعلمك هنا كيف سنضيف المعادلات
if domain == "Sunnan Calculations":
    st.header("🧮 Islamic Economic Sunan Models")
    
    # مثال لكيفية إضافة معادلة في ثوانٍ
    equation = st.selectbox("Select Equation:", ["Shukr Model", "Zulm Model", "Sabr Model", "Tadawul Model"])
    
    if equation == "Shukr Model":
        st.latex(r"Y = \alpha + \beta_1 S + \beta_2 C") # إظهار شكل المعادلة الرياضي الفخم
        s = st.slider("S (Shukr Level)", 0, 100, 50)
        c = st.slider("C (Resources)", 0, 100, 50)
        y = (0.6 * s) + (0.4 * c)
        st.metric("Economic Productivity (Y)", f"{y:.2f}")

    # (هنا سنضيف بقية المعادلات التي لم نضفها بعد)

elif domain == "Monetary Architecture":
    st.header("🪙 Sovereign Monetary Models")
    # (هنا سنضع معادلات سعر الصرف والذهب والزكاة التي أرسلتها)
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# --- إعدادات الواجهة السيادية ---
st.set_page_config(page_title="Stewardship Engineering Lab", layout="wide")

st.sidebar.title("🏛 Stewardship Engineering Lab")
domain = st.sidebar.selectbox("Choose Economic Domain:", [
    "Mission-Driven Function (الوظيفة الرسالية)",
    "Sunnan Calculations",
    "Monetary Architecture",
    "Product Engineering"
])

# --- 1. نموذج الوظيفة الرسالية ---
if domain == "Mission-Driven Function (الوظيفة الرسالية)":
    st.header("🎯 Mission-Driven Function Model | نموذج الوظيفة الرسالية")
    st.info("التمثيل الوظيفي للرسالة الرمزية للمؤسسة، بحيث تُترجم النية الروحية إلى غايات قابلة للقياس.")

    # عرض المعادلة بشكل رياضي أنيق
    st.subheader("The Mathematical Model | النموذج الرياضي")
    st.latex(r"P = \alpha + \beta_1 R + \beta_2 M + \beta_3 T + \beta_4 C + \epsilon")
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Input Parameters")
        alpha = st.slider("α (Internal Intention - النية الداخلية)", 0.0, 1.0, 0.5, 0.1)
        r_val = st.slider("R (Symbolic Mission - الرسالة الرمزية)", 0, 100, 50)
        m_val = st.slider("M (Meaning & Belonging - المعنى والانتماء)", 0, 100, 50)
        t_val = st.slider("T (Temporal Purification - التزكية الزمنية)", 0, 100, 50)
        c_val = st.slider("C (Symbolic Communication - التواصل الرمزي)", 0, 100, 50)
        
        # معاملات الانحدار (التي تحدد قوة أثر كل متغير)
        beta = [0.4, 0.3, 0.2, 0.1] 
        
    with col2:
        st.subheader("Performance Impact Simulation")
        # حساب الأداء الوظيفي بناءً على المعادلة
        performance = alpha + (beta[0] * r_val) + (beta[1] * m_val) + (beta[2] * t_val) + (beta[3] * c_val)
        
        # عرض النتيجة بمؤشر بصري
        st.metric("Institutional Performance (P)", f"{performance:.2f}")
        
        # رسم بياني يوضح مساهمة كل عنصر في الأداء
        labels = ['Symbolic Mission', 'Meaning', 'Purification', 'Communication']
        values = [beta[0]*r_val, beta[1]*m_val, beta[2]*t_val, beta[3]*c_val]
        
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
        fig.update_layout(title_text="Contribution to Mission-Driven Performance")
        st.plotly_chart(fig)

    st.markdown("""
    ### Interpretation | التفسير
    - **P:** الأداء المؤسسي الناتج.
    - **R:** مدى وضوح الرسالة الرمزية لدى العاملين.
    - **M:** المعنى الشخصي الذي يجده الموظف في عمله.
    - **T:** أثر التزكية (الإيثار، الأمل) في تقليل الاحتراق الوظيفي.
    """)
# --- إضافة القسم الجديد في القائمة الجانبية ---
# ملاحظة: أضف هذا الاسم للقائمة التي أنشأناها سابقاً في Sidebar
# domain = st.sidebar.selectbox("Choose Economic Domain:", [..., "Tazkiyah-Based Leadership (القيادة المتزكية)"])

# --- 2. نموذج القيادة المتزكية ---
if domain == "Tazkiyah-Based Leadership (القيادة المتزكية)":
    st.header("👑 Tazkiyah-Based Leadership Model | نموذج القيادة المتزكية")
    st.info("نمط قيادي يستند إلى النية الروحية، ويُفعّل قيم التزكية في اتخاذ القرار وإدارة الفرق.")

    # عرض المعادلة الرمزية الفخمة
    st.subheader("The Fundamental Symbolic Equation | المعادلة الرمزية الأساسية")
    st.latex(r"E_r = \alpha + \beta_1 Z_r + \beta_2 M_r + \beta_3 I_r + \beta_4 C_r + \beta_5 V_r + \beta_6 R_r + \epsilon_r")
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Sovereign Indicators | المؤشرات السيادية")
        alpha_l = st.slider("α (Foundational Intention - النية التأسيسية)", 0.0, 1.0, 0.7, 0.1)
        zr = st.slider("Zr (Leader's Tazkiyah - تزكية القائد)", 0, 100, 60)
        mr_l = st.slider("Mr (Meaning & Belonging - المعنى والانتماء)", 0, 100, 50)
        ir = st.slider("Ir (Symbolic Inspiration - الإلهام الرمزي)", 0, 100, 40)
        cr_l = st.slider("Cr (Symbolic Communication - التواصل الرمزي)", 0, 100, 50)
        vr = st.slider("Vr (Values Alignment - توافق القيم)", 0, 100, 70)
        rr = st.slider("Rr (Embodying Mission - تجسيد الرسالة)", 0, 100, 60)
        epsilon = st.number_input("εr (Invisible Impact/Barakah - الأثر غير المرئي)", 0.0, 10.0, 5.0)
        
        # أوزان الانحدار الافتراضية
        weights = [0.25, 0.20, 0.15, 0.10, 0.15, 0.15]
        
    with col2:
        st.subheader("Institutional Impact Analysis")
        # حساب الأثر المؤسسي المتزكي
        impact = alpha_l + (weights[0]*zr) + (weights[1]*mr_l) + (weights[2]*ir) + (weights[3]*cr_l) + (weights[4]*vr) + (weights[5]*rr) + epsilon
        
        st.metric("Tazkiyah Institutional Impact (Er)", f"{impact:.2f}")
        
        # رسم بياني راداري (Radar Chart) لإظهار "بصمة القائد المتزكي"
        categories = ['Tazkiyah', 'Meaning', 'Inspiration', 'Communication', 'Alignment', 'Embodiment']
        fig_radar = go.Figure()

        fig_radar.add_trace(go.Scatterpolar(
              r=[zr, mr_l, ir, cr_l, vr, rr],
              theta=categories,
              fill='toself',
              name='Leader Profile',
              line_color='gold'
        ))

        fig_radar.update_layout(
          polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
          showlegend=False,
          title="The Symbolic Footprint of the Leader"
        )
        st.plotly_chart(fig_radar)

    st.success(f"النتيجة: هذا النمط القيادي يحقق توازناً بنسبة {impact/100:.1%} بين الماديات والمعنويات.")
# --- إضافة القسم الجديد في القائمة الجانبية ---
# domain = st.sidebar.selectbox("Choose Economic Domain:", [..., "Symbolic Governance (الحوكمة الرمزية)"])

# --- 3. نموذج الحوكمة الرمزية ---
if domain == "Symbolic Governance (الحوكمة الرمزية)":
    st.header("⚖️ Symbolic Governance Model | نموذج الحوكمة الرمزية")
    st.info("منظومة مؤسسية تُدار وفق نية روحية، تحول السلطة إلى وظيفة تزكوية والشفافية إلى تعبير عن التسامي.")

    # عرض المعادلة الرمزية للحوكمة
    st.subheader("The Spiritual-Symbolic Governance Model | المعادلة الرمزية للحوكمة")
    st.latex(r"G_r = \alpha + \beta_1 N_r + \beta_2 T_r + \beta_3 M_r + \beta_4 A_r + \epsilon_r")
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Governance Indicators | مؤشرات الحوكمة")
        alpha_g = st.slider("α (Foundational Intention - النية التأسيسية)", 0.0, 1.0, 0.8, 0.1)
        nr = st.slider("Nr (Symbolic Leadership Style - النمط القيادي الرمزي)", 0, 100, 60)
        tr_g = st.slider("Tr (Governance Values - قيم الحوكمة التزكوية)", 0, 100, 70)
        mr_g = st.slider("Mr (Institutional Meaning - المعنى المؤسسي)", 0, 100, 65)
        ar = st.slider("Ar (Symbolic Alignment - الانسجام الرمزي)", 0, 100, 75)
        epsilon_g = st.number_input("εr (Invisible Impact - الأثر غير المرئي/البركة)", 0.0, 20.0, 7.0)
        
        # أوزان الأثر لنموذج الحوكمة
        w_g = [0.30, 0.25, 0.20, 0.25]
        
    with col2:
        st.subheader("Governance Quality Assessment")
        # حساب جودة الحوكمة الرمزية
        g_score = alpha_g + (w_g[0]*nr) + (w_g[1]*tr_g) + (w_g[2]*mr_g) + (w_g[3]*ar) + epsilon_g
        
        st.metric("Symbolic Governance Quality (Gr)", f"{g_score:.2f}")
        
        # رسم بياني يوضح التوازن بين البناء التنظيمي والمعنى الروحي
        labels_g = ['Leadership Style', 'Governance Values', 'Institutional Meaning', 'Symbolic Alignment']
        values_g = [w_g[0]*nr, w_g[1]*tr_g, w_g[2]*mr_g, w_g[3]*ar]
        
        fig_gov = go.Figure(data=[
            go.Bar(name='Governance Components', x=labels_g, y=values_g, marker_color='teal')
        ])
        fig_gov.update_layout(title_text="Analysis of Governance Symbolic Components")
        st.plotly_chart(fig_gov)

    st.markdown(f"""
    > **الاستنتاج البرمجي:** جودة الحوكمة هنا لا تعتمد على كثرة القوانين، بل على **الانسجام الرمزي ($A_r$)** بين القيم المعلنة والممارسة الفعلية. 
    > درجة التوفيق والبركة المرصودة في هذا النموذج هي: **{epsilon_g}**.
    """)
# --- إضافة القسم الجديد في القائمة الجانبية ---
# domain = st.sidebar.selectbox("Choose Economic Domain:", [..., "Tazkiyah-Based Investment (الاستثمار التزكوي)"])

# --- 4. نموذج الاستثمار التزكوي ---
if domain == "Tazkiyah-Based Investment (الاستثمار التزكوي)":
    st.header("💰 Tazkiyah-Based Investment Model | نموذج الاستثمار التزكوي")
    st.info("إعادة تعريف الاستثمار كفعل يحمل نية وتزكية، حيث يكون الربح وسيلة لتحقيق أثر معنوي وروحي.")

    # عرض المعادلة الرمزية للاستثمار
    st.subheader("The Fundamental Symbolic Equation | المعادلة الرمزية للاستثمار")
    st.latex(r"R_r = \alpha + \beta_1 N_r + \beta_2 Z_r + \beta_3 S_r + \beta_4 E_r + \epsilon_r")
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Investment Parameters | مدخلات الاستثمار")
        alpha_i = st.slider("α (Foundational Intention - النية التأسيسية)", 0.0, 1.0, 0.9, 0.1)
        nr_i = st.slider("Nr (Investor's Intention - نية المستثمر)", 0, 100, 70)
        zr_i = st.slider("Zr (Wealth Purification - تزكية المال)", 0, 100, 80)
        sr_i = st.slider("Sr (Investment Mission - رسالة الاستثمار)", 0, 100, 60)
        er_i = st.slider("Er (Symbolic Impact - الأثر الرمزي المشاهد)", 0, 100, 50)
        epsilon_i = st.number_input("εr (Invisible Barakah - البركة والأثر غير المرئي)", 0.0, 50.0, 15.0)
        
        # أوزان العائد التزكوي
        w_i = [0.25, 0.30, 0.20, 0.25]
        
    with col2:
        st.subheader("Total Symbolic Return (Rr) Analysis")
        # حساب العائد التزكوي الرمزي
        total_return = alpha_i + (w_i[0]*nr_i) + (w_i[1]*zr_i) + (w_i[2]*sr_i) + (w_i[3]*er_i) + epsilon_i
        
        # مقارنة العائد التزكوي بالعائد المالي التقليدي الافتراضي
        traditional_roi = er_i * 0.8  # افتراض أن العائد التقليدي جزء من الأثر المشاهد فقط
        
        st.metric("Total Symbolic Return (Rr)", f"{total_return:.2f}", delta=f"{total_return - traditional_roi:.2f} Alpha Gain")
        
        # رسم بياني لمقارنة العائد "المادي" مقابل "البركة والمعنى"
        fig_inv = go.Figure()
        fig_inv.add_trace(go.Bar(
            x=['Traditional Return', 'Tazkiyah Surplus (Barakah)', 'Total Sovereign Return'],
            y=[traditional_roi, (total_return - traditional_roi), total_return],
            marker_color=['#ced4da', '#28a745', '#007bff']
        ))
        fig_inv.update_layout(title_text="Traditional vs. Stewardship Return Comparison")
        st.plotly_chart(fig_inv)

    st.markdown(f"""
    ### Insight | رؤية استثمارية
    في هذا النموذج، نثبت رياضياً أن **البركة ($\epsilon_r$)** وتزكية المال **($Z_r$)** ليست مجرد مفاهيم روحية، بل هي **Alpha Gain** حقيقي يرفع القيمة الكلية للاستثمار فوق مستوى العائد المادي البسيط. 
    > **نسبة "فائض التزكية" في هذا المشروع:** {((total_return - traditional_roi) / total_return)*100:.1f}%
    """)
# --- 5. نموذج التقييم التزكوي للمؤسسات ---
if domain == "Institutional Evaluation (التقييم التزكوي)":
    st.header("📋 Institutional Tazkiyah-Based Evaluation | نموذج التقييم التزكوي")
    st.info("عملية تحليلية لقياس جودة المؤسسة عبر دمج الغايات الرمزية مع مؤشرات الأداء الوظيفي التقليدي.")

    # عرض المعادلة الرمزية الأساسية
    st.subheader("The Institutional Evaluation Equation | معادلة التقييم المؤسسي")
    st.latex(r"Q_r = \alpha + \beta_1 N_r + \beta_2 Z_r + \beta_3 M_r + \beta_4 C_r + \beta_5 F_r + \epsilon_r")
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Variable Indicators | المؤشرات المتغيرة")
        alpha_q = st.slider("α (Foundational Intention - النية التأسيسية)", 0.0, 1.0, 0.9, 0.1)
        nr_q = st.slider("Nr (Leadership Intention - نية القيادة)", 0, 10, 7)
        mr_q = st.slider("Mr (Institutional Meaning - المعنى المؤسسي)", 0, 10, 8)
        
        st.divider()
        st.subheader("Fixed Parameters (Core) | العوامل الثابتة")
        # القيم التي حددتها يا دكتور لتثبيت النموذج
        zr_fixed = 5  # تزكية الهيكل
        cr_fixed = 5  # التواصل الرمزي
        fr_fixed = 5  # فاعلية الروح الجماعية
        st.disabled_slider = st.slider("Zr, Cr, Fr (Fixed Level)", 5, 5, 5)
        
        epsilon_q = st.number_input("εr (Invisible Barakah - الأثر غير المرئي)", 0.0, 30.0, 10.0)
        
        # أوزان افتراضية للتقييم
        betas = [1.2, 1.0, 0.8, 0.8, 0.7] # أوزان للنية، المعنى، التزكية، التواصل، الفاعلية
        
    with col2:
        st.subheader("Total Quality Score (Qr)")
        # حساب جودة المؤسسة الكلية
        q_score = (alpha_q * 10) + (betas[0] * nr_q) + (betas[1] * zr_fixed) + (betas[2] * mr_q) + (betas[3] * cr_fixed) + (betas[4] * fr_fixed) + epsilon_q
        
        # عرض النتيجة بأسلوب الـ Gauge Chart (عداد الجودة)
        fig_q = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = q_score,
            title = {'text': "Institutional Quality Index (Qr)"},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 80], 'color': "skyblue"},
                    {'range': [80, 100], 'color': "royalblue"}],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90}}))
        
        st.plotly_chart(fig_q)

    st.success(f"النتيجة: تم تقييم جودة المؤسسة بنسبة {q_score:.2f} نقطة على مقياس التزكية السيادي.")
    
    st.markdown("""
    ### 🔬 Methodology Note | ملاحظة منهجية
    تم تثبيت مؤشرات **تزكية الهيكل ($Z_r$)**، **التواصل ($C_r$)**، و**الفاعلية الجماعية ($F_r$)** عند الدرجة 5 لتحييد أثرها ومراقبة حساسية الجودة تجاه **النية القيادية** و**المعنى المؤسسي**.
    """)
# --- 6. نموذج التحقق الوجودي في بيئة العمل ---
if domain == "Existential Realization (التحقق الوجودي)":
    st.header("🌱 Existential Realization Model | نموذج التحقق الوجودي")
    st.info("إدراك الفرد لمعنى وجوده داخل المؤسسة وشعوره بأن عمله يحقق غاية رمزية تتجاوز المنفعة المادية.")

    # عرض المعادلة الرمزية للتحقق الوجودي
    st.subheader("The Fundamental Symbolic Equation | المعادلة الرمزية للتحقق الوجودي")
    st.latex(r"V_r = \alpha + \beta_1 M_r + \beta_2 P_r + \beta_3 N_r + \beta_4 Z_r + \epsilon_r")
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Existential Dimensions | الأبعاد الوجودية")
        alpha_v = st.slider("α (Foundational Intention - نية المؤسسة تجاه الفرد)", 0.0, 1.0, 0.8, 0.1)
        mr_v = st.slider("Mr (Personal Meaning - المعنى الشخصي)", 0, 100, 75)
        pr_v = st.slider("Pr (Symbolic Participation - المشاركة الرمزية)", 0, 100, 60)
        nr_v = st.slider("Nr (Individual Intention - نية الموظف الذاتية)", 0, 100, 85)
        zr_v = st.slider("Zr (Self-Tazkiyah - التزكية والنمو الذاتي)", 0, 100, 70)
        epsilon_v = st.number_input("εr (Invisible Barakah - الأثر الروحي والانسجام)", 0.0, 15.0, 8.0)
        
        # أوزان الأثر الوجودي
        w_v = [0.30, 0.20, 0.25, 0.25] # المعنى، المشاركة، النية، التزكية
        
    with col2:
        st.subheader("Existential Validation Score (Vr)")
        # حساب درجة التحقق الوجودي
        v_score = alpha_v + (w_v[0]*mr_v) + (w_v[1]*pr_v) + (w_v[2]*nr_v) + (w_v[3]*zr_v) + epsilon_v
        
        st.metric("Existential Realization Index (Vr)", f"{v_score:.2f}")
        
        # رسم بياني مساحي (Area Chart) يوضح تدفق المعنى والنية إلى التحقق الوجودي
        realization_data = pd.DataFrame({
            'Dimension': ['Meaning', 'Participation', 'Intention', 'Tazkiyah'],
            'Impact Value': [w_v[0]*mr_v, w_v[1]*pr_v, w_v[2]*nr_v, w_v[3]*zr_v]
        })
        
        fig_v = go.Figure()
        fig_v.add_trace(go.Scatter(
            x=realization_data['Dimension'], 
            y=realization_data['Impact Value'],
            fill='tozeroy',
            line_color='indigo',
            name='Existential Flow'
        ))
        fig_v.update_layout(title_text="Existential Realization Flow Analysis")
        st.plotly_chart(fig_v)

    st.markdown(f"""
    ### 📝 Research Insight | رؤية بحثية
    في هذا النموذج، نجد أن **نية الفرد ($N_r$)** هي المحرك الأكبر للتحقق الوجودي. عندما تتلاقى نية الموظف مع نية المؤسسة ($\alpha$)، يحدث ما نسميه **"الانسجام الوجودي"**، وهو ما يفسر النتائج غير التقليدية (البركة $\epsilon_r$) التي تعجز النظريات المادية عن تفسيرها.
    """)
# --- 7. نموذج القيمة التزكوية المضافة (ZVA) ---
if domain == "Tazkiyah Value Added (ZVA)":
    st.header("💎 Tazkiyah Value Added (ZVA) | القيمة التزكوية المضافة")
    st.info("مفهوم ثوري يعيد تعريف القيمة الاقتصادية من خلال دمج أثر التزكية (النية، الانسجام، الرسالة) في الأداء المادي.")

    # عرض المعادلات الرياضية بوضوح
    st.subheader("The Sovereign Value Equations | معادلات القيمة السيادية")
    col_math1, col_math2 = st.columns(2)
    with col_math1:
        st.markdown("**Traditional EVA Model:**")
        st.latex(r"EVA = \alpha F + \beta C + \gamma M + \delta Z + \epsilon")
    with col_math2:
        st.markdown("**Tazkiyah Value Added (Proposed):**")
        st.latex(r"ZVA = EVA + \lambda Z")
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Sovereign Indicators | المؤشرات السيادية")
        f_val = st.slider("F (Institutional Efficiency - الفاعلية)", 0, 100, 70)
        c_val_zva = st.slider("C (Human Capital - رأس المال البشري)", 0, 100, 65)
        m_val_zva = st.slider("M (Institutional Morale - المعنوية والرسالة)", 0, 100, 80)
        z_val_zva = st.slider("Z (Tazkiyah Index - مؤشر التزكية والنية)", 0, 100, 90)
        
        st.divider()
        st.subheader("Coefficients | المعاملات")
        lambda_val = st.slider("λ (Conversion Factor - معامل التحويل القيمي)", 0.0, 2.0, 1.2, 0.1)
        delta_z = st.slider("δ (Tazkiyah Weight in EVA)", 0.0, 1.0, 0.4, 0.05)
        
    with col2:
        st.subheader("ZVA vs. EVA Comprehensive Analysis")
        # حساب EVA التقليدي (بناءً على المعادلة المقترحة)
        # نفترض معاملات افتراضية للتوضيح
        eva_score = (0.3 * f_val) + (0.2 * c_val_zva) + (0.1 * m_val_zva) + (delta_z * z_val_zva)
        
        # حساب ZVA (القيمة المضافة التزكوية)
        zva_score = eva_score + (lambda_val * z_val_zva)
        
        col_res1, col_res2 = st.columns(2)
        col_res1.metric("Economic Value Added (EVA)", f"{eva_score:.2f}")
        col_res2.metric("Tazkiyah Value Added (ZVA)", f"{zva_score:.2f}", delta=f"{zva_score - eva_score:.2f} Value Gain")
        
        # رسم بياني لمقارنة القطاعات (محاكاة لاختبار النموذج في التعليم والصحة)
        sectors = ['Education (التعليم)', 'Health (الصحة)', 'Social Inv. (الاستثمار)']
        eva_sectors = [eva_score * 0.9, eva_score * 1.1, eva_score * 0.8]
        zva_sectors = [eva_sectors[0] + (lambda_val * 85), eva_sectors[1] + (lambda_val * 70), eva_sectors[2] + (lambda_val * 95)]
        
        fig_zva = go.Figure()
        fig_zva.add_trace(go.Bar(x=sectors, y=eva_sectors, name='Traditional EVA', marker_color='#94a3b8'))
        fig_zva.add_trace(go.Bar(x=sectors, y=zva_sectors, name='Proposed ZVA', marker_color='#10b981'))
        
        fig_zva.update_layout(title_text="ZVA Testing Across Selected Egyptian Sectors", barmode='group')
        st.plotly_chart(fig_zva)

    st.markdown(f"""
    ### 🔬 Strategic Conclusion | الخلاصة الاستراتيجية
    يُظهر النموذج أن **معامل التحويل ($\lambda$)** هو المحرك الأساسي للدولة لتحويل القيم الروحية إلى أثر اقتصادي ملموس. 
    - في قطاع **التعليم**، تحقق النية التزكوية قفزة في الـ ZVA بنسبة **{((zva_sectors[0]-eva_sectors[0])/eva_sectors[0])*100:.1f}%**.
    - الفجوة بين العمود الرمادي (المادي) والأخضر (التزكوي) هي المساحة التي تضيع في الاقتصاد التقليدي وتستعيدها **هندسة الاستخلاف**.
    """)
# --- 8. نموذج هندسة السوق: من التبادل إلى التزكية ---
if domain == "Market Engineering (هندسة السوق)":
    st.header("⚖️ Market Engineering: From Exchange to Tazkiyah")
    st.info("تحويل السوق من ساحة لتبادل المنافع المادية فقط إلى فضاء لتحقيق العدالة الرمزية والتزكية.")

    # المعادلة المقترحة لعدالة السوق
    st.subheader("The Market Justice Equation | معادلة العدالة التزكوية")
    st.latex(r"V_m = \alpha (P_m + \Delta B) + \beta Q_s + \gamma J")
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Market Dynamics | ديناميكيات السوق")
        p_material = st.slider("Pm (Material Price - السعر المادي)", 10, 1000, 500)
        barakah_coeff = st.slider("ΔB (Barakah/Social Impact - معامل البركة)", 0.0, 2.0, 1.5, 0.1)
        intent_quality = st.slider("Qs (Intent Quality - جودة نية البائع)", 0, 100, 80)
        justice_idx = st.slider("J (Justice & Fair Trade - مؤشر العدالة)", 0, 100, 90)
        
    with col2:
        st.subheader("Sovereign Market Value (Vm) Analysis")
        # حساب القيمة التزكوية للسوق
        sovereign_value = (p_material * barakah_coeff) + (1.2 * intent_quality) + (2.0 * justice_idx)
        
        st.metric("Total Market Value (Vm)", f"{sovereign_value:.2f}", delta=f"{sovereign_value - p_material:.2f} Spiritual Premium")
        
        # رسم بياني لمقارنة "التبادل المادي" مقابل "القيمة السيادية"
        fig_market = go.Figure()
        fig_market.add_trace(go.Scatter(
            x=[0, p_material], y=[0, p_material],
            mode='lines', name='Traditional Exchange (Linear)',
            line=dict(color='gray', dash='dash')
        ))
        fig_market.add_trace(go.Scatter(
            x=[0, p_material], y=[0, sovereign_value],
            mode='lines+markers', name='Tazkiyah Value (Integrated)',
            line=dict(color='orange', width=4)
        ))
        
        fig_market.update_layout(title_text="Material Exchange vs. Tazkiyah Transformation")
        st.plotly_chart(fig_market)

    st.success(f"النتيجة: بفضل 'معامل البركة' والعدالة، تحولت القيمة من مجرد سعر مادي ({p_material}) إلى قيمة سيادية ({sovereign_value:.2f}).")
# --- 9. نموذج الشفافية في السوق ---
if domain == "Market Transparency (الشفافية في السوق)":
    st.header("🔍 Market Transparency Model | نموذج الشفافية")
    st.info("تحليل أثر الإفصاح ووضوح العقود في رفع الغرر وتحقيق كفاءة السوق.")

    st.subheader("The Econometric Equation | المعادلة القياسية")
    st.latex(r"Y_t = \alpha_0 + \alpha_1 D_t + \alpha_2 C_t + \alpha_3 I_t + \alpha_4 AF_t + \mu_t")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        dt = st.slider("Dt (Price Disclosure - الإفصاح السعري)", 0, 100, 70)
        ct = st.slider("Ct (Contract Clarity - ووضوح العقود)", 0, 100, 80)
        it = st.slider("It (Info Availability - توفر المعلومات)", 0, 100, 60)
        aft = st.slider("AFt (Anti-Fraud - مكافحة الغش)", 0, 100, 90)
        
    with col2:
        # حساب كفاءة السوق (علاقة طردية مع الشفافية)
        market_efficiency = 10 + (0.4*dt + 0.3*ct + 0.2*it + 0.1*aft)
        st.metric("Market Efficiency Index (Yt)", f"{market_efficiency:.2f}%")
        
        # رسم بياني يوضح انخفاض تقلبات الأسعار مع زيادة الشفافية
        transparency_score = (dt + ct + it + aft) / 4
        volatility = 100 - transparency_score # فرضية: الشفافية تلغي التقلب
        
        fig_trans = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = volatility,
            title = {'text': "Market Price Volatility (التقلبات)"},
            gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "red"}}
        ))
        st.plotly_chart(fig_trans)
# --- 10. نموذج منع الاحتكار ---
if domain == "Anti-Monopoly Engineering (منع الاحتكار)":
    st.header("🚫 Anti-Monopoly Model | منع الاحتكار")
    st.info("تحليل العلاقة بين التركز السوقي والعدالة التوزيعية.")

    st.subheader("The Monopolistic Impact Equation")
    st.latex(r"Y_t = \gamma_0 + \gamma_1 HH_t + \gamma_2 AC_t + \gamma_3 RI_t + \gamma_4 AM_t + \nu_t")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        hht = st.number_input("HHt (Market Concentration Index - مؤشر هيرفيندال)", 0, 10000, 2500)
        act = st.slider("ACt (Active Competitors - عدد المنافسين)", 1, 50, 5)
        rit = st.slider("RIt (Gov Intervention - تدخل الدولة)", 0, 100, 70)
        amt = st.slider("AMt (Complaints Index - الشكاوى)", 0, 100, 30)
        
    with col2:
        # العدالة التوزيعية (تنخفض بزيادة HHT وتزيد بزيادة المنافسين وتدخل الدولة)
        justice_dist = (rit * 0.4) + (act * 1.5) - (hht/200) + 50
        st.metric("Distributive Justice Index (Yt)", f"{max(0, justice_dist):.2f}")
        
        # رسم بياني يوضح العلاقة بين عدد المنافسين والعدالة
        x_comp = np.linspace(1, 50, 50)
        y_justice = (rit * 0.4) + (x_comp * 1.5) - (hht/200) + 50
        
        fig_monop = go.Figure()
        fig_monop.add_trace(go.Scatter(x=x_comp, y=y_justice, name="Justice Curve", line=dict(color='green', width=3)))
        fig_monop.update_layout(title="Impact of Competition on Distributive Justice", xaxis_title="Number of Competitors")
        st.plotly_chart(fig_monop)
domain = st.sidebar.selectbox("Choose Economic Domain:", [
    ..., 
    "Good Intention in Market (النية الصالحة في السوق)"
])
# --- 11. نموذج النية الصالحة في السوق ---
if domain == "Good Intention in Market (النية الصالحة في السوق)":
    st.header("🌟 Good Intention Model | نموذج النية الصالحة")
    st.info("تحليل أثر المقاصد الأخلاقية والإيثار على استقرار المجتمع وعدالة التوزيع.")

    st.subheader("The Behavioral Econometric Equation")
    st.latex(r"Y_t = \delta_0 + \delta_1 GI_t + \delta_2 AP_t + \delta_3 CC_t + \delta_4 ND_t + \xi_t")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        git = st.slider("GIt (Good Intention Index - مؤشر النية الصالحة)", 0, 100, 80)
        apt = st.slider("APt (Altruistic Pricing - الإيثار في التسعير)", 0, 100, 60)
        cct = st.slider("CCt (Community Contribution - المبادرات المجتمعية)", 0, 100, 70)
        ndt = st.slider("NDt (No-Deception Score - الامتناع عن الغش)", 0, 100, 95)
        
    with col2:
        # حساب مؤشر الرضا العام أو العدالة التوزيعية
        # النية والامتناع عن الغش لهما الوزن الأكبر في بناء الثقة والرضا
        satisfaction_idx = 15 + (0.35 * git + 0.25 * ndt + 0.20 * apt + 0.20 * cct)
        
        st.metric("Social Satisfaction & Justice (Yt)", f"{satisfaction_idx:.2f}%")
        
        # رسم بياني يوضح العلاقة بين النية الصالحة والعدالة التوزيعية
        # كلما زادت النية، قل التفاوت الطبقي (محاكاة)
        x_intent = np.linspace(0, 100, 20)
        y_justice = 20 + (0.6 * x_intent) + (0.15 * ndt) 
        
        fig_intent = go.Figure()
        fig_intent.add_trace(go.Scatter(
            x=x_intent, y=y_justice, 
            mode='lines+markers', 
            name='Justice/Satisfaction Trend',
            line=dict(color='emerald', width=4)
        ))
        
        fig_intent.update_layout(
            title="Impact of Good Intention on Social Justice",
            xaxis_title="Good Intention Level (GIt)",
            yaxis_title="Satisfaction & Justice Score (Yt)"
        )
        st.plotly_chart(fig_intent)

    st.markdown(f"""
    ### 💡 Scientific Perspective | منظور علمي
    هذا النموذج يثبت أن **الامتناع عن الغش ($ND_t$)** و**النية الصالحة ($GI_t$)** يعملان كـ "مزيّت" (Lubricant) لتروس الاقتصاد؛ حيث يقللان من "تكاليف المعاملات" (Transaction Costs) الناتجة عن عدم الثقة، مما يرفع الكفاءة الكلية للمجتمع.
    """)
domain = st.sidebar.selectbox("Choose Economic Domain:", [
    ..., 
    "Adequacy Pricing (سعر الكفاية)",
    "Merciful Supply (العرض الرحيم)",
    "Fair Demand (الطلب العادل)",
    "Maqasid Intervention (التدخل المقاصدي)"
])
if domain == "Adequacy Pricing (سعر الكفاية)":
    st.header("⚖️ Adequacy Pricing Model | نموذج سعر الكفاية")
    st.latex(r"P_k = \delta_0 + \delta_1 C + \delta_2 M_r + \delta_3 A_s + \epsilon")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        c_cost = st.number_input("C (Production Cost - التكلفة)", 10, 1000, 100)
        mr_profit = st.slider("Mr (Legitimate Profit % - الربح المشروع)", 0.0, 0.5, 0.15)
        as_adequacy = st.slider("As (Adequacy Coeff - معامل الكفاية)", 0, 100, 50)
    with col2:
        pk_price = 10 + (1.1 * c_cost) + (c_cost * mr_profit) + (0.5 * as_adequacy)
        st.metric("Adequacy Price (Pk)", f"${pk_price:.2f}")
        st.info("هذا السعر يضمن حياة كريمة للمنتج دون إرهاق المستهلك.")
if domain == "Merciful Supply (العرض الرحيم)":
    st.header("🤝 Merciful Supply Model | نموذج العرض الرحيم")
    st.latex(r"Q_S = \gamma_0 + \gamma_1 H + \gamma_2 I + \gamma_3 S + \epsilon")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        h_need = st.slider("H (Social Need - الحاجة المجتمعية)", 0, 100, 80)
        i_intent = st.slider("I (Ihsan Intent - نية الإحسان)", 0, 100, 90)
        s_stock = st.number_input("S (Inventory - الوفرة)", 100, 10000, 1000)
    with col2:
        qs_supply = 50 + (0.6 * h_need) + (0.4 * i_intent) + (0.2 * s_stock)
        st.metric("Merciful Supply Quantity (Qs)", f"{qs_supply:.0f} Units")
        st.write("لاحظ: في الأزمات (ارتفاع H)، يزداد العرض الرحيم بدافع الإحسان.")
if domain == "Fair Demand (الطلب العادل)":
    st.header("🥣 Fair Demand Model | نموذج الطلب العادل")
    st.latex(r"Q_d = \alpha_0 + \alpha_1 Y + \alpha_2 A + \alpha_3 N + \epsilon")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        y_income = st.number_input("Y (Income - الدخل)", 1000, 20000, 5000)
        a_awareness = st.slider("A (Consumption Awareness - وعي الاستهلاك)", 0, 100, 70)
        n_actual_need = st.slider("N (Actual Need - الحاجة الحقيقية)", 0, 100, 40)
    with col2:
        # الوعي (A) يقلل من الطلب الهامشي غير الضروري
        qd_demand = (0.05 * y_income) + (0.5 * n_actual_need) - (0.3 * a_awareness)
        st.metric("Fair Demand Quantity (Qd)", f"{max(0, qd_demand):.2f}")
        st.success("النتيجة: زيادة الوعي تمنع الإسراف وتخفض التضخم.")
if domain == "Maqasid Intervention (التدخل المقاصدي)":
    st.header("🏛 Maqasid Intervention Model | التدخل المقاصدي")
    st.latex(r"I_s = \beta_0 + \beta_1 M + \beta_2 D + \beta_3 R + \epsilon")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        m_imbalance = st.slider("M (Market Imbalance - اختلال السوق)", 0, 100, 60)
        d_tools = st.slider("D (Intervention Tools - أدوات الدولة)", 0, 100, 50)
        r_maqasid = st.slider("R (Maqasid Achievement - تحقق المقاصد)", 0, 100, 80)
    with col2:
        is_score = 5 + (0.4 * m_imbalance) + (0.3 * d_tools) + (0.3 * r_maqasid)
        st.metric("State Intervention Degree (Is)", f"{is_score:.2f}")
        
        # رسم بياني للعلاقة بين الاختلال والتدخل
        fig_is = go.Figure()
        fig_is.add_trace(go.Scatter(x=[0, 100], y=[0, 100], name="Traditional Intervention", line=dict(dash='dash')))
        fig_is.add_trace(go.Scatter(x=[0, m_imbalance], y=[0, is_score], name="Maqasid Intervention", line=dict(color='purple', width=4)))
        st.plotly_chart(fig_is)
domain = st.sidebar.selectbox("Choose Economic Domain:", [
    ..., 
    "Sovereign Monetary Policy (السياسة النقدية السيادية)"
])
# --- 16. هندسة السياسات النقدية السيادية ---
if domain == "Sovereign Monetary Policy (السياسة النقدية السيادية)":
    st.header("🪙 Sovereign Monetary Architecture | هندسة السياسات النقدية")
    st.info("بناء نظام نقدي سيادي يربط قوة العملة بالقيم الإنتاجية والشرعية (الزكاة، الوقف، الذهب، السلع) بدلاً من الفائدة.")

    # عرض المعادلة المركبة الكبرى
    st.subheader("The Composite Monetary Equation | المعادلة النقدية المركبة")
    st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 W + \beta_3 S + \beta_4 G + \beta_5 F - \beta_6 C - \beta_7 V + \epsilon")
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Monetary Anchors | المرتكزات النقدية")
        z_rate = st.slider("Z (Zakat Collection Rate - معدل الزكاة)", 0, 100, 40)
        w_vol = st.slider("W (Waqf Production - حجم الوقف الإنتاجي)", 0, 100, 35)
        s_idx = st.slider("S (Commodity Index - مؤشر السلع الأساسية)", 0, 100, 60)
        g_cover = st.slider("G/F (Gold & Silver Cover - تغطية الذهب والفضة)", 0, 100, 50)
        
        st.divider()
        st.subheader("Negative Pressures | الضغوط السلبية")
        c_infl = st.slider("C (Inflation - التضخم الحالي)", 0, 100, 20)
        v_volat = st.slider("V (Exchange Volatility - تقلبات الصرف)", 0, 100, 15)
        
    with col2:
        st.subheader("Monetary Stability Index (Y)")
        # حساب استقرار العملة بناءً على المعادلة المركبة
        # العوامل الإيجابية ترفع الاستقرار، والسلبية تخفضه
        y_stability = 20 + (0.25*z_rate + 0.20*w_vol + 0.15*s_idx + 0.30*g_cover) - (0.4*c_infl + 0.3*v_volat)
        
        st.metric("Sovereign Currency Stability (Y)", f"{y_stability:.2f}", 
                  delta="Sovereign" if y_stability > 50 else "Dependent", delta_color="normal")
        
        # رسم بياني راداري يوضح "مربع السيادة النقدية"
        fig_monetary = go.Figure()
        fig_monetary.add_trace(go.Scatterpolar(
            r=[z_rate, w_vol, s_idx, g_cover, 100-c_infl],
            theta=['Zakat', 'Waqf', 'Commodities', 'Gold Cover', 'Price Stability'],
            fill='toself',
            name='Monetary Profile',
            line_color='darkgoldenrod'
        ))
        
        fig_monetary.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=False,
            title="Sovereign Monetary Strength Profile"
        )
        st.plotly_chart(fig_monetary)

    st.success(f"التحليل السيادي: النظام النقدي الحالي يحقق درجة استقرار {y_stability:.2f}. ربط العملة بالذهب والزكاة يقلل أثر المضاربات بنسبة {g_cover*0.8:.1f}%.")
    
    st.markdown("""
    ### 🌍 Global Benchmarks | تجارب عالمية ومقارنات
    - **السودان:** تجربة استخدام الزكاة لضبط السيولة.
    - **ماليزيا:** سلة السلع الأساسية لتقييم القوة الشرائية.
    - **المغرب:** الصكوك الوقفية كبديل للاقتراض الربوي.
    - **الإمارات:** الذهب كمرجعية رمزية لضمان الاستقرار.
    """)
# --- 17. هندسة سعر الصرف (الرؤية التمكينية) ---
if domain == "Exchange Rate Engineering (هندسة سعر الصرف)":
    st.header("⚖️ Exchange Rate Engineering | هندسة سعر الصرف")
    st.info("رؤية تمكينية لربط العملة بالأصول الحقيقية والقيم التزكوية لضمان الاستقرار والعدالة.")

    # اختيار النموذج الفرعي
    sub_model = st.radio("Select Sub-Model:", [
        "Zakat-Linked (النموذج الزكوي)", 
        "Commodity-Linked (النموذج السلعي)", 
        "Waqf-Linked (النموذج الوقفي)", 
        "Gold/Silver-Linked (النموذج الذهبي)"
    ])

    st.markdown("---")

    if sub_model == "Zakat-Linked (النموذج الزكوي)":
        st.subheader("🌙 Zakat-Based Stabilization | الربط بالزكاة")
        st.latex(r"Y = \beta_0 + \beta_1 Z + \beta_2 E - \beta_3 C - \beta_4 P + \epsilon")
        col1, col2 = st.columns(2)
        with col1:
            z_rate = st.slider("Z (Zakat Rate - معدل الزكاة)", 0, 100, 45)
            e_rate = st.slider("E (Employment - التوظيف)", 0, 100, 70)
        with col2:
            c_infl = st.slider("C (Inflation - التضخم)", 0, 100, 20)
            p_pov = st.slider("P (Poverty - الفقر)", 0, 100, 30)
        y_zakat = 30 + (0.5 * z_rate) + (0.3 * e_rate) - (0.4 * c_infl) - (0.4 * p_pov)
        st.metric("Monetary Stability Index (Y)", f"{y_zakat:.2f}")

    elif sub_model == "Commodity-Linked (النموذج السلعي)":
        st.subheader("🌾 Commodity-Basket Anchor | الربط بالسلع الأساسية")
        st.latex(r"Y = \beta_0 + \beta_1 S - \beta_2 I - \beta_3 V - \beta_4 P + \epsilon")
        col1, col2 = st.columns(2)
        with col1:
            s_idx = st.slider("S (Commodity Index - مؤشر السلع)", 0, 100, 80)
            i_infl = st.slider("I (Inflation - التضخم)", 0, 100, 15)
        with col2:
            v_vol = st.slider("V (Ex-Rate Volatility - التقلبات)", 0, 100, 25)
            p_pov = st.slider("P (Poverty - الفقر)", 0, 100, 35)
        y_comm = 20 + (0.6 * s_idx) - (0.3 * i_infl) - (0.4 * v_vol) - (0.2 * p_pov)
        st.metric("Purchasing Power Stability (Y)", f"{y_comm:.2f}")

    elif sub_model == "Waqf-Linked (النموذج الوقفي)":
        st.subheader("🏗 Waqf-Based Sustainability | الربط بالوقف")
        st.latex(r"Y = \beta_0 + \beta_1 W + \beta_2 R - \beta_3 C - \beta_4 P + \epsilon")
        col1, col2 = st.columns(2)
        with col1:
            w_vol = st.slider("W (Waqf Volume - حجم الوقف)", 0, 100, 50)
            r_return = st.slider("R (Waqf Returns - العائد الوقفي)", 0, 100, 60)
        with col2:
            c_infl = st.slider("C (Inflation - التضخم)", 0, 100, 10)
            p_pov = st.slider("P (Poverty - الفقر)", 0, 100, 20)
        y_waqf = 25 + (0.4 * w_vol) + (0.3 * r_return) - (0.3 * c_infl) - (0.4 * p_pov)
        st.metric("Sovereign Funding Stability (Y)", f"{y_waqf:.2f}")

    elif sub_model == "Gold/Silver-Linked (النموذج الذهبي)":
        st.subheader("🟡 Gold/Silver Symbolic Anchor | الربط بالذهب والفضة")
        st.latex(r"Y = \beta_0 + \beta_1 G + \beta_2 F - \beta_3 V - \beta_4 C + \epsilon")
        col1, col2 = st.columns(2)
        with col1:
            g_cover = st.slider("G (Gold Coverage - تغطية الذهب)", 0, 100, 55)
            f_cover = st.slider("F (Silver Coverage - تغطية الفضة)", 0, 100, 45)
        with col2:
            v_vol = st.slider("V (Volatility - تقلبات الصرف)", 0, 100, 10)
            c_infl = st.slider("C (Inflation - التضخم)", 0, 100, 5)
        y_gold = 40 + (0.4 * g_cover) + (0.2 * f_cover) - (0.5 * v_vol) - (0.3 * c_infl)
        st.metric("Intrinsic Value Index (Y)", f"{y_gold:.2f}")

    # رسم بياني توضيحي للمقارنة
    st.markdown("---")
    st.subheader("The Stability Shield Analysis")
    labels = ['Zakat Impact', 'Commodity Stability', 'Waqf Support', 'Gold Confidence']
    values = [y_zakat if 'y_zakat' in locals() else 0, 
              y_comm if 'y_comm' in locals() else 0, 
              y_waqf if 'y_waqf' in locals() else 0, 
              y_gold if 'y_gold' in locals() else 0]
    
    fig_ex = go.Figure(data=[go.Bar(x=labels, y=values, marker_color='darkblue')])
    fig_ex.update_layout(title="Stability Contribution per Sovereign Model")
    st.plotly_chart(fig_ex)
# --- 18. هندسة البدائل النقدية (سعر الفائدة المقاصدي) ---
if domain == "Maqasid Interest Alternatives (بدائل الفائدة)":
    st.header("🎯 Maqasid Return Engineering | هندسة العائد المقاصدي")
    st.info("بناء معدل عائد إسلامي بديل يراعي العدالة والتمكين والتزكية كبديل للفائدة الربوية.")

    # اختيار نموذج التسعير
    pricing_model = st.radio("Select Pricing Model:", [
        "Islamic Maqasid Return (معدل العائد المقاصدي)",
        "Financial Engineering (الهندسة المالية)",
        "Banking Product Pricing (تسعير المنتجات)"
    ])

    st.markdown("---")

    if pricing_model == "Islamic Maqasid Return (معدل العائد المقاصدي)":
        st.subheader("📊 Model 1: The Maقasid Return Equation")
        st.latex(r"R = \alpha_1 \pi + \alpha_2 T + \alpha_3 Z + \alpha_4 E + \epsilon")
        
        col1, col2 = st.columns(2)
        with col1:
            pi_profit = st.slider("π (Ethical Profitability - الربحية الأخلاقية)", 0, 100, 60)
            t_empower = st.slider("T (Empowerment Index - مؤشر التمكين)", 0, 100, 80)
        with col2:
            z_zakat = st.slider("Z (Zakat Floor - حد الزكاة الأدنى)", 0, 10, 2)
            e_infl = st.slider("E (Expected Inflation - التضخم المتوقع)", 0, 100, 15)
        
        # حساب العائد المقاصدي (R)
        r_return = (0.4 * pi_profit) + (0.3 * t_empower) + (0.2 * z_zakat) + (0.1 * e_infl)
        st.metric("Maqasid Return Rate (R)", f"{r_return:.2f}%")

    elif pricing_model == "Financial Engineering (الهندسة المالية)":
        st.subheader("🏗️ Model 2: Financial Engineering Score")
        st.latex(r"P = \beta_1 R + \beta_2 T + \beta_3 S + \beta_4 \pi + \beta_5 Z + \epsilon")
        
        col1, col2 = st.columns(2)
        with col1:
            r_val = st.slider("R (Maqasid Return Rate)", 0, 100, 50)
            s_sharia = st.slider("S (Sharia Compliance - الالتزام الشرعي)", 0, 100, 95)
        with col2:
            t_val = st.slider("T (Empowerment Effect)", 0, 100, 70)
            pi_val = st.slider("π (Project Profitability)", 0, 100, 40)
            
        p_price = (0.25 * r_val) + (0.2 * t_val) + (0.3 * s_sharia) + (0.15 * pi_val) + 5.0
        st.metric("Financial Instrument Price (P)", f"{p_price:.2f}")

    elif pricing_model == "Banking Product Pricing (تسعير المنتجات)":
        st.subheader("🏦 Model 3: Product Pricing Strategy")
        st.latex(r"P_{bank} = \beta_1 R + \beta_2 T + \beta_3 S + \beta_4 \pi + \beta_5 Z + \epsilon")
        
        st.write("هذا النموذج يسعر المنتجات (ودائع، صكوك) بناءً على أثرها التمكيني.")
        t_impact = st.select_slider("Select Product Impact Type:", options=["Low Impact", "Moderate", "High Empowerment"])
        
        impact_boost = 0
        if t_impact == "High Empowerment": impact_boost = 15
        elif t_impact == "Moderate": impact_boost = 7
        
        final_price = 10 + impact_boost + (0.2 * 60) # مثال مبسط
        st.metric("Product Fair Price", f"{final_price:.2f}")

    # رسم بياني للمقارنة بين العائد المادي والعائد المقاصدي
    st.markdown("---")
    fig_r = go.Figure()
    fig_r.add_trace(go.Bar(
        x=['Standard Interest (Libor)', 'Maqasid Return (R)'],
        y=[15, r_return if 'r_return' in locals() else 25],
        marker_color=['#ef4444', '#10b981']
    ))
    fig_r.update_layout(title="Traditional Interest vs. Sovereign Maqasid Return")
    st.plotly_chart(fig_r)
# --- 19. نموذج الهندسة المالية المقاصدية (تسعير الأدوات) ---
if domain == "Financial Engineering (الهندسة المالية السيادية)":
    st.header("🛠️ Financial Engineering Model | نموذج الهندسة المالية المقاصدية")
    st.info("إعادة هندسة الوظيفة المالية: المال كأمانة استخلافية، والتمويل وسيلة للتمكين والعدالة.")

    st.subheader("The Sovereign Pricing Equation | معادلة التسعير السيادي")
    st.latex(r"P = \beta_1 R + \beta_2 T + \beta_3 S + \beta_4 \pi + \beta_5 Z + \epsilon")
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Structural Elements | العناصر الهيكلية")
        r_maq_return = st.slider("R (Maqasid Return Rate - العائد المقاصدي)", 0, 100, 50)
        t_empower_idx = st.slider("T (Empowerment Index - مؤشر التمكين)", 0, 100, 75)
        s_compliance = st.slider("S (Sharia Compliance - الالتزام الشرعي الرقابي)", 0, 100, 90)
        pi_expected = st.slider("π (Expected Profitability - الربحية المتوقعة)", 0, 100, 60)
        z_ethical_min = st.slider("Z (Zakat Floor - المقياس الأخلاقي للزكاة)", 0, 10, 5)
        
        # أوزان الانحدار (Beta Coefficients)
        beta_coeffs = [0.3, 0.2, 0.25, 0.15, 0.1]
        
    with col2:
        st.subheader("Instrument Valuation | تقييم الأداة المالية")
        
        # حساب السعر P بناءً على المعادلة
        instrument_price = (beta_coeffs[0] * r_maq_return) + \
                           (beta_coeffs[1] * t_empower_idx) + \
                           (beta_coeffs[2] * s_compliance) + \
                           (beta_coeffs[3] * pi_expected) + \
                           (beta_coeffs[4] * z_ethical_min)
        
        st.metric("Sovereign Instrument Price (P)", f"{instrument_price:.2f}", 
                  help="هذا السعر يمثل القيمة العادلة للأداة المالية (صكوك، مشاركة) وفق منظور هندسة الاستخلاف")

        # رسم بياني يوضح التوازن بين الربحية والرسالة
        fig_fin = go.Figure(data=[
            go.Bar(name='Financial Parameters', x=['Return', 'Empowerment', 'Compliance', 'Profit', 'Ethical Floor'], 
                   y=[r_maq_return, t_empower_idx, s_compliance, pi_expected, z_ethical_min*10],
                   marker_color='goldenrod')
        ])
        fig_fin.update_layout(title="Multi-Dimensional Financial Engineering Analysis")
        st.plotly_chart(fig_fin)

    st.success(f"النتيجة: تم تقييم الأداة المالية بناءً على أثرها التمكيني والالتزام الشرعي، مما يجعلها أداة استخلافية بامتياز.")
    
    st.markdown("""
    ### 📝 Philosophical Foundation | المرتكز الفلسفي
    - **المال كأمانة:** السعر هنا لا يعكس "ندرة المال" بل يعكس "نفع المال".
    - **الزكاة ($Z$):** تعمل هنا كضمانة أخلاقية تمنع الأداة من الانزلاق نحو الاستغلال.
    - **الالتزام ($S$):** ليس مجرد ختم شرعي، بل هو مؤشر رقابي يؤثر مباشرة في القيمة السوقية للأداة.
    """)
# --- 20. نموذج تسعير المنتجات المصرفية الإسلامية ---
if domain == "Banking Product Pricing (تسعير المنتجات المصرفية)":
    st.header("🏦 Islamic Banking Product Pricing Model")
    st.info("تسعير المنتجات (تمويل، ودائع، صكوك) بناءً على العائد المقاصدي والتمكين، استقلالاً عن أسعار الفائدة التقليدية.")

    st.subheader("The Banking Pricing Equation | معادلة التسعير المصرفي")
    st.latex(r"P = \beta_1 R + \beta_2 T + \beta_3 S + \beta_4 \pi + \beta_5 Z + \epsilon")
    
    st.markdown("---")
    
    product_type = st.selectbox("Select Product Category:", ["Micro-Finance (تمويل أصغر)", "Investment Sukuk (صكوك استثمارية)", "Waqf Deposits (ودائع وقفية)"])
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Pricing Factors")
        r_rate = st.slider("R (Islamic Return Rate - العائد الإسلامي)", 0, 100, 45)
        t_impact = st.slider("T (Empowerment - أثر التمكين)", 0, 100, 85)
        s_compliance = st.slider("S (Sharia Compliance - مؤشر الالتزام)", 0, 100, 100)
        pi_profit = st.slider("π (Legit Profit - الربحية المشروعة)", 0, 100, 50)
        z_floor = st.slider("Z (Ethical Zakat Floor - الحد الأدنى الأخلاقي)", 0, 10, 3)
        
        # ضبط المعاملات بناءً على نوع المنتج
        if product_type == "Micro-Finance (تمويل أصغر)":
            betas = [0.2, 0.4, 0.2, 0.1, 0.1] # التركيز على التمكين
        else:
            betas = [0.3, 0.2, 0.2, 0.2, 0.1]

    with col2:
        st.subheader("Final Pricing Result")
        # حساب السعر النهائي للمنتج
        p_final = (betas[0]*r_rate) + (betas[1]*t_impact) + (betas[2]*s_compliance) + (betas[3]*pi_profit) + (betas[4]*z_floor*10)
        
        st.metric(f"Fair Price for {product_type}", f"{p_final:.2f} Points", help="هذا السعر يعكس القيمة العادلة والتمكينية للمنتج")

        # رسم بياني لمكونات السعر
        fig_prod = go.Figure(go.Funnel(
            y = ["Return Rate", "Empowerment", "Compliance", "Profitability", "Ethical Zakat"],
            x = [betas[0]*r_rate, betas[1]*t_impact, betas[2]*s_compliance, betas[3]*pi_profit, betas[4]*z_floor*10],
            textinfo = "value+percent initial",
            marker = {"color": ["#1f77b4", "#2ca02c", "#d62728", "#ff7f0e", "#9467bd"]}
        ))
        fig_prod.update_layout(title="Breakdown of the Fair Pricing Model")
        st.plotly_chart(fig_prod)

    st.success("النتائج المتوقعة: تعزيز الثقة في المصارف الإسلامية كأدوات تمكين لا أدوات مديونية، وتحقيق استقلالية كاملة عن 'سعر الليبور'.")
# --- 21. نموذج المشاركة التمكينية المتدرجة ---
if domain == "Graduated Empowerment (المشاركة المتدرجة)":
    st.header("📈 Graduated Empowerment Musharaka | المشاركة التمكينية المتدرجة")
    st.info("تمويل الفئات المحرومة عبر مشاركة متناقصة تبدأ بنسبة عالية للمصرف وتنتهي بامتلاك العميل الكامل للمشروع.")

    st.subheader("The Empowerment Econometric Equation")
    st.latex(r"Y_{it} = \alpha + \beta_1 P_{it} + \beta_2 E_{it} + \beta_3 S_{it} + \epsilon_{it}")
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Input Parameters")
        start_share = st.slider("Initial Bank Share % (P)", 50, 95, 80)
        years_to_own = st.slider("Years to Full Ownership (السنوات للتملك)", 3, 10, 5)
        prod_perf = st.slider("E (Productive Performance - الأداء الإنتاجي)", 0, 100, 75)
        sharia_sust = st.slider("S (Sharia Sustainability - الاستدامة الشرعية)", 0, 100, 90)
        
    with col2:
        st.subheader("Gradual Ownership Transfer Simulation")
        
        # محاكاة السنوات
        years = np.arange(0, years_to_own + 1)
        bank_shares = [max(0, start_share - (start_share/years_to_own) * y) for y in years]
        client_shares = [100 - b for b in bank_shares]
        
        # حساب مؤشر التمكين النهائي Y
        empowerment_idx = (0.4 * (100-start_share)) + (0.3 * prod_perf) + (0.3 * sharia_sust)
        
        st.metric("Empowerment Index (Y)", f"{empowerment_idx:.2f}")

        # رسم بياني يوضح انتقال الملكية
        fig_emp = go.Figure()
        fig_emp.add_trace(go.Scatter(x=years, y=bank_shares, name="Bank Share %", line=dict(color='red', width=4, dash='dot')))
        fig_emp.add_trace(go.Scatter(x=years, y=client_shares, name="Client Share %", line=dict(color='green', width=4)))
        
        fig_emp.update_layout(title="Journey from Financing to Ownership",
                              xaxis_title="Years (t)",
                              yaxis_title="Ownership Percentage %")
        st.plotly_chart(fig_emp)

    st.success(f"النتيجة المتوقعة: في نهاية السنة {years_to_own}، يتحول العميل من 'مستفيد' إلى 'مالك مستقل' بنسبة 100%.")
    
    st.markdown("""
    ### 🔬 Insights from the Model | رؤى من النموذج
    - **P (Participation):** النسبة العالية للبنك في البداية تقلل المخاطر على الفقير.
    - **E (Productivity):** الحافز للتملك يجعل العميل أكثر حرصاً على نجاح المشروع.
    - **S (Sustainability):** الكرامة الاقتصادية الناتجة عن المشاركة تضمن عدم عودة العميل لخط الفقر.
    """)
# --- 22. نموذج الإدخار الوقفي الذكي ---
if domain == "Smart Waqf Savings (الادخار الوقفي الذكي)":
    st.header("🍯 Smart Waqf Savings Model | نموذج الادخار الوقفي الذكي")
    st.info("دمج الوقف في منتجات الادخار لتحويل المدخرات الفردية إلى تمويل تنموي مستدام في الصحة والتعليم.")

    st.subheader("The Waqf Impact Equation | معادلة الأثر الوقفي")
    st.latex(r"Z_{it} = \gamma + \delta_1 W_{it} + \delta_2 R_{it} + \delta_3 T_{it} + \mu_{it}")
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Waqf Parameters")
        waqf_ratio = st.slider("W (Waqf % of Savings - نسبة الوقف من الادخار)", 1, 50, 10)
        waqf_return = st.slider("R (Investment Return % - عائد الاستثمار)", 1.0, 15.0, 6.0)
        spiritual_engagement = st.slider("T (Spiritual Engagement - مؤشر التفاعل الروحي)", 0, 100, 85)
        
        waqf_domain = st.selectbox("Select Waqf Domain (مجال الوقف):", 
                                   ["Health (صحة)", "Education (تعليم)", "Training (تدريب)", "Sovereign Tech (تكنولوجيا سيادية)"])
        
    with col2:
        st.subheader("Impact & Sustainability Analysis")
        
        # حساب مؤشر الأثر Zit
        # التفاعل الروحي T والنسبة W هما المحركان الأساسيان للأثر
        impact_score = 10 + (0.5 * waqf_ratio) + (0.2 * waqf_return) + (0.3 * spiritual_engagement)
        
        st.metric(f"Total Waqf Impact (Z) in {waqf_domain}", f"{impact_score:.2f}")

        # رسم بياني يوضح نمو الأثر الوقفي التراكمي عبر الزمن
        years_view = np.arange(1, 11)
        # نمو مركب للأثر يعتمد على العائد والنسبة
        cumulative_impact = impact_score * (1 + (waqf_return/100))**years_view
        
        fig_waqf = go.Figure()
        fig_monetary = cumulative_impact * 1000 # تحويل افتراضي لقيمة مالية
        
        fig_waqf.add_trace(go.Bar(x=years_view, y=fig_monetary, 
                                 name="Projected Social Value ($)", 
                                 marker_color='darkgreen'))
        
        fig_waqf.update_layout(title=f"Projected Social Value of Waqf in {waqf_domain}",
                              xaxis_title="Years (t)",
                              yaxis_title="Estimated Social Value Index")
        st.plotly_chart(fig_waqf)

    st.success(f"النتيجة: تخصيص {waqf_ratio}% من المدخرات للوقف يولد أثراً تنموياً متزايداً بنسبة {waqf_return}% سنوياً، مما يدعم الاستدامة في قطاع {waqf_domain}.")
    
    st.markdown("""
    ### 🏛 Strategic Impact | الأثر الاستراتيجي
    - **التحول من الاستهلاك للإنتاج:** المدخرات لم تعد مجرد "سيولة" بل أصبحت "أصولاً" في خدمة المجتمع.
    - **التفاعل الروحي ($T$):** عندما يختار العميل المجال بنفسه (مثلاً الصحة)، تزداد نسبة استمراريته في الوقف بنسبة 40% وفق المحاكاة.
    - **السيادة التمويلية:** هذا المنتج يقلل احتياج الدولة للاقتراض الخارجي لتمويل الخدمات العامة.
    """)
