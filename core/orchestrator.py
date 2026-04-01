"""
OmicsAgent Orchestrator — routes natural language to the correct omics skill.
"""
import os
from typing import Optional

SKILL_REGISTRY = {
    "genomics":           ["wgs","wes","snp","vcf","variant","gatk","bcftools","plink"],
    "transcriptomics":    ["rna-seq","rnaseq","deseq","bulk rna","differential expression"],
    "scrna":              ["scrna","single cell","single-cell","scanpy","seurat","umap","clustering"],
    "proteomics":         ["proteomics","mass spec","maxquant","dia-nn","protein"],
    "metabolomics":       ["metabolomics","metabolite","xcms","mzmine","gc-ms"],
    "epigenomics":        ["atac","chip","chromatin","macs","deeptools","histone"],
    "spatial":            ["spatial","visium","squidpy","spatialDE"],
    "metagenomics":       ["metagenomics","kraken","metaphlan","microbiome","16s"],
    "sc_proteomics":      ["cite-seq","cite seq","adt","surface protein"],
    "integration":        ["integrat","multi-omics","mofa","diablo","wnn"],
    "scatac":             ["scatac","sc-atac","single-cell atac","chromvar","lsi"],
    "bulk_epigenomics":   ["bulk atac","chip-seq","h3k27ac","h3k4me3","diffbind"],
    "spatial_full":       ["merfish","cosmx","stereo-seq","rctd","cellchat"],
    "scTCR_BCR":          ["tcr","bcr","clonotype","repertoire","vdj","cdr3"],
    "sc_proteomics_full": ["scope-ms","scope ms","single cell proteomics","intracellular"],
}

def route_intent(prompt: str) -> list:
    prompt_lower = prompt.lower()
    matched = [skill for skill, keywords in SKILL_REGISTRY.items()
               if any(kw in prompt_lower for kw in keywords)]
    return matched if matched else ["transcriptomics"]

class OmicsOrchestrator:
    def __init__(self, api_key: Optional[str] = None, mock: bool = False):
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY", "")
        self.mock = mock or not self.api_key
        self.conversation_history = []

    def chat(self, user_message: str) -> dict:
        skills = route_intent(user_message)
        self.conversation_history.append({"role": "user", "content": user_message})
        if self.mock:
            response = (
                f"[MOCK MODE — set ANTHROPIC_API_KEY for real responses]\n\n"
                f"Skills routed: {', '.join(skills)}\n"
                f"I would analyze: '{user_message[:80]}'\n\n"
                f"Steps: 1. Validate data  2. Run QC  3. Execute pipeline  "
                f"4. Generate figures  5. Produce reproducibility bundle"
            )
        else:
            try:
                import anthropic
                client = anthropic.Anthropic(api_key=self.api_key)
                msg = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=2048,
                    system="You are OmicsAgent.ai, an expert multi-omics bioinformatics AI agent.",
                    messages=self.conversation_history
                )
                response = msg.content[0].text
            except Exception as e:
                response = f"API error: {e}"
        self.conversation_history.append({"role": "assistant", "content": response})
        return {"response": response, "skills_used": skills, "mock": self.mock}

    def reset(self):
        self.conversation_history = []
