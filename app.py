import os
from flask import Flask, render_template

app = Flask(__name__)

# Add your published Tableau embed URLs in Render's Environment settings,
# or set them locally before running the app.
DASHBOARD_URL = os.getenv("TABLEAU_DASHBOARD_URL", "").strip()
STORY_URL = os.getenv("TABLEAU_STORY_URL", "").strip()

@app.route("/")
def home():
    return render_template(
        "index.html",
        dashboard_url=DASHBOARD_URL,
        story_url=STORY_URL
    )

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    # Render supplies PORT; local development defaults to 5000.
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
