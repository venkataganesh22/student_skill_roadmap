import streamlit as st
import pandas as pd
import random
from datetime import date

st.set_page_config(
    page_title=" Personalized SkillRoadmap",
    page_icon="🎯",
    layout="wide",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

:root {
  --bg:        #020817;
  --surface:   rgba(15,23,42,0.72);
  --border:    rgba(99,102,241,0.22);
  --indigo:    #6366f1;
  --violet:    #8b5cf6;
  --emerald:   #34d399;
  --sky:       #38bdf8;
  --amber:     #fbbf24;
  --rose:      #fb7185;
  --text:      #e2e8f0;
  --muted:     #64748b;
}

html, body, [class*="css"] {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  background: var(--bg) !important;
  color: var(--text) !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 0 !important; max-width: 100% !important; }

::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--indigo); border-radius: 99px; }

/* ── LANDING ── */
.landing {
  min-height: 100vh;
  background:
    radial-gradient(ellipse 80% 60% at 15% 55%,  rgba(99,102,241,0.38) 0%, transparent 60%),
    radial-gradient(ellipse 60% 50% at 85% 25%,  rgba(139,92,246,0.30) 0%, transparent 55%),
    radial-gradient(ellipse 70% 55% at 55% 90%,  rgba(16,185,129,0.18) 0%, transparent 58%),
    radial-gradient(ellipse 50% 40% at 80% 75%,  rgba(56,189,248,0.12) 0%, transparent 55%),
    #020817;
  padding-bottom: 80px;
}
.nav {
  display: flex; align-items: center; justify-content: space-between;
  padding: 20px 48px;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}
.nav-logo {
  font-family: 'Syne', sans-serif; font-size: 18px; font-weight: 800;
  background: linear-gradient(135deg, #a5b4fc, #34d399);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.nav-badge {
  background: rgba(99,102,241,0.15); border: 1px solid rgba(99,102,241,0.30);
  color: #a5b4fc; font-size: 11px; font-weight: 600; padding: 5px 14px;
  border-radius: 999px; letter-spacing: 0.06em;
}
.hero { text-align: center; padding: 72px 24px 48px; }
.confused-tag {
  display: inline-block;
  background: rgba(251,191,36,0.12); border: 1px solid rgba(251,191,36,0.30);
  color: #fcd34d; font-size: 13px; font-weight: 600;
  padding: 6px 18px; border-radius: 999px; margin-bottom: 28px;
  letter-spacing: 0.04em; animation: fadeDown 0.6s ease both;
}
@keyframes fadeDown {
  from { opacity:0; transform:translateY(-12px); }
  to   { opacity:1; transform:translateY(0); }
}
.hero-h1 {
  font-family: 'Syne', sans-serif;
  font-size: clamp(32px, 6vw, 60px); font-weight: 800; line-height: 1.08;
  margin-bottom: 22px; animation: fadeDown 0.7s ease 0.1s both;
}
.hero-h1 .line1 {
  display: block;
  background: linear-gradient(135deg, #fff 30%, #c7d2fe);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero-h1 .line2 {
  display: block;
  background: linear-gradient(135deg, #a5b4fc, #34d399 70%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero-sub {
  font-size: 16px; color: #64748b; max-width: 520px;
  margin: 0 auto 40px; line-height: 1.7;
  animation: fadeDown 0.7s ease 0.2s both;
}
.quote-card {
  max-width: 600px; margin: 0 auto 52px;
  background: rgba(15,23,42,0.70); backdrop-filter: blur(12px);
  border: 1px solid rgba(99,102,241,0.22); border-left: 4px solid #6366f1;
  border-radius: 16px; padding: 22px 28px;
  animation: fadeDown 0.7s ease 0.3s both;
}
.quote-text  { font-size: 15px; font-style: italic; color: #e2e8f0; line-height: 1.65; margin-bottom: 10px; }
.quote-author{ font-size: 12px; color: #6366f1; font-weight: 600; letter-spacing: 0.05em; }
.img-row {
  display: flex; justify-content: center; gap: 16px;
  margin: 0 auto 56px; max-width: 860px; padding: 0 24px;
  animation: fadeDown 0.7s ease 0.35s both;
}
.img-card {
  flex: 1; min-width: 0; border-radius: 20px; overflow: hidden;
  border: 1px solid rgba(255,255,255,0.08); box-shadow: 0 8px 32px rgba(0,0,0,0.45);
  position: relative; transition: transform 0.25s;
}
.img-card:hover { transform: translateY(-5px); }
.img-card img  { width: 100%; height: 200px; object-fit: cover; display: block; filter: brightness(0.82) saturate(1.1); }
.img-overlay   { position: absolute; bottom:0; left:0; right:0; background: linear-gradient(transparent, rgba(2,8,23,0.85)); padding: 20px 16px 14px; }
.img-label     { font-family: 'Syne', sans-serif; font-size: 13px; font-weight: 700; color: #fff; }
.img-sub       { font-size: 11px; color: rgba(255,255,255,0.50); margin-top: 2px; }
.stats-row {
  display: flex; justify-content: center; gap: 32px;
  margin: 0 auto 56px; flex-wrap: wrap;
  animation: fadeDown 0.7s ease 0.4s both;
}
.stat-num {
  font-family: 'Syne', sans-serif; font-size: 28px; font-weight: 800;
  background: linear-gradient(135deg, #a5b4fc, #34d399);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.stat-label { font-size: 12px; color: #475569; margin-top: 4px; letter-spacing: 0.04em; text-transform: uppercase; }
.features {
  display: flex; justify-content: center; gap: 16px;
  max-width: 860px; margin: 0 auto 56px; padding: 0 24px; flex-wrap: wrap;
  animation: fadeDown 0.7s ease 0.45s both;
}
.feat-card {
  flex: 1; min-width: 200px;
  background: rgba(15,23,42,0.65); border: 1px solid rgba(99,102,241,0.18);
  border-radius: 16px; padding: 20px 18px; backdrop-filter: blur(10px);
  transition: border-color 0.2s, transform 0.2s;
}
.feat-card:hover { border-color: rgba(99,102,241,0.45); transform: translateY(-3px); }
.feat-icon  { font-size: 24px; margin-bottom: 10px; }
.feat-title { font-family: 'Syne', sans-serif; font-size: 14px; font-weight: 700; color: #e2e8f0; margin-bottom: 6px; }
.feat-desc  { font-size: 12px; color: #64748b; line-height: 1.6; }

/* ── CTA button ── */
div[data-testid="stButton"] > button {
  background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
  color: #fff !important; border: none !important; border-radius: 14px !important;
  padding: 16px 48px !important; font-family: 'Syne', sans-serif !important;
  font-size: 16px !important; font-weight: 800 !important; letter-spacing: 0.04em !important;
  box-shadow: 0 6px 28px rgba(99,102,241,0.45) !important;
  transition: all 0.2s !important; min-width: 260px !important;
}
div[data-testid="stButton"] > button:hover {
  opacity: 0.88 !important; transform: translateY(-3px) !important;
  box-shadow: 0 12px 36px rgba(99,102,241,0.55) !important;
}

/* ── APP PAGE ── */
.app-header {
  padding: 20px 48px 18px;
  border-bottom: 1px solid rgba(99,102,241,0.18);
  background: rgba(2,8,23,0.97) !important;
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  position: sticky; top: 0; z-index: 100;
}
.app-logo {
  font-family: 'Syne', sans-serif; font-size: 22px; font-weight: 800;
  background: linear-gradient(135deg, #a5b4fc, #34d399);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.g-card {
  background: rgba(15,23,42,0.65);
  border: 1px solid rgba(99,102,241,0.20);
  border-radius: 20px; padding: 28px 32px;
  backdrop-filter: blur(14px);
  margin-bottom: 20px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.35);
}
.g-card-title {
  font-family: 'Syne', sans-serif; font-size: 18px; font-weight: 800;
  color: #e2e8f0; margin-bottom: 6px;
}
.g-card-sub { font-size: 13px; color: #475569; }
.sec-pill {
  display: inline-flex; align-items: center; gap: 8px;
  background: rgba(99,102,241,0.12); border: 1px solid rgba(99,102,241,0.28);
  color: #a5b4fc; font-size: 12px; font-weight: 700;
  padding: 5px 16px; border-radius: 999px; letter-spacing: 0.06em;
  margin-bottom: 16px; text-transform: uppercase;
}
.goal-item {
  display: flex; align-items: flex-start; gap: 12px;
  background: rgba(52,211,153,0.07); border: 1px solid rgba(52,211,153,0.20);
  border-radius: 12px; padding: 12px 16px; margin-bottom: 10px;
}
.goal-dot { width: 8px; height: 8px; border-radius: 50%; background: #34d399; margin-top: 5px; flex-shrink: 0; }
.goal-text { font-size: 14px; color: #e2e8f0; line-height: 1.6; }
.risk-item {
  display: flex; align-items: flex-start; gap: 12px;
  background: rgba(251,113,133,0.08); border: 1px solid rgba(251,113,133,0.22);
  border-radius: 12px; padding: 12px 16px; margin-bottom: 10px;
}
.risk-dot { width: 8px; height: 8px; border-radius: 50%; background: #fb7185; margin-top: 5px; flex-shrink: 0; }
.habit-item {
  display: flex; align-items: flex-start; gap: 12px;
  background: rgba(56,189,248,0.07); border: 1px solid rgba(56,189,248,0.20);
  border-radius: 12px; padding: 12px 16px; margin-bottom: 10px;
}
.habit-dot { width: 8px; height: 8px; border-radius: 50%; background: #38bdf8; margin-top: 5px; flex-shrink: 0; }
.step-item {
  display: flex; align-items: flex-start; gap: 14px;
  background: rgba(139,92,246,0.07); border: 1px solid rgba(139,92,246,0.20);
  border-radius: 12px; padding: 12px 16px; margin-bottom: 10px;
}
.step-num {
  width: 26px; height: 26px; border-radius: 50%;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  display: flex; align-items: center; justify-content: center;
  font-size: 12px; font-weight: 800; color: #fff; flex-shrink: 0;
}
.week-card {
  background: rgba(15,23,42,0.60); border: 1px solid rgba(99,102,241,0.18);
  border-radius: 16px; padding: 20px 24px; margin-bottom: 16px;
}
.week-title {
  font-family: 'Syne', sans-serif; font-size: 15px; font-weight: 800;
  margin-bottom: 12px;
  background: linear-gradient(135deg, #a5b4fc, #34d399);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.week-bullet {
  display: flex; align-items: flex-start; gap: 10px;
  font-size: 13px; color: #94a3b8; line-height: 1.6; margin-bottom: 8px;
}
.week-bullet::before { content: '▸'; color: #6366f1; flex-shrink: 0; margin-top: 1px; }
.proj-card {
  background: rgba(251,191,36,0.06); border: 1px solid rgba(251,191,36,0.20);
  border-radius: 14px; padding: 14px 18px; margin-bottom: 10px;
  display: flex; align-items: center; gap: 12px;
}
.proj-icon { font-size: 20px; }
.proj-name { font-size: 14px; font-weight: 600; color: #fcd34d; }
.res-card {
  background: rgba(56,189,248,0.06); border: 1px solid rgba(56,189,248,0.20);
  border-radius: 14px; padding: 14px 18px; margin-bottom: 10px;
  display: flex; align-items: center; gap: 12px;
}
.res-icon { font-size: 18px; }
.res-name  { font-size: 14px; color: #7dd3fc; }
.score-ring-wrap { text-align: center; padding: 20px 0; }
.score-big {
  font-family: 'Syne', sans-serif; font-size: 64px; font-weight: 800;
  background: linear-gradient(135deg, #a5b4fc, #34d399);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  line-height: 1;
}
.score-label { font-size: 13px; color: #475569; margin-top: 4px; letter-spacing: 0.08em; text-transform: uppercase; }
.score-bar-wrap { margin-bottom: 14px; }
.score-bar-label {
  display: flex; justify-content: space-between;
  font-size: 12px; font-weight: 600; margin-bottom: 5px;
}
.score-bar-track {
  height: 8px; border-radius: 999px; background: rgba(255,255,255,0.08);
  overflow: hidden;
}
.score-bar-fill { height: 100%; border-radius: 999px; }
.metric-tile {
  background: rgba(15,23,42,0.65); border: 1px solid rgba(99,102,241,0.20);
  border-radius: 16px; padding: 18px 22px; text-align: center;
}
.metric-val {
  font-family: 'Syne', sans-serif; font-size: 28px; font-weight: 800;
  background: linear-gradient(135deg, #a5b4fc, #34d399);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.metric-label { font-size: 11px; color: #475569; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.06em; }
.skill-have {
  background: rgba(52,211,153,0.10); border: 1px solid rgba(52,211,153,0.30);
  border-radius: 10px; padding: 10px 16px; margin-bottom: 8px;
  font-size: 13px; color: #6ee7b7; font-weight: 600;
  display: flex; align-items: center; gap: 8px;
}
.skill-need {
  background: rgba(251,113,133,0.10); border: 1px solid rgba(251,113,133,0.30);
  border-radius: 10px; padding: 10px 16px; margin-bottom: 8px;
  font-size: 13px; color: #fda4af; font-weight: 600;
  display: flex; align-items: center; gap: 8px;
}
.learn-step {
  display: flex; align-items: center; gap: 12px;
  background: rgba(139,92,246,0.08); border: 1px solid rgba(139,92,246,0.22);
  border-radius: 12px; padding: 12px 16px; margin-bottom: 8px;
}
.learn-step-num {
  width: 28px; height: 28px; border-radius: 50%;
  background: linear-gradient(135deg, #8b5cf6, #6366f1);
  display: flex; align-items: center; justify-content: center;
  font-size: 12px; font-weight: 800; color: #fff; flex-shrink: 0;
}
.learn-step-text { font-size: 14px; color: #c4b5fd; }

/* ── PROGRESS BAR ── */
.stProgress > div > div > div > div {
  background: linear-gradient(90deg, #6366f1, #8b5cf6, #34d399) !important;
  border-radius: 999px !important;
}
.stProgress > div > div > div { background: rgba(255,255,255,0.08) !important; border-radius: 999px !important; }

/* ════════════════════════════════════════
   SELECTBOX — ALWAYS VISIBLE (BUG FIX)
   ════════════════════════════════════════ */
div[data-baseweb="select"] > div {
  background: rgba(15,23,42,0.88) !important;
  border: 1.5px solid rgba(99,102,241,0.55) !important;
  border-radius: 12px !important;
  color: #e2e8f0 !important;
  transition: border-color 0.2s, box-shadow 0.2s !important;
}
div[data-baseweb="select"] > div:hover {
  border-color: rgba(99,102,241,0.90) !important;
  box-shadow: 0 0 0 3px rgba(99,102,241,0.15) !important;
}
div[data-baseweb="select"] > div:focus-within {
  border-color: #6366f1 !important;
  box-shadow: 0 0 0 3px rgba(99,102,241,0.22) !important;
}
div[data-baseweb="select"] span,
div[data-baseweb="select"] div[class*="ValueContainer"] {
  color: #e2e8f0 !important;
  background: transparent !important;
}
div[data-baseweb="select"] svg {
  fill: #a5b4fc !important;
}
ul[data-baseweb="menu"],
div[data-baseweb="popover"] > div,
div[role="listbox"] {
  background-color: #0f172a !important;
  border: 1px solid rgba(99,102,241,0.35) !important;
  border-radius: 14px !important;
  box-shadow: 0 12px 40px rgba(0,0,0,0.60) !important;
  padding: 6px !important;
}
li[role="option"] {
  background: transparent !important;
  color: #cbd5e1 !important;
  font-size: 14px !important;
  border-radius: 8px !important;
  padding: 10px 14px !important;
  transition: background 0.15s !important;
}
li[role="option"]:hover {
  background: rgba(99,102,241,0.22) !important;
  color: #fff !important;
}
li[role="option"][aria-selected="true"] {
  background: rgba(99,102,241,0.30) !important;
  color: #c7d2fe !important;
  font-weight: 600 !important;
}
div[data-baseweb="select"] input::placeholder {
  color: #475569 !important;
}

/* ════════════════════════════════════════
   TEXT INPUT — ALWAYS VISIBLE
   ════════════════════════════════════════ */
.stTextInput > div > div > input {
  background: rgba(15,23,42,0.88) !important;
  border: 1.5px solid rgba(99,102,241,0.55) !important;
  border-radius: 12px !important;
  color: #e2e8f0 !important;
  font-size: 14px !important;
  transition: border-color 0.2s, box-shadow 0.2s !important;
}
.stTextInput > div > div > input:focus {
  border-color: #6366f1 !important;
  box-shadow: 0 0 0 3px rgba(99,102,241,0.22) !important;
  outline: none !important;
}
.stTextInput > div > div > input::placeholder { color: #475569 !important; }

/* ════════════════════════════════════════
   NUMBER INPUT — ALWAYS VISIBLE
   ════════════════════════════════════════ */
.stNumberInput > div > div > input {
  background: rgba(15,23,42,0.88) !important;
  border: 1.5px solid rgba(99,102,241,0.55) !important;
  border-radius: 12px !important;
  color: #e2e8f0 !important;
  font-size: 14px !important;
  transition: border-color 0.2s, box-shadow 0.2s !important;
}
.stNumberInput > div > div > input:focus {
  border-color: #6366f1 !important;
  box-shadow: 0 0 0 3px rgba(99,102,241,0.22) !important;
}
.stNumberInput button {
  background: rgba(99,102,241,0.12) !important;
  border: 1px solid rgba(99,102,241,0.35) !important;
  color: #a5b4fc !important;
  border-radius: 8px !important;
}
.stNumberInput button:hover {
  background: rgba(99,102,241,0.28) !important;
}

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
  background: rgba(15,23,42,0.60) !important;
  border-radius: 14px !important; padding: 4px !important;
  gap: 4px !important; border: 1px solid rgba(99,102,241,0.18) !important;
}
.stTabs [data-baseweb="tab"] {
  background: transparent !important; border-radius: 10px !important;
  color: #64748b !important; font-weight: 600 !important; font-size: 13px !important;
  padding: 8px 16px !important;
}
.stTabs [aria-selected="true"] {
  background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
  color: #fff !important; box-shadow: 0 2px 12px rgba(99,102,241,0.40) !important;
}

/* ── EXPANDER ── */
.streamlit-expanderHeader {
  background: rgba(15,23,42,0.65) !important;
  border: 1px solid rgba(99,102,241,0.20) !important;
  border-radius: 12px !important; color: #e2e8f0 !important; font-weight: 600 !important;
}

/* ── DOWNLOAD BUTTON ── */
.stDownloadButton > button {
  background: linear-gradient(135deg, #059669, #34d399) !important;
  color: #fff !important; border: none !important; border-radius: 12px !important;
  font-weight: 700 !important; letter-spacing: 0.04em !important;
  box-shadow: 0 4px 18px rgba(52,211,153,0.35) !important;
}

/* ── WIDGET LABELS ── */
.stSelectbox label, .stSlider label, .stTextInput label,
.stNumberInput label, .stMultiSelect label {
  color: #94a3b8 !important; font-size: 13px !important; font-weight: 600 !important;
}

/* ── MULTISELECT tags ── */
div[data-baseweb="tag"] {
  background: rgba(99,102,241,0.22) !important;
  border: 1px solid rgba(99,102,241,0.40) !important;
  border-radius: 6px !important; color: #c7d2fe !important; font-size: 12px !important;
}
div[data-baseweb="tag"] span { color: #c7d2fe !important; }
div[data-baseweb="tag"] button svg { fill: #a5b4fc !important; }
div[data-testid="stMultiSelect"] div[data-baseweb="select"] > div {
  background: rgba(15,23,42,0.88) !important;
  border: 1.5px solid rgba(99,102,241,0.55) !important;
  border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "home"
if "roadmap_data" not in st.session_state:
    st.session_state.roadmap_data = None
if "student_info" not in st.session_state:
    st.session_state.student_info = None
if "student_name" not in st.session_state:
    st.session_state.student_name = ""

# ─────────────────────────────────────────────
# LANDING PAGE
# ─────────────────────────────────────────────
def show_landing_page():
    QUOTES = [
        ("\"The secret of getting ahead is getting started.\"", "— Mark Twain"),
        ("\"Don't watch the clock; do what it does. Keep going.\"", "— Sam Levenson"),
        ("\"You don't have to be great to start, but you have to start to be great.\"", "— Zig Ziglar"),
        ("\"Push yourself, because no one else is going to do it for you.\"", "— Anonymous"),
        ("\"Dream big. Start small. Act now.\"", "— Robin Sharma"),
        ("\"Your future is created by what you do today, not tomorrow.\"", "— Robert Kiyosaki"),
        ("\"Success is the sum of small efforts repeated day in and day out.\"", "— Robert Collier"),
        ("\"Believe you can and you're halfway there.\"", "— Theodore Roosevelt"),
    ]
    quote_text, quote_author = random.choice(QUOTES)
    STUDENT_IMAGES = [
        "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=400&q=80",
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=400&q=80",
        "https://images.unsplash.com/photo-1529390079861-591de354faf5?w=400&q=80",
    ]
    st.markdown(f"""
    <div class="landing">
      <div class="nav">
        <div class="nav-logo">🎯  Personalized SkillRoadmap</div>
      </div>
      <div class="hero">
        <div class="confused-tag">😕 &nbsp; Not sure where to start?</div>
        <h1 class="hero-h1">
          <span class="line1">Stop feeling lost.</span>
          <span class="line2">Build your roadmap today.</span>
        </h1>
        <p class="hero-sub">
          Answer a few simple questions about yourself — we'll generate a
          personalised 4-week learning plan with projects, resources, and a
          readiness score. Made for engineering students like you.
        </p>
        <div class="quote-card">
          <div class="quote-text">{quote_text}</div>
          <div class="quote-author">{quote_author}</div>
        </div>
      </div>
      <div class="img-row">
        <div class="img-card">
          <img src="{STUDENT_IMAGES[0]}" alt="Students studying"/>
          <div class="img-overlay"><div class="img-label">Collaborate &amp; Grow</div><div class="img-sub">Learn with peers</div></div>
        </div>
        <div class="img-card">
          <img src="{STUDENT_IMAGES[1]}" alt="Group project"/>
          <div class="img-overlay"><div class="img-label">Build Real Projects</div><div class="img-sub">Portfolio-grade work</div></div>
        </div>
        <div class="img-card">
          <img src="{STUDENT_IMAGES[2]}" alt="Student laptop"/>
          <div class="img-overlay"><div class="img-label">Learn at Your Pace</div><div class="img-sub">Structured &amp; clear</div></div>
        </div>
      </div>
      <div class="stats-row">
        <div class="stat-item"><div class="stat-num">14+</div><div class="stat-label">Learning Tracks</div></div>
        <div class="stat-item"><div class="stat-num">4</div><div class="stat-label">Week Plan</div></div>
        <div class="stat-item"><div class="stat-num">50+</div><div class="stat-label">Free Resources</div></div>
        <div class="stat-item"><div class="stat-num">100%</div><div class="stat-label">Personalised</div></div>
      </div>
      <div class="features">
        <div class="feat-card"><div class="feat-icon">📊</div><div class="feat-title">Readiness Score</div><div class="feat-desc">Get a breakdown of your academics, skills, routine, and communication.</div></div>
        <div class="feat-card"><div class="feat-icon">🗓️</div><div class="feat-title">4-Week Plan</div><div class="feat-desc">A clear week-by-week learning roadmap tailored to your interest and level.</div></div>
        <div class="feat-card"><div class="feat-icon">🧩</div><div class="feat-title">Skill Gap Analysis</div><div class="feat-desc">Pick a job role and instantly see what skills you have and what to learn next.</div></div>
        <div class="feat-card"><div class="feat-icon">⬇️</div><div class="feat-title">Download Roadmap</div><div class="feat-desc">Save your full roadmap as a Markdown file to keep and revisit anytime.</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.4, 1])
    with col2:
        if st.button("🚀  Start My Roadmap", use_container_width=True):
            st.session_state.page = "app"
            st.rerun()
    st.markdown('<p style="text-align:center;color:#334155;font-size:12px;margin-top:8px">Takes less than 2 minutes · No signup needed</p>', unsafe_allow_html=True)


# ─────────────────────────────────────────────
# COURSE DATABASE
# ─────────────────────────────────────────────
COURSE_DB = {
    "ML": {
        "courses": ["Andrew Ng — Machine Learning Specialization (Coursera)", "Krish Naik — Machine Learning Playlist (YouTube)", "fast.ai — Practical Deep Learning for Coders"],
        "weeks": ["Python + Numpy/Pandas + basics of ML (Regression, metrics).", "Scikit-learn: Decision Trees, Random Forest, model validation.", "Feature engineering + classification + overfitting control.", "Project: Build an end-to-end ML app and deploy via Streamlit."],
        "projects": ["House Price Predictor", "Student Performance Dashboard + Prediction", "Customer Segmentation (K-Means)"],
    },
    "WEB": {
        "courses": ["The Odin Project (Full Stack foundations)", "FreeCodeCamp — Responsive Web Design", "JavaScript/React Crash Course (YouTube)"],
        "weeks": ["HTML + CSS (Flex/Grid) + build 1 landing page.", "JavaScript (DOM, ES6, Fetch API) + small interactive UI.", "React basics (components, state, props) + mini app.", "Project: Deploy a portfolio-grade site/app (GitHub Pages/Vercel)."],
        "projects": ["Portfolio Website (Dark mode + sections)", "To-do App (LocalStorage)", "Mini E-commerce Product Gallery UI"],
    },
    "DSA": {
        "courses": ["Striver A2Z DSA Sheet (TakeUForward)", "NeetCode 150 (structured problems)", "Abdul Bari — Algorithms (YouTube)"],
        "weeks": ["Arrays/Strings + time complexity + 20 problems.", "Linked List + Stack/Queue + 15 problems.", "Trees + Recursion/Backtracking + 12 problems.", "Sorting/Searching + DP basics + mock interview set."],
        "projects": ["Sorting Visualizer", "Sudoku Solver", "Pathfinding Visualizer (BFS/Dijkstra)"],
    },
    "CYBER": {
        "courses": ["TryHackMe — Pre Security / Beginner Path", "OverTheWire (Bandit) — Linux basics practice", "YouTube: Networking + Web security basics (OWASP Top 10)"],
        "weeks": ["Linux + networking basics + command line practice.", "Web fundamentals + OWASP Top 10 (SQLi, XSS, auth issues).", "Hands-on labs (TryHackMe rooms) + write notes.", "Project: Security checklist + demo report (mini pentest style)."],
        "projects": ["Basic Web Security Audit Report (OWASP checklist)", "Password strength checker + hashing demo", "Phishing awareness mini-site (educational)"],
    },
    "ECE": {
        "courses": ["NPTEL — Digital Circuits / Microprocessors (choose 1)", "Embedded Systems (Arduino/ESP32) playlist (YouTube)", "VLSI Basics / Communication Systems intro (NPTEL/YouTube)"],
        "weeks": ["Core: C basics + digital logic fundamentals (gates, flip-flops).", "Embedded basics: Arduino/ESP32 + sensors (read data, print/plot).", "Choose one: VLSI basics OR Communication Systems basics.", "Project: Mini IoT/Embedded demo + documentation + results."],
        "projects": ["IoT Temperature/Humidity Monitor (sensor + dashboard)", "Arduino Sensor Data Logger", "Mini Communication System simulation report (basic)"],
    },
    "COMM_SYSTEMS": {
        "courses": ["NPTEL — Communication Systems", "Signals & Systems basics (YouTube/NPTEL)", "MATLAB/Python signal processing basics (tutorial series)"],
        "weeks": ["Signals basics: sampling, frequency, noise concept.", "AM/FM basics + modulation/demodulation understanding.", "Digital comm intro: ASK/FSK/PSK concept + simple plots.", "Project: small simulation notebook + report (plots + explanation)."],
        "projects": ["AM/FM simulation notebook", "Noise impact on signal plots", "Digital modulation demo (basic)"],
    },
    "VLSI": {
        "courses": ["NPTEL — VLSI Design", "Digital Electronics (NPTEL/YouTube)", "Verilog basics playlist (YouTube)"],
        "weeks": ["Digital design recap + number systems + logic optimization.", "Verilog basics: modules, testbench, simulation flow.", "Combinational + sequential circuits in Verilog.", "Project: design a small digital system + simulate + report."],
        "projects": ["4-bit ALU in Verilog", "Traffic Light Controller (FSM) in Verilog", "Simple Counter/Shift Register designs"],
    },
    "SIGNAL": {
        "courses": ["NPTEL — Signals and Systems / DSP intro", "Python for Signal Processing (NumPy/Scipy) tutorials", "YouTube: DSP basics (filters, FFT)"],
        "weeks": ["Signals basics + plotting + basic transforms concept.", "FFT basics + noise removal concept.", "Filters (low/high pass) concept + simple implementations.", "Project: signal cleaning / analysis notebook + report."],
        "projects": ["Noise filtering demo (FFT + filter)", "Audio signal analysis notebook", "Sensor signal smoothing + plots"],
    },
    "IOT": {
        "courses": ["Arduino/ESP32 IoT playlist (YouTube)", "NPTEL — Introduction to IoT", "Basics of MQTT/HTTP + simple dashboards"],
        "weeks": ["Microcontroller + sensor basics + read values.", "Send data: serial/log file + basic visualization.", "Add connectivity (Wi-Fi/MQTT/HTTP) basic.", "Project: IoT dashboard demo + short video + README."],
        "projects": ["Smart home sensor dashboard", "Weather station mini project", "Room monitoring (temp/light) demo"],
    },
    "EMBEDDED": {
        "courses": ["Embedded C basics (YouTube)", "Arduino/ESP32 practical series", "Basics of interrupts/timers (tutorial series)"],
        "weeks": ["Embedded C: loops, pointers basics, debugging mindset.", "GPIO + sensor interfacing + basic timing.", "Interrupts/timers basics + simple control logic.", "Project: embedded mini demo + documentation."],
        "projects": ["Digital stopwatch timer", "Sensor-based alert system", "LED patterns with interrupts/timers"],
    },
    "EEE": {
        "courses": ["NPTEL — Power Systems", "NPTEL — Electrical Machines", "Industrial Automation basics (YouTube/NPTEL)"],
        "weeks": ["Basics: power system components + machines recap.", "Protection & control basics + simple problem practice.", "Renewable/Smart grid basics (choose 1 focus).", "Project: mini case-study/report with calculations + charts."],
        "projects": ["Load analysis mini report (Excel/Python)", "Renewable energy comparison case study", "Basic fault analysis notes + examples"],
    },
    "POWER": {
        "courses": ["NPTEL — Power Systems (core)", "Protection & Switchgear basics (YouTube/NPTEL)", "Power flow intro (basic concepts)"],
        "weeks": ["Power system overview + per-unit basics (light).", "Protection basics (relays, faults) + examples.", "Transmission/distribution concepts + reliability.", "Project: load/fault calculation sheet + report."],
        "projects": ["Fault calculation worksheet + explanation", "Load estimation report for hostel/house", "Transmission line parameter mini notebook"],
    },
    "RENEW": {
        "courses": ["NPTEL — Renewable Energy", "Solar PV basics (YouTube/NPTEL)", "Wind energy basics (tutorial series)"],
        "weeks": ["Solar PV basics + components + sizing idea.", "Wind/other renewables basics + pros/cons.", "Hybrid systems + storage basics (battery).", "Project: solar sizing calculator + mini report."],
        "projects": ["Solar sizing calculator (Excel/Python)", "Renewable comparison infographic/report", "Microgrid case study summary"],
    },
    "SMARTGRID": {
        "courses": ["Smart Grid basics (NPTEL/YouTube)", "Power electronics intro (for grid integration)", "SCADA basics overview (intro)"],
        "weeks": ["Smart grid concept + components + communication basics.", "Demand response + metering + grid monitoring concepts.", "Grid integration of renewables + challenges.", "Project: smart grid concept report + diagram + demo slides."],
        "projects": ["Smart grid architecture diagram + report", "Demand response mini case study", "Energy monitoring dashboard concept"],
    },
    "AUTOMATION": {
        "courses": ["Industrial Automation basics (YouTube/NPTEL)", "PLC fundamentals (intro course)", "Sensors + actuators basics"],
        "weeks": ["Automation basics + sensors/actuators overview.", "PLC fundamentals (ladder logic concept).", "Control basics: feedback, stability concept.", "Project: automation workflow diagram + mini case study."],
        "projects": ["PLC ladder logic mini examples (documented)", "Sensor-actuator workflow demo (simulation/report)", "Industry process automation case study"],
    },
    "ELECTRICAL_DESIGN": {
        "courses": ["Electrical Design basics (YouTube/notes)", "AutoCAD Electrical basics (optional)", "Basics of wiring, safety, standards (overview)"],
        "weeks": ["Wiring basics + safety + common components.", "Reading single-line diagrams (SLD) basics.", "Load calculation + protection selection basics.", "Project: Create an SLD + load sheet + report."],
        "projects": ["Single-line diagram + explanation", "Load calculation sheet for a building", "Protection device selection notes"],
    },
    "MECH": {
        "courses": ["CAD basics (Fusion 360/SolidWorks tutorials)", "NPTEL — Manufacturing / Thermal Engineering (choose 1)", "Robotics basics (intro course/playlist)"],
        "weeks": ["CAD basics: sketches + 3 simple parts.", "Manufacturing basics OR Thermal basics (choose one).", "Robotics basics + mechanisms overview.", "Project: design + report (CAD model + documentation)."],
        "projects": ["CAD assembly mini project", "Manufacturing process comparison report", "Thermal analysis mini notes + examples"],
    },
    "CAD": {
        "courses": ["Fusion 360 / SolidWorks beginner tutorials", "Engineering drawing basics (YouTube)", "Basic GD&T overview (optional)"],
        "weeks": ["Sketching + constraints + 3 practice parts.", "3D modeling + assembly basics.", "Drawings + dimensions + tolerances basics.", "Project: model + drawing pack + short explanation."],
        "projects": ["CAD model of simple machine part", "Assembly of basic mechanism", "Drawing sheet pack (PDF) + notes"],
    },
    "ROBOTICS": {
        "courses": ["Robotics basics playlist (YouTube)", "Arduino basics (for small robotics demos)", "Mechanisms + control intro (overview)"],
        "weeks": ["Basics: sensors + motors overview + simple control idea.", "Arduino motor control basics + small demo.", "Robot mechanisms + path planning intro (basic).", "Project: mini robot demo plan + documentation/video."],
        "projects": ["Line follower robot plan/demo", "Obstacle avoidance mini demo", "Robot arm concept + CAD (optional)"],
    },
    "AUTO": {
        "courses": ["Automobile basics (YouTube/NPTEL)", "Engine + transmission basics overview", "Vehicle dynamics intro (basic)"],
        "weeks": ["Vehicle components + engine basics.", "Transmission + braking + steering basics.", "Vehicle dynamics intro + safety concepts.", "Project: vehicle subsystem report + diagrams."],
        "projects": ["Vehicle subsystem case study (brakes/engine)", "Maintenance checklist + explanation", "Auto trends summary report"],
    },
    "THERMAL": {
        "courses": ["NPTEL — Thermal Engineering basics", "Heat transfer intro playlist (YouTube)", "Basic thermodynamics notes + problems"],
        "weeks": ["Thermo basics: laws + properties + simple problems.", "Heat transfer basics (conduction/convection/radiation).", "Cycles overview (Rankine/Brayton) basic.", "Project: mini thermal calculation sheet + report."],
        "projects": ["Heat loss calculation mini sheet", "Thermal cycle summary report", "Cooling system concept notes"],
    },
    "MANUFACTURING": {
        "courses": ["NPTEL — Manufacturing Processes", "Metrology basics (YouTube/NPTEL)", "Lean manufacturing overview (intro)"],
        "weeks": ["Manufacturing basics: casting/forming/machining overview.", "Metrology basics + quality concepts.", "Lean basics (5S, waste reduction).", "Project: process comparison + case study report."],
        "projects": ["Manufacturing process comparison report", "Lean 5S checklist for workshop", "Quality control mini notes + examples"],
    },
    "SOFT": {
        "courses": ["Basic Communication Skills playlist (YouTube)", "TED Talks (practice + notes)", "Resume & Interview basics resources"],
        "weeks": ["Daily speaking practice + 5–7 lines writing summary.", "Improve vocabulary + clarity + small presentations.", "Mock interview practice + feedback from peers.", "Project: 2-min self intro video + updated resume."],
        "projects": ["2-min self-introduction video", "Resume + LinkedIn update checklist", "Weekly speaking practice log"],
    },
}

JOB_SKILL_ANALYSIS = {
    "Software Developer":     {"skills": ["Python / Java", "Data Structures & Algorithms", "HTML, CSS, JavaScript", "Git & GitHub", "Databases (SQL)", "OOPS", "Problem Solving"], "projects": ["Student Management System", "Task Tracker Application", "Portfolio Website", "REST API Mini Project"], "resources": ["NPTEL – Programming & DSA", "YouTube – freeCodeCamp", "GeeksForGeeks – DSA", "GitHub – Open Source Projects"]},
    "Frontend Developer":     {"skills": ["HTML", "CSS", "JavaScript", "React", "Responsive Design", "Git & GitHub"], "projects": ["Portfolio Website", "React To-Do App", "UI Clone (Netflix / Amazon)"], "resources": ["MDN Web Docs", "Traversy Media (YouTube)", "React Official Docs"]},
    "Backend Developer":      {"skills": ["Node.js / Python / Java", "Databases (SQL/NoSQL)", "APIs / RESTful Services", "Git & GitHub", "Authentication & Security"], "projects": ["REST API Project", "E-commerce Backend", "Blog Platform Backend"], "resources": ["Udemy Backend Courses", "YouTube – Tech With Tim / Traversy Media", "MongoDB University"]},
    "Data Scientist":         {"skills": ["Python", "Statistics", "Pandas & NumPy", "Data Visualization", "Machine Learning Basics"], "projects": ["Student Performance Analysis", "Sales Prediction Model", "EDA Project"], "resources": ["Kaggle Learn", "Krish Naik (YouTube)", "Coursera ML (Audit Mode)"]},
    "Machine Learning Engineer": {"skills": ["Python", "Linear Algebra & Statistics", "Scikit-learn / TensorFlow / PyTorch", "Data Preprocessing", "Model Deployment"], "projects": ["Predictive Analytics Model", "Image Classification Project", "Recommendation System"], "resources": ["Fast.ai Courses", "DeepLearning.ai (Coursera)", "YouTube – Sentdex / Krish Naik"]},
    "DevOps Engineer":        {"skills": ["Linux / Shell Scripting", "CI/CD (Jenkins/GitHub Actions)", "Docker / Kubernetes", "Cloud Platforms (AWS / GCP / Azure)", "Monitoring & Logging"], "projects": ["CI/CD Pipeline Setup", "Dockerized Application Deployment", "Cloud Infrastructure Project"], "resources": ["Linux Academy / A Cloud Guru", "YouTube – TechWorld with Nana", "Official Docker & Kubernetes Docs"]},
    "UI/UX Designer":         {"skills": ["Figma / Adobe XD", "Wireframing & Prototyping", "User Research & Testing", "Responsive Design Principles", "Portfolio Creation"], "projects": ["Mobile App Wireframes", "Website Redesign Project", "Interactive Prototype"], "resources": ["Figma Learn Tutorials", "Coursera UI/UX Courses", "YouTube – DesignCourse / CharliMarieTV"]},
    "Cybersecurity Analyst":  {"skills": ["Networking Basics", "Linux & Windows Security", "Penetration Testing", "Firewalls & IDS/IPS", "Security Tools (Wireshark, Nmap)"], "projects": ["Vulnerability Assessment", "Phishing Simulation", "Secure Web Application Setup"], "resources": ["TryHackMe / Hack The Box", "Cybrary Courses", "YouTube – NetworkChuck / The Cyber Mentor"]},
    "Mobile App Developer":   {"skills": ["Java / Kotlin / Swift / Flutter", "UI/UX for Mobile", "APIs & Backend Integration", "App Deployment (Play Store / App Store)", "Debugging & Testing"], "projects": ["Todo App", "Weather Forecast App", "E-commerce Mobile App"], "resources": ["Udemy Mobile App Courses", "YouTube – CodeWithChris / The Net Ninja", "Official Flutter Docs"]},
    "Cloud Engineer":         {"skills": ["AWS / Azure / GCP", "Cloud Architecture & Design", "Networking & Security", "CI/CD Pipelines", "Infrastructure as Code (Terraform)"], "projects": ["Deploy Web App on Cloud", "Serverless Application Project", "Cloud Monitoring Setup"], "resources": ["AWS / Azure / GCP Official Docs", "A Cloud Guru Courses", "YouTube – TechWorld with Nana"]},
    "Business Analyst":       {"skills": ["Excel / SQL / Tableau / PowerBI", "Requirement Gathering", "Process Modeling", "Data Analysis & Reporting", "Communication & Presentation"], "projects": ["Sales Dashboard", "Customer Analysis Report", "Process Optimization Project"], "resources": ["Coursera Business Analytics", "Udemy SQL / Tableau Courses", "YouTube – Analytics University"]},
    "Digital Marketing Specialist": {"skills": ["SEO / SEM", "Google Analytics", "Content Creation", "Social Media Marketing", "Email Marketing"], "projects": ["SEO Campaign Project", "Social Media Ad Campaign", "Email Marketing Automation"], "resources": ["Google Digital Garage", "HubSpot Academy", "YouTube – Neil Patel / Brian Dean"]},
    "Blockchain Developer":   {"skills": ["Solidity / Ethereum", "Smart Contracts", "Web3.js / Ethers.js", "Blockchain Architecture", "Cryptography Basics"], "projects": ["Smart Contract Deployment", "NFT Minting Platform", "Decentralized App (DApp)"], "resources": ["CryptoZombies.io", "Coursera Blockchain Courses", "YouTube – Dapp University"]},
    "AI Researcher":          {"skills": ["Python / R", "Mathematics (Linear Algebra, Probability)", "Deep Learning", "NLP / Computer Vision", "Research Paper Reading & Implementation"], "projects": ["Image Captioning Model", "Text Summarization Model", "Custom Neural Network Research"], "resources": ["arXiv Papers", "DeepLearning.ai", "YouTube – Yannic Kilcher / Two Minute Papers"]},
}

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def safe_unique(df, col, fallback):
    if col not in df.columns:
        return fallback
    try:
        vals = df[col].dropna().unique().tolist()
        vals = [v for v in vals
                if v is not None
                and str(v).strip() not in ("", "nan", "none", "null", "NaN")]
        return sorted(vals, key=lambda x: str(x)) if vals else fallback
    except Exception:
        return fallback

def normalize_yes_no(x):
    return str(x).strip() if x is not None else "Day Scholar"

def detect_category(interest: str) -> str:
    s = str(interest).lower()
    if any(k in s for k in ["ai/ml", "ml", "ai", "data science", "data analysis"]): return "ML"
    if "web" in s or "app" in s: return "WEB"
    if "competitive coding" in s: return "DSA"
    if "cyber" in s: return "CYBER"
    if "vlsi" in s: return "VLSI"
    if "iot" in s: return "IOT"
    if "embedded" in s: return "EMBEDDED"
    if "signal processing" in s: return "SIGNAL"
    if "communication systems" in s: return "COMM_SYSTEMS"
    if "power systems" in s: return "POWER"
    if "renewable energy" in s: return "RENEW"
    if "smart grid" in s: return "SMARTGRID"
    if "industrial automation" in s: return "AUTOMATION"
    if "electrical design" in s: return "ELECTRICAL_DESIGN"
    if "robotics" in s: return "ROBOTICS"
    if "cad design" in s: return "CAD"
    if "automobile" in s: return "AUTO"
    if "thermal" in s: return "THERMAL"
    if "manufacturing" in s: return "MANUFACTURING"
    if "communication skills" in s: return "SOFT"
    return "DSA"

def clamp(x, lo, hi): return max(lo, min(hi, x))

def level_to_bucket(skill_level: str):
    s = str(skill_level).lower()
    if "begin" in s: return "Beginner"
    if "inter" in s: return "Intermediate"
    return "Advanced"

def get_similar_students(df, info):
    f = df.copy()
    strict = f[
        (f["branch"] == info["branch"]) &
        (f["interest"] == info["interest"])
    ]
    if len(strict) >= 5:
        return strict
    relaxed = f[f["branch"] == info["branch"]]
    if len(relaxed) >= 5:
        return relaxed
    return f

def build_week_plan(interest, skill_level, budget_level):
    cat  = detect_category(interest)
    data = COURSE_DB.get(cat, COURSE_DB["DSA"])
    free_note = "Use free resources (YouTube/NPTEL/free audits)." if str(budget_level) == "Low" else "Consider 1 paid course for faster progress."
    lvl = str(skill_level).lower()
    practice = "45–60 mins daily practice." if "begin" in lvl else "60–90 mins daily practice."
    week_plan = []
    for i in range(4):
        week_plan.append({
            "title": f"Week {i+1} — " + ["Foundation", "Core Skills", "Build Projects", "Portfolio & Review"][i],
            "bullets": [
                f"Course focus: {data['courses'][min(i, len(data['courses'])-1)]}",
                data["weeks"][i],
                practice,
                free_note,
            ],
        })
    return week_plan, data["courses"], data["projects"]

# ─────────────────────────────────────────────
# ✅ FIXED FUNCTION — only change from original
# ─────────────────────────────────────────────
def generate_structured_roadmap(info, df):
    steps = []; risks = []; habits = []; goals = []
    sim = get_similar_students(df, info)
    if len(sim) >= 5:
        avg_gpa   = sim["gpa"].mean()        if "gpa"         in sim.columns else None
        avg_study = sim["study_hours"].mean() if "study_hours" in sim.columns else None
        if avg_gpa is not None and avg_study is not None:
            sim_note = f"Based on {len(sim)} similar students, avg GPA {avg_gpa:.2f}, avg study hours {avg_study:.1f}/day."
        else:
            sim_note = f"Showing general roadmap ({len(sim)} similar students found)."
    else:
        sim_note = "Showing a general roadmap based on available data."

    # ── Safely resolve all fields (fixes budget key mismatch + any None values) ──
    budget        = str(info.get("budget") or info.get("budget_level") or "Low").strip()
    gpa           = float(info.get("gpa") or 10)
    study_hours   = int(info.get("study_hours") or 3)
    communication = str(info.get("communication") or info.get("communication_level") or "Average").strip()
    stress_level  = str(info.get("stress_level") or "Medium").strip()
    confusion     = str(info.get("confusion_level") or "Medium").strip()
    hostel        = str(info.get("hostel") or "No").strip()
    family_support = str(info.get("family_support") or "Medium").strip()
    interest      = str(info.get("interest") or "").strip()
    skill_level   = str(info.get("skill_level") or "Beginner").strip()

    # Goals — always at least 1
    goals.append(f"Build a clear learning path in {interest}.")
    if gpa < 6.0:
        goals.append("Improve academic consistency (target +0.5 GPA next semester).")
    if study_hours < 3:
        goals.append("Increase study hours gradually to a sustainable level.")
    if communication in ("Poor", "Low"):
        goals.append("Improve communication through weekly speaking/writing practice.")

    # Risks
    if stress_level == "High" or confusion == "High":
        risks.append("High stress/confusion detected — use weekly planning + short focused sessions.")
        habits.append("10 min breathing/meditation + 25/5 Pomodoro (2 cycles).")

    # Habits — always at least 1
    habits.append(
        "Hostel routine: fixed sleep + fixed study slot + limit late-night scrolling."
        if hostel == "Yes"
        else "Home routine: fixed study slot + communicate study time to family."
    )
    habits.append("Review your week every Sunday — 15 min planning saves hours of confusion.")

    # Steps — always at least 2
    steps.append(
        "Get external support: mentor/teacher/peer group + online communities."
        if family_support == "Low"
        else "Use family support: share weekly goals and ask for accountability."
    )
    steps.append(
        "Use free resources first + build projects (proof > certificates)."
        if budget == "Low"
        else "Pick 1 high-quality paid course OR mentorship for faster progress."
    )
    if study_hours < 3:
        steps.append("Study plan: add +30 mins/week until you reach 3–4 hours/day.")
    if gpa < 6.0:
        steps.append("Academics: revise daily + weekly tests + focus on weak subjects.")
    if communication in ("Poor", "Low"):
        steps.append("Communication: 2 short talks/week + write 1 summary/day (5–7 lines).")

    week_plan, course_resources, course_projects = build_week_plan(
        interest, skill_level, budget
    )

    return {
        "similar_note": sim_note,
        "goals":    [x for x in goals  if x],
        "risks":    [x for x in risks  if x],
        "habits":   [x for x in habits if x],
        "steps":    [x for x in steps  if x],
        "week_plan":  week_plan,
        "resources":  course_resources,
        "projects":   course_projects,
    }

def readiness_breakdown(info):
    g = float(info.get("gpa", 0))
    academics = 30 if g>=8 else 26 if g>=7 else 20 if g>=6 else 14 if g>=5 else 8
    lvl  = level_to_bucket(info.get("skill_level","Beginner"))
    sh   = int(info.get("study_hours",0))
    base = 12 if lvl=="Beginner" else 20 if lvl=="Intermediate" else 26
    bonus= 6 if sh>=4 else 3 if sh>=3 else 1
    skills = clamp(base+bonus, 0, 30)
    sleep    = int(info.get("sleep_hours",6))
    stress   = info.get("stress_level","Medium")
    confusion= info.get("confusion_level","Medium")
    routine  = (8 if sleep>=7 else 5 if sleep>=6 else 2) + (6 if stress=="Low" else 4 if stress=="Medium" else 2) + (6 if confusion=="Low" else 4 if confusion=="Medium" else 2)
    routine  = clamp(routine, 0, 20)
    comm  = str(info.get("communication","Average"))
    communication = 20 if comm in ("Good","High") else 14 if comm in ("Average","Medium") else 8
    return {"Academics": academics, "Skills": skills, "Routine": routine, "Communication": communication, "Total": clamp(academics+skills+routine+communication, 0, 100)}

def roadmap_to_markdown(name, info, roadmap):
    def s(x):
        try:
            if pd.isna(x): return ""
        except Exception: pass
        return str(x)
    
    lines = [
        f"# Personalised Roadmap for {s(name) or 'Student'}", 
        f"**Generated:** {date.today().isoformat()}", 
        "", 
        "## Profile"
    ]
    
    for k in ["year","branch","interest","skill_level","budget","hostel","study_hours","gpa","stress_level","confusion_level","communication","family_support"]:
        lines.append(f"- **{k.replace('_',' ').title()}**: {s(info.get(k))}")
    
    lines += ["", "## Data Insight", s(roadmap.get("similar_note","")), "", "## Goals"]
    
    # Corrected: Use standard for loops instead of list comprehensions
    for g in roadmap.get("goals", []):
        lines.append(f"- {s(g)}")
    
    if roadmap.get("risks"):
        lines += ["", "## Risks"]
        for r in roadmap["risks"]:
            lines.append(f"- {s(r)}")
            
    lines += ["", "## Daily Habits"]
    for h in roadmap.get("habits", []):
        lines.append(f"- {s(h)}")
        
    lines += ["", "## Action Steps"]
    for step in roadmap.get("steps", []):
        lines.append(f"- {s(step)}")
        
    lines += ["", "## 4-Week Plan"]
    for w in roadmap.get("week_plan", []):
        lines += [f"### {s(w['title'])}"]
        for b in w.get("bullets", []):
            lines.append(f"- {s(b)}")
        lines += [""]
        
    lines += ["## Suggested Projects"]
    for p in roadmap.get("projects", []):
        lines.append(f"- {s(p)}")
        
    lines += ["", "## Resources"]
    for r in roadmap.get("resources", []):
        lines.append(f"- {s(r)}")
        
    return "\n".join(lines)

def compute_skill_gap(required, known):
    have    = [s for s in required if s in known]
    missing = [s for s in required if s not in known]
    return have, missing


# ─────────────────────────────────────────────
# ROUTING
# ─────────────────────────────────────────────
if st.session_state.page == "home":
    show_landing_page()
    st.stop()

# ═══════════════════════════════════════════════
#  APP PAGE
# ═══════════════════════════════════════════════
@st.cache_data
def load_data():
    df = pd.read_csv("student_performance_final.csv")
    df.columns = df.columns.str.lower()
    if "hostel" in df.columns:
        df["hostel"] = df["hostel"].astype(str).str.strip().str.lower()
        df["hostel"] = df["hostel"].replace({
            "day scholar": "No",
            "dayscholar":  "No",
            "hosteler":    "Yes",
            "hosteller":   "Yes"
        })
    df = df.dropna(subset=["year", "branch", "interest", "skill_level",
                            "budget_level", "stress_level",
                            "confusion_level", "communication_level"])
    df = df.reset_index(drop=True)
    return df

data = load_data()

st.markdown("""
<div class="app-header">
  <div style="display:flex;align-items:center;justify-content:space-between;">
    <div class="app-logo">🎯 SkillRoadmap</div>
    <span style="font-size:12px;color:#475569;">AI-Powered · Free</span>
  </div>
</div>
""", unsafe_allow_html=True)

col_back, _ = st.columns([1, 8])
with col_back:
    if st.button("← Back"):
        st.session_state.page = "home"
        st.session_state.roadmap_data = None
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

years        = [1, 2, 3, 4]
branches     = ["CSE", "ECE", "EEE", "IT", "Mechanical"]
interests    = sorted(data["interest"].dropna().unique().tolist())
budgets      = ["High", "Low", "Medium"]
skill_levels = ["Beginner", "Intermediate"]
stress_lvls  = ["High", "Low", "Medium"]
conf_lvls    = ["High", "Low", "Medium"]
comm_lvls    = ["Average", "Good", "Poor"]
hostel_display = ["Yes", "No"]

st.markdown('<div class="g-card"><div class="g-card-title">📋 Your Profile</div><div class="g-card-sub">Fill your details to generate a personalised roadmap + readiness score + skill gap analysis.</div></div>', unsafe_allow_html=True)

with st.form("profile_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        name         = st.text_input("👤 Student Name", "")
        year         = st.selectbox("📅 Year", years)
        branch       = st.selectbox("🏛️ Branch", branches)
        gpa          = st.slider("🎓 GPA", 0.0, 10.0, 7.0, 0.1)
        study_hours  = st.slider("📖 Daily Study Hours", 0, 12, 3)
    with col2:
        failures     = st.number_input("❌ Number of Failures", min_value=0, max_value=10, value=0)
        hostel       = st.selectbox("🏠 Hostel?", hostel_display)
        sleep_hours  = st.slider("😴 Daily Sleep Hours", 0, 12, 7)
        family_support = st.selectbox("👨‍👩‍👦 Family Support", ["Low","Medium","High"])
        interest     = st.selectbox("💡 Primary Interest", interests)
    with col3:
        budget       = st.selectbox("💰 Budget Level", budgets)
        skill_level  = st.selectbox("🛠️ Skill Level", skill_levels)
        stress_level = st.selectbox("😰 Stress Level", stress_lvls)
        confusion_level = st.selectbox("🤔 Confusion Level", conf_lvls)
        communication   = st.selectbox("🗣️ Communication Level", comm_lvls)

    submitted = st.form_submit_button("🔍  Generate My Roadmap", use_container_width=True)

if submitted:
    st.session_state.student_name = name
    st.session_state.student_info = {
        "year": year, "branch": branch, "gpa": float(gpa),
        "study_hours": int(study_hours), "failures": int(failures),
        "hostel": hostel, "sleep_hours": int(sleep_hours),
        "family_support": family_support, "interest": interest,
        "budget": budget, "skill_level": skill_level,
        "stress_level": stress_level, "confusion_level": confusion_level,
        "communication": communication,
    }
    st.session_state.roadmap_data = generate_structured_roadmap(st.session_state.student_info, data)

if st.session_state.roadmap_data is not None:
    roadmap = st.session_state.roadmap_data
    info    = st.session_state.student_info
    sname   = st.session_state.student_name

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<div style="text-align:center;font-family:Syne,sans-serif;font-size:22px;font-weight:800;background:linear-gradient(135deg,#a5b4fc,#34d399);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:24px;">✅ Roadmap Generated for {sname or "Student"}</div>', unsafe_allow_html=True)

    score = readiness_breakdown(info)
    c1,c2,c3,c4,c5 = st.columns(5)
    tiles = [
        ("GPA", f"{info['gpa']:.1f}"),
        ("Study hrs/day", str(info["study_hours"])),
        ("Sleep hrs", str(info["sleep_hours"])),
        ("Readiness", f"{score['Total']}/100"),
        ("Skill Level", info["skill_level"]),
    ]
    for col, (label, val) in zip([c1,c2,c3,c4,c5], tiles):
        col.markdown(f'<div class="metric-tile"><div class="metric-val">{val}</div><div class="metric-label">{label}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("📊  Readiness Score Breakdown", expanded=True):
        col_score, col_bars = st.columns([1, 2])
        with col_score:
            st.markdown(f'<div class="score-ring-wrap"><div class="score-big">{score["Total"]}</div><div class="score-label">out of 100</div></div>', unsafe_allow_html=True)
        with col_bars:
            bar_config = [
                ("Academics",     score["Academics"],     30,  "linear-gradient(90deg,#6366f1,#818cf8)"),
                ("Skills",        score["Skills"],        30,  "linear-gradient(90deg,#8b5cf6,#a78bfa)"),
                ("Routine",       score["Routine"],       20,  "linear-gradient(90deg,#0ea5e9,#38bdf8)"),
                ("Communication", score["Communication"], 20,  "linear-gradient(90deg,#34d399,#6ee7b7)"),
            ]
            for label, val, mx, grad in bar_config:
                pct = int(val/mx*100)
                st.markdown(f"""
                <div class="score-bar-wrap">
                  <div class="score-bar-label">
                    <span style="color:#e2e8f0">{label}</span>
                    <span style="color:#6366f1">{val}/{mx}</span>
                  </div>
                  <div class="score-bar-track">
                    <div class="score-bar-fill" style="width:{pct}%;background:{grad}"></div>
                  </div>
                </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🧭 Roadmap", "🗓️ 4-Week Plan", "🚀 Projects", "📚 Resources", "🧩 Skill Gap"])

    with tab1:
        st.markdown(f'<div style="background:rgba(99,102,241,0.10);border:1px solid rgba(99,102,241,0.28);border-radius:14px;padding:16px 20px;font-size:14px;color:#a5b4fc;margin-bottom:20px;">💡 {roadmap["similar_note"]}</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-pill">🎯 Goals</div>', unsafe_allow_html=True)
        for g in roadmap["goals"]:
            st.markdown(f'<div class="goal-item"><div class="goal-dot"></div><div class="goal-text">{g}</div></div>', unsafe_allow_html=True)
        if roadmap["risks"]:
            st.markdown('<br><div class="sec-pill">⚠️ Risks to Watch</div>', unsafe_allow_html=True)
            for r in roadmap["risks"]:
                st.markdown(f'<div class="risk-item"><div class="risk-dot"></div><div class="goal-text">{r}</div></div>', unsafe_allow_html=True)
        st.markdown('<br><div class="sec-pill">🧠 Daily Habits</div>', unsafe_allow_html=True)
        for h in roadmap["habits"]:
            st.markdown(f'<div class="habit-item"><div class="habit-dot"></div><div class="goal-text">{h}</div></div>', unsafe_allow_html=True)
        st.markdown('<br><div class="sec-pill">✅ Action Steps</div>', unsafe_allow_html=True)
        for i, step in enumerate(roadmap["steps"], 1):
            st.markdown(f'<div class="step-item"><div class="step-num">{i}</div><div class="goal-text">{step}</div></div>', unsafe_allow_html=True)

    with tab2:
        for w in roadmap["week_plan"]:
            bullets_html = "".join(f'<div class="week-bullet">{b}</div>' for b in w["bullets"])
            st.markdown(f'<div class="week-card"><div class="week-title">{w["title"]}</div>{bullets_html}</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="sec-pill">🚀 Suggested Projects</div>', unsafe_allow_html=True)
        icons = ["🔵","🟣","🟡","🟢","🔴"]
        for i, p in enumerate(roadmap["projects"]):
            st.markdown(f'<div class="proj-card"><div class="proj-icon">{icons[i%len(icons)]}</div><div class="proj-name">{p}</div></div>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:12px;color:#475569;margin-top:12px;">Tip: Add screenshots + README + clear results. That makes your project look strong.</p>', unsafe_allow_html=True)

    with tab4:
        st.markdown('<div class="sec-pill">📚 Recommended Resources</div>', unsafe_allow_html=True)
        res_icons = ["🎥","📖","🌐"]
        for i, r in enumerate(roadmap["resources"]):
            st.markdown(f'<div class="res-card"><div class="res-icon">{res_icons[i%len(res_icons)]}</div><div class="res-name">{r}</div></div>', unsafe_allow_html=True)

    with tab5:
        st.markdown('<div class="sec-pill">🧩 Skill Gap Analysis</div>', unsafe_allow_html=True)
        st.markdown("""<p style='font-size:14px;color:#64748b;margin-bottom:20px;'>Select a job role, then tick the skills you already know — we will show your match % and what to learn next.</p>""", unsafe_allow_html=True)
        job_roles = ["— Select a role —"] + list(JOB_SKILL_ANALYSIS.keys())
        job_choice = st.selectbox("🎯 Target Job Role", job_roles, key="sg_role_tab")
        if job_choice != "— Select a role —":
            job_info = JOB_SKILL_ANALYSIS[job_choice]
            col_left, col_right = st.columns([1, 1])
            with col_left:
                st.markdown('<div class="sec-pill">🧠 Required Skills</div>', unsafe_allow_html=True)
                for sk in job_info["skills"]:
                    st.markdown(f'<div style="background:rgba(99,102,241,0.08);border:1px solid rgba(99,102,241,0.22);border-radius:10px;padding:8px 14px;margin-bottom:6px;font-size:13px;color:#c7d2fe;">• {sk}</div>', unsafe_allow_html=True)
            with col_right:
                st.markdown('<div class="sec-pill">🧪 Sample Projects</div>', unsafe_allow_html=True)
                for p in job_info["projects"]:
                    st.markdown(f'<div class="proj-card" style="margin-bottom:6px;"><div class="proj-name" style="color:#fcd34d;">{p}</div></div>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="sec-pill">✅ Mark Skills You Already Know</div>', unsafe_allow_html=True)
            known_skills = st.multiselect("Select skills you already have:", options=job_info["skills"], key="sg_known_tab")
            have, missing = compute_skill_gap(job_info["skills"], known_skills)
            pct = int(len(have) / len(job_info["skills"]) * 100) if job_info["skills"] else 0
            st.markdown("<br>", unsafe_allow_html=True)
            bar_color = "#34d399" if pct >= 70 else "#fbbf24" if pct >= 40 else "#fb7185"
            st.markdown(f"""
            <div style="margin-bottom:8px;">
              <div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:6px;">
                <span style="color:#e2e8f0;font-weight:700;">📊 Skill Match</span>
                <span style="color:{bar_color};font-weight:800;">{pct}%</span>
              </div>
              <div style="height:12px;border-radius:999px;background:rgba(255,255,255,0.08);overflow:hidden;">
                <div style="height:100%;width:{pct}%;background:{bar_color};border-radius:999px;transition:width 0.5s ease;"></div>
              </div>
              <div style="font-size:12px;color:#475569;margin-top:6px;">
                {"🟢 Strong match — ready to apply!" if pct>=70 else "🟡 Getting there — keep building!" if pct>=40 else "🔴 Start learning — you've got this!"}
              </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            col_h, col_m = st.columns(2)
            with col_h:
                st.markdown('<div class="sec-pill" style="background:rgba(52,211,153,0.12);border-color:rgba(52,211,153,0.35);color:#6ee7b7;">✅ Skills You Have</div>', unsafe_allow_html=True)
                if have:
                    for sk in have:
                        st.markdown(f'<div class="skill-have">✅ {sk}</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<p style="font-size:13px;color:#475569;">Select skills you know above.</p>', unsafe_allow_html=True)
            with col_m:
                st.markdown('<div class="sec-pill" style="background:rgba(251,113,133,0.12);border-color:rgba(251,113,133,0.35);color:#fda4af;">🔴 Skills to Learn</div>', unsafe_allow_html=True)
                if missing:
                    for sk in missing:
                        st.markdown(f'<div class="skill-need">🔴 {sk}</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div style="background:rgba(52,211,153,0.10);border:1px solid rgba(52,211,153,0.30);border-radius:12px;padding:14px;font-size:14px;color:#6ee7b7;font-weight:700;">🎉 You have all required skills!</div>', unsafe_allow_html=True)
            if missing:
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown('<div class="sec-pill">🛣️ Recommended Learning Order</div>', unsafe_allow_html=True)
                for i, sk in enumerate(missing, 1):
                    st.markdown(f'<div class="learn-step"><div class="learn-step-num">{i}</div><div class="learn-step-text">Learn <strong style="color:#e2e8f0">{sk}</strong></div></div>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="sec-pill">📚 Resources for this Role</div>', unsafe_allow_html=True)
            for r in job_info["resources"]:
                st.markdown(f'<div class="res-card"><div class="res-icon">📌</div><div class="res-name">{r}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    md = roadmap_to_markdown(sname, info, roadmap)
    st.download_button(
        label="⬇️  Download Full Roadmap (Markdown)",
        data=md.encode("utf-8"),
        file_name=f"roadmap_{(sname or 'student').replace(' ','_').lower()}.md",
        mime="text/markdown",
        use_container_width=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
with st.expander("📊  Sample Student Dataset (Preview)"):
    st.dataframe(data, use_container_width=True)

st.markdown('<p style="text-align:center;font-size:11px;color:#1e293b;margin-top:32px;">Student Skill Roadmap · Streamlit</p>', unsafe_allow_html=True)
