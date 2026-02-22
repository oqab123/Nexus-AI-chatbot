"""
NEXUS AI — Ultimate Personal AI Assistant
Dark Theme — Maximum Contrast + Full Animations
"""

import streamlit as st
import time, json, sqlite3, hashlib, io
from datetime import datetime

st.set_page_config(
    page_title="NEXUS AI",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&family=JetBrains+Mono:wght@300;400;500;600&family=Inter:wght@300;400;500;600;700&display=swap');

:root {
  --bg:        #08080f;
  --bg-2:      #0d0d18;
  --bg-3:      #121220;
  --card:      rgba(255,255,255,0.05);
  --card-h:    rgba(255,255,255,0.09);

  --t1:  #f0eeff;
  --t2:  #c4bed8;
  --t3:  #7c7590;
  --t4:  #3d3850;

  --ac:    #ff6b35;
  --ac2:   #ff8555;
  --ac-s:  rgba(255,107,53,0.14);
  --ac-b:  rgba(255,107,53,0.07);
  --ac-bd: rgba(255,107,53,0.4);
  --ac-gl: rgba(255,107,53,0.25);

  --cyan:  #00d4e8;
  --cyan-s:rgba(0,212,232,0.12);
  --grn:   #00e87a;
  --grn-s: rgba(0,232,122,0.12);
  --gold:  #ffcc44;
  --vio:   #bd93f9;

  --b1: rgba(255,255,255,0.07);
  --b2: rgba(255,255,255,0.13);
  --b3: rgba(255,255,255,0.22);

  --r:    8px;
  --r-lg: 14px;
  --r-xl: 20px;
  --r-f:  9999px;

  --sh:    0 8px 32px rgba(0,0,0,0.55);
  --sh-lg: 0 20px 60px rgba(0,0,0,0.65);
  --gl-ac: 0 0 40px rgba(255,107,53,0.2);

  --mono:  'JetBrains Mono', monospace;
  --serif: 'Playfair Display', Georgia, serif;
  --sans:  'Inter', sans-serif;
}

/* ── Base ── */
*, *::before, *::after { box-sizing: border-box; }

html, body { background: var(--bg) !important; }

.stApp {
  background: var(--bg) !important;
  font-family: var(--sans) !important;
}

/* Force ALL text to be bright white — override everything */
.stApp,
.stApp p, .stApp span, .stApp div, .stApp label,
.stApp h1, .stApp h2, .stApp h3, .stApp h4,
.stApp li, .stApp a, .stApp small {
  color: var(--t1) !important;
}

/* ── Animated BG ── */
.stApp::before {
  content: '';
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
  background:
    radial-gradient(ellipse 75% 55% at 12% 8%,  rgba(255,107,53,0.09) 0%, transparent 58%),
    radial-gradient(ellipse 60% 45% at 88% 92%, rgba(0,212,232,0.07)  0%, transparent 58%),
    radial-gradient(ellipse 45% 38% at 50% 50%, rgba(189,147,249,0.05) 0%, transparent 65%);
  animation: bg-breathe 20s ease-in-out infinite alternate;
}
@keyframes bg-breathe {
  0%   { opacity: 0.5; transform: scale(1)    translateY(0px); }
  100% { opacity: 1;   transform: scale(1.09) translateY(-12px); }
}
.stApp::after {
  content: '';
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
  background-image: radial-gradient(rgba(255,255,255,0.022) 1px, transparent 1px);
  background-size: 30px 30px;
  animation: grid-scroll 28s linear infinite;
}
@keyframes grid-scroll {
  from { transform: translateY(0); }
  to   { transform: translateY(30px); }
}

/* ── Streamlit chrome ── */
#MainMenu, footer, .stDeployButton { visibility: hidden !important; }
header[data-testid="stHeader"] { background: transparent !important; border: none !important; }
[data-testid="stSidebarCollapsedControl"] { visibility: visible !important; }

/* ════ SIDEBAR ════ */
[data-testid="stSidebar"] {
  background: rgba(6,6,12,0.98) !important;
  border-right: 1px solid var(--b2) !important;
  backdrop-filter: blur(24px) !important;
}
[data-testid="stSidebar"] > div:first-child { padding-top: 0 !important; }

[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] small,
[data-testid="stSidebar"] span {
  color: var(--t2) !important;
  font-family: var(--mono) !important;
}
[data-testid="stSidebar"] input,
[data-testid="stSidebar"] textarea {
  background: rgba(255,255,255,0.05) !important;
  border: 1px solid var(--b2) !important;
  border-radius: var(--r) !important;
  color: var(--t1) !important;
  font-family: var(--mono) !important;
  font-size: 0.8rem !important;
  transition: all 0.25s ease !important;
}
[data-testid="stSidebar"] input:focus,
[data-testid="stSidebar"] textarea:focus {
  border-color: var(--ac) !important;
  box-shadow: 0 0 0 3px var(--ac-s), var(--gl-ac) !important;
  outline: none !important;
}
[data-testid="stSidebar"] input::placeholder { color: var(--t4) !important; }

/* Selectbox */
[data-testid="stSelectbox"] > div > div {
  background: rgba(255,255,255,0.05) !important;
  border: 1px solid var(--b2) !important;
  border-radius: var(--r) !important;
  font-family: var(--mono) !important;
  font-size: 0.78rem !important;
  color: var(--t1) !important;
  transition: all 0.2s !important;
}
[data-testid="stSelectbox"] > div > div:hover {
  border-color: var(--ac-bd) !important;
  box-shadow: var(--gl-ac) !important;
}
[data-testid="stSelectbox"] > div > div span { color: var(--t1) !important; }
[data-testid="stSelectbox"] li {
  background: var(--bg-2) !important;
  color: var(--t2) !important;
  font-family: var(--mono) !important;
  font-size: 0.78rem !important;
}
[data-testid="stSelectbox"] li:hover {
  background: var(--ac-s) !important;
  color: var(--ac) !important;
}

/* Radio */
[data-testid="stRadio"] label {
  font-family: var(--sans) !important;
  font-size: 0.85rem !important;
  color: var(--t2) !important;
  padding: 9px 14px !important;
  border-radius: var(--r) !important;
  border: 1px solid transparent !important;
  transition: all 0.2s ease !important;
  cursor: pointer !important;
}
[data-testid="stRadio"] label:hover {
  color: var(--t1) !important;
  background: var(--card-h) !important;
  border-color: var(--b2) !important;
}

/* Sliders */
[data-testid="stSlider"] [role="slider"] {
  background: var(--ac) !important;
  border: 2px solid var(--bg) !important;
  box-shadow: 0 0 0 2px var(--ac), 0 0 16px var(--ac-gl) !important;
  transition: all 0.25s !important;
}
[data-testid="stSlider"] [role="slider"]:hover {
  box-shadow: 0 0 0 2px var(--ac), 0 0 32px var(--ac-gl) !important;
  transform: scale(1.2) !important;
}
[data-testid="stSlider"] label { color: var(--t3) !important; font-size: 0.7rem !important; }

/* ═══ BUTTONS ═══ */
.stButton > button {
  background: var(--card) !important;
  border: 1px solid var(--b2) !important;
  color: var(--t2) !important;
  border-radius: var(--r) !important;
  font-family: var(--mono) !important;
  font-size: 0.7rem !important;
  font-weight: 500 !important;
  letter-spacing: 1.5px !important;
  text-transform: uppercase !important;
  padding: 10px 20px !important;
  transition: all 0.22s cubic-bezier(0.16,1,0.3,1) !important;
}
.stButton > button:hover {
  background: var(--card-h) !important;
  border-color: var(--ac-bd) !important;
  color: var(--ac) !important;
  transform: translateY(-2px) !important;
  box-shadow: var(--sh), var(--gl-ac) !important;
}
.stButton > button[kind="primary"] {
  background: linear-gradient(135deg, var(--ac) 0%, var(--ac2) 100%) !important;
  border-color: transparent !important;
  color: #fff !important;
  font-weight: 700 !important;
  box-shadow: 0 4px 20px var(--ac-gl) !important;
}
.stButton > button[kind="primary"]:hover {
  transform: translateY(-3px) !important;
  box-shadow: 0 10px 36px var(--ac-gl) !important;
  filter: brightness(1.12) !important;
}

/* ═══ CHAT MESSAGES ═══ */
[data-testid="stChatMessage"] {
  background: rgba(255,255,255,0.04) !important;
  border: 1px solid var(--b1) !important;
  border-radius: var(--r-lg) !important;
  margin: 10px 0 !important;
  padding: 6px !important;
  animation: msg-slide 0.4s cubic-bezier(0.16,1,0.3,1) both;
  transition: border-color 0.25s, box-shadow 0.25s !important;
}
[data-testid="stChatMessage"]:hover {
  border-color: var(--b2) !important;
  box-shadow: var(--sh) !important;
}
@keyframes msg-slide {
  from { opacity: 0; transform: translateY(14px) scale(0.98); }
  to   { opacity: 1; transform: translateY(0)    scale(1); }
}
[data-testid="stChatMessage"] p {
  color: var(--t1) !important;
  font-family: var(--sans) !important;
  font-size: 0.93rem !important;
  line-height: 1.85 !important;
}

/* ═══ CHAT INPUT ═══ */
[data-testid="stChatInput"] {
  background: rgba(255,255,255,0.05) !important;
  border: 1.5px solid var(--b2) !important;
  border-radius: var(--r-xl) !important;
  transition: border-color 0.25s, box-shadow 0.25s !important;
}
[data-testid="stChatInput"]:focus-within {
  border-color: var(--ac) !important;
  box-shadow: 0 0 0 3px var(--ac-s), var(--gl-ac) !important;
}
[data-testid="stChatInput"] textarea {
  background: transparent !important;
  border: none !important;
  color: var(--t1) !important;
  font-family: var(--sans) !important;
  font-size: 0.92rem !important;
  caret-color: var(--ac) !important;
}
[data-testid="stChatInput"] textarea::placeholder { color: var(--t4) !important; font-style: italic !important; }

/* ═══ TABS ═══ */
[data-testid="stTabs"] { border-bottom: 1px solid var(--b2) !important; }
[data-testid="stTabs"] [role="tab"] {
  font-family: var(--mono) !important; font-size: 0.62rem !important;
  letter-spacing: 2.5px !important; text-transform: uppercase !important;
  color: var(--t3) !important; padding: 12px 26px !important;
  transition: color 0.2s !important; border-radius: 0 !important;
}
[data-testid="stTabs"] [role="tab"]:hover { color: var(--t1) !important; }
[data-testid="stTabs"] [role="tab"][aria-selected="true"] {
  color: var(--ac) !important;
  border-bottom: 2px solid var(--ac) !important;
  background: transparent !important;
  text-shadow: 0 0 20px var(--ac-gl) !important;
}

/* ═══ METRICS ═══ */
[data-testid="stMetric"] {
  background: var(--card) !important; border: 1px solid var(--b1) !important;
  border-radius: var(--r) !important; padding: 16px !important;
  transition: all 0.25s !important;
}
[data-testid="stMetric"]:hover {
  border-color: var(--ac-bd) !important;
  transform: translateY(-2px) !important;
  box-shadow: var(--sh), var(--gl-ac) !important;
}
[data-testid="stMetricValue"] {
  font-family: var(--serif) !important; font-size: 1.6rem !important;
  font-weight: 700 !important; color: var(--ac) !important;
}
[data-testid="stMetricLabel"] {
  font-family: var(--mono) !important; font-size: 0.55rem !important;
  letter-spacing: 2px !important; text-transform: uppercase !important;
  color: var(--t3) !important;
}

/* ═══ FILE UPLOADER ═══ */
[data-testid="stFileUploader"] {
  background: var(--card) !important; border: 1.5px dashed var(--b2) !important;
  border-radius: var(--r-lg) !important; transition: all 0.25s !important;
}
[data-testid="stFileUploader"]:hover {
  border-color: var(--ac-bd) !important;
  background: var(--ac-b) !important;
  box-shadow: var(--gl-ac) !important;
}
[data-testid="stFileUploader"] p,
[data-testid="stFileUploader"] small { color: var(--t3) !important; }

/* ═══ ALERTS ═══ */
[data-testid="stAlert"] {
  background: var(--card) !important; border: 1px solid var(--b1) !important;
  border-left: 3px solid var(--ac) !important; border-radius: var(--r) !important;
  animation: fade-up 0.35s ease both;
}
[data-testid="stAlert"] p { color: var(--t1) !important; font-size: 0.88rem !important; }

/* ═══ MISC ═══ */
hr { border: none !important; border-top: 1px solid var(--b1) !important; margin: 16px 0 !important; }
.stSpinner > div { border-top-color: var(--ac) !important; }
::-webkit-scrollbar { width: 3px; }
::-webkit-scrollbar-thumb { background: var(--b2); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--ac-bd); }
[data-testid="stExpander"] {
  background: var(--card) !important; border: 1px solid var(--b1) !important;
  border-radius: var(--r) !important; transition: border-color 0.2s !important;
}
[data-testid="stExpander"]:hover { border-color: var(--b2) !important; }
[data-testid="stExpander"] summary { color: var(--t2) !important; font-family: var(--mono) !important; font-size: 0.75rem !important; }
.stMarkdown code {
  background: var(--ac-s) !important; border: 1px solid var(--ac-bd) !important;
  border-radius: 4px !important; color: var(--ac2) !important;
  font-family: var(--mono) !important; font-size: 0.82rem !important; padding: 2px 7px !important;
}
[data-testid="column"] > div { padding: 0 5px !important; }

/* ═══ KEYFRAMES ═══ */
@keyframes fade-up {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes fade-in { from { opacity: 0; } to { opacity: 1; } }
@keyframes float {
  0%,100% { transform: translateY(0) rotate(0deg); }
  40%      { transform: translateY(-14px) rotate(2deg); }
  70%      { transform: translateY(-7px)  rotate(-1deg); }
}
@keyframes blink { 0%,100% { opacity: 1; } 50% { opacity: 0.15; } }
@keyframes shimmer-slide {
  0%   { left: -100%; }
  100% { left: 100%; }
}
@keyframes glow-pulse {
  0%,100% { box-shadow: 0 0 16px var(--ac-gl), 0 0 32px rgba(255,107,53,0.1); }
  50%      { box-shadow: 0 0 32px var(--ac-gl), 0 0 64px rgba(255,107,53,0.15); }
}
@keyframes border-rotate {
  0%   { border-color: var(--ac-bd); }
  33%  { border-color: rgba(0,212,232,0.45); }
  66%  { border-color: rgba(189,147,249,0.45); }
  100% { border-color: var(--ac-bd); }
}
@keyframes rule-grow { from { width: 0; opacity: 0; } to { width: 24px; opacity: 1; } }

/* ══════════════════════════════════════════════
   CUSTOM COMPONENTS
══════════════════════════════════════════════ */

/* Sidebar brand */
.sb-head {
  padding: 26px 20px 20px;
  border-bottom: 1px solid var(--b1);
  position: relative; overflow: hidden;
}
.sb-shimmer {
  position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, var(--ac), rgba(0,212,232,0.8), transparent);
  animation: shimmer-slide 3.5s ease-in-out infinite;
}
.sb-icon {
  width: 36px; height: 36px;
  background: linear-gradient(135deg, var(--ac-s), rgba(0,212,232,0.1));
  border: 1px solid var(--ac-bd); border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-size: 16px; margin-bottom: 12px;
  animation: glow-pulse 3s ease-in-out infinite;
}
.sb-title {
  font-family: var(--serif); font-size: 1.4rem; font-weight: 700;
  color: var(--t1) !important; letter-spacing: -0.5px; line-height: 1;
}
.sb-title em { font-style: italic; color: var(--ac) !important; }
.sb-sub {
  font-family: var(--mono); font-size: 0.52rem; letter-spacing: 3px;
  text-transform: uppercase; color: var(--t4) !important; margin-top: 6px;
}

/* Section label */
.slbl {
  font-family: var(--mono) !important;
  font-size: 0.56rem !important; letter-spacing: 3px !important;
  text-transform: uppercase !important; color: var(--t3) !important;
  display: block !important; margin: 6px 0 4px !important;
}

/* Status pill */
.pill {
  display: inline-flex; align-items: center; gap: 7px;
  padding: 5px 13px; border-radius: var(--r-f);
  font-family: var(--mono); font-size: 0.58rem;
  letter-spacing: 1.5px; text-transform: uppercase;
  margin-bottom: 10px; animation: fade-up 0.5s ease both;
}
.pill.on  { background: var(--grn-s);  border: 1px solid rgba(0,232,122,0.3); color: var(--grn) !important; }
.pill.off { background: var(--ac-s);   border: 1px solid var(--ac-bd);        color: var(--ac) !important; }
.pill .dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }
.pill.on  .dot { background: var(--grn); box-shadow: 0 0 10px var(--grn); animation: blink 2s infinite; }
.pill.off .dot { background: var(--ac);  box-shadow: 0 0 8px var(--ac-gl); }

/* Hero */
.hero {
  padding: 38px 0 26px;
  border-bottom: 1px solid var(--b1);
  margin-bottom: 22px; position: relative;
}
.hero-eye {
  font-family: var(--mono); font-size: 0.62rem;
  letter-spacing: 4px; text-transform: uppercase;
  color: var(--ac) !important; margin-bottom: 14px;
  display: flex; align-items: center; gap: 10px;
  animation: fade-up 0.5s ease both; opacity: 0;
}
.hero-eye::before {
  content: '';
  display: inline-block; width: 22px; height: 1.5px;
  background: var(--ac); box-shadow: 0 0 8px var(--ac-gl);
  animation: rule-grow 0.6s ease both;
}
.hero-title {
  font-family: var(--serif); font-size: 3.8rem; font-weight: 700;
  letter-spacing: -2.5px; line-height: 0.95; color: var(--t1) !important;
  animation: fade-up 0.6s 0.05s cubic-bezier(0.16,1,0.3,1) both; opacity: 0;
}
.hero-title em {
  font-style: italic; color: var(--ac) !important;
  text-shadow: 0 0 60px rgba(255,107,53,0.45);
}
.hero-desc {
  font-family: var(--sans); font-size: 0.93rem; font-weight: 300;
  color: var(--t2) !important; margin-top: 16px; line-height: 1.65;
  animation: fade-up 0.6s 0.15s ease both; opacity: 0;
}
.hero-status {
  display: flex; align-items: center; gap: 9px; margin-top: 20px;
  animation: fade-up 0.5s 0.25s ease both; opacity: 0;
}
.hero-dot {
  width: 8px; height: 8px; border-radius: 50%;
  background: var(--ac); box-shadow: 0 0 12px var(--ac-gl);
  animation: blink 2.5s ease-in-out infinite;
}
.hero-status-text {
  font-family: var(--mono); font-size: 0.62rem;
  letter-spacing: 1px; color: var(--t3) !important;
}

/* Hero right tags */
.h-tag {
  font-family: var(--mono); font-size: 0.6rem; letter-spacing: 1.5px;
  text-transform: uppercase; color: var(--t2) !important;
  background: var(--card); border: 1px solid var(--b2);
  padding: 7px 14px; border-radius: var(--r);
  transition: all 0.2s; display: block; margin-bottom: 6px;
  animation: fade-up 0.5s ease both; opacity: 0;
}
.h-tag:hover { border-color: var(--ac-bd); color: var(--ac) !important; transform: translateX(-4px); }

/* Mode strip */
.mstrip {
  display: flex; align-items: center; gap: 14px;
  margin-bottom: 22px; animation: fade-up 0.4s ease both;
}
.mpill {
  font-family: var(--mono); font-size: 0.6rem;
  letter-spacing: 1.5px; text-transform: uppercase;
  color: var(--ac) !important;
  background: var(--ac-b); border: 1px solid var(--ac-bd);
  padding: 5px 15px; border-radius: var(--r-f);
  box-shadow: 0 0 16px var(--ac-s);
  animation: border-rotate 7s linear infinite;
}
.minfo { font-family: var(--mono); font-size: 0.6rem; letter-spacing: 1px; color: var(--t3) !important; }
.msep  { color: var(--b2) !important; }

/* Empty state */
.empty {
  text-align: center; padding: 90px 20px;
  animation: fade-in 0.8s ease both;
}
.e-glyph {
  font-family: var(--serif); font-size: 4rem; font-style: italic;
  color: var(--t4) !important; display: block;
  animation: float 7s ease-in-out infinite;
}
.e-title {
  font-family: var(--mono); font-size: 0.64rem;
  letter-spacing: 4px; text-transform: uppercase;
  color: var(--t3) !important; margin-top: 24px;
}
.e-hint {
  font-family: var(--sans); font-size: 0.82rem;
  color: var(--t4) !important; margin-top: 10px; font-style: italic;
}

/* Glass card */
.gc {
  background: rgba(255,255,255,0.04); border: 1px solid var(--b1);
  border-radius: var(--r-lg); padding: 22px;
  backdrop-filter: blur(14px); position: relative; overflow: hidden;
  transition: all 0.28s cubic-bezier(0.16,1,0.3,1);
}
.gc::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
}
.gc:hover { border-color: var(--b2); box-shadow: var(--sh); transform: translateY(-3px); }
.gc-rule {
  width: 24px; height: 2px;
  background: linear-gradient(90deg, var(--ac), transparent);
  border-radius: 2px; margin-bottom: 14px;
  box-shadow: 0 0 10px var(--ac-gl);
  animation: rule-grow 0.6s ease both;
}

/* Memory row */
.mrow {
  display: flex; align-items: baseline; gap: 12px;
  padding: 12px 0; border-bottom: 1px solid var(--b1);
  font-family: var(--mono); font-size: 0.78rem;
  animation: fade-up 0.35s ease both; transition: padding-left 0.2s;
}
.mrow:last-child { border-bottom: none; }
.mrow:hover { padding-left: 8px; }
.mk { color: var(--ac) !important; font-weight: 600; min-width: 100px; }
.ma { color: var(--t4) !important; }
.mv { color: var(--t1) !important; flex: 1; }
.mt { color: var(--t4) !important; font-size: 0.58rem; margin-left: auto; white-space: nowrap; }

/* Voice row */
.vrow {
  padding: 14px 0; border-bottom: 1px solid var(--b1);
  animation: fade-up 0.35s ease both; transition: padding-left 0.2s;
}
.vrow:last-child { border-bottom: none; }
.vrow:hover { padding-left: 8px; }
.vlbl {
  font-family: var(--mono); font-size: 0.56rem;
  letter-spacing: 2px; text-transform: uppercase; margin-bottom: 6px;
}
.vcnt { font-family: var(--sans); font-size: 0.9rem; color: var(--t1) !important; line-height: 1.65; }

/* Chip */
.chip {
  display: inline-flex; align-items: center; gap: 5px;
  background: var(--card); border: 1px solid var(--b2);
  border-radius: var(--r-f); padding: 4px 12px;
  font-family: var(--mono); font-size: 0.6rem;
  color: var(--t2) !important; margin: 3px;
  transition: all 0.2s;
}
.chip:hover { border-color: var(--ac-bd); color: var(--ac) !important; background: var(--ac-b); }

/* Info row */
.ir {
  display: flex; justify-content: space-between; align-items: baseline;
  padding: 11px 0; border-bottom: 1px solid var(--b1);
  font-family: var(--mono); font-size: 0.78rem;
  transition: padding-left 0.2s;
}
.ir:last-child { border-bottom: none; }
.ir:hover { padding-left: 8px; }
.il { color: var(--t3) !important; }
.iv { color: var(--t1) !important; font-weight: 500; }
.iv.org  { color: var(--ac)   !important; text-shadow: 0 0 20px var(--ac-gl); }
.iv.grn  { color: var(--grn)  !important; }
.iv.gold { color: var(--gold) !important; }
.iv.cyn  { color: var(--cyan) !important; }
</style>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
#  DATABASE
# ════════════════════════════════════════════════════════════
DB_PATH = "nexus_memory.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS chat_sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT, role TEXT, content TEXT,
        mode TEXT, timestamp TEXT, tokens INTEGER DEFAULT 0, response_time REAL DEFAULT 0
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS user_memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT, key TEXT, value TEXT, created_at TEXT
    )""")
    conn.commit(); conn.close()

def save_message(session_id, role, content, mode="chat", tokens=0, response_time=0):
    conn = sqlite3.connect(DB_PATH)
    conn.cursor().execute(
        "INSERT INTO chat_sessions (session_id,role,content,mode,timestamp,tokens,response_time) VALUES (?,?,?,?,?,?,?)",
        (session_id, role, content, mode, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), tokens, response_time)
    ); conn.commit(); conn.close()

def load_history(session_id, limit=50):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT role,content,mode,timestamp FROM chat_sessions WHERE session_id=? ORDER BY id DESC LIMIT ?", (session_id, limit))
    rows = c.fetchall(); conn.close()
    return list(reversed(rows))

def get_all_sessions():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT DISTINCT session_id, MIN(timestamp), COUNT(*) FROM chat_sessions GROUP BY session_id ORDER BY MIN(timestamp) DESC LIMIT 20")
    rows = c.fetchall(); conn.close(); return rows

def save_memory(session_id, key, value):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM user_memory WHERE session_id=? AND key=?", (session_id, key))
    c.execute("INSERT INTO user_memory (session_id,key,value,created_at) VALUES (?,?,?,?)",
              (session_id, key, value, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit(); conn.close()

def get_memories(session_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT key,value,created_at FROM user_memory WHERE session_id=? ORDER BY id DESC", (session_id,))
    rows = c.fetchall(); conn.close(); return rows

def extract_pdf_text(uploaded_file):
    try:
        content = uploaded_file.read()
        try:
            import pdfplumber
            with pdfplumber.open(io.BytesIO(content)) as pdf:
                return "\n".join([p.extract_text() or "" for p in pdf.pages])
        except:
            import PyPDF2
            reader = PyPDF2.PdfReader(io.BytesIO(content))
            return "\n".join([p.extract_text() or "" for p in reader.pages])
    except: return None

def chunk_text(text, size=500, overlap=50):
    words = text.split()
    return [" ".join(words[i:i+size]) for i in range(0, len(words), size-overlap) if words[i:i+size]]

def find_relevant_chunks(query, chunks, top_k=3):
    qw = set(query.lower().split())
    scored = [(len(qw & set(c.lower().split())), i, c) for i, c in enumerate(chunks)]
    scored.sort(reverse=True)
    return [c for _, _, c in scored[:top_k]]

def web_search(query, max_results=4):
    try:
        from duckduckgo_search import DDGS
        with DDGS() as ddgs:
            return [{"title": r.get("title",""), "snippet": r.get("body",""), "url": r.get("href","")}
                    for r in ddgs.text(query, max_results=max_results)]
    except Exception as e: return [{"title": "Error", "snippet": str(e), "url": ""}]

def extract_and_save_memory(session_id, user_msg, ai_resp, api_key, model):
    try:
        from groq import Groq
        client = Groq(api_key=api_key)
        resp = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role":"user","content":
                f"Extract key facts as JSON array [{{\"key\":\"x\",\"value\":\"y\"}}]. If none return [].\nUser: {user_msg}\nAI: {ai_resp[:300]}"}],
            max_tokens=200, temperature=0)
        text = resp.choices[0].message.content.strip()
        s, e = text.find("["), text.rfind("]")+1
        if s >= 0 and e > s:
            for f in json.loads(text[s:e]):
                if "key" in f and "value" in f: save_memory(session_id, f["key"], f["value"])
    except: pass

# ════════ SESSION STATE ════════
init_db()
if "session_id" not in st.session_state:
    st.session_state.session_id = hashlib.md5(datetime.now().isoformat().encode()).hexdigest()[:10]
if "messages"   not in st.session_state: st.session_state.messages = []
if "pdf_chunks" not in st.session_state: st.session_state.pdf_chunks = []; st.session_state.pdf_name = None
if "stats"      not in st.session_state: st.session_state.stats = {"msgs":0,"tokens":0,"times":[]}
if "voice_text" not in st.session_state: st.session_state.voice_text = None

# ════════════════════════════════════════════════════════════
#  SIDEBAR
# ════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div class="sb-head">
      <div class="sb-shimmer"></div>
      <div class="sb-icon">◈</div>
      <div class="sb-title"><em>Nexus</em> AI</div>
      <div class="sb-sub">Personal Assistant · v2.0</div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<span class="slbl" style="margin-top:18px;">Groq API Key</span>', unsafe_allow_html=True)
    api_key = st.text_input("key", type="password", placeholder="gsk_...", label_visibility="collapsed", key="api_key_input")
    ok = bool(api_key and api_key.startswith("gsk_"))
    st.markdown(f"""<div class="pill {'on' if ok else 'off'}">
      <span class="dot"></span>{'Connected' if ok else 'No API Key'}</div>""", unsafe_allow_html=True)
    st.divider()

    st.markdown('<span class="slbl">Model</span>', unsafe_allow_html=True)
    model = st.selectbox("m", ["llama-3.3-70b-versatile","llama-3.1-8b-instant","mixtral-8x7b-32768","gemma2-9b-it"], label_visibility="collapsed")
    c1, c2 = st.columns(2)
    with c1: temperature = st.slider("Temperature", 0.0, 2.0, 0.7, 0.1)
    with c2: max_tokens  = st.slider("Max Tokens",  256, 4096, 1500, 128)
    st.divider()

    st.markdown('<span class="slbl">Mode</span>', unsafe_allow_html=True)
    mode = st.radio("mode", ["💬 Chat","📄 PDF / RAG","🌐 Web Search","🎤 Voice","🧠 Memory"], label_visibility="collapsed")
    st.session_state.mode = mode
    st.divider()

    st.markdown('<span class="slbl">Persona</span>', unsafe_allow_html=True)
    PERSONAS = {
        "◈ NEXUS":     "You are NEXUS, an elite personal AI. Be precise, intelligent, and helpful.",
        "⌨ Developer": "You are a senior software engineer. Focus on clean code and best practices.",
        "⊞ Analyst":   "You are an expert data analyst. Focus on data-driven insights.",
        "✦ Writer":    "You are a creative writer. Help with storytelling and content.",
        "◉ Professor": "You are a knowledgeable professor. Explain with clarity and depth.",
        "✎ Custom":    None,
    }
    persona = st.selectbox("p", list(PERSONAS.keys()), label_visibility="collapsed")
    if persona == "✎ Custom":
        system_prompt = st.text_area("Custom", height=72, placeholder="Define personality...", label_visibility="collapsed")
    else:
        system_prompt = PERSONAS[persona]
    st.divider()

    st.markdown('<span class="slbl">Session Stats</span>', unsafe_allow_html=True)
    rt = st.session_state.stats["times"]
    avg = sum(rt)/len(rt) if rt else 0
    m1, m2 = st.columns(2)
    with m1: st.metric("Messages", st.session_state.stats["msgs"]); st.metric("Tokens", st.session_state.stats["tokens"])
    with m2: st.metric("Avg Speed", f"{avg:.1f}s"); st.metric("Session", st.session_state.session_id[:6]+"…")
    st.divider()

    b1, b2 = st.columns(2)
    with b1:
        if st.button("Clear", use_container_width=True): st.session_state.messages = []; st.rerun()
    with b2:
        if st.button("New", use_container_width=True):
            st.session_state.session_id = hashlib.md5(datetime.now().isoformat().encode()).hexdigest()[:10]
            st.session_state.messages = []; st.rerun()

    st.markdown("""<div style="text-align:center;padding:16px 0 4px;
        font-family:'JetBrains Mono',monospace;font-size:0.5rem;letter-spacing:2px;
        color:#3d3850;text-transform:uppercase;">Python · Groq · Streamlit</div>""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
#  MAIN — HERO
# ════════════════════════════════════════════════════════════
MODE_LABELS = {"💬 Chat":"Standard Chat","📄 PDF / RAG":"Document Intelligence",
               "🌐 Web Search":"Live Web Search","🎤 Voice":"Voice Interface","🧠 Memory":"Memory Manager"}
mlabel = MODE_LABELS.get(mode,"Active")
mshort = model.split("-")[0].upper()

lc, rc = st.columns([7,3])
with lc:
    st.markdown(f"""
    <div class="hero">
      <div class="hero-eye">Personal Intelligence System</div>
      <div class="hero-title"><em>Nexus</em> AI</div>
      <div class="hero-desc">Your adaptive AI assistant — ultra-fast Groq inference, always ready.</div>
      <div class="hero-status">
        <span class="hero-dot"></span>
        <span class="hero-status-text">System Online · {mshort} · Session {st.session_state.session_id[:8]}</span>
      </div>
    </div>""", unsafe_allow_html=True)
with rc:
    st.markdown(f"""
    <div style="padding:38px 0 26px;display:flex;flex-direction:column;
         align-items:flex-end;gap:5px;border-bottom:1px solid rgba(255,255,255,0.07);
         margin-bottom:22px;">
      <div class="h-tag">{mode}</div>
      <div class="h-tag">{mshort} Model</div>
      <div class="h-tag">{temperature}t · {max_tokens} tok</div>
    </div>""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
#  TABS
# ════════════════════════════════════════════════════════════
tab_chat, tab_hist, tab_mem, tab_sys = st.tabs(["CHAT","HISTORY","MEMORY","SYSTEM"])

# ── TAB 1: CHAT ──
with tab_chat:
    st.markdown(f"""<div class="mstrip">
      <span class="mpill">{mlabel}</span>
      <span class="minfo">{mshort}</span><span class="msep">·</span>
      <span class="minfo">{temperature} temp</span><span class="msep">·</span>
      <span class="minfo">{max_tokens} tok</span>
    </div>""", unsafe_allow_html=True)

    if mode == "📄 PDF / RAG":
        uploaded = st.file_uploader("Upload PDF", type=["pdf"], key="pdf_up")
        if uploaded:
            with st.spinner("Reading document…"):
                txt = extract_pdf_text(uploaded)
                if txt:
                    st.session_state.pdf_chunks = chunk_text(txt)
                    st.session_state.pdf_name   = uploaded.name
                    st.success(f"✓  {uploaded.name} — {len(st.session_state.pdf_chunks)} chunks")
                else: st.error("Could not read PDF. Install: pip install pdfplumber")
        if st.session_state.pdf_name:
            st.markdown(f"""<div class="gc" style="padding:13px 18px;margin-bottom:14px;">
              <span class="chip">📄 Active</span>
              <span style="font-family:'JetBrains Mono',monospace;font-size:0.76rem;color:#7c7590;margin-left:8px;">
                {st.session_state.pdf_name} · {len(st.session_state.pdf_chunks)} chunks</span>
            </div>""", unsafe_allow_html=True)

    elif mode == "🎤 Voice":
        st.markdown("""<div style="font-family:'Playfair Display',serif;font-size:1.25rem;
             font-weight:600;letter-spacing:-0.3px;margin-bottom:20px;color:#f0eeff;">
          Voice Interface</div>""", unsafe_allow_html=True)
        if not api_key:
            st.warning("Enter your Groq API Key in the sidebar first.")
        else:
            if st.session_state.messages:
                st.markdown('<span class="slbl" style="margin-bottom:10px;display:block;">Recent</span>', unsafe_allow_html=True)
                for msg in st.session_state.messages[-6:]:
                    lclr = "var(--ac)" if msg["role"]=="assistant" else "var(--t3)"
                    ic = "◈" if msg["role"]=="assistant" else "◌"
                    st.markdown(f"""<div class="vrow">
                      <div class="vlbl" style="color:{lclr};">{ic}  {msg['role'].upper()}</div>
                      <div class="vcnt">{msg['content'][:200]}{'…' if len(msg['content'])>200 else ''}</div>
                    </div>""", unsafe_allow_html=True)
                st.divider()

            v1, v2 = st.columns(2)
            with v1:
                st.markdown("""<div class="gc"><div class="gc-rule"></div>
                  <span class="slbl" style="color:var(--grn);">Option 1 — Browser Mic</span>
                  <div style="font-family:'Inter',sans-serif;font-size:0.82rem;color:#7c7590;margin:8px 0 14px;font-style:italic;">Record in browser</div>
                </div>""", unsafe_allow_html=True)
                st.components.v1.html("""<!DOCTYPE html><html><head><style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap');
*{box-sizing:border-box;margin:0;padding:0;}
body{background:transparent;font-family:'JetBrains Mono',monospace;}
#w{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);
   border-radius:12px;padding:20px;text-align:center;backdrop-filter:blur(12px);}
#btn{width:100%;padding:12px 20px;border-radius:9999px;cursor:pointer;
     font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:2px;
     text-transform:uppercase;font-weight:500;transition:all .25s;
     background:transparent;border:1.5px solid rgba(255,255,255,0.12);color:#7c7590;}
#btn:hover{background:rgba(255,107,53,0.12);border-color:rgba(255,107,53,0.45);color:#ff6b35;box-shadow:0 0 24px rgba(255,107,53,0.2);}
#btn.rec{border-color:#ff6b35;color:#ff6b35;background:rgba(255,107,53,0.1);animation:gp 1.2s ease-in-out infinite;}
@keyframes gp{0%,100%{box-shadow:0 0 16px rgba(255,107,53,0.25);}50%{box-shadow:0 0 40px rgba(255,107,53,0.5);}}
#t{font-size:24px;color:#ff6b35;margin:12px 0;display:none;font-weight:600;letter-spacing:4px;text-shadow:0 0 20px rgba(255,107,53,0.5);}
#s{font-size:10px;color:#3d3850;margin-top:8px;letter-spacing:1.5px;text-transform:uppercase;}
#s.ok{color:#00e87a;} #s.er{color:#ff6b35;}
audio{width:100%;margin-top:12px;display:none;border-radius:8px;opacity:0.7;}
#dl{display:none;margin-top:12px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:12px;}
#lnk{color:#ff6b35;text-decoration:none;display:block;margin-top:6px;font-size:10px;letter-spacing:.5px;transition:color .2s;}
#lnk:hover{color:#ff8555;}
#nt{color:#00e87a;margin-top:6px;font-size:10px;letter-spacing:.5px;text-transform:uppercase;}
</style></head><body>
<div id="w">
  <button id="btn" onclick="tgl()">⏺ &nbsp; Start Recording</button>
  <div id="t">00:00</div>
  <div id="s">Microphone ready</div>
  <audio id="au" controls></audio>
  <div id="dl">
    <div style="color:#3d3850;font-size:10px;text-transform:uppercase;letter-spacing:.5px;">Ready — upload in Option 2</div>
    <a id="lnk" download="recording.wav">↓ Download recording.wav</a>
    <div id="nt">✓ Then upload below</div>
  </div>
</div>
<script>
let mr=null,ac=[],rec=false,ti=null,s=0;
function tk(){s++;let m=String(Math.floor(s/60)).padStart(2,'0'),sc=String(s%60).padStart(2,'0');
  document.getElementById('t').textContent=m+':'+sc;}
async function tgl(){
  if(!rec){
    try{
      const st=await navigator.mediaDevices.getUserMedia({audio:true});
      mr=new MediaRecorder(st);ac=[];
      mr.ondataavailable=e=>{if(e.data.size>0)ac.push(e.data)};
      mr.onstop=()=>{
        const bl=new Blob(ac,{type:'audio/wav'}),ur=URL.createObjectURL(bl);
        const a=document.getElementById('au');a.src=ur;a.style.display='block';
        document.getElementById('lnk').href=ur;
        document.getElementById('dl').style.display='block';
        document.getElementById('s').textContent='Recording ready';
        document.getElementById('s').className='ok';
        st.getTracks().forEach(t=>t.stop());
      };
      mr.start();rec=true;s=0;
      document.getElementById('btn').textContent='⏹  Stop Recording';
      document.getElementById('btn').className='rec';
      document.getElementById('s').textContent='Recording…';
      document.getElementById('s').className='ok';
      document.getElementById('t').style.display='block';
      document.getElementById('dl').style.display='none';
      document.getElementById('au').style.display='none';
      ti=setInterval(tk,1000);
    }catch(e){
      document.getElementById('s').textContent='Mic denied: '+e.message;
      document.getElementById('s').className='er';
    }
  }else{
    mr.stop();rec=false;clearInterval(ti);
    document.getElementById('t').style.display='none';
    document.getElementById('btn').textContent='⏺  Start Recording';
    document.getElementById('btn').className='';
  }
}
</script></body></html>""", height=265)

            with v2:
                st.markdown("""<div class="gc"><div class="gc-rule"></div>
                  <span class="slbl" style="color:var(--ac);">Option 2 — Upload & Transcribe</span>
                  <div style="font-family:'Inter',sans-serif;font-size:0.82rem;color:#7c7590;margin:8px 0 14px;font-style:italic;">WAV / MP3 / M4A</div>
                </div>""", unsafe_allow_html=True)
                af = st.file_uploader("Audio", type=["wav","mp3","m4a","ogg","webm"], label_visibility="collapsed", key="aud_up")
                if af:
                    st.audio(af)
                    if st.button("Transcribe with Whisper", use_container_width=True, type="primary"):
                        with st.spinner("Whisper listening…"):
                            from groq import Groq
                            client = Groq(api_key=api_key)
                            aio = io.BytesIO(af.read()); aio.name = af.name
                            try:
                                r = client.audio.transcriptions.create(file=aio, model="whisper-large-v3")
                                st.success("Transcribed!"); st.info(f"🎤  {r.text}")
                                st.session_state.voice_text = r.text
                            except Exception as e: st.error(f"Error: {e}")
                else:
                    st.markdown("""<div style="border:1.5px dashed rgba(255,255,255,0.1);border-radius:10px;
                         padding:32px;text-align:center;color:#3d3850;
                         font-family:'JetBrains Mono',monospace;font-size:0.68rem;
                         letter-spacing:1px;text-transform:uppercase;background:rgba(255,255,255,0.02);">
                      Record → Download → Upload here</div>""", unsafe_allow_html=True)

            if st.session_state.voice_text:
                st.divider()
                st.markdown(f"""<div class="gc" style="border-color:rgba(255,107,53,0.35);">
                  <div class="gc-rule"></div>
                  <span class="slbl" style="color:var(--ac);display:block;margin-bottom:10px;">Ready to Send</span>
                  <div style="font-family:'Inter',sans-serif;font-size:0.95rem;color:#f0eeff;
                       background:rgba(255,107,53,0.06);padding:14px;border-radius:10px;
                       border-left:3px solid var(--ac);font-style:italic;line-height:1.7;">
                    "{st.session_state.voice_text}"</div>
                </div>""", unsafe_allow_html=True)
                sa, sb = st.columns([3,1])
                with sa:
                    if st.button("Send to AI", use_container_width=True, type="primary"):
                        vt = st.session_state.voice_text
                        st.session_state.messages.append({"role":"user","content":f"🎤 {vt}"})
                        st.session_state.voice_text = None
                        with st.spinner("Thinking…"):
                            try:
                                from groq import Groq
                                client = Groq(api_key=api_key)
                                api_msgs = [{"role":"system","content":system_prompt}]
                                for m in st.session_state.messages[-10:]:
                                    api_msgs.append({"role":m["role"],"content":m["content"]})
                                resp = client.chat.completions.create(model=model,messages=api_msgs,temperature=temperature,max_tokens=max_tokens)
                                reply = resp.choices[0].message.content; tokens = resp.usage.total_tokens
                                st.session_state.messages.append({"role":"assistant","content":reply,"meta":f"voice · {tokens} tokens"})
                                st.session_state.stats["msgs"] += 1; st.session_state.stats["tokens"] += tokens
                                save_message(st.session_state.session_id,"user",f"🎤 {vt}","voice")
                                save_message(st.session_state.session_id,"assistant",reply,"voice",tokens)
                                st.rerun()
                            except Exception as e: st.error(f"Error: {e}")
                with sb:
                    if st.button("Discard", use_container_width=True):
                        st.session_state.voice_text = None; st.rerun()

    if mode != "🎤 Voice":
        if not st.session_state.messages:
            st.markdown("""<div class="empty">
              <span class="e-glyph">◈</span>
              <div class="e-title">Nexus Online</div>
              <div class="e-hint">Select a mode and begin the conversation</div>
            </div>""", unsafe_allow_html=True)
        else:
            for msg in st.session_state.messages:
                with st.chat_message(msg["role"]):
                    st.markdown(msg["content"])
                    if "meta" in msg: st.caption(msg["meta"])

        placeholders = {"💬 Chat":"Ask anything…","📄 PDF / RAG":"Ask about your document…",
                        "🌐 Web Search":"Search the web for…","🧠 Memory":"Tell me something to remember…"}
        prompt = st.chat_input(placeholders.get(mode,"Type here…"))

        if prompt:
            if not api_key: st.error("Enter your Groq API Key in sidebar → console.groq.com"); st.stop()
            st.session_state.messages.append({"role":"user","content":prompt})
            with st.chat_message("user"): st.markdown(prompt)

            extra = ""; search_results = []
            if mode == "📄 PDF / RAG" and st.session_state.pdf_chunks:
                chunks = find_relevant_chunks(prompt, st.session_state.pdf_chunks)
                extra  = f"\n\n[Document: {st.session_state.pdf_name}]\n" + "\n---\n".join(chunks)
            elif mode == "🌐 Web Search":
                with st.spinner("Searching the web…"):
                    search_results = web_search(prompt)
                    if search_results:
                        extra = "\n\n[Web Search Results]\n" + "\n".join([f"[{r['title']}]: {r['snippet']}" for r in search_results if r['snippet']])
                        extra += "\n\nAnswer based on these results."

            memories = get_memories(st.session_state.session_id)
            mem_ctx = ("\n\n[User Memory]\n" + "\n".join([f"- {k}: {v}" for k,v,_ in memories])) if memories else ""

            api_msgs = [{"role":"system","content": system_prompt + mem_ctx + extra}]
            for m in st.session_state.messages[-10:]: api_msgs.append({"role":m["role"],"content":m["content"]})

            with st.chat_message("assistant"):
                with st.spinner("Thinking…"):
                    try:
                        from groq import Groq
                        client = Groq(api_key=api_key)
                        t0 = time.time()
                        resp = client.chat.completions.create(model=model,messages=api_msgs,temperature=temperature,max_tokens=max_tokens)
                        elapsed = time.time()-t0; reply = resp.choices[0].message.content; tokens = resp.usage.total_tokens
                        st.markdown(reply)
                        if search_results:
                            with st.expander("Sources"):
                                for r in search_results:
                                    if r["url"]: st.markdown(f"- [{r['title']}]({r['url']})")
                        meta = f"{elapsed:.2f}s · {tokens} tokens · {model.split('-')[0].upper()}"
                        st.caption(meta)
                        st.session_state.messages.append({"role":"assistant","content":reply,"meta":meta})
                        st.session_state.stats["msgs"] += 1; st.session_state.stats["tokens"] += tokens
                        st.session_state.stats["times"].append(elapsed)
                        save_message(st.session_state.session_id,"user",prompt,mode)
                        save_message(st.session_state.session_id,"assistant",reply,mode,tokens,elapsed)
                        if mode in ["💬 Chat","🧠 Memory"]:
                            extract_and_save_memory(st.session_state.session_id,prompt,reply,api_key,model)
                    except Exception as e:
                        err = str(e)
                        if "invalid_api_key" in err.lower(): st.error("Invalid API Key.")
                        elif "rate_limit" in err.lower(): st.error("Rate limit — please wait.")
                        else: st.error(f"Error: {err}")

# ── TAB 2: HISTORY ──
with tab_hist:
    st.markdown("""<div style="font-family:'Playfair Display',serif;font-size:1.3rem;font-weight:600;
         letter-spacing:-0.3px;margin-bottom:6px;color:#f0eeff;">Chat History</div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:0.62rem;letter-spacing:2px;
         text-transform:uppercase;color:#3d3850;margin-bottom:22px;">Persistent across sessions</div>""",
        unsafe_allow_html=True)
    sessions = get_all_sessions()
    if not sessions:
        st.markdown("""<div class="empty" style="padding:50px 20px;">
          <span class="e-glyph" style="font-size:2.5rem;">∅</span>
          <div class="e-title">No History Yet</div>
          <div class="e-hint">Start chatting to save sessions</div>
        </div>""", unsafe_allow_html=True)
    else:
        for sid, start, count in sessions:
            is_cur = sid == st.session_state.session_id
            with st.expander(f"{'● ' if is_cur else '○ '}Session {sid}  ·  {count} messages  ·  {start}"):
                for role, content, hmode, ts in load_history(sid, 30):
                    ic = "◈" if role=="assistant" else "◌"
                    lc = "var(--ac)" if role=="assistant" else "var(--t3)"
                    st.markdown(f"""<div class="vrow">
                      <div class="vlbl" style="color:{lc};">{ic}  {role.upper()}  ·  {ts}  ·  {hmode}</div>
                      <div class="vcnt">{content[:280]}{'…' if len(content)>280 else ''}</div>
                    </div>""", unsafe_allow_html=True)

# ── TAB 3: MEMORY ──
with tab_mem:
    st.markdown("""<div style="font-family:'Playfair Display',serif;font-size:1.3rem;font-weight:600;
         letter-spacing:-0.3px;margin-bottom:6px;color:#f0eeff;">Memory Store</div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:0.62rem;letter-spacing:2px;
         text-transform:uppercase;color:#3d3850;margin-bottom:22px;">AI learns key facts automatically</div>""",
        unsafe_allow_html=True)
    ma, mb, mc_ = st.columns([2,3,1])
    with ma: mk = st.text_input("Key",   placeholder="e.g. name",  label_visibility="collapsed")
    with mb: mv = st.text_input("Value", placeholder="e.g. Ahmed", label_visibility="collapsed")
    with mc_:
        st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
        if st.button("Save", use_container_width=True, type="primary"):
            if mk and mv: save_memory(st.session_state.session_id, mk, mv); st.success("Saved!"); st.rerun()
    st.divider()
    mems = get_memories(st.session_state.session_id)
    if not mems:
        st.markdown("""<div class="empty" style="padding:50px 20px;">
          <span class="e-glyph" style="font-size:2.5rem;">∅</span>
          <div class="e-title">No Memories Yet</div>
          <div class="e-hint">Chat in Memory mode — AI will learn automatically</div>
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown(f'<span class="slbl" style="margin-bottom:12px;display:block;">{len(mems)} facts · Session {st.session_state.session_id}</span>', unsafe_allow_html=True)
        for key, val, created in mems:
            st.markdown(f"""<div class="mrow">
              <span class="mk">{key}</span><span class="ma">→</span>
              <span class="mv">{val}</span><span class="mt">{created}</span>
            </div>""", unsafe_allow_html=True)

# ── TAB 4: SYSTEM ──
with tab_sys:
    st.markdown("""<div style="font-family:'Playfair Display',serif;font-size:1.3rem;font-weight:600;
         letter-spacing:-0.3px;margin-bottom:6px;color:#f0eeff;">System</div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:0.62rem;letter-spacing:2px;
         text-transform:uppercase;color:#3d3850;margin-bottom:22px;">Configuration & Performance</div>""",
        unsafe_allow_html=True)
    sc1, sc2 = st.columns(2)
    with sc1:
        st.markdown("""<div class="gc" style="margin-bottom:14px;">
          <div class="gc-rule"></div>
          <span class="slbl" style="display:block;margin-bottom:14px;">Active Features</span>
          <span class="chip">⚡ Groq LLM</span><span class="chip">🗄 SQLite</span>
          <span class="chip">📄 PDF/RAG</span><span class="chip">🌐 DuckDuckGo</span>
          <span class="chip">🎤 Whisper v3</span><span class="chip">🧠 Auto Memory</span>
        </div>""", unsafe_allow_html=True)
        st.markdown("""<div class="gc">
          <div class="gc-rule"></div>
          <span class="slbl" style="display:block;margin-bottom:14px;">Tech Stack</span>
          <div class="ir"><span class="il">Language</span><span class="iv org">Python 3.10+</span></div>
          <div class="ir"><span class="il">LLM API</span><span class="iv org">Groq SDK</span></div>
          <div class="ir"><span class="il">Models</span><span class="iv">LLaMA · Mixtral · Gemma</span></div>
          <div class="ir"><span class="il">Frontend</span><span class="iv cyn">Streamlit</span></div>
          <div class="ir"><span class="il">Database</span><span class="iv">SQLite3</span></div>
          <div class="ir"><span class="il">Search</span><span class="iv">DuckDuckGo API</span></div>
          <div class="ir"><span class="il">Voice</span><span class="iv">Whisper Large v3</span></div>
        </div>""", unsafe_allow_html=True)
    with sc2:
        rt2 = st.session_state.stats["times"]
        st.markdown(f"""<div class="gc" style="margin-bottom:14px;">
          <div class="gc-rule"></div>
          <span class="slbl" style="display:block;margin-bottom:14px;">Performance</span>
          <div class="ir"><span class="il">Session ID</span><span class="iv org">{st.session_state.session_id}</span></div>
          <div class="ir"><span class="il">Messages</span><span class="iv grn">{st.session_state.stats['msgs']}</span></div>
          <div class="ir"><span class="il">Total Tokens</span><span class="iv grn">{st.session_state.stats['tokens']:,}</span></div>
          <div class="ir"><span class="il">Avg Response</span><span class="iv gold">{(sum(rt2)/len(rt2) if rt2 else 0):.2f}s</span></div>
          <div class="ir"><span class="il">Fastest</span><span class="iv gold">{(min(rt2) if rt2 else 0):.2f}s</span></div>
          <div class="ir"><span class="il">Model</span><span class="iv">{model.split('-')[0].upper()}</span></div>
        </div>""", unsafe_allow_html=True)
        st.markdown("""<div class="gc">
          <div class="gc-rule"></div>
          <span class="slbl" style="display:block;margin-bottom:14px;">Quick Install</span>
          <div style="background:rgba(0,0,0,0.45);border-radius:10px;padding:16px;
               font-family:'JetBrains Mono',monospace;font-size:0.76rem;
               color:#ff6b35;line-height:2.4;border:1px solid rgba(255,107,53,0.15);">
            pip install streamlit groq<br>
            pip install duckduckgo-search<br>
            pip install pdfplumber PyPDF2<br>
            <span style="color:#00e87a;">streamlit run app.py</span>
          </div>
        </div>""", unsafe_allow_html=True)
