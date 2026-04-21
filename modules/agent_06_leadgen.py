import json

class LeadGen:
    def synthesize(self):
        with open('style_manifest.json', 'r') as f:
            manifest = json.load(f)
        
        niche = manifest['niche']
        stack = manifest['stack']
        
        content = f"# {niche.upper()} ALPHA DIAGNOSTIC\n\n## Technical Audit\n"
        for tech in stack:
            content += f"- [ ] Is your {tech} environment optimized?\n"
            
        filename = f"{manifest['bundle_id']}_diagnostic.md"
        with open(filename, 'w') as f:
            f.write(content)
        print(f"📡 [LEAD GEN] Dynamic Diagnostic locked: {filename}")

if __name__ == "__main__":
    LeadGen().synthesize()
