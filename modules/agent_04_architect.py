import json

class Architect:
    def conceptualize(self):
        with open('current_bundle_dna.json', 'r') as f:
            dna = json.load(f)
        
        # Dynamic style mapping
        style_library = {
            "SaaS Boilerplate Bundles": {"color": "#5D5FEF", "vibe": "Deep Cobalt Stealth"},
            "High-Ticket AI Automation": {"color": "#00FF41", "vibe": "Matrix Green Cyber"},
            "Solar Automation": {"color": "#FF8C00", "vibe": "Amber Energy"}
        }
        
        style = style_library.get(dna['niche'], {"color": "#00FFFF", "vibe": "Neon-Noir"})
        
        # KEY FIX: Using 'stack_recommendations' to match Ghostwriter's requirements
        manifest = {
            **dna,
            "style_guide": style,
            "stack_recommendations": ["Python 3.11", "Termux", "GitHub CLI", "OpenAI API"]
        }
        
        with open('style_manifest.json', 'w') as f:
            json.dump(manifest, f, indent=4)
        print(f"✅ [ARCHITECT] Manifest locked and harmonized for {dna['niche']}")

if __name__ == "__main__":
    Architect().conceptualize()
