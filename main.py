import os
from datetime import datetime
from graph.workflow import build_graph
from utils.file_writer import save_html_file

if __name__ == "__main__":
    # Taking inputs from the user

    topic = input("Enter article topic: ").strip()
    temperature = float(
        input("Enter creativity level (0.0 – 1.0): ").strip()
    )

    # BUILDING GRAPH
    app = build_graph()

    input_state = {
        "topic": topic,
        "temperature": temperature,
        "retry_count" : 0
    }

    result = app.invoke(input_state)

    # -------- SAVE HTML --------
    html_content = result["html_content"]
    saved_path = save_html_file(topic, html_content)

    print("\n✅ HTML file generated successfully!")
    print(f"📄 Saved at: {saved_path}")
