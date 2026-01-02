import streamlit as st
import os
from graph.workflow import build_graph
from utils.logger import setup_logger


# ---------- LOGGER ----------
logger = setup_logger("StreamlitUI")


# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Zenara AI Article Generator",
    layout="wide"
)


# ---------- UI ----------
st.title("Zenara – GenAI Article Generator")
st.markdown(
    "Generate structured, evaluated, and standardized articles using a multi-agent LangGraph pipeline."
)

st.divider()

# ---------- INPUTS ----------
topic = st.text_input(
    "Enter Article Topic",
    placeholder="e.g., Stock Market in India"
)

temperature = st.slider(
    "🎨 Creativity (Temperature)",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)

generate_btn = st.button("Generate Article")


# ---------- ACTION ----------
if generate_btn:
    if not topic.strip():
        st.error("Please enter a valid topic.")
    else:
        with st.spinner("Running multi-agent pipeline..."):
            logger.info("UI pipeline started")
            logger.info(f"Topic: {topic}")
            logger.info(f"Temperature: {temperature}")

            app = build_graph()

            input_state = {
                "topic": topic,
                "temperature": temperature,
                "retry_count": 0
            }

            result = app.invoke(input_state)

        st.success("Article generation completed!")

        # ---------- OUTPUTS ----------
        retries = result.get("retry_count", 0)
        html_content = result.get("html_content", "")

        st.divider()

        # Retry Info
        st.metric("Writer Retries Used", retries)

        # Render HTML
        st.subheader("Final Article (HTML Preview)")
        st.components.v1.html(html_content, height=700, scrolling=True)

        # Find latest saved file
        html_dir = "HTML_files"
        latest_file = None

        if os.path.exists(html_dir):
            files = sorted(
                [f for f in os.listdir(html_dir) if f.endswith(".html")],
                reverse=True
            )
            if files:
                latest_file = os.path.join(html_dir, files[0])

        if latest_file:
            st.subheader("Saved HTML File")
            st.code(latest_file)

            with open(latest_file, "r", encoding="utf-8") as f:
                st.download_button(
                    label="⬇Download HTML File",
                    data=f.read(),
                    file_name=os.path.basename(latest_file),
                    mime="text/html"
                )
