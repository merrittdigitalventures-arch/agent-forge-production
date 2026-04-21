import json

with open('style_manifest.json', 'r') as f:
    m = json.load(f)

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{m['niche']} | Alpha Portal</title>
    <style>
        body {{ background: {m['style_guide']['color']}; color: white; font-family: 'Courier New', monospace; padding: 50px; }}
        .btn {{ display: inline-block; border: 1px solid white; padding: 10px; color: white; text-decoration: none; }}
    </style>
</head>
<body>
    <h1>[SYSTEM ACTIVE] {m['niche'].upper()}</h1>
    <p>Aesthetic: {m['style_guide']['vibe']}</p>
    <hr>
    <h3>Download Your Assets:</h3>
    <ul>
        <li><a href="Alpha_Strategy_Playbook.pdf" class="btn">Download Playbook</a></li>
        <li><a href="Alpha_Stack_Suggestions.pdf" class="btn">Download Tech Stack</a></li>
    </ul>
</body>
</html>
"""
with open('index.html', 'w') as f:
    f.write(html)
