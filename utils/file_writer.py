import os
from datetime import datetime

def save_html_file(topic: str, html_content: str):
    # Create directory if not exists
    output_dir = "HTML_files"
    os.makedirs(output_dir, exist_ok=True)

    # Sanitize topic for filename
    safe_topic = "".join(
        c if c.isalnum() or c in (" ", "_") else "" for c in topic
    ).replace(" ", "_")

    # Timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Final filename
    filename = f"{safe_topic}_{timestamp}.html"
    filepath = os.path.join(output_dir, filename)

    # Write file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)

    return filepath