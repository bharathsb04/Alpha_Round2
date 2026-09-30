# HUMAN TWIN AI
> **"The Intelligent Digital Twin of a Person"**  
> *Personal Productivity, Circadian Lifestyle & Probabilistic Decision Support*

> 📌 **Central Access Links & Hub File**: [`LINKS.md`](file:///c:/Users/sbabu/OneDrive/Desktop/Hackothon/LINKS.md)

---

## 🌟 Executive Summary

**HumanTwin AI** is not a generic chatbot or a basic task manager. It is an evolving **Personal Digital Twin platform** designed to map, understand, and refine a user's habits, circadian rhythms, goals, and behavioral constraints.

Unlike typical AI assistants that only remember text fragments or blindly overwrite user preferences, HumanTwin features:
1. **The Continuous Twin Evolution Loop**: Simulates What-If decisions, captures real-world outcomes, measures prediction discrepancies, and updates the behavioral model non-destructively.
2. **Context & Pattern Engine**: Grounding AI decisions in actual goals, tasks, circadian peaks, and wearable biometric telemetry without hallucination.
3. **What-If Scenario Simulator**: Split-screen probabilistic comparison (Option A vs Option B) highlighting benefits, risks, trade-offs, confidence levels, and explicit assumptions.
4. **Non-Destructive Memory Matrix**: When a user changes habits (e.g. Morning Study → Evening Study), historical anchors are preserved while active recommendations adapt with developing confidence.
5. **Data Control & Autonomy Center**: "Your Data. Your Twin. Your Control." Complete transparency, memory-by-memory erasure, single-click full JSON export, and twin reset.

---

## 🔄 The HumanTwin Continuous Cycle

```
USER
  ↓
DATA CONTROL
  ↓
PERSONAL TWIN
  ↓
MEMORY + USER MODEL (Structured & Non-destructive)
  ↓
CONTEXT & PATTERN ENGINE (Circadian + Biometrics + Goals)
  ↓
"WHAT-IF?" SCENARIO SIMULATOR
  ↓
OPTION A vs OPTION B (Benefits, Risks, Trade-offs, Uncertainty)
  ↓
PERSONALIZED DECISION SUPPORT (Balanced, Non-coercive)
  ↓
USER MAKES FINAL DECISION
  ↓
REAL-WORLD OUTCOME & USER FEEDBACK
  ↓
TWIN LEARNS & REFINES FATIGUE / TIME MULTIPLIERS
  ↓
PERSONAL TWIN EVOLVES
```

---

## 🛠️ Technology Stack

### Frontend
- **Framework**: React 18, TypeScript, Vite
- **Styling**: Tailwind CSS (Tailwind v4), Glassmorphic Theme (Midnight Navy `#070b14` with Cyber-Cyan & Violet glowing accents)
- **Animations**: Framer Motion (Radial Neural Visualizer, Smooth Card Transitions, Modal Dialogs)
- **Visualizations**: Recharts (Circadian Focus vs Physical Energy curve with Fatigue Boundary lines)
- **Celebration Feedback**: Canvas Confetti
- **Icons**: Lucide React

### Backend
- **Framework**: Python 3.11+, FastAPI (Async REST APIs)
- **Data Validation & Schemas**: Pydantic V2
- **Database & ORM**: SQLAlchemy 2.0 (Async engine), SQLite / PostgreSQL support
- **Authentication**: JWT Bearer Tokens (`python-jose`), Passlib / Bcrypt password hashing
- **AI Architecture**: Clean AI Provider abstraction supporting Google Gemini, OpenAI, and a built-in Local Digital Twin Neural Engine for instant zero-config execution.

---

## 🚀 Quick Start Instructions

### Prerequisites
- Node.js v18+ & npm
- Python 3.10+ & pip

### 1. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
The backend will be available at **`http://127.0.0.1:8000`** (Interactive OpenAPI docs at **`http://127.0.0.1:8000/docs`**).

### 2. Frontend Setup
```bash
# In a new terminal, navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start Vite development server
npm run dev
```
The frontend will be live at **`http://127.0.0.1:5173`**.

---

## 🧪 Testing

Run the automated backend test suite covering auth, memory non-destructive evolution, context engine, scenario simulations, feedback loop, and data export:

```bash
# Run pytest test suite
pytest backend/test_main.py

# Run live endpoint verification script against running server
python test_live.py
```

---

## 🎭 The Hackathon Demo Story (Alex Mercer Persona)

1. **One-Click Launch**: On the Auth Screen, click **`Launch Demo Persona (Alex Mercer)`**.
2. **Dashboard Overview**:
   - Greeted by the Hero Banner displaying circadian peak status (Evening focus window active).
   - Inspect the **Digital Twin Status** capsule (Goals: 6, Memories: 42, Patterns: 18, Confidence: 82%).
   - Review the **Biometric & Circadian Curve** displaying the 7:00–9:30 PM peak and the post-9:30 PM fatigue boundary.
3. **Explore "My Twin" Studio**:
   - View the animated radial neural core with 8 interconnected orbiting nodes.
   - Click **Preferences** or **Behaviour** to view active states vs historical anchors and confidence levels.
   - Click **Trigger Preference Shift Demo** to observe real-time non-destructive adaptation.
4. **Run "What-If?" Scenario**:
   - Dilemma: *"Should I study for my exam or finish my assignment tonight?"*
   - Inspect the comparative split cards:
     - **Option A (Study for Exam)**: Directly protects tomorrow morning's exam; potential cramming fatigue if session exceeds 2.5 hours.
     - **Option B (Finish Assignment)**: Coursework certainty; reduced review depth for exam.
   - Click **`Choose Option A`** to record your decision.
5. **The Feedback Loop & Twin Evolution**:
   - Navigate to **Feedback Loop**.
   - Select Rating: `🙁 Not Useful`.
   - Enter Outcome: *"I was too tired and only studied for 30 minutes."*
   - Enter Reflection: *"Prediction did not account for my energy level after a long day."*
   - Click **`Submit Real Outcome & Evolve Twin`**.
   - Confetti triggers! The **Twin Evolution Engine** detects the fatigue discrepancy, adjusts the evening energy decay model, updates confidence (+5%), and logs a new behavioral memory.
6. **Ask Your Twin (AI Assistant)**:
   - Ask *"When am I usually most productive?"*.
   - Notice the transparent **`Grounding Context Referenced`** drawer showcasing exactly what goals and routine anchors were used.
7. **Data Control & Privacy Center**:
   - Visit **Data Control** to inspect what HumanTwin knows.
   - Click **`Export Complete JSON Archive`** to download your complete data matrix.

---

## 🔒 Security & Privacy Guarantees
- **No Hallucinated Facts**: The Context Engine strictly filters memories and explicitly labels assumptions.
- **User in Full Control**: The AI provides balanced trade-off analysis; the user makes the final choice.
- **Right to be Forgotten**: Single-memory wipe, batch memory wipe, or complete twin reset available anytime.

---

**Developed for Hackathon 2026 — HUMAN TWIN AI**
