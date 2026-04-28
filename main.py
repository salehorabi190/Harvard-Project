import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
st.set_page_config(page_title="S.E.P 2026 | Prof. Dr. Saleh Orabi",layout="wide")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&family=Amiri:wght@700&display=swap');
.stApp{background-color:#f4f7f6;font-family:'Cairo',sans-serif;}
.logo-container{text-align:center;padding:45px;background:linear-gradient(135deg,#0f3d2e 0%,#08251b 100%);border-radius:30px;border-bottom:12px solid #d4af37;margin-bottom:40px;color:white;box-shadow:0 20px 40px rgba(0,0,0,0.4);}
.logo-text{font-family:'Amiri',serif;font-size:80px;letter-spacing:4px;}
.section-title{font-family:'Cairo',sans-serif;font-size:28px;font-weight:700;color:#0f3d2e;text-align:right;margin-bottom:10px;}
.card-btn{background:white;border:3px solid #d4af37;padding:22px 18px;border-radius:18px;font-family:'Cairo',sans-serif;font-size:18px;font-weight:700;color:#0f3d2e;width:100%;text-align:right;box-shadow:0 10px 25px rgba(0,0,0,0.08);transition:0.25s;}
.card-btn:hover{background:#0f3d2e;color:white;transform:translateY(-3px);cursor:pointer;}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px;}
.explanation-box{background:#ffffff;border-left:5px solid #d4af37;padding:15px 18px;border-radius:10px;margin:10px 0 20px 0;font-size:15px;}
.header-style{font-family:'Cairo',sans-serif;font-size:30px;font-weight:800;color:#0f3d2e;text-align:right;margin-top:10px;}
</style>
""",unsafe_allow_html=True)
st.markdown("""
<div class="logo-container">
<div class="logo-text">S.E.P 2026</div>
<div style="font-size:32px;color:#d4af37;font-weight:bold;margin-top:15px;">بروتوكول هندسة الاستخلاف الاقتصادي</div>
<div style="font-size:20px;opacity:0.9;">إعداد وتطوير: أ.د. صالح عرابي - 2026</div>
</div>
""",unsafe_allow_html=True)
col_lang1,col_lang2=st.columns([1,3])
with col_lang1:
    lang=st.radio("Language / اللغة",["العربية","English"],index=0)
st.session_state["lang"]=lang
models={
"P1. الإدخار الوقفي الذكي":"p1",
"P2. المشاركة التمكينية المتدرجة":"p2",
"P3. الصكوك الوقفية التنموية":"p3",
"P4. المضاربة الاجتماعية التمكينية":"p4",
"P5. صندوق الوقف التمكيني المشترك":"p5",
"P6. الإجارة الوقفية الموصوفة في الذمة":"p6",
"1. نموذج الأثر الرمزي":"m1",
"2. نموذج القيادة المتزكية":"m2",
"3. نموذج الحوكمة الرمزية":"m3",
"4. نموذج الاستثمار التزكوي":"m4",
"5. نموذج التقييم التزكوي":"m5",
"6. نموذج التحقق الوجودي":"m6",
"7. القيمة التزكوية المضافة":"m7",
"السُّنن في السياسات الاقتصادية":"m8_m11",
"تطبيق السياسات الاقتصادية السننية":"m12_m15",
"هندسة السوق: من التبادل إلى التزكية":"m16_m19",
"هندسة العرض والطلب المقاصدية":"m20_m23",
"24. التمكين المالي العام":"m24",
"25. النموذج النقدي المركب":"m25",
"26. هندسة سعر الصرف":"m26",
"27. هندسة سعر الفائدة":"m27",
"28. هندسة المالية المقاصدية":"m28",
"29. تسعير المنتجات المصرفية":"m29",
"30. خوارزمية التقييم الشرعي التنبؤية":"m30",
"31. مؤشر الأمان الشرعي":"m31",
"32. بروتوكول الإشراف وتصنيف الأصول":"m32",
"33. بروتوكول أمانة (مؤشر البركة)":"m33"
}
st.markdown("<div class='section-title'>النماذج الهندسية</div>",unsafe_allow_html=True)
st.markdown("<div class='grid'>",unsafe_allow_html=True)
for label,key in models.items():
    if st.button(label,key=f"btn_{key}"):
        st.session_state["mid"]=key
        st.session_state["choice"]=label
st.markdown("</div>",unsafe_allow_html=True)
# ------------------ دالة Dashboard الديناميكية ------------------
def dashboard(title, main_value, radar_labels, radar_values, bar_labels, bar_values):
    st.markdown(f"<h2 class='header-style'>{title}</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    # ----------- Gauge Meter (المؤشر الرئيسي) -----------
    with col1:
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=main_value,
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': '#0f3d2e'},
                'steps': [
                    {'range': [0, 50], 'color': '#d4af37'},
                    {'range': [50, 100], 'color': '#0f3d2e'}
                ],
            },
            number={'suffix': "%", 'font': {'size': 40}}
        ))
        fig_gauge.update_layout(height=350, margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig_gauge, use_container_width=True)

    # ----------- Radar Chart (الأبعاد) -----------
    with col2:
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=radar_values,
            theta=radar_labels,
            fill='toself',
            line=dict(color='#0f3d2e', width=3)
        ))
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100])
            ),
            showlegend=False,
            height=350,
            margin=dict(l=10, r=10, t=10, b=10)
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    # ----------- Bar Chart (المقارنات) -----------
    fig_bar = px.bar(
        x=bar_labels,
        y=bar_values,
        color=bar_values,
        color_continuous_scale=["#d4af37", "#0f3d2e"]
    )
    fig_bar.update_layout(
        height=350,
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis_title="",
        yaxis_title="القيمة"
    )
    st.plotly_chart(fig_bar, use_container_width=True)
    # ------------------ دوال النماذج P1–P6 ------------------

def model_p1(lang):
    st.markdown(f"<h1 class='header-style'>P1. الإدخار الوقفي الذكي</h1>", unsafe_allow_html=True)
    st.latex(r"Z_{it} = \gamma + \delta_1 W_{it} + \delta_2 R_{it} + \delta_3 T_{it} + \mu_{it}")
    desc="مُنْتَجُ الإِدِّخَارِ الوَقْفِيِّ الذَّكِيِّ: يتيح للعميل تخصيص نسبة من مدخراته كوقف يُستثمر في مشاريع تنموية." if lang=="العربية" else "Smart Endowment Savings: A model integrating waqf into savings for sustainable development."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    col1,col2,col3=st.columns(3)
    with col1: v1=st.number_input("Wit",0.0,100.0,80.0,key="wit_p1")
    with col2: v2=st.number_input("Rit",0.0,100.0,70.0,key="rit_p1")
    with col3: v3=st.number_input("Tit",0.0,100.0,90.0,key="tit_p1")
    z=(0.4*v1+0.3*v2+0.3*v3)
    dashboard("مؤشرات نموذج P1",z,["Wit","Rit","Tit"],[v1,v2,v3],["Wit","Rit","Tit"],[v1,v2,v3])
    st.metric("Zit",f"{z:.2f}")

def model_p2(lang):
    st.markdown(f"<h1 class='header-style'>P2. المشاركة التمكينية المتدرجة</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{it} = \alpha + \beta_1 P_{it} + \beta_2 E_{it} + \beta_3 S_{it} + \epsilon_{it}")
    desc="مشاركة تمكينية تتناقص فيها حصة المصرف 20% سنوياً حتى التملك الكامل." if lang=="العربية" else "Progressive empowerment participation with decreasing bank share."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    col1,col2,col3=st.columns(3)
    with col1: v1=st.number_input("Pit",0.0,100.0,80.0,key="pit_p2")
    with col2: v2=st.number_input("Eit",0.0,100.0,70.0,key="eit_p2")
    with col3: v3=st.number_input("Sit",0.0,100.0,90.0,key="sit_p2")
    y=(0.4*v1+0.3*v2+0.3*v3)
    dashboard("مؤشرات نموذج P2",y,["Pit","Eit","Sit"],[v1,v2,v3],["Pit","Eit","Sit"],[v1,v2,v3])
    st.metric("Yit",f"{y:.2f}")

def model_p3(lang):
    st.markdown(f"<h1 class='header-style'>P3. الصكوك الوقفية التنموية</h1>", unsafe_allow_html=True)
    st.latex(r"W_{it} = \theta + \lambda_1 C_{it} + \lambda_2 R_{it} + \lambda_3 I_{it} + \nu_{it}")
    desc="صكوك وقفية ذكية تجمع بين الربح والاستدامة الوقفية." if lang=="العربية" else "Smart waqf sukuk combining profit and endowment sustainability."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    col1,col2,col3=st.columns(3)
    with col1: v1=st.number_input("Cit",0.0,10000.0,500.0,key="cit_p3")
    with col2: v2=st.number_input("Rit",0.0,100.0,20.0,key="rit_p3")
    with col3: v3=st.number_input("Iit",0.0,100.0,80.0,key="iit_p3")
    w=(0.01*v1+0.4*v2+0.5*v3)
    dashboard("مؤشرات نموذج P3",w,["Cit","Rit","Iit"],[v1,v2,v3],["Cit","Rit","Iit"],[v1,v2,v3])
    st.metric("Wit",f"{w:.2f}")

def model_p4(lang):
    st.markdown(f"<h1 class='header-style'>P4. المضاربة الاجتماعية التمكينية</h1>", unsafe_allow_html=True)
    st.latex(r"Y_{it} = \alpha + \beta_1 P_{it} + \beta_2 E_{it} + \beta_3 S_{it} + \epsilon_{it}")
    desc="مضاربة اجتماعية لتمكين الفئات المحرومة عبر مشاركة متدرجة." if lang=="العربية" else "Social mudaraba for empowerment."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    col1,col2,col3=st.columns(3)
    with col1: v1=st.number_input("Pit",0.0,100.0,80.0,key="pit_p4")
    with col2: v2=st.number_input("Eit",0.0,100.0,75.0,key="eit_p4")
    with col3: v3=st.number_input("Sit",0.0,100.0,90.0,key="sit_p4")
    y=(0.4*v1+0.3*v2+0.3*v3)
    dashboard("مؤشرات نموذج P4",y,["Pit","Eit","Sit"],[v1,v2,v3],["Pit","Eit","Sit"],[v1,v2,v3])
    st.metric("Yit",f"{y:.2f}")

def model_p5(lang):
    st.markdown(f"<h1 class='header-style'>P5. صندوق الوقف التمكيني المشترك</h1>", unsafe_allow_html=True)
    st.latex(r"Q_{it} = \psi + \eta_1 V_{it} + \eta_2 D_{it} + \eta_3 B_{it} + \xi_{it}")
    desc="صندوق يجمع بين أموال الوقف والمستثمرين لتمويل مشاريع إنتاجية." if lang=="العربية" else "Joint waqf-investor empowerment fund."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    col1,col2,col3=st.columns(3)
    with col1: v1=st.number_input("Vit",0.0,10000.0,600.0,key="vit_p5")
    with col2: v2=st.number_input("Dit",0.0,100.0,100.0,key="dit_p5")
    with col3: v3=st.number_input("Bit",0.0,100.0,15.0,key="bit_p5")
    q=(0.02*v1+0.5*v2+0.3*v3)
    dashboard("مؤشرات نموذج P5",q,["Vit","Dit","Bit"],[v1,v2,v3],["Vit","Dit","Bit"],[v1,v2,v3])
    st.metric("Qit",f"{q:.2f}")

def model_p6(lang):
    st.markdown(f"<h1 class='header-style'>P6. الإجارة الوقفية الموصوفة في الذمة</h1>", unsafe_allow_html=True)
    st.latex(r"H_{it} = \omega + \sigma_1 E_{it} + \sigma_2 Q_{it} + \sigma_3 K_{it} + \varsigma_{it}")
    desc="إجارة وقفية لتمويل السكن أو التعليم أو العلاج للفقراء." if lang=="العربية" else "Forward waqf ijarah for social services."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    col1,col2,col3=st.columns(3)
    with col1: v1=st.number_input("Eit",0.0,100.0,80.0,key="eit_p6")
    with col2: v2=st.number_input("Qit",0.0,100.0,85.0,key="qit_p6")
    with col3: v3=st.number_input("Kit",0.0,100.0,100.0,key="kit_p6")
    h=(0.3*v1+0.3*v2+0.4*v3)
    dashboard("مؤشرات نموذج P6",h,["Eit","Qit","Kit"],[v1,v2,v3],["Eit","Qit","Kit"],[v1,v2,v3])
    st.metric("Hit",f"{h:.2f}")
    # ------------------ دوال النماذج M1–M7 ------------------

def model_m1(lang):
    st.markdown(f"<h1 class='header-style'>M1. نموذج الأثر الرمزي</h1>",unsafe_allow_html=True)
    st.latex(r"P_r=\alpha+\beta_1R_r+\beta_2M_r+\beta_3T_r+\beta_4C_r+\epsilon_r")
    desc="نموذج يربط بين الرسالة والمعنى والتزكية والتواصل لإنتاج أثر رمزي في الأداء." if lang=="العربية" else "Symbolic impact model linking mission, meaning, tazkiyah and communication."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    tabs=st.tabs(["Rr","Mr","Tr","Cr","α & ε"])
    with tabs[0]:
        r1=st.slider("وضوح الرسالة",1,5,4);r2=st.slider("تجسيد الرسالة",1,5,4);r3=st.slider("الالتزام بالرسالة",1,5,4);Rr=(r1+r2+r3)/3
    with tabs[1]:
        m1=st.slider("المعنى الداخلي",1,5,5);m2=st.slider("الانتماء",1,5,4);m3=st.slider("الحافز القيمي",1,5,5);Mr=(m1+m2+m3)/3
    with tabs[2]:
        t1=st.slider("تزكية الوقت",1,5,3);t2=st.slider("تزكية السلوك",1,5,3);t3=st.slider("التوازن الروحي",1,5,4);Tr=(t1+t2+t3)/3
    with tabs[3]:
        c1=st.slider("لغة رمزية",1,5,3);c2=st.slider("إشارات رمزية",1,5,4);c3=st.slider("تواصل قيمي",1,5,4);Cr=(c1+c2+c3)/3
    with tabs[4]:
        alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    Pr=alpha+(0.3*Rr)+(0.25*Mr)+(0.2*Tr)+(0.15*Cr)+(0.1*eps)
    dashboard("مؤشرات نموذج M1",Pr*20,["Rr","Mr","Tr","Cr"],[Rr*20,Mr*20,Tr*20,Cr*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Pr",f"{Pr:.2f}")

def model_m2(lang):
    st.markdown(f"<h1 class='header-style'>M2. نموذج القيادة المتزكية</h1>",unsafe_allow_html=True)
    st.latex(r"E_r=\alpha+\beta_1Z_r+\beta_2M_r+\beta_3I_r+\beta_4C_r+\beta_5V_r+\beta_6R_r+\epsilon_r")
    desc="قيادة قائمة على التزكية والإلهام والمعنى والتواصل والرسالة." if lang=="العربية" else "Tazkiyah-based leadership model."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    tabs=st.tabs(["Zr","Mr","Ir","Cr","Vr","Rr","α","ε"])
    with tabs[0]:z1=st.slider("تزكية ذاتية",1,5,4);z2=st.slider("نمو روحي",1,5,3);z3=st.slider("ضبط الأنا",1,5,4);Zr=(z1+z2+z3)/3
    with tabs[1]:m1=st.slider("معنى",1,5,5);m2=st.slider("انتماء",1,5,4);m3=st.slider("قيم",1,5,4);Mr=(m1+m2+m3)/3
    with tabs[2]:i1=st.slider("إلهام",1,5,4);i2=st.slider("قصص رمزية",1,5,4);Ir=(i1+i2)/2
    with tabs[3]:c1=st.slider("تواصل رمزي",1,5,3);c2=st.slider("إشارات",1,5,4);Cr=(c1+c2)/2
    with tabs[4]:v1=st.slider("توافق قيم",1,5,5);v2=st.slider("ثقافة رمزية",1,5,4);Vr=(v1+v2)/2
    with tabs[5]:r1=st.slider("رسالة",1,5,4);r2=st.slider("تجسيد الرسالة",1,5,5);Rr=(r1+r2)/2
    with tabs[6]:alpha=st.slider("α",1,5,5)
    with tabs[7]:eps=st.slider("ε",1,5,5)
    Er=alpha+(0.2*Zr)+(0.15*Mr)+(0.15*Ir)+(0.1*Cr)+(0.15*Vr)+(0.15*Rr)+(0.1*eps)
    dashboard("مؤشرات نموذج M2",Er*20,["Zr","Mr","Ir","Cr","Vr","Rr"],[Zr*20,Mr*20,Ir*20,Cr*20,Vr*20,Rr*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Er",f"{Er:.2f}")

def model_m3(lang):
    st.markdown(f"<h1 class='header-style'>M3. نموذج الحوكمة الرمزية</h1>",unsafe_allow_html=True)
    st.latex(r"G_r=\alpha+\beta_1N_r+\beta_2T_r+\beta_3M_r+\beta_4A_r+\epsilon_r")
    desc="حوكمة تربط بين النية والمعنى والتزكية والنظام المؤسسي." if lang=="العربية" else "Symbolic governance model."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    tabs=st.tabs(["Nr","Tr","Mr","Ar","α","ε"])
    with tabs[0]:n1=st.slider("نية",1,5,4);n2=st.slider("قصد",1,5,4);Nr=(n1+n2)/2
    with tabs[1]:t1=st.slider("تزكية",1,5,3);t2=st.slider("توازن",1,5,4);Tr=(t1+t2)/2
    with tabs[2]:m1=st.slider("معنى",1,5,5);m2=st.slider("قيم",1,5,4);Mr=(m1+m2)/2
    with tabs[3]:a1=st.slider("نظام",1,5,4);a2=st.slider("إجراءات",1,5,4);Ar=(a1+a2)/2
    with tabs[4]:alpha=st.slider("α",1,5,5)
    with tabs[5]:eps=st.slider("ε",1,5,5)
    Gr=alpha+(0.25*Nr)+(0.2*Tr)+(0.2*Mr)+(0.25*Ar)+(0.1*eps)
    dashboard("مؤشرات نموذج M3",Gr*20,["Nr","Tr","Mr","Ar"],[Nr*20,Tr*20,Mr*20,Ar*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Gr",f"{Gr:.2f}")

def model_m4(lang):
    st.markdown(f"<h1 class='header-style'>M4. نموذج الاستثمار التزكوي</h1>",unsafe_allow_html=True)
    st.latex(r"S_r=\alpha+\beta_1Z_r+\beta_2E_r+\beta_3M_r+\epsilon_r")
    desc="استثمار قائم على التزكية والمعنى والأثر." if lang=="العربية" else "Tazkiyah-based investment model."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    z=st.slider("Zr",1,5,4);e=st.slider("Er",1,5,4);m=st.slider("Mr",1,5,5);alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    Sr=alpha+(0.3*z)+(0.3*e)+(0.3*m)+(0.1*eps)
    dashboard("مؤشرات نموذج M4",Sr*20,["Zr","Er","Mr"],[z*20,e*20,m*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Sr",f"{Sr:.2f}")

def model_m5(lang):
    st.markdown(f"<h1 class='header-style'>M5. نموذج التقييم التزكوي</h1>",unsafe_allow_html=True)
    st.latex(r"T_r=\alpha+\beta_1M_r+\beta_2Z_r+\beta_3C_r+\epsilon_r")
    desc="تقييم يعتمد على المعنى والتزكية والتواصل." if lang=="العربية" else "Tazkiyah-based evaluation model."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    m=st.slider("Mr",1,5,5);z=st.slider("Zr",1,5,4);c=st.slider("Cr",1,5,4);alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    Tr=alpha+(0.3*m)+(0.3*z)+(0.3*c)+(0.1*eps)
    dashboard("مؤشرات نموذج M5",Tr*20,["Mr","Zr","Cr"],[m*20,z*20,c*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Tr",f"{Tr:.2f}")

def model_m6(lang):
    st.markdown(f"<h1 class='header-style'>M6. نموذج التحقق الوجودي</h1>",unsafe_allow_html=True)
    st.latex(r"E_x=\alpha+\beta_1M_x+\beta_2T_x+\beta_3R_x+\epsilon_x")
    desc="نموذج يقيس تحقق الإنسان بوجوده عبر المعنى والتزكية والرسالة." if lang=="العربية" else "Existential verification model."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    m=st.slider("Mx",1,5,5);t=st.slider("Tx",1,5,4);r=st.slider("Rx",1,5,4);alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    Ex=alpha+(0.3*m)+(0.3*t)+(0.3*r)+(0.1*eps)
    dashboard("مؤشرات نموذج M6",Ex*20,["Mx","Tx","Rx"],[m*20,t*20,r*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Ex",f"{Ex:.2f}")

def model_m7(lang):
    st.markdown(f"<h1 class='header-style'>M7. القيمة التزكوية المضافة</h1>",unsafe_allow_html=True)
    st.latex(r"Z_v=\alpha+\beta_1S_r+\beta_2M_r+\beta_3T_r+\epsilon_r")
    desc="قياس القيمة التزكوية المضافة في العمل أو المؤسسة." if lang=="العربية" else "Added tazkiyah value model."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    s=st.slider("Sr",1,5,4);m=st.slider("Mr",1,5,5);t=st.slider("Tr",1,5,4);alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    Zv=alpha+(0.3*s)+(0.3*m)+(0.3*t)+(0.1*eps)
    dashboard("مؤشرات نموذج M7",Zv*20,["Sr","Mr","Tr"],[s*20,m*20,t*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Zv",f"{Zv:.2f}")
    # ------------------ دوال النماذج M8–M15 ------------------

def model_m8_m11(lang):
    st.markdown(f"<h1 class='header-style'>M8–M11. السُنن في السياسات الاقتصادية</h1>",unsafe_allow_html=True)
    st.latex(r"S_e=\alpha+\beta_1F_e+\beta_2T_e+\beta_3M_e+\beta_4R_e+\epsilon_e")
    desc="نماذج السنن الاقتصادية: الفطرة، التوازن، الميزان، الرحمة كأسس لصياغة السياسات." if lang=="العربية" else "Economic Sunnah models: fitrah, balance, justice, mercy as policy foundations."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    f=st.slider("Fitrah",1,5,4);t=st.slider("Tawazun",1,5,4);m=st.slider("Mizan",1,5,5);r=st.slider("Rahmah",1,5,5);alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    Se=alpha+(0.25*f)+(0.25*t)+(0.25*m)+(0.15*r)+(0.1*eps)
    dashboard("مؤشرات السنن الاقتصادية",Se*20,["Fitrah","Tawazun","Mizan","Rahmah"],[f*20,t*20,m*20,r*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Se",f"{Se:.2f}")

def model_m12_m15(lang):
    st.markdown(f"<h1 class='header-style'>M12–M15. تطبيق السياسات الاقتصادية السننية</h1>",unsafe_allow_html=True)
    st.latex(r"A_s=\alpha+\beta_1I_s+\beta_2J_s+\beta_3T_s+\epsilon_s")
    desc="تطبيق السنن في السياسات: الإحسان، العدل، التوازن، التكافل." if lang=="العربية" else "Applying Sunnah principles: benevolence, justice, balance, solidarity."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    i=st.slider("Ihsan",1,5,5);j=st.slider("Justice",1,5,4);t=st.slider("Tawazun",1,5,4);alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    As=alpha+(0.3*i)+(0.3*j)+(0.3*t)+(0.1*eps)
    dashboard("مؤشرات تطبيق السنن",As*20,["Ihsan","Justice","Tawazun"],[i*20,j*20,t*20],["α","ε"],[alpha*20,eps*20])
    st.metric("As",f"{As:.2f}")

def model_m16_m19(lang):
    st.markdown(f"<h1 class='header-style'>M16–M19. هندسة السوق: من التبادل إلى التزكية</h1>",unsafe_allow_html=True)
    st.latex(r"Z_m=\alpha+\beta_1E_m+\beta_2F_m+\beta_3T_m+\epsilon_m")
    desc="تحويل السوق من مجرد تبادل إلى تزكية عبر الأخلاق والعدل والرحمة." if lang=="العربية" else "Transforming markets from exchange to tazkiyah."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    e=st.slider("Ethics",1,5,5);f=st.slider("Fairness",1,5,4);t=st.slider("Tazkiyah",1,5,4);alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    Zm=alpha+(0.3*e)+(0.3*f)+(0.3*t)+(0.1*eps)
    dashboard("مؤشرات هندسة السوق",Zm*20,["Ethics","Fairness","Tazkiyah"],[e*20,f*20,t*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Zm",f"{Zm:.2f}")

def model_m20_m23(lang):
    st.markdown(f"<h1 class='header-style'>M20–M23. هندسة العرض والطلب المقاصدية</h1>",unsafe_allow_html=True)
    st.latex(r"D_c=\alpha+\beta_1S_c+\beta_2N_c+\beta_3M_c+\epsilon_c")
    desc="هندسة العرض والطلب وفق المقاصد: السعة، الندرة، المنفعة." if lang=="العربية" else "Maqasid-based supply-demand engineering."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    s=st.slider("Sa'ah (Availability)",1,5,4);n=st.slider("Nadra (Scarcity)",1,5,3);m=st.slider("Manfa'ah (Utility)",1,5,5);alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    Dc=alpha+(0.3*s)+(0.3*n)+(0.3*m)+(0.1*eps)
    dashboard("مؤشرات هندسة العرض والطلب",Dc*20,["Sa'ah","Nadra","Manfa'ah"],[s*20,n*20,m*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Dc",f"{Dc:.2f}")
    # ------------------ دوال النماذج M24–M29 ------------------

def model_m24(lang):
    st.markdown(f"<h1 class='header-style'>M24. التمكين المالي العام</h1>",unsafe_allow_html=True)
    st.latex(r"E_f=\alpha+\beta_1A_f+\beta_2S_f+\beta_3T_f+\epsilon_f")
    desc="نموذج يقيس التمكين المالي العام عبر الوصول، السعة، التمكين." if lang=="العربية" else "General financial empowerment model."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    a=st.slider("Access",1,5,4);s=st.slider("Capacity",1,5,4);t=st.slider("Empowerment",1,5,5);alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    Ef=alpha+(0.3*a)+(0.3*s)+(0.3*t)+(0.1*eps)
    dashboard("مؤشرات التمكين المالي",Ef*20,["Access","Capacity","Empowerment"],[a*20,s*20,t*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Ef",f"{Ef:.2f}")

def model_m25(lang):
    st.markdown(f"<h1 class='header-style'>M25. النموذج النقدي المركب</h1>",unsafe_allow_html=True)
    st.latex(r"M_c=\alpha+\beta_1L_c+\beta_2S_c+\beta_3I_c+\epsilon_c")
    desc="نموذج نقدي يجمع بين السيولة، الاستقرار، الاستثمار." if lang=="العربية" else "Composite monetary model."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    l=st.slider("Liquidity",1,5,4);s=st.slider("Stability",1,5,4);i=st.slider("Investment",1,5,5);alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    Mc=alpha+(0.3*l)+(0.3*s)+(0.3*i)+(0.1*eps)
    dashboard("مؤشرات النموذج النقدي",Mc*20,["Liquidity","Stability","Investment"],[l*20,s*20,i*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Mc",f"{Mc:.2f}")

def model_m26(lang):
    st.markdown(f"<h1 class='header-style'>M26. هندسة سعر الصرف</h1>",unsafe_allow_html=True)
    st.latex(r"X_r=\alpha+\beta_1S_r+\beta_2D_r+\beta_3I_r+\epsilon_r")
    desc="هندسة سعر الصرف عبر العرض والطلب والتدفقات الاستثمارية." if lang=="العربية" else "Exchange rate engineering."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    s=st.slider("Supply",1,5,4);d=st.slider("Demand",1,5,4);i=st.slider("Inflows",1,5,5);alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    Xr=alpha+(0.3*s)+(0.3*d)+(0.3*i)+(0.1*eps)
    dashboard("مؤشرات سعر الصرف",Xr*20,["Supply","Demand","Inflows"],[s*20,d*20,i*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Xr",f"{Xr:.2f}")

def model_m27(lang):
    st.markdown(f"<h1 class='header-style'>M27. هندسة سعر الفائدة</h1>",unsafe_allow_html=True)
    st.latex(r"R_i=\alpha+\beta_1I_s+\beta_2L_s+\beta_3M_s+\epsilon_s")
    desc="هندسة سعر الفائدة عبر التضخم والسيولة والمال المتداول." if lang=="العربية" else "Interest rate engineering."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    i=st.slider("Inflation",1,5,4);l=st.slider("Liquidity",1,5,4);m=st.slider("Money Supply",1,5,5);alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    Ri=alpha+(0.3*i)+(0.3*l)+(0.3*m)+(0.1*eps)
    dashboard("مؤشرات سعر الفائدة",Ri*20,["Inflation","Liquidity","Money Supply"],[i*20,l*20,m*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Ri",f"{Ri:.2f}")

def model_m28(lang):
    st.markdown(f"<h1 class='header-style'>M28. هندسة المالية المقاصدية</h1>",unsafe_allow_html=True)
    st.latex(r"M_q=\alpha+\beta_1A_q+\beta_2H_q+\beta_3S_q+\epsilon_q")
    desc="مالية قائمة على المقاصد: العدالة، الحفظ، السعة." if lang=="العربية" else "Maqasid-based public finance."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    a=st.slider("Justice",1,5,5);h=st.slider("Protection",1,5,4);s=st.slider("Capacity",1,5,4);alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    Mq=alpha+(0.3*a)+(0.3*h)+(0.3*s)+(0.1*eps)
    dashboard("مؤشرات المالية المقاصدية",Mq*20,["Justice","Protection","Capacity"],[a*20,h*20,s*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Mq",f"{Mq:.2f}")

def model_m29(lang):
    st.markdown(f"<h1 class='header-style'>M29. تسعير المنتجات المصرفية</h1>",unsafe_allow_html=True)
    st.latex(r"P_b=\alpha+\beta_1C_b+\beta_2R_b+\beta_3S_b+\epsilon_b")
    desc="تسعير المنتجات المصرفية وفق التكلفة والعائد والمخاطر." if lang=="العربية" else "Bank product pricing model."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    c=st.slider("Cost",1,5,4);r=st.slider("Return",1,5,4);s=st.slider("Risk",1,5,5);alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    Pb=alpha+(0.3*c)+(0.3*r)+(0.3*s)+(0.1*eps)
    dashboard("مؤشرات التسعير المصرفي",Pb*20,["Cost","Return","Risk"],[c*20,r*20,s*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Pb",f"{Pb:.2f}")
    # ------------------ دوال النماذج M30–M33 ------------------

def model_m30(lang):
    st.markdown(f"<h1 class='header-style'>M30. خوارزمية التقييم الشرعي التنبؤية</h1>",unsafe_allow_html=True)
    st.latex(r"S_p=\alpha+\beta_1C_s+\beta_2R_s+\beta_3M_s+\beta_4T_s+\epsilon_s")
    desc="خوارزمية تنبؤية لتقييم المنتجات المالية وفق الامتثال الشرعي والمقاصدي." if lang=="العربية" else "Predictive Shariah compliance scoring algorithm."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    c=st.slider("Compliance",1,5,5);r=st.slider("Risk",1,5,4);m=st.slider("Maqasid Fit",1,5,5);t=st.slider("Transparency",1,5,4);alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    Sp=alpha+(0.25*c)+(0.25*r)+(0.25*m)+(0.15*t)+(0.1*eps)
    dashboard("مؤشرات التقييم الشرعي",Sp*20,["Compliance","Risk","Maqasid","Transparency"],[c*20,r*20,m*20,t*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Sp",f"{Sp:.2f}")

def model_m31(lang):
    st.markdown(f"<h1 class='header-style'>M31. مؤشر الأمان الشرعي</h1>",unsafe_allow_html=True)
    st.latex(r"S_s=\alpha+\beta_1C_s+\beta_2T_s+\beta_3E_s+\epsilon_s")
    desc="مؤشر يقيس مستوى الأمان الشرعي للمنتجات المالية." if lang=="العربية" else "Shariah safety index."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    c=st.slider("Compliance",1,5,5);t=st.slider("Transparency",1,5,4);e=st.slider("Ethical Fit",1,5,5);alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    Ss=alpha+(0.35*c)+(0.3*t)+(0.25*e)+(0.1*eps)
    dashboard("مؤشرات الأمان الشرعي",Ss*20,["Compliance","Transparency","Ethics"],[c*20,t*20,e*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Ss",f"{Ss:.2f}")

def model_m32(lang):
    st.markdown(f"<h1 class='header-style'>M32. بروتوكول الإشراف وتصنيف الأصول</h1>",unsafe_allow_html=True)
    st.latex(r"A_c=\alpha+\beta_1R_c+\beta_2S_c+\beta_3M_c+\epsilon_c")
    desc="بروتوكول لتصنيف الأصول وفق المخاطر، السلامة، والامتثال الشرعي." if lang=="العربية" else "Supervision and asset classification protocol."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    r=st.slider("Risk Level",1,5,4);s=st.slider("Safety",1,5,5);m=st.slider("Maqasid Fit",1,5,4);alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    Ac=alpha+(0.3*r)+(0.3*s)+(0.3*m)+(0.1*eps)
    dashboard("مؤشرات تصنيف الأصول",Ac*20,["Risk","Safety","Maqasid"],[r*20,s*20,m*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Ac",f"{Ac:.2f}")

def model_m33(lang):
    st.markdown(f"<h1 class='header-style'>M33. بروتوكول أمانة (مؤشر البركة)</h1>",unsafe_allow_html=True)
    st.latex(r"B_k=\alpha+\beta_1N_k+\beta_2E_k+\beta_3S_k+\epsilon_k")
    desc="مؤشر البركة: يقيس أثر النية، الإخلاص، السلوك، والامتثال في البركة الاقتصادية." if lang=="العربية" else "Barakah index measuring intention, ethics, sincerity and compliance."
    st.markdown(f"<div class='explanation-box'><b>💡 {desc}</b></div>",unsafe_allow_html=True)
    n=st.slider("Niyyah (Intention)",1,5,5);e=st.slider("Ikhlas (Sincerity)",1,5,5);s=st.slider("Salook (Ethical Conduct)",1,5,4);alpha=st.slider("α",1,5,5);eps=st.slider("ε",1,5,5)
    Bk=alpha+(0.3*n)+(0.3*e)+(0.3*s)+(0.1*eps)
    dashboard("مؤشرات البركة",Bk*20,["Niyyah","Ikhlas","Salook"],[n*20,e*20,s*20],["α","ε"],[alpha*20,eps*20])
    st.metric("Bk",f"{Bk:.2f}")
    # ------------------ Main Controller ------------------

def run_selected_model():
    if "mid" not in st.session_state:
        st.info("اختر نموذجاً من البطاقات أعلاه للبدء.")
        return
    mid=st.session_state["mid"]
    lang=st.session_state["lang"]
    if mid=="p1": model_p1(lang)
    elif mid=="p2": model_p2(lang)
    elif mid=="p3": model_p3(lang)
    elif mid=="p4": model_p4(lang)
    elif mid=="p5": model_p5(lang)
    elif mid=="p6": model_p6(lang)
    elif mid=="m1": model_m1(lang)
    elif mid=="m2": model_m2(lang)
    elif mid=="m3": model_m3(lang)
    elif mid=="m4": model_m4(lang)
    elif mid=="m5": model_m5(lang)
    elif mid=="m6": model_m6(lang)
    elif mid=="m7": model_m7(lang)
    elif mid=="m8_m11": model_m8_m11(lang)
    elif mid=="m12_m15": model_m12_m15(lang)
    elif mid=="m16_m19": model_m16_m19(lang)
    elif mid=="m20_m23": model_m20_m23(lang)
    elif mid=="m24": model_m24(lang)
    elif mid=="m25": model_m25(lang)
    elif mid=="m26": model_m26(lang)
    elif mid=="m27": model_m27(lang)
    elif mid=="m28": model_m28(lang)
    elif mid=="m29": model_m29(lang)
    elif mid=="m30": model_m30(lang)
    elif mid=="m31": model_m31(lang)
    elif mid=="m32": model_m32(lang)
    elif mid=="m33": model_m33(lang)
    else:
        st.error("النموذج غير معروف.")

run_selected_model()
