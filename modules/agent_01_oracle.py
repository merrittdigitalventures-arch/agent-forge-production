import json

class Oracle:
    def __init__(self, target_niche=None):
        # In production, this pulls from a headless scraper
        self.niche = target_niche or "SaaS Boilerplate Bundles"

    def lock_dna(self):
        dna = {
            "niche": self.niche,
            "bundle_id": self.niche.lower().replace(" ", "_"),
            "logos": {"primary": "merritt_digital_white.png", "icon": "m_icon_cyan.png"}
        }
        with open('current_bundle_dna.json', 'w') as f:
            json.dump(dna, f, indent=4)
        print(f"📦 [ORACLE] DNA Locked: {self.niche}")

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else None
    Oracle(target).lock_dna()
