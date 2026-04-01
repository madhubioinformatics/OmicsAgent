#!/bin/bash
# ════════════════════════════════════════════════════════════════
#  OmicsAgent.ai — Push to GitHub
#  Run this script from inside the omics-agent/ directory
#  Requirements: git, GitHub account madhubioinformatics
# ════════════════════════════════════════════════════════════════
set -euo pipefail

echo ""
echo "🧬  OmicsAgent.ai — GitHub Push Script"
echo "════════════════════════════════════════"
echo ""

# ── Step 1: Verify we are in the right directory ──────────────────
if [ ! -f "omics_agent.py" ]; then
  echo "ERROR: Run this script from inside the omics-agent/ directory."
  exit 1
fi

# ── Step 2: Run tests to confirm everything passes ────────────────
echo "▶  Running tests..."
python3 tests/run_tests.py
echo ""

# ── Step 3: Set remote ────────────────────────────────────────────
REMOTE_URL="https://github.com/madhubioinformatics/omics-agent.git"
echo "▶  Setting remote → $REMOTE_URL"
git remote remove origin 2>/dev/null || true
git remote add origin "$REMOTE_URL"

# ── Step 4: Push ──────────────────────────────────────────────────
echo "▶  Pushing all 6 commits to GitHub..."
git push -u origin main

echo ""
echo "════════════════════════════════════════"
echo "✓  Pushed successfully!"
echo ""
echo "Next steps:"
echo "  1. Go to: https://github.com/madhubioinformatics/omics-agent"
echo "  2. Settings → Pages → Source: main branch / /docs folder"
echo "  3. Your site will be live at:"
echo "     https://madhubioinformatics.github.io/omics-agent/"
echo ""
echo "Tip: Add the emblem as your repo social preview:"
echo "  Settings → Social preview → Upload docs/assets/omicsagent-emblem.svg"
echo "════════════════════════════════════════"
