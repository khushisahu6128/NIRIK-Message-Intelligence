import streamlit as st


def render_header():
    left, nav, theme = st.columns([2.2, 4.5, 1], vertical_alignment="center")
    with left:
        st.html("""
        <div class="brand">
          <div class="brand-seal">✉</div>
          <div><div class="brand-name">NIRIK</div><div class="brand-sub">MESSAGE INTELLIGENCE</div></div>
        </div>
        """)
    with nav:
        st.html("""
        <nav class="nav">
          <a href="#home">Home</a><a href="#how-it-works">How It Works</a><a href="#about-model">About Model</a>
        </nav>
        """)
    with theme:
        icon = "☀" if st.session_state.dark_mode else "☾"
        if st.button(icon, key="theme_toggle", help="Switch between light and dark vintage mode"):
            st.session_state.dark_mode = not st.session_state.dark_mode
            st.rerun()
    st.html('<div class="top-rule"></div>')
