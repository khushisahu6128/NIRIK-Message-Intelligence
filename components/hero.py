import streamlit as st
from services.classifier import classify_message


def _set_message(sample):
    st.session_state.message_input = sample


def render_hero():
    st.html('<div id="home"></div>')
    text_col, art_col, result_col = st.columns([1.55, 1.05, 1.0], gap="large")

    with text_col:
        st.html('<div class="eyebrow">✦ SMART · SAFE · RELIABLE ✦</div><h1>Is this message<br><em>safe to trust?</em></h1><p class="hero-copy">Paste a message below. NIRIK studies its language patterns and tells you whether it looks like spam.</p>')
        message = st.text_area(
            "Message", placeholder="Type or paste your message here...", height=155,
            label_visibility="collapsed", max_chars=1000, key="message_input",
        )
        st.html(f'<div class="input-meta"><span>MESSAGE</span><span>{len(message)}/1000</span></div>')
        check = st.button("Check Message  →", type="primary", key="check_message")

        st.html('<div class="quick-title">ϟ QUICK TEST · CLICK TO FILL</div>')
        q1, q2, q3 = st.columns(3)
        samples = [
            (q1, "Prize message", "CONGRATULATIONS! You have won a cash prize. Call now to claim your reward!"),
            (q2, "College message", "Hey, are you coming to college tomorrow? Let me know when you reach."),
            (q3, "Friendly message", "Call me when you are free. I will be waiting after class."),
        ]
        for col, label, sample in samples:
            with col:
                st.button(
                    label,
                    key=f"sample_{label}",
                    use_container_width=True,
                    on_click=_set_message,
                    args=(sample,),
                )

    # Classify before rendering the result card, so the same click displays the verdict.
    if check:
        if not message.strip():
            st.session_state.result = None
            st.warning("Please enter a message first.")
        else:
            try:
                st.session_state.result = classify_message(message.strip())
            except Exception as exc:
                st.session_state.result = None
                st.error(f"NIRIK could not analyse this message. Check that the saved model files and NLTK resources are available. Details: {exc}")

    with art_col:
        st.html("""
        <div class="hero-art"><div class="sun-ring"></div><div class="small-star star-a">✦</div>
          <div class="small-star star-b">·</div><div class="envelope-art"><div class="envelope-flap"></div><div class="seal">N</div></div>
          <div class="art-note">Not every<br>message is<br>what it seems...</div>
        </div>
        """)

    with result_col:
        result = st.session_state.get("result")
        if result:
            label, confidence = result
            is_spam = str(label).strip().lower() == "spam"
            title = "SPAM" if is_spam else "NOT SPAM"
            symbol = "⚠" if is_spam else "✓"
            cls = "spam" if is_spam else "ham"
            description = (
                "This message matches patterns commonly found in spam. Treat links, prizes and urgent requests with caution."
                if is_spam else
                "This message does not strongly match the spam patterns learned by NIRIK. Still verify unexpected requests."
            )
            confidence_value = max(0.0, min(100.0, float(confidence) * 100))
            card = (
                '<div class="result-card"><div class="card-title">◉ &nbsp; NIRIK RESULT</div>'
                f'<div class="result-main {cls}">{symbol} {title}</div>'
                f'<div class="result-description">{description}</div>'
                f'<div class="confidence-label"><span>Model confidence</span><b>{confidence_value:.1f}%</b></div>'
                f'<div class="confidence"><span style="width:{confidence_value:.1f}%"></span></div></div>'
            )
        else:
            card = (
                '<div class="result-card"><div class="card-title">◉ &nbsp; NIRIK RESULT</div>'
                '<div class="result-empty"><div><span>✦</span><br>Your result will<br>appear here</div></div>'
                '<div class="confidence-label"><span>Model confidence</span><b>—</b></div>'
                '<div class="confidence"><span style="width:0%"></span></div></div>'
            )
        st.html(card)
