import streamlit as st

from components.header import render_header
from components.hero import render_hero
from components.how_it_works import render_how_it_works
from components.about_model import render_about_model
from components.footer import render_footer
from styles.styles import load_styles

st.set_page_config(
    page_title="NIRIK — Message Intelligence",
    page_icon="✉",
    layout="wide",
    initial_sidebar_state="collapsed",
)

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False
if "result" not in st.session_state:
    st.session_state.result = None

load_styles(st.session_state.dark_mode)
render_header()
render_hero()  # Prediction is handled before the result panel is rendered.
render_how_it_works()
render_about_model()
render_footer()
