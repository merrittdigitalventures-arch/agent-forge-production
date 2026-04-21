#!/bin/bash

# Check if a niche was provided
if [ -z "$1" ]; then
    echo "❌ Error: Please provide a niche name."
    echo "Usage: ./deploy_niche.sh 'Solar Automation'"
    exit 1
fi

NICHE=$1

echo "🚀 Starting Production Run for: $NICHE"

# 1. Feed the Oracle
python3 modules/agent_01_oracle.py "$NICHE"

# 2. Re-synthesize Assets (Architect, Ghostwriter, LeadGen)
python3 modules/agent_04_architect.py
python3 modules/agent_03_ghostwriter.py
python3 modules/agent_06_leadgen.py

# 3. Generate New PDF Deliverables
python3 modules/agent_08_pdf_engine.py

# 4. Push Updates to GitHub Production
git add .
git commit -m "🚀 Automated Update: $NICHE Bundle Assets"
git push origin main

echo "✅ Deployment Complete! Your portal is updating at:"
echo "https://merrittdigitalventures-arch.github.io/agent-forge-production/"
