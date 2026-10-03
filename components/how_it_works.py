import streamlit as st

STEPS = [
    ("01", "✉", "Clean the message", "Remove URLs, numbers and special characters that are not needed for this model."),
    ("02", "⚙", "Process the text", "NLTK tokenizes the words, removes common stop-words and lemmatizes words."),
    ("03", "⌁", "Convert with TF-IDF", "Text is converted into numerical features the machine-learning model can use."),
    ("04", "✓", "Predict the result", "Logistic Regression predicts whether the message looks like spam or ham."),
]
LAYERS = [
    ("01", "Text preparation", "Cleaning makes messages more consistent before analysis."),
    ("02", "Feature extraction", "TF-IDF gives words weights based on how useful they are in the dataset."),
    ("03", "Classification", "The trained model combines learned patterns to produce one prediction."),
]


def render_how_it_works():
    st.html('<div id="how-it-works"></div><section class="section"><div class="section-heading"><div><div class="eyebrow">✦ SIMPLE · TRANSPARENT · EXPLAINABLE ✦</div><h2>How NIRIK Works</h2><p>Four clear steps take a message from raw text to a prediction.</p></div></div></section>')
    cols = st.columns(4, gap="medium")
    for col, (num, icon, title, body) in zip(cols, STEPS):
        with col:
            st.html(f'<article class="process-card"><div class="card-number">{num}</div><div class="card-icon">{icon}</div><h3>{title}</h3><p>{body}</p></article>')

    st.html('<div class="defense-heading"><div class="eyebrow">✦ MULTIPLE LAYERS OF ANALYSIS ✦</div><h2>How NIRIK reaches a decision</h2><p>These are stages of one machine-learning pipeline—not separate security products.</p></div>')
    cols = st.columns(3, gap="medium")
    for col, (num, title, body) in zip(cols, LAYERS):
        with col:
            st.html(f'<article class="layer-card"><span>{num}</span><div><div class="mini-label">{title}</div><p>{body}</p></div></article>')
