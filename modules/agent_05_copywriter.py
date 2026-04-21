import json
import os

class Copywriter:
    def __init__(self):
        self.manifest_path = 'style_manifest.json'

    def load_manifest(self):
        with open(self.manifest_path, 'r') as f:
            return json.load(f)

    def generate_sales_assets(self, manifest):
        niche = manifest['niche']
        vibe = manifest['style_guide']['vibe']
        stack = ", ".join(manifest['stack'])
        bundle_id = manifest['bundle_id']
        
        print(f"📈 [COPYWRITER] Drafting high-conversion assets for {niche}...")

        # 1. Gumroad Sales Copy
        sales_copy = f"""# THE {niche.upper()} ALPHA BUNDLE
## Stop guessing. Start executing with the {vibe} framework.

Your diagnostic revealed gaps. This bundle closes them.
Included in this technical suite:
- **The Alpha Playbook**: Your strategic roadmap for {niche}.
- **The AI Prompt Pack**: Advanced system instructions optimized for your workflow.
- **The Stack Suggestions**: A professional infrastructure featuring {stack}.

### Why this works:
Built for the Cypher Executive, this bundle eliminates the friction of manual deployment.
"""
        with open(f'{bundle_id}_gumroad_copy.txt', 'w') as f:
            f.write(sales_copy)

        # 2. SEO & Web Metadata
        seo_meta = {
            "title": f"Alpha Bundle: {niche} Automation",
            "description": f"Professional-grade {niche} resources and technical stack suggestions for high-yield automation.",
            "keywords": [niche, "automation", "alpha bundle", "merritt digital", "AI prompts"]
        }
        with open(f'{bundle_id}_seo_meta.json', 'w') as f:
            json.dump(seo_meta, f, indent=4)

        print(f"✅ [COPYWRITER] Sales Copy and SEO Metadata locked for {bundle_id}.")

if __name__ == "__main__":
    if not os.path.exists('style_manifest.json'):
        print("❌ [ERROR] Manifest missing. Cannot generate copy.")
    else:
        copy_agent = Copywriter()
        manifest = copy_agent.load_manifest()
        copy_agent.generate_sales_assets(manifest)
