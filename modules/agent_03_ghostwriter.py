import json
import os

class Ghostwriter:
    def __init__(self):
        self.manifest_path = 'style_manifest.json'

    def load_manifest(self):
        with open(self.manifest_path, 'r') as f:
            return json.load(f)

    def synthesize_epubs(self, manifest):
        niche = manifest['niche']
        vibe = manifest['style_guide']['vibe']
        stack = manifest['stack_recommendations']
        
        print(f"✍️ [GHOSTWRITER] Synthesizing {niche} content with a {vibe} tone...")

        # 1. Alpha Playbook Synthesis
        playbook_content = f"# {niche}: The Alpha Playbook\n\n## Strategy\nHigh-yield automation for {niche}..."
        with open('alpha_playbook.md', 'w') as f:
            f.write(playbook_content)
        print("📗 [PLAYBOOK] Alpha Playbook structure generated.")

        # 2. AI Prompt Pack Synthesis
        prompt_content = f"# {niche}: AI Prompt Pack\n\n## System Prompts\nAdvanced LLM instructions for {niche}..."
        with open('prompt_pack.md', 'w') as f:
            f.write(prompt_content)
        print("📗 [PROMPTS] AI Prompt Pack synthesized.")

        # 3. Stack Suggestions Synthesis
        stack_content = f"# {niche}: High-Tier Tech Stack\n\n## Recommended Infrastructure\n" + "\n".join([f"* {item}" for item in stack])
        with open('stack_suggestions.md', 'w') as f:
            f.write(stack_content)
        print("📗 [STACK] Technical Stack Suggestions locked.")

if __name__ == "__main__":
    if not os.path.exists('style_manifest.json'):
        print("❌ [ERROR] Style manifest missing.")
    else:
        writer = Ghostwriter()
        manifest = writer.load_manifest()
        writer.synthesize_epubs(manifest)
