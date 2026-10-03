import streamlit as st

CARDS = [
    ("Dataset", "▦", "SMS Spam Collection", "5,572 labelled SMS messages", "The dataset contains messages labelled ham (normal) or spam. The model learns from examples rather than from a list of hand-written rules."),
    ("Preprocessing", "⚙", "NLTK", "Clean · tokenize · lemmatize", "The text is lowercased, URLs and non-letter characters are removed, words are tokenized, common stop-words are filtered and remaining words are lemmatized."),
    ("Vectorization", "⌁", "TF-IDF", "Text becomes numbers", "TF-IDF assigns weights to words based on their importance in a message and the dataset. This gives the classifier numerical features."),
    ("Algorithm", "◈", "Logistic Regression", "Binary classification", "The trained Logistic Regression model uses the TF-IDF features to choose one of two labels: spam or ham (not spam)."),
    ("Evaluation", "◎", "Test performance", "96.77% accuracy", "On the held-out test set, precision was 100%, recall was 75.84% and F1-score was 86.26%. Accuracy alone does not mean every spam message is caught."),
]


def render_about_model():
    st.html('<div id="about-model"></div><section class="section"><div class="section-heading"><div><div class="eyebrow">✦ UNDER THE SURFACE ✦</div><h2>About the Model</h2><p>Select a card to bring that part of NIRIK into focus.</p></div><div class="model-note">Simple steps.<br>Clear reasoning.<br>Measured results.</div></div></section>')
    if "model_card" not in st.session_state:
        st.session_state.model_card = 2
    active = st.session_state.model_card
    left, center, right = st.columns([0.45, 9.1, 0.45], vertical_alignment="center")
    with left:
        if st.button("‹", key="model_prev", help="Previous model topic"):
            st.session_state.model_card = (active - 1) % len(CARDS)
            st.rerun()
    with center:
        cols = st.columns(5, gap="small")
        for col, index in zip(cols, range(len(CARDS))):
            title, icon, name, short, detail = CARDS[index]
            is_active = index == active
            with col:
                st.html(f'<article class="model-card {"active" if is_active else ""}"><div class="card-icon">{icon}</div><div class="mini-label">{title}</div><h3>{name}</h3><p>{short}</p></article>')
                if st.button("Viewing" if is_active else "Explore", key=f"model_select_{index}", use_container_width=True):
                    st.session_state.model_card = index
                    st.rerun()
    with right:
        if st.button("›", key="model_next", help="Next model topic"):
            st.session_state.model_card = (active + 1) % len(CARDS)
            st.rerun()

    title, icon, name, short, detail = CARDS[active]
    st.html(f'<div class="model-detail-panel"><div class="mini-label">SELECTED TOPIC · {title.upper()}</div><h3>{icon} &nbsp; {name}</h3><p>{detail}</p></div>')
    st.html('<div class="metrics"><span>Accuracy 96.77%</span><span>Precision 100%</span><span>Recall 75.84%</span><span>F1-score 86.26%</span></div>')
