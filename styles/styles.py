import streamlit as st

def load_styles(dark=False):
    paper = "#171511" if dark else "#f3e8d2"
    panel = "#211c16" if dark else "#f8f0df"
    panel2 = "#282118" if dark else "#eee2ca"
    ink = "#ead9b8" if dark else "#30291f"
    muted = "#b9a88a" if dark else "#746957"
    gold = "#c8a76a"
    border = "#715932" if dark else "#bba57a"
    danger = "#b97556"
    safe = "#82936b"

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Libre+Baskerville:wght@400;700&display=swap');

    :root {{
        --paper:{paper}; --panel:{panel}; --panel2:{panel2}; --ink:{ink};
        --muted:{muted}; --gold:{gold}; --border:{border};
        --danger:{danger}; --safe:{safe};
    }}

    [data-testid="stHeader"] {{ background:transparent !important; }}
    [data-testid="stToolbar"] {{ display:none !important; }}
    .stAppDeployButton {{ display:none !important; }}
    .stApp {{
        background:
            radial-gradient(circle at 20% 10%, rgba(200,167,106,.07), transparent 25%),
            radial-gradient(circle at 80% 60%, rgba(200,167,106,.05), transparent 28%),
            var(--paper);
        color:var(--ink);
        font-family:'Libre Baskerville', Georgia, serif;
    }}
    .block-container {{ max-width:1220px; padding:1.4rem 2rem 2.2rem; }}

    h1,h2,h3,.brand-name,.result-main,.footer-brand {{
        font-family:'Cormorant Garamond', Georgia, serif !important;
        color:var(--ink) !important;
    }}
    h1 {{ font-size:clamp(3.4rem,5.3vw,5.7rem) !important; line-height:.78 !important; margin:.55rem 0 1.1rem !important; letter-spacing:-.025em; }}
    h1 em {{ color:var(--gold); font-weight:500; }}
    h2 {{ font-size:2.8rem !important; margin:0 !important; }}
    h3 {{ font-size:1.35rem !important; margin:.35rem 0 !important; }}
    p {{ color:var(--muted); line-height:1.65; }}

    .brand {{ display:flex; align-items:center; gap:.75rem; }}
    .brand-seal {{
        width:43px; height:43px; border:1px solid var(--gold); border-radius:50%;
        display:flex; align-items:center; justify-content:center; color:var(--gold);
        font-size:1.35rem; box-shadow:inset 0 0 0 3px var(--paper);
    }}
    .brand-name {{ font-size:2.05rem; letter-spacing:.18em; line-height:.75; }}
    .brand-sub {{ color:var(--muted); font-size:.55rem; letter-spacing:.2em; margin-top:.45rem; }}
    .nav {{ display:flex; justify-content:center; gap:3.3rem; padding-top:.55rem; }}
    .nav a {{ color:var(--ink); text-decoration:none; font-size:.78rem; position:relative; }}
    .nav a:after {{ content:""; position:absolute; left:50%; bottom:-9px; width:0; height:1px; background:var(--gold); transition:.25s; transform:translateX(-50%); }}
    .nav a:hover:after,.nav a.active:after {{ width:25px; }}
    .nav a:hover {{ color:var(--gold); }}
    .top-rule {{ border-top:1px solid var(--border); margin:1.15rem 0 2.2rem; opacity:.8; }}

    .eyebrow,.quick-title,.mini-label {{
        color:var(--gold); letter-spacing:.18em; font-size:.66rem; font-weight:700;
    }}
    .hero-copy {{ max-width:570px; font-size:.9rem; margin-bottom:1rem; }}
    .input-meta {{ display:flex; justify-content:space-between; color:var(--muted); font-size:.58rem; letter-spacing:.12em; margin:-1.45rem .7rem 1rem; position:relative; pointer-events:none; }}
    .quick-title {{ margin:1.1rem 0 .35rem; }}

    textarea {{
        background:var(--panel) !important; color:var(--ink) !important;
        border:1px solid var(--border) !important; border-radius:5px !important;
        font-family:'Libre Baskerville', Georgia, serif !important;
        box-shadow:inset 0 0 18px rgba(120,90,40,.035) !important;
    }}
    textarea:focus {{ border-color:var(--gold) !important; box-shadow:0 0 0 1px var(--gold) !important; }}

    .stButton > button {{
        border:1px solid var(--border) !important; background:transparent !important;
        color:var(--ink) !important; border-radius:5px !important;
        transition:.2s !important;
    }}
    .stButton > button:hover {{ border-color:var(--gold) !important; color:var(--gold) !important; transform:translateY(-1px); }}
    .stButton > button[kind="primary"] {{
        background:var(--ink) !important; color:var(--paper) !important;
        border-color:var(--ink) !important; font-family:'Cormorant Garamond' !important;
        font-size:1.08rem !important; padding:.42rem 1.45rem !important;
        letter-spacing:.03em;
    }}
    .stButton > button[kind="primary"]:hover {{
        background:var(--gold) !important; color:var(--paper) !important;
        border-color:var(--gold) !important;
    }}

    .hero-art {{ min-height:380px; position:relative; display:flex; align-items:center; justify-content:center; }}
    .sun-ring {{ position:absolute; width:280px; height:280px; border:1px solid var(--border); border-radius:50%; box-shadow:0 0 0 16px rgba(200,167,106,.025); }}
    .sun-ring:before,.sun-ring:after {{ content:""; position:absolute; inset:22px; border:1px dashed var(--border); border-radius:50%; opacity:.5; }}
    .envelope-art {{
        width:190px; height:130px; background:var(--panel);
        border:1.5px solid var(--gold); position:relative; transform:rotate(-5deg);
        box-shadow:10px 12px 0 rgba(90,65,30,.08);
    }}
    .envelope-art:before,.envelope-art:after {{
        content:""; position:absolute; top:20px; width:115px; height:1px;
        background:var(--gold); opacity:.8;
    }}
    .envelope-art:before {{ left:-2px; transform:rotate(31deg); transform-origin:left; }}
    .envelope-art:after {{ right:-2px; transform:rotate(-31deg); transform-origin:right; }}
    .envelope-flap {{
        position:absolute; left:20px; right:20px; top:-1px; height:75px;
        border-bottom:1px solid var(--gold); transform:skewY(-28deg);
        opacity:.8;
    }}
    .seal {{
        position:absolute; left:50%; top:50%; transform:translate(-50%,-50%);
        width:38px; height:38px; border:1px solid var(--gold); border-radius:50%;
        display:flex; align-items:center; justify-content:center; color:var(--gold);
        background:var(--panel); font-family:'Cormorant Garamond'; font-size:1.3rem;
    }}
    .feather-art {{ position:absolute; top:58px; right:46px; color:var(--gold); font-size:5.8rem; transform:rotate(-38deg); opacity:.9; }}
    .small-star {{ position:absolute; color:var(--gold); font-size:1rem; }}
    .star-a {{ top:60px; left:28px; }} .star-b {{ bottom:76px; left:64px; font-size:2rem; }}
    .art-note {{ position:absolute; right:-4px; bottom:8px; color:var(--gold); font-family:'Cormorant Garamond'; font-size:1.05rem; font-style:italic; line-height:1.15; }}

    .result-card,.process-card,.model-card {{
        background:linear-gradient(145deg,var(--panel),var(--panel2));
        border:1px solid var(--border); border-radius:7px;
        padding:1.25rem; box-shadow:3px 4px 0 rgba(120,90,40,.06);
    }}
    .result-card {{ min-height:280px; margin-top:1rem; }}
    .card-title {{ font-family:'Cormorant Garamond'; font-size:1.18rem; border-bottom:1px solid var(--border); padding-bottom:.7rem; letter-spacing:.03em; }}
    .result-empty {{ min-height:130px; display:flex; align-items:center; justify-content:center; text-align:center; color:var(--muted); font-family:'Cormorant Garamond'; font-size:1.28rem; line-height:1.05; }}
    .result-empty span {{ color:var(--gold); font-size:.8rem; }}
    .result-main {{ font-size:2.15rem; font-weight:700; margin:1.3rem 0 .5rem; }}
    .result-main.spam {{ color:var(--danger) !important; }}
    .result-main.ham {{ color:var(--safe) !important; }}
    .result-description {{ color:var(--muted); font-size:.7rem; line-height:1.6; min-height:50px; margin-bottom:1.2rem; }}
    .confidence-label {{ display:flex; justify-content:space-between; color:var(--muted); font-size:.68rem; }}
    .confidence {{ height:7px; border:1px solid var(--border); border-radius:10px; margin-top:.45rem; overflow:hidden; }}
    .confidence span {{ display:block; height:100%; background:var(--gold); }}

    .section {{ border-top:1px solid var(--border); margin-top:2.5rem; padding-top:2.1rem; }}
    .section-heading {{ display:flex; justify-content:space-between; align-items:end; gap:2rem; margin-bottom:1.45rem; }}
    .section-heading p {{ font-size:.75rem; margin:.15rem 0 0; }}
    .process-card {{ min-height:210px; position:relative; transition:.25s; }}
    .process-card:hover {{ transform:translateY(-5px); border-color:var(--gold); }}
    .card-number {{ position:absolute; top:10px; right:12px; color:var(--gold); font-size:.65rem; letter-spacing:.08em; }}
    .card-icon {{ font-size:1.45rem; color:var(--gold); }}
    .process-card p,.model-card p {{ font-size:.72rem; }}

    .model-note {{ color:var(--gold); font-family:'Cormorant Garamond'; font-style:italic; text-align:right; line-height:1.1; }}
    .model-card {{ min-height:238px; transition:all .3s ease; }}
    .model-card:hover {{ border-color:var(--gold); }}
    .model-card.active {{ transform:translateY(-11px) scale(1.045); border-color:var(--gold); box-shadow:0 15px 28px rgba(0,0,0,.15); }}
    .metrics {{ display:flex; justify-content:center; gap:2rem; flex-wrap:wrap; margin-top:1.35rem; color:var(--muted); font-size:.68rem; letter-spacing:.04em; }}
    .metrics span:before {{ content:"✦"; color:var(--gold); margin-right:.4rem; }}

    footer {{ border-top:1px solid var(--border); padding:1.5rem 0 .4rem; margin-top:2.2rem; text-align:center; color:var(--muted); font-size:.63rem; }}
    .footer-brand {{ font-size:1.5rem; letter-spacing:.18em; color:var(--gold) !important; }}
    .footer-line {{ width:100px; border-top:1px solid var(--border); margin:.7rem auto; }}

    @media(max-width:900px) {{
        .block-container {{ padding:1rem; }}
        .nav {{ gap:1rem; }}
        .hero-art {{ min-height:250px; }}
        .section-heading {{ display:block; }}
        .model-note {{ text-align:left; margin-top:.6rem; }}
    }}

    .defense-heading {{ margin:2.1rem 0 1rem; }}
    .defense-heading h2 {{ font-size:2.2rem !important; margin:.3rem 0 !important; }}
    .defense-heading p {{ max-width:700px; font-size:.78rem; }}
    .layer-card {{ display:flex; gap:1rem; align-items:flex-start; min-height:120px; padding:1.15rem; border:1px solid var(--border); border-radius:7px; background:linear-gradient(145deg,var(--panel),var(--panel2)); transition:transform .25s,border-color .25s; }}
    .layer-card:hover {{ transform:translateY(-4px); border-color:var(--gold); }}
    .layer-card > span {{ color:var(--gold); font-family:'Cormorant Garamond'; font-size:1.5rem; }}
    .layer-card p {{ font-size:.72rem; margin:.35rem 0 0; }}
    .model-detail-panel {{ margin:1.2rem auto 0; max-width:820px; padding:1.35rem 1.6rem; border:1px solid var(--gold); border-radius:7px; background:linear-gradient(145deg,var(--panel),var(--panel2)); box-shadow:0 8px 22px rgba(60,45,20,.07); animation:riseIn .28s ease-out; }}
    .model-detail-panel h3 {{ margin:.45rem 0 !important; }}
    .model-detail-panel p {{ margin:.4rem 0 0; font-size:.8rem; }}
    @keyframes riseIn {{ from {{ opacity:.45; transform:translateY(8px); }} to {{ opacity:1; transform:translateY(0); }} }}
    .stHtml {{ overflow:visible; }}
    [data-testid="stVerticalBlock"] {{ gap:.6rem; }}
    @media(max-width:1100px) {{
        .model-card {{ min-height:210px; padding:.85rem; }}
        .model-card.active {{ transform:translateY(-5px) scale(1.015); }}
        .model-card h3 {{ font-size:1.1rem !important; }}
    }}
    @media(max-width:760px) {{
        h1 {{ font-size:3rem !important; line-height:.92 !important; }}
        h2 {{ font-size:2.2rem !important; }}
        .brand-name {{ font-size:1.55rem; }}
        .nav {{ gap:.6rem; flex-wrap:wrap; }}
        .nav a {{ font-size:.68rem; }}
        .hero-art {{ min-height:210px; }}
        .sun-ring {{ width:190px; height:190px; }}
        .envelope-art {{ transform:scale(.8) rotate(-5deg); }}
        .model-note {{ text-align:left; margin-top:.6rem; }}
    }}
    </style>
    """, unsafe_allow_html=True)