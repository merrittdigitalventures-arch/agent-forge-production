import json

class LeadGen:
    def synthesize(self):
        with open('style_manifest.json', 'r') as f:
            manifest = json.load(f)
        
        niche = manifest['niche']
        # KEY FIX: Updated to 'stack_recommendations' to match the Architect's output
        stack = manifest.get('stack_recommendations', ["General Automation Stack"])
        
        content = f"# {niche.upper()} ALPHA DIAGNOSTIC\n\n## Technical Audit\n"
        for tech in stack:
            content += f"- [ ] Is your {tech} environment optimized?\n"
            
        bundle_id = manifest.get('bundle_id', 'niche_bundle')
        filename = f"{bundle_id}_diagnostic.md"
        with open(filename, 'w') as f:
            f.write(content)
        print(f"📡 [LEAD GEN] Dynamic Diagnostic locked: {filename}")

if __name__ == "__main__":
    LeadGen().synthesize()
