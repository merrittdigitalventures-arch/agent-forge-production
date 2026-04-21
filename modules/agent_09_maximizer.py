import json

class ProfitMaximizer:
    def lock_upsell(self):
        with open('style_manifest.json', 'r') as f:
            manifest = json.load(f)
            
        upsell = {
            "niche": manifest['niche'],
            "offer": "1-on-1 Automation Architecture Session",
            "price": "$497",
            "link": "https://merrittdv.gumroad.com/l/executive-consult"
        }
        
        with open('active_upsell.json', 'w') as f:
            json.dump(upsell, f, indent=4)
        print(f"💎 [MAXIMIZER] Strategic Upsell Locked: {upsell['offer']}")

if __name__ == "__main__":
    ProfitMaximizer().lock_upsell()
