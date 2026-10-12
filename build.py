"""Render the Flask site to static files in dist/ for Netlify."""
import shutil
from pathlib import Path

from app import app

OUTPUT = Path("dist")

if OUTPUT.exists():
    shutil.rmtree(OUTPUT)
OUTPUT.mkdir()

with app.test_client() as client:
    response = client.get("/")
    if response.status_code != 200:
        raise SystemExit(f"Rendering / failed with status {response.status_code}")
    (OUTPUT / "index.html").write_bytes(response.data)

shutil.copytree("static", OUTPUT / "static")
print("Built static site in dist/")
