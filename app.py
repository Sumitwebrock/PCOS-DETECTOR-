import streamlit as st
import time

st.set_page_config(
    page_title="PCOS Check · Your Friendly Guide 🌸",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed",
)


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Nunito:wght@300;400;500;600;700&display=swap');

:root {
    --rose:       #e8637a;
    --rose-light: #f2a0af;
    --blush:      #fce4ec;
    --blush2:     #fdf0f4;
    --lavender:   #e8d5f5;
    --lav-deep:   #c3a8e0;
    --mint:       #d4f0e8;
    --mint-deep:  #6bbfa0;
    --cream:      #fff8f9;
    --text-dark:  #3d2c35;
    --text-mid:   #7a5a66;
    --text-light: #b08a99;
    --card-bg:    #ffffff;
    --border:     #f5dce4;
    --shadow:     rgba(232,99,122,0.12);
}

html, body, [class*="css"], [data-testid="stAppViewContainer"], 
[data-testid="stVerticalBlock"], .main, section.main {
    font-family: 'Nunito', sans-serif !important;
    background-color: var(--cream) !important;
    color: var(--text-dark) !important;
}

/* Force entire app background to cream/white */
[data-testid="stAppViewContainer"] {
    background: var(--cream) !important;
}
[data-testid="stHeader"] { background: transparent !important; }

/* Force ALL text to be dark — overrides dark theme */
p, span, div, label, h1, h2, h3, h4, li {
    color: var(--text-dark) !important;
}

/* Background blobs */
body::before {
    content: '';
    position: fixed; top: -100px; right: -100px;
    width: 400px; height: 400px;
    background: radial-gradient(circle, rgba(232,213,245,0.5) 0%, transparent 70%);
    border-radius: 50%; pointer-events: none; z-index: 0;
}
body::after {
    content: '';
    position: fixed; bottom: -80px; left: -80px;
    width: 350px; height: 350px;
    background: radial-gradient(circle, rgba(252,228,236,0.6) 0%, transparent 70%);
    border-radius: 50%; pointer-events: none; z-index: 0;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container {
    max-width: 720px;
    padding: 2rem 1.5rem 4rem;
    position: relative; z-index: 1;
}

/* ── Floating petals decoration ── */
.petal-bar {
    text-align: center;
    font-size: 1.4rem;
    letter-spacing: 0.5rem;
    margin: 0.5rem 0 1.5rem;
    opacity: 0.6;
}

/* ── Hero ── */
.hero {
    text-align: center;
    padding: 2.5rem 2rem 2rem;
    background: linear-gradient(145deg, #fff0f4 0%, #fce4ec 50%, #ede7f6 100%);
    border-radius: 28px;
    border: 1.5px solid var(--border);
    box-shadow: 0 8px 40px var(--shadow);
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '🌸';
    position: absolute; top: -10px; right: 20px;
    font-size: 5rem; opacity: 0.12;
}
.hero-emoji { font-size: 3rem; margin-bottom: 0.5rem; }
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.4rem;
    color: var(--rose);
    margin: 0 0 0.4rem;
    line-height: 1.2;
}
.hero-title em { font-style: italic; color: var(--lav-deep); }
.hero-sub {
    font-size: 1.0rem;
    color: var(--text-mid);
    margin: 0 auto 1.2rem;
    max-width: 500px;
    line-height: 1.6;
    font-weight: 400;
}
.hero-tag {
    display: inline-block;
    background: white;
    border: 1.5px solid var(--rose-light);
    color: var(--rose);
    padding: 0.3rem 1rem;
    border-radius: 99px;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}

/* ── Progress bar ── */
.progress-wrap {
    margin: 1.2rem 0 2rem;
}
.progress-label {
    display: flex;
    justify-content: space-between;
    font-size: 0.82rem;
    color: var(--text-light);
    font-weight: 600;
    margin-bottom: 0.5rem;
}
.progress-track {
    background: var(--blush);
    border-radius: 99px;
    height: 8px;
    overflow: hidden;
}
.progress-fill {
    height: 100%;
    border-radius: 99px;
    background: linear-gradient(90deg, var(--rose-light), var(--rose));
    transition: width 0.5s ease;
}
.step-dots {
    display: flex;
    justify-content: center;
    gap: 0.5rem;
    margin-top: 0.6rem;
}
.step-dot {
    width: 10px; height: 10px;
    border-radius: 50%;
    border: 2px solid var(--rose-light);
    background: white;
    display: inline-block;
}
.step-dot.done { background: var(--rose); border-color: var(--rose); }
.step-dot.current { background: var(--rose-light); border-color: var(--rose); transform: scale(1.3); }

/* ── Question Card ── */
.q-card {
    background: white;
    border-radius: 24px;
    border: 1.5px solid var(--border);
    padding: 2rem 2rem 1.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 24px var(--shadow);
    animation: fadeUp 0.4s ease;
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}
.q-number {
    display: inline-block;
    background: linear-gradient(135deg, var(--rose-light), var(--rose));
    color: white;
    font-size: 0.75rem;
    font-weight: 700;
    padding: 0.25rem 0.75rem;
    border-radius: 99px;
    margin-bottom: 0.8rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}
.q-text {
    font-family: 'Playfair Display', serif;
    font-size: 1.35rem;
    color: var(--text-dark);
    line-height: 1.45;
    margin: 0 0 0.5rem;
}
.q-hint {
    font-size: 0.85rem;
    color: var(--text-light);
    margin: 0 0 1.4rem;
    font-weight: 400;
    line-height: 1.5;
}

/* ── Option Buttons — FORCE VISIBLE TEXT ── */
.stRadio > div { gap: 0.6rem !important; }

/* Target every possible Streamlit radio label structure */
.stRadio > div > label,
.stRadio label,
div[data-testid="stRadio"] label,
div[role="radiogroup"] label {
    background: #fff0f4 !important;
    border: 1.5px solid #f2a0af !important;
    border-radius: 14px !important;
    padding: 0.85rem 1.2rem !important;
    width: 100% !important;
    font-size: 0.96rem !important;
    font-weight: 600 !important;
    color: #3d2c35 !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    display: flex !important;
    align-items: center !important;
}

/* Force ALL child spans/p inside labels to be dark */
.stRadio > div > label *,
.stRadio label *,
div[data-testid="stRadio"] label *,
div[role="radiogroup"] label * {
    color: #3d2c35 !important;
    font-weight: 600 !important;
}

.stRadio > div > label:hover,
div[data-testid="stRadio"] label:hover {
    border-color: #e8637a !important;
    background: #fce4ec !important;
}

/* Radio circle */
div[data-testid="stRadio"] > div > label > div:first-child,
div[role="radiogroup"] label > div:first-child {
    border-color: #e8637a !important;
    min-width: 18px !important;
}
div[data-testid="stRadio"] input[type="radio"]:checked + div {
    background-color: #e8637a !important;
}

/* ── Next / Submit Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, var(--rose-light) 0%, var(--rose) 100%);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 0.75rem 2rem;
    font-family: 'Nunito', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    width: 100%;
    letter-spacing: 0.02em;
    box-shadow: 0 4px 16px rgba(232,99,122,0.3);
    transition: transform 0.15s, box-shadow 0.15s;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(232,99,122,0.4);
}

/* ── Result Cards ── */
.result-positive {
    background: linear-gradient(145deg, #fff5f7, #ffe0e6);
    border: 2px solid #f2a0af;
    border-radius: 24px;
    padding: 2.2rem 2rem;
    text-align: center;
    box-shadow: 0 8px 40px rgba(232,99,122,0.15);
    animation: fadeUp 0.5s ease;
}
.result-negative {
    background: linear-gradient(145deg, #f0fbf7, #d4f0e8);
    border: 2px solid var(--mint-deep);
    border-radius: 24px;
    padding: 2.2rem 2rem;
    text-align: center;
    box-shadow: 0 8px 40px rgba(107,191,160,0.15);
    animation: fadeUp 0.5s ease;
}
.result-emoji { font-size: 3.5rem; margin-bottom: 0.5rem; }
.result-title {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    margin: 0 0 0.6rem;
    line-height: 1.2;
}
.result-subtitle {
    font-size: 0.98rem;
    line-height: 1.65;
    margin: 0 auto 0.5rem;
    max-width: 500px;
}
.score-bar-wrap { margin: 1.2rem auto; max-width: 380px; }
.score-bar-track {
    background: rgba(255,255,255,0.6);
    border-radius: 99px; height: 12px; overflow: hidden;
}
.score-bar-fill {
    height: 100%; border-radius: 99px;
    transition: width 1s ease;
}

/* ── Info Cards (post-result) ── */
.info-card {
    background: white;
    border-radius: 20px;
    border: 1.5px solid var(--border);
    padding: 1.5rem 1.8rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 2px 12px var(--shadow);
}
.info-card-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    color: var(--rose);
    margin: 0 0 0.8rem;
}
.info-card p, .info-card li {
    font-size: 0.9rem;
    color: var(--text-mid);
    line-height: 1.7;
    margin: 0.2rem 0;
}
.tag-pill {
    display: inline-block;
    background: var(--blush);
    color: var(--rose);
    border-radius: 99px;
    padding: 0.25rem 0.85rem;
    font-size: 0.8rem;
    font-weight: 600;
    margin: 0.2rem 0.15rem;
}
.tag-pill.lav {
    background: var(--lavender);
    color: var(--lav-deep);
}
.tag-pill.mint {
    background: var(--mint);
    color: var(--mint-deep);
}
.doctor-card {
    background: linear-gradient(135deg, #fff0f4, #ede7f6);
    border: 1.5px solid var(--rose-light);
    border-radius: 20px;
    padding: 1.5rem 1.8rem;
    margin-bottom: 1.2rem;
}
.doctor-card p {
    font-size: 0.9rem;
    color: var(--text-mid);
    line-height: 1.7;
    margin: 0.3rem 0;
}
.urgent-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    display: inline-block;
    background: var(--rose);
    margin-right: 0.4rem;
}
.disclaimer {
    background: #fffde7;
    border-left: 4px solid #f9a825;
    border-radius: 10px;
    padding: 0.9rem 1.2rem;
    font-size: 0.8rem;
    color: #7a6000;
    margin: 1.5rem 0;
    line-height: 1.6;
}

/* ── Restart button variant ── */
.restart-btn > button {
    background: white !important;
    color: var(--rose) !important;
    border: 2px solid var(--rose-light) !important;
    box-shadow: none !important;
}
.restart-btn > button:hover {
    background: var(--blush) !important;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# QUESTIONS DATA
# ─────────────────────────────────────────────
QUESTIONS = [
    {
        "id": "cycle",
        "emoji": "🗓️",
        "number": "Question 1 of 10",
        "text": "How regular are your periods?",
        "hint": "Think about the last 6 months. A regular cycle comes every 21–35 days.",
        "options": [
            ("They come every 21–35 days, pretty on time 🟢", 0),
            ("Sometimes early or late by a few days 🟡", 1),
            ("Often irregular — I never know when they'll come 🔴", 2),
            ("I skip months or barely get them 🔴", 3),
        ],
    },
    {
        "id": "cycle_length",
        "emoji": "📅",
        "number": "Question 2 of 10",
        "text": "How many days does your period usually last?",
        "hint": "A typical period lasts 3–7 days.",
        "options": [
            ("3 to 7 days — totally normal 🟢", 0),
            ("Less than 2 days — quite short 🟡", 1),
            ("More than 8 days — quite long 🔴", 2),
            ("It varies a lot each time 🟡", 1),
        ],
    },
    {
        "id": "hair_growth",
        "emoji": "🌿",
        "number": "Question 3 of 10",
        "text": "Do you notice unusual hair growth on your face, chest, or stomach?",
        "hint": "This is called hirsutism — hair growing in places it typically doesn't for women.",
        "options": [
            ("No, nothing unusual 🟢", 0),
            ("A little — some chin or lip hair 🟡", 1),
            ("Yes — noticeable hair on face, chest or tummy 🔴", 2),
            ("It's been getting more over time 🔴", 2),
        ],
    },
    {
        "id": "hair_loss",
        "emoji": "💇‍♀️",
        "number": "Question 4 of 10",
        "text": "Are you experiencing hair thinning or hair fall from your scalp?",
        "hint": "PCOS can cause hair to thin on the top or temples — like male-pattern baldness.",
        "options": [
            ("Nope, my hair feels healthy 🟢", 0),
            ("A little more shedding lately 🟡", 1),
            ("Noticeable thinning or patches 🔴", 2),
            ("I've lost a significant amount 🔴", 3),
        ],
    },
    {
        "id": "acne",
        "emoji": "🌺",
        "number": "Question 5 of 10",
        "text": "How would you describe your skin and acne?",
        "hint": "Hormonal acne linked to PCOS typically appears on the jawline, chin, and neck.",
        "options": [
            ("Clear or minimal acne 🟢", 0),
            ("Some pimples around period time 🟡", 1),
            ("Persistent acne on jawline/chin 🔴", 2),
            ("Severe acne that won't respond to treatment 🔴", 3),
        ],
    },
    {
        "id": "weight",
        "emoji": "⚖️",
        "number": "Question 6 of 10",
        "text": "Have you noticed unexplained weight gain, especially around your belly?",
        "hint": "PCOS often causes weight to collect around the middle due to insulin resistance.",
        "options": [
            ("No unusual weight changes 🟢", 0),
            ("A little weight gain, not sure why 🟡", 1),
            ("Yes — gaining weight despite eating normally 🔴", 2),
            ("Significant belly weight that won't budge 🔴", 3),
        ],
    },
    {
        "id": "skin",
        "emoji": "✨",
        "number": "Question 7 of 10",
        "text": "Do you notice dark patches on your neck, underarms, or groin?",
        "hint": "These dark, velvety patches are called Acanthosis Nigricans — a sign of insulin resistance.",
        "options": [
            ("No, my skin looks even 🟢", 0),
            ("Maybe slightly darker in neck/underarms 🟡", 1),
            ("Yes — clearly darker, velvety patches 🔴", 2),
        ],
    },
    {
        "id": "mood",
        "emoji": "💭",
        "number": "Question 8 of 10",
        "text": "Do you often feel anxious, depressed, or have extreme mood swings?",
        "hint": "Hormonal imbalances in PCOS can significantly affect mood and mental wellbeing.",
        "options": [
            ("I feel mostly balanced emotionally 🟢", 0),
            ("PMS mood swings that are manageable 🟡", 1),
            ("Frequent anxiety, low mood, or mood swings 🔴", 2),
            ("Significant depression or anxiety affecting daily life 🔴", 3),
        ],
    },
    {
        "id": "fatigue",
        "emoji": "😴",
        "number": "Question 9 of 10",
        "text": "Do you feel excessively tired or have trouble losing weight despite effort?",
        "hint": "Fatigue and weight loss resistance are hallmarks of insulin resistance — common in PCOS.",
        "options": [
            ("Energy levels feel normal 🟢", 0),
            ("Tired sometimes, but manageable 🟡", 1),
            ("Often exhausted even after a full night's sleep 🔴", 2),
            ("Chronic fatigue + diet/exercise barely works for me 🔴", 3),
        ],
    },
    {
        "id": "age_family",
        "emoji": "👨‍👩‍👧",
        "number": "Question 10 of 10",
        "text": "Do any of these apply to you?",
        "hint": "Family history and age of onset can increase your risk of PCOS.",
        "options": [
            ("None of these apply to me 🟢", 0),
            ("My periods became irregular after stopping birth control 🟡", 1),
            ("A close female relative has PCOS or diabetes 🔴", 2),
            ("My periods were irregular right from the start (within 2 years of first period) 🔴", 2),
        ],
    },
]

TOTAL_STEPS = len(QUESTIONS)

# ─────────────────────────────────────────────
# SESSION STATE INIT
# ─────────────────────────────────────────────
if "step" not in st.session_state:
    st.session_state.step = 0          # 0 = welcome
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "score" not in st.session_state:
    st.session_state.score = 0
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "current_answer" not in st.session_state:
    st.session_state.current_answer = None


def reset():
    st.session_state.step = 0
    st.session_state.answers = {}
    st.session_state.score = 0
    st.session_state.show_result = False
    st.session_state.current_answer = None


# ─────────────────────────────────────────────
# WELCOME SCREEN (step == 0)
# ─────────────────────────────────────────────
if st.session_state.step == 0 and not st.session_state.show_result:

    st.markdown("""
    <div class="hero">
        <div class="hero-emoji">🌸</div>
        <h1 class="hero-title">Hey Beautiful, <em>are you okay?</em></h1>
        <p class="hero-sub">
            Feeling confused about your body? Irregular periods, unexpected hair changes,
            stubborn weight, or just something feeling <em>off</em>?<br><br>
            This quick, friendly check-in will help you understand if your symptoms
            might be related to <strong>PCOS</strong> — and what to do next. 💕
        </p>
        <div class="hero-tag">🔒 Private · Free · Takes 2 minutes</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">💬 What is PCOS?</div>
        <p>
            <strong>Polycystic Ovary Syndrome (PCOS)</strong> is one of the most common
            hormonal conditions in women — affecting <strong>1 in 10 women</strong> of
            reproductive age. The tricky part? Up to <strong>70% don't know they have it.</strong>
        </p>
        <p style="margin-top:0.7rem">
            It can cause irregular periods, acne, hair changes, weight gain, mood swings,
            and more. The good news — with the right care, it's <strong>completely manageable</strong>. 🌱
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">📋 How this works</div>
        <p>✅ &nbsp;Answer <strong>10 simple questions</strong> about your body and lifestyle</p>
        <p>✅ &nbsp;Get an <strong>instant, personalised result</strong></p>
        <p>✅ &nbsp;Learn what your symptoms mean and <strong>what to do next</strong></p>
        <p style="margin-top:0.7rem;font-size:0.82rem;color:#b08a99;">
            ⚠️ This is not a medical diagnosis — always consult a doctor for proper evaluation.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Let's Start! 🌸"):
        st.session_state.step = 1
        st.session_state.current_answer = None
        st.rerun()


# ─────────────────────────────────────────────
# QUESTIONS SCREEN
# ─────────────────────────────────────────────
elif not st.session_state.show_result and 1 <= st.session_state.step <= TOTAL_STEPS:

    q_idx = st.session_state.step - 1
    q = QUESTIONS[q_idx]
    pct = int((q_idx / TOTAL_STEPS) * 100)

    # Progress
    dots_html = ""
    for i in range(TOTAL_STEPS):
        if i < q_idx:
            dots_html += "<span class='step-dot done'></span>"
        elif i == q_idx:
            dots_html += "<span class='step-dot current'></span>"
        else:
            dots_html += "<span class='step-dot'></span>"

    st.markdown(f"""
    <div class="progress-wrap">
        <div class="progress-label">
            <span>Question {st.session_state.step} of {TOTAL_STEPS}</span>
            <span>{pct}% done</span>
        </div>
        <div class="progress-track">
            <div class="progress-fill" style="width:{pct}%"></div>
        </div>
        <div class="step-dots">{dots_html}</div>
    </div>
    """, unsafe_allow_html=True)

    # Question card
    option_labels = [opt[0] for opt in q["options"]]

    st.markdown(f"""
    <div class="q-card">
        <div class="q-number">{q['emoji']} &nbsp;{q['number']}</div>
        <div class="q-text">{q['text']}</div>
        <div class="q-hint">💡 {q['hint']}</div>
    </div>
    """, unsafe_allow_html=True)

    selected = st.radio(
        label="Choose an answer:",
        options=option_labels,
        index=None,
        key=f"q_{q['id']}",
        label_visibility="collapsed",
    )

    st.markdown("")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.session_state.step > 1:
            with st.container():
                st.markdown("<div class='restart-btn'>", unsafe_allow_html=True)
                if st.button("← Back"):
                    # Remove previous answer score
                    prev_q = QUESTIONS[q_idx - 1]
                    if prev_q["id"] in st.session_state.answers:
                        prev_score = st.session_state.answers[prev_q["id"]]
                        st.session_state.score -= prev_score
                        del st.session_state.answers[prev_q["id"]]
                    st.session_state.step -= 1
                    st.session_state.current_answer = None
                    st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        btn_label = "Next Question →" if st.session_state.step < TOTAL_STEPS else "See My Result 🌸"
        if st.button(btn_label, disabled=(selected is None)):
            if selected is not None:
                # Find score for selected option
                for label, score_val in q["options"]:
                    if label == selected:
                        st.session_state.answers[q["id"]] = score_val
                        st.session_state.score += score_val
                        break
                if st.session_state.step == TOTAL_STEPS:
                    st.session_state.show_result = True
                else:
                    st.session_state.step += 1
                    st.session_state.current_answer = None
                st.rerun()


# ─────────────────────────────────────────────
# RESULT SCREEN
# ─────────────────────────────────────────────
elif st.session_state.show_result:

    score = st.session_state.score
    max_score = sum(max(v for _, v in q["options"]) for q in QUESTIONS)
    pct = int((score / max_score) * 100)

    # Determine risk level
    if pct >= 55:
        level = "high"
    elif pct >= 30:
        level = "moderate"
    else:
        level = "low"

    # ── Result Banner ──
    if level == "high":
        st.markdown(f"""
        <div class="result-positive">
            <div class="result-emoji">🌸</div>
            <div class="result-title" style="color:#c0404e">
                Your symptoms suggest PCOS may be present
            </div>
            <div class="result-subtitle" style="color:#7a5a66">
                Based on your answers, you have a <strong>higher likelihood</strong> of PCOS symptoms.
                This doesn't mean you definitely have it — only a doctor can confirm.
                But your body is telling you something worth listening to. 💕
            </div>
            <div class="score-bar-wrap">
                <div class="progress-label"><span>Symptom Score</span><span>{pct}%</span></div>
                <div class="score-bar-track">
                    <div class="score-bar-fill" style="width:{pct}%;background:linear-gradient(90deg,#f2a0af,#e8637a)"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif level == "moderate":
        st.markdown(f"""
        <div class="result-positive" style="background:linear-gradient(145deg,#fff8f0,#fdebd0);border-color:#f0c070;">
            <div class="result-emoji">🌼</div>
            <div class="result-title" style="color:#c07830">
                Some PCOS signs — worth keeping an eye on
            </div>
            <div class="result-subtitle" style="color:#7a5a66">
                You have <strong>some symptoms</strong> that can be associated with PCOS,
                but they may also have other causes. Getting checked by a doctor would give
                you clarity and peace of mind. 🌻
            </div>
            <div class="score-bar-wrap">
                <div class="progress-label"><span>Symptom Score</span><span>{pct}%</span></div>
                <div class="score-bar-track">
                    <div class="score-bar-fill" style="width:{pct}%;background:linear-gradient(90deg,#f6d365,#f0a030)"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown(f"""
        <div class="result-negative">
            <div class="result-emoji">🌿</div>
            <div class="result-title" style="color:#2e8b6e">
                You're looking good! Low PCOS likelihood
            </div>
            <div class="result-subtitle" style="color:#3d6b5e">
                Your symptoms don't strongly suggest PCOS right now. That's great news! 🎉
                Keep up healthy habits and check in with your doctor if anything changes.
            </div>
            <div class="score-bar-wrap">
                <div class="progress-label"><span>Symptom Score</span><span>{pct}%</span></div>
                <div class="score-bar-track">
                    <div class="score-bar-fill" style="width:{pct}%;background:linear-gradient(90deg,#a8edcc,#52c789)"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Your Symptom Summary ──
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">📋 Your Symptom Summary</div>
    """, unsafe_allow_html=True)

    symptom_map = {
        "cycle": ("Period regularity", ["Regular 🟢", "Slightly irregular 🟡", "Often irregular 🔴", "Rarely/never 🔴"]),
        "cycle_length": ("Period duration", ["Normal (3-7 days) 🟢", "Short 🟡", "Long 🔴", "Very variable 🟡"]),
        "hair_growth": ("Body hair growth", ["Normal 🟢", "Mild hirsutism 🟡", "Noticeable hirsutism 🔴", "Worsening 🔴"]),
        "hair_loss": ("Scalp hair loss", ["Healthy 🟢", "Mild shedding 🟡", "Thinning 🔴", "Significant loss 🔴"]),
        "acne": ("Skin/acne", ["Clear 🟢", "Hormonal PMS acne 🟡", "Persistent jawline acne 🔴", "Severe acne 🔴"]),
        "weight": ("Weight changes", ["Stable 🟢", "Slight gain 🟡", "Unexplained gain 🔴", "Stubborn belly weight 🔴"]),
        "skin": ("Skin darkening", ["Even skin 🟢", "Slightly darker 🟡", "Dark patches (Acanthosis) 🔴"]),
        "mood": ("Mood & anxiety", ["Balanced 🟢", "PMS swings 🟡", "Frequent mood issues 🔴", "Significant anxiety/depression 🔴"]),
        "fatigue": ("Energy levels", ["Normal 🟢", "Sometimes tired 🟡", "Often exhausted 🔴", "Chronic fatigue + weight resistant 🔴"]),
        "age_family": ("Family/history factors", ["None 🟢", "Post-pill irregularity 🟡", "Family history 🔴", "Early irregular cycles 🔴"]),
    }

    for qid, (label, desc_list) in symptom_map.items():
        score_val = st.session_state.answers.get(qid, 0)
        if score_val == 0:
            pill_cls, chip = "mint", desc_list[0]
        elif score_val == 1:
            pill_cls, chip = "lav", desc_list[min(1, len(desc_list)-1)]
        else:
            pill_cls, chip = "", desc_list[min(score_val, len(desc_list)-1)]
        st.markdown(
            f"<div style='display:flex;justify-content:space-between;align-items:center;"
            f"padding:0.5rem 0;border-bottom:1px solid #fde8ef;font-size:0.88rem;'>"
            f"<span style='color:#7a5a66;font-weight:600'>{label}</span>"
            f"<span class='tag-pill {pill_cls}'>{chip}</span>"
            f"</div>",
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # ── When to See a Doctor ──
    if level in ["high", "moderate"]:
        st.markdown("""
        <div class="doctor-card">
            <div class="info-card-title">🩺 When Should You See a Doctor?</div>
        """, unsafe_allow_html=True)

        if level == "high":
            st.markdown("""
            <p><strong>Please book an appointment soon</strong> — ideally within the next few weeks. Look for:</p>
            <p><span class="urgent-dot"></span><strong>Gynaecologist</strong> — for period irregularities and hormonal evaluation</p>
            <p><span class="urgent-dot"></span><strong>Endocrinologist</strong> — if you have significant weight/insulin concerns</p>
            <p><span class="urgent-dot"></span><strong>Dermatologist</strong> — if acne or hair loss is affecting your confidence</p>
            <br>
            <p style="font-weight:600;color:#c0404e">🔴 See a doctor urgently if you experience:</p>
            <p>• Periods missing for 3+ months</p>
            <p>• Severe pelvic pain</p>
            <p>• Extreme fatigue or sudden weight changes</p>
            <p>• Difficulty conceiving after 12 months of trying</p>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <p>Consider booking a <strong>routine appointment</strong> with your gynaecologist — no urgency, but worth doing:</p>
            <p><span class="urgent-dot" style="background:#f0a030"></span>Get a <strong>hormonal blood panel</strong> done (LH, FSH, AMH, Testosterone)</p>
            <p><span class="urgent-dot" style="background:#f0a030"></span>Ask about a <strong>pelvic ultrasound</strong> to check ovaries</p>
            <p><span class="urgent-dot" style="background:#f0a030"></span>Track your cycle for 3 months with an app like <em>Clue</em> or <em>Flo</em></p>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # ── What Tests Will the Doctor Do ──
        st.markdown("""
        <div class="info-card">
            <div class="info-card-title">🔬 What Tests Will the Doctor Do?</div>
            <p>PCOS is diagnosed using the <strong>"Rotterdam Criteria"</strong> — you need 2 of these 3:</p>
            <br>
            <p>🌸 <strong>Irregular or absent periods</strong> — assessed by your history</p>
            <p>🌸 <strong>High androgens (male hormones)</strong> — blood test for testosterone, DHEA</p>
            <p>🌸 <strong>Polycystic ovaries on ultrasound</strong> — 12+ follicles visible in one ovary</p>
            <br>
            <p>They may also check: <span class="tag-pill">Blood sugar</span> <span class="tag-pill">Insulin</span> <span class="tag-pill">Thyroid</span> <span class="tag-pill">AMH levels</span> <span class="tag-pill">Prolactin</span></p>
        </div>
        """, unsafe_allow_html=True)

    # ── Understanding PCOS ──
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">💡 Understanding PCOS — Simplified</div>
        <p>
            Think of PCOS like a hormonal traffic jam 🚦 — your body produces slightly too
            much of certain hormones, which throws your cycle, skin, and metabolism off balance.
        </p>
        <br>
        <p><strong>The main hormonal issues in PCOS:</strong></p>
        <p>🔺 <strong>Too much LH</strong> (Luteinising Hormone) — disrupts ovulation</p>
        <p>🔺 <strong>High androgens</strong> (male hormones like testosterone) — cause acne, hair growth, hair loss</p>
        <p>🔺 <strong>Insulin resistance</strong> — your cells resist insulin, causing weight gain and fatigue</p>
        <p>🔺 <strong>Low progesterone</strong> — makes periods irregular or absent</p>
        <br>
        <p>The tiny "cysts" in PCOS are actually <em>immature follicles</em> that couldn't ovulate — they're not dangerous.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── What You Can Do ──
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">🌱 What You Can Do — Right Now</div>
        <p>Whether or not you have PCOS, these lifestyle habits make a huge difference:</p>
        <br>
        <p>🥗 <strong>Anti-inflammatory diet</strong> — whole grains, leafy greens, berries, omega-3s.
           Cut processed sugar and refined carbs (they spike insulin).</p>
        <p>🏃‍♀️ <strong>Move your body</strong> — even 30 minutes of walking daily improves insulin sensitivity.</p>
        <p>😴 <strong>Prioritise sleep</strong> — poor sleep worsens hormonal imbalances.</p>
        <p>🧘‍♀️ <strong>Manage stress</strong> — cortisol (stress hormone) directly disrupts ovulation.</p>
        <p>📱 <strong>Track your cycle</strong> — use Flo, Clue, or Ovia. Data helps your doctor.</p>
        <p>💊 <strong>Ask about supplements</strong> — Inositol, Vitamin D, and Spearmint tea have evidence for PCOS.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── PCOS & Fertility ──
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">💕 PCOS & Fertility — The Hopeful Truth</div>
        <p>
            Many women worry that PCOS means they can't have children. <strong>That's a myth.</strong>
        </p>
        <p style="margin-top:0.6rem">
            PCOS is one of the <em>most treatable</em> causes of fertility challenges.
            With the right care — lifestyle changes, medication, or fertility treatments —
            most women with PCOS go on to have healthy pregnancies. 🤱
        </p>
        <p style="margin-top:0.6rem">
            If you're planning to conceive, <strong>don't wait</strong> — speak to a
            gynaecologist early so you have the best possible support.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── You're not alone ──
    st.markdown("""
    <div style="background:linear-gradient(135deg,#fff0f4,#ede7f6);border-radius:20px;
                padding:1.8rem;text-align:center;margin-bottom:1.2rem;
                border:1.5px solid #f2c5d0;">
        <div style="font-size:2rem;margin-bottom:0.5rem">💌</div>
        <div style="font-family:'Playfair Display',serif;font-size:1.2rem;color:#c0404e;margin-bottom:0.6rem">
            You're not alone in this
        </div>
        <div style="font-size:0.9rem;color:#7a5a66;max-width:450px;margin:0 auto;line-height:1.7">
            Millions of women live full, happy, healthy lives with PCOS.
            Getting informed is the first and bravest step. You're already doing it. 🌸
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Disclaimer ──
    st.markdown("""
    <div class="disclaimer">
        ⚕️ <strong>Medical Disclaimer:</strong> This tool is for educational awareness only and
        does not constitute a medical diagnosis. PCOS can only be diagnosed by a qualified
        healthcare professional through blood tests and ultrasound. Please consult your doctor
        for proper evaluation and personalised medical advice.
    </div>
    """, unsafe_allow_html=True)

    # ── Restart ──
    st.markdown("")
    with st.container():
        st.markdown("<div class='restart-btn'>", unsafe_allow_html=True)
        if st.button("🔄  Start Over"):
            reset()
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="petal-bar">🌸 🌺 🌸 🌺 🌸</div>
    <div style="text-align:center;font-size:0.78rem;color:#c9a0b0;padding-bottom:2rem;">
        Made with love for every woman navigating her health journey 💕
    </div>
    """, unsafe_allow_html=True)
