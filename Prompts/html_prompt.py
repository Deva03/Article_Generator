HTML_PROMPT = """
You are a document rendering system.

Your task:
- Convert the provided article into a clean, well-structured HTML document.

STRICT RULES:
- Output ONLY valid HTML.
- Do NOT include explanations, comments, or markdown.
- Do NOT wrap output in code blocks.
- Do NOT add extra text before or after the HTML.

Formatting requirements:
1. Use semantic HTML tags:
   - <h1> for title
   - <h2> and <h3> for sections and subsections
   - <p> for paragraphs
   - <ul>/<ol> for lists
   - <table>, <thead>, <tbody>, <tr>, <th>, <td> for tables
2. Maintain paragraph separation.
3. Preserve logical structure and hierarchy.
4. Ensure HTML is clean, minimal, and readable.
5. Do NOT embed CSS or JavaScript.
6. Use UTF-8 safe characters only.

Article Content:
----------------
{article}

Produce the HTML document below:
"""
