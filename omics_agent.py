#!/usr/bin/env python3
"""OmicsAgent.ai — Multi-omics AI agent powered by Claude API."""
import argparse, sys, pathlib, importlib

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT))
from core.orchestrator import OmicsOrchestrator, route_intent

SKILL_NAMES = [
    "genomics","transcriptomics","scrna","proteomics","metabolomics",
    "epigenomics","spatial","metagenomics","sc_proteomics","integration",
    "scatac","bulk_epigenomics","spatial_full","scTCR_BCR","sc_proteomics_full",
]
SKILL_LABELS = {
    "genomics":"Genomics (WGS/WES/SNP)",
    "transcriptomics":"Transcriptomics (Bulk RNA-seq)",
    "scrna":"scRNA-seq (Single-cell)",
    "proteomics":"Proteomics (Mass Spec)",
    "metabolomics":"Metabolomics (LC-MS)",
    "epigenomics":"Epigenomics (Bulk ATAC/ChIP-seq)",
    "spatial":"Spatial Transcriptomics (Visium)",
    "metagenomics":"Metagenomics (Shotgun/16S)",
    "sc_proteomics":"sc-Proteomics (CITE-seq)",
    "integration":"Multi-omics Integration (MOFA+)",
    "scatac":"scATAC-seq (ChromVAR / LSI)",
    "bulk_epigenomics":"Bulk Epigenomics (ATAC + ChIP-seq)",
    "spatial_full":"Spatial Transcriptomics (Visium/MERFISH/CosMx/Stereo-seq)",
    "scTCR_BCR":"scTCR/BCR-seq (Immune Repertoire)",
    "sc_proteomics_full":"sc-Proteomics Full (CITE-seq + SCoPE-MS)",
}

def print_banner():
    print("""
╔══════════════════════════════════════════════════════════════╗
║       🧬  OmicsAgent.ai — Multi-Omics AI Agent             ║
║       Built on Claude API  ·  Local-first  ·  MIT           ║
║       github.com/madhubioinformatics/OmicsAgent             ║
╚══════════════════════════════════════════════════════════════╝
""")

def list_skills():
    print_banner()
    print("Available Skills:\n")
    for name, label in SKILL_LABELS.items():
        md = ROOT / "skills" / name / "SKILL.md"
        status = "✓" if md.exists() else "○"
        print(f"  {status}  {name:<22} {label}")

def run_chat(api_key=None):
    print_banner()
    import os
    api_key = api_key or os.environ.get("ANTHROPIC_API_KEY","")
    mock = not api_key
    if mock:
        print("[MOCK MODE] Set ANTHROPIC_API_KEY for real Claude responses.\n")
    else:
        print("[LIVE MODE] Connected to Claude API.\n")
    agent = OmicsOrchestrator(api_key=api_key, mock=mock)
    print("Type your omics analysis request (or 'exit' to quit).\n")
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!"); break
        if not user_input: continue
        if user_input.lower() in ("exit","quit","q"):
            print("Goodbye!"); break
        result = agent.chat(user_input)
        print(f"\n[Skills: {', '.join(result['skills_used'])}]\n")
        print(f"Agent: {result['response']}\n")

def main():
    parser = argparse.ArgumentParser(description="OmicsAgent.ai — Multi-omics AI agent")
    parser.add_argument("--demo",   action="store_true", help="Run all skills with demo data")
    parser.add_argument("--chat",   action="store_true", help="Interactive chat mode")
    parser.add_argument("--skill",  type=str,            help="Run a single skill by name")
    parser.add_argument("--list",   action="store_true", help="List all available skills")
    parser.add_argument("--output", type=str, default="output", help="Output directory")
    parser.add_argument("--api-key",type=str, default=None, help="Anthropic API key")
    args = parser.parse_args()

    if args.list:
        list_skills()
    elif args.chat:
        run_chat(api_key=args.api_key)
    elif args.skill:
        if args.skill not in SKILL_NAMES:
            print(f"Unknown skill '{args.skill}'. Use --list to see available skills.")
            sys.exit(1)
        print(f"Running skill: {args.skill}")
        print("Note: Add skill run.py files to skills/ folder to execute analyses.")
    elif args.demo:
        print_banner()
        print("OmicsAgent.ai — 15 omics skills ready.")
        print("Add your ANTHROPIC_API_KEY and skill run.py files to execute analyses.")
        list_skills()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
