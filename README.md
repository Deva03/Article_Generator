# Zenara – Multi‑Agent GenAI Article Generation System

**Streamlit UI**

  * Topic input
  * Creativity (temperature) slider

**Centralized Logging**
  * Daily + time‑based log files
  * Full agent execution trace

---

## Architecture Overview

```
User Input (UI)
      ↓
Search Agent
      ↓
Writer Agent ↔ Evaluator Agent (feedback loop)
      ↓
Refiner Agent
      ↓
HTML Generator
      ↓
Saved HTML Output
```

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Environment Variables

Create a `.env` file:

```env
SERPER_API_KEY=your_serper_api_key
GROQ_API_KEY=your_groq_key
```

---

## ▶️ Running the Project

### CLI Mode

```bash
python main.py
```

### Streamlit UI

```bash
streamlit run app.py
```

Stop Streamlit using:

```
CTRL + C
```

---

## 🧪 Example Output

* Number of retries: `2`
* Generated file:

```
html_files/Stock_Market_India_2026-01-02_23-41-18.html
```