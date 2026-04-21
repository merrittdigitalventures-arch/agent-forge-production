from flask import Flask, render_template_string, redirect
import json
import os

app = Flask(__name__)

def get_manifest():
    manifest_path = 'style_manifest.json'
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r') as f:
            return json.load(f)
    return None

@app.route('/')
def home():
    manifest = get_manifest()
    if not manifest:
        return "System Offline: No Manifest Detected.", 500
    
    # Dynamic HTML based on Architect's Vibe
    vibe = manifest['style_guide']['vibe']
    niche = manifest['niche']
    bg_color = manifest['style_guide'].get('color', '#000000')
    
    html = f"""
    <html>
    <head><title>{niche} | Alpha Portal</title></head>
    <body style="background-color: {bg_color}; color: white; font-family: monospace; padding: 50px;">
        <h1>[STATUS: ACTIVE] {niche.upper()}</h1>
        <p>Vibe: {vibe}</p>
        <hr/>
        <h3>Access Technical Diagnostic</h3>
        <p>The {niche} infrastructure audit is ready for review.</p>
        <a href="/alpha-diagnostic" style="color: cyan; text-decoration: none;">> INITIATE ALPHA SCAN</a>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/alpha-diagnostic')
def diagnostic():
    manifest = get_manifest()
    diag_file = f"{manifest['bundle_id']}_diagnostic.md"
    if os.path.exists(diag_file):
        with open(diag_file, 'r') as f:
            content = f.read()
        return f"<pre style='background: #111; color: #0f0; padding: 20px;'>{content}</pre>"
    return "Diagnostic file missing.", 404

@app.route('/upgrade')
def upgrade():
    # Redirecting to the Gumroad link found in your environment
    return redirect("https://merrittdv.gumroad.com/l/bqkota")

if __name__ == "__main__":
    print("🌐 [PORTAL] Launching Cypher Executive Interface...")
    app.run(host='0.0.0.0', port=8080)
