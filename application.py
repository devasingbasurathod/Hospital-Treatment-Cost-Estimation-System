import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Healthcare Cost Prediction",
    page_icon="🩺",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#102542,#0b4f6c,#0f766e);
background-size:400% 400%;
animation:gradient 15s ease infinite;
}

@keyframes gradient{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.block-container{
padding-top:1rem;
}

.hero{
padding:30px;
border-radius:25px;
background:rgba(255,255,255,.08);
backdrop-filter:blur(18px);
border:1px solid rgba(255,255,255,.2);
text-align:center;
box-shadow:0px 10px 40px rgba(0,0,0,.35);
margin-bottom:20px;
}

.hero h1{
font-size:45px;
color:white;
}

.hero p{
font-size:18px;
color:#d6f5ff;
}

.card{
background:rgba(255,255,255,.08);
padding:20px;
border-radius:20px;
backdrop-filter:blur(18px);
border:1px solid rgba(255,255,255,.15);
box-shadow:0px 8px 20px rgba(0,0,0,.25);
margin-bottom:20px;
transition:0.4s;
}

.card:hover{
transform:translateY(-8px);
box-shadow:0px 15px 30px rgba(0,255,255,.3);
}

.result{
padding:30px;
background:linear-gradient(135deg,#06b6d4,#3b82f6);
border-radius:20px;
text-align:center;
color:white;
font-size:32px;
font-weight:bold;
box-shadow:0px 12px 35px rgba(0,0,0,.3);
}

.sidebar .sidebar-content{
background:#111827;
}

div[data-testid="stSidebar"]{
background:linear-gradient(#0f172a,#1e3a8a);
}

div[data-testid="stSidebar"] *{
color:white;
}

.stButton>button{
background:linear-gradient(90deg,#06b6d4,#3b82f6);
color:white;
font-size:18px;
font-weight:bold;
padding:12px;
border:none;
border-radius:12px;
width:100%;
transition:0.4s;
}

.stButton>button:hover{
transform:scale(1.05);
background:linear-gradient(90deg,#14b8a6,#2563eb);
}

.wave {
display:flex;
justify-content:center;
align-items:center;
margin-top:20px;
margin-bottom:20px;
}

.wave span{
display:block;
width:6px;
height:30px;
margin:3px;
background:#00e5ff;
animation:wave 1s infinite ease-in-out;
border-radius:20px;
}

.wave span:nth-child(2){animation-delay:.1s;}
.wave span:nth-child(3){animation-delay:.2s;}
.wave span:nth-child(4){animation-delay:.3s;}
.wave span:nth-child(5){animation-delay:.4s;}
.wave span:nth-child(6){animation-delay:.5s;}
.wave span:nth-child(7){animation-delay:.6s;}
.wave span:nth-child(8){animation-delay:.7s;}
.wave span:nth-child(9){animation-delay:.8s;}
.wave span:nth-child(10){animation-delay:.9s;}

@keyframes wave{
0%,100%{height:20px;}
50%{height:60px;}
}

.metric{
text-align:center;
font-size:20px;
color:white;
font-weight:bold;
}

hr{
border:1px solid rgba(255,255,255,.2);
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hero'>
<h1>🩺🏥 Healthcare Cost Prediction System</h1>
<p>Medical Insurance Cost Estimation System</p>

<div class="wave">
<span></span><span></span><span></span><span></span><span></span>
<span></span><span></span><span></span><span></span><span></span>
</div>

</div>
""", unsafe_allow_html=True)

df = pd.read_csv("insurance.csv")
model = pickle.load(open("healthcare_model.pkl","rb"))

st.sidebar.image(
"https://cdn-icons-png.flaticon.com/512/2966/2966488.png",
width=120
)

st.sidebar.title("📝 Patient Information")

age = st.sidebar.slider("🎂 Age",18,100,25)

sex = st.sidebar.selectbox(
"👨 Gender",
sorted(df["sex"].unique())
)

bmi = st.sidebar.slider(
"⚖ BMI",
10.0,
60.0,
25.0
)

children = st.sidebar.slider(
"👶 Children",
0,
10,
0
)

smoker = st.sidebar.selectbox(
"🚬 Smoker",
sorted(df["smoker"].unique())
)

region = st.sidebar.selectbox(
"🌍 Region",
sorted(df["region"].unique())
)

predict = st.sidebar.button("💰 Predict Medical Cost")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class='card'>
    <div class='metric'>🧑<br>Patient</div>
    </div>
    """,unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='card'>
    <div class='metric'>❤️<br>Health</div>
    </div>
    """,unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='card'>
    <div class='metric'>🩺
	<br>Diagnosis</div>
    </div>
    """,unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class='card'>
    <div class='metric'>💰<br>
	Insurance</div>
    </div>
    """,unsafe_allow_html=True)

if predict:

    st.markdown("## 📋 Patient Summary")

    col1,col2,col3=st.columns(3)

    with col1:
        st.markdown(f"""
        <div class='card'>
        <h4>👤 Personal</h4>
        Age : {age}<br>
        Gender : {sex}<br>
        Children : {children}
        </div>
        """,unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='card'>
        <h4>❤️ Health</h4>
        BMI : {bmi}<br>
        Smoker : {smoker}
        </div>
        """,unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class='card'>
        <h4>🌍 Location</h4>
        Region : {region}
        </div>
        """,unsafe_allow_html=True)

    myinput = pd.DataFrame({
        "age":[age],
        "bmi":[bmi],
        "children":[children],
        "sex_male":[1 if sex=="male" else 0],
        "smoker_yes":[1 if smoker=="yes" else 0],
        "region_northwest":[1 if region=="northwest" else 0],
        "region_southeast":[1 if region=="southeast" else 0],
        "region_southwest":[1 if region=="southwest" else 0]
    })

    prediction = model.predict(myinput)[0]

    st.markdown("<br>",unsafe_allow_html=True)

    st.markdown(f"""
    <div class='result'>
    💰 Estimated Medical Charges
    <br><br>
    ₹ {prediction:,.2f}
    </div>
    """,unsafe_allow_html=True)

    if prediction < 10000:
        st.success("🟢 Low Medical Cost")

    elif prediction < 30000:
        st.warning("🟡 Moderate Medical Cost")

    else:
        st.error("🔴 High Medical Cost")

st.markdown("<br>",unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;color:white;">
<hr>
<h4>🏥 Healthcare Cost Prediction System</h4>
<p>Made with ❤️ using Streamlit & Machine Learning</p>
</div>
""",unsafe_allow_html=True)
