# 🧬 OmicsAgent.ai

<p align="center">
  <img src="docs/assets/omicsagent-emblem.svg" width="420" alt="OmicsAgent.ai emblem"/>
</p>

<p align="center">
  <strong>The complete multi-omics AI agent for bioinformatics</strong><br>
  Built on the Claude API · Local-first · Reproducible · MIT licensed
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue?logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/license-MIT-green"/>
  <img src="https://img.shields.io/badge/omics_skills-15-orange"/>
  <img src="https://img.shields.io/badge/tests-37%2F37-brightgreen"/>
</p>

<p align="center">
  <a href="https://madhubioinformatics.github.io/OmicsAgent/demo.html">
    <img src="https://img.shields.io/badge/Live_Demo-Click_to_Run-22d3ee?style=for-the-badge&logo=github"/>
  </a>
</p>

---

## 🎮 Interactive Demo

**[▶ Click here to run the live pipeline demo](https://madhubioinformatics.github.io/OmicsAgent/demo.html)**

Simulate all 15 omics skills running on PBMC data — watch the pipeline execute in real time, explore chat mode examples, and preview output file structures.

---

## 15 Omics Skills

| # | Skill | Data Type | Key Tools |
|---|---|---|---|
| 1 | Genomics | WGS/WES/SNP | GATK, bcftools, plink |
| 2 | Transcriptomics | Bulk RNA-seq | DESeq2, salmon |
| 3 | scRNA-seq | Single-cell RNA | Scanpy, Seurat |
| 4 | Proteomics | Mass spec | MaxQuant, DIA-NN |
| 5 | Metabolomics | LC-MS/GC-MS | XCMS, MZmine |
| 6 | Bulk Epigenomics | ATAC + ChIP-seq | MACS3, deepTools |
| 7 | Spatial v1 | Visium | Squidpy, SpatialDE |
| 8 | Metagenomics | Shotgun/16S | MetaPhlAn, Kraken2 |
| 9 | sc-Proteomics | CITE-seq | Seurat WNN |
| 10 | Integration | Multi-omics | MOFA+, DIABLO |
| 11 | **scATAC-seq** | Single-cell ATAC | ArchR, ChromVAR |
| 12 | **Bulk Epigenomics Full** | 6 histone marks | deepTools, DiffBind |
| 13 | **Spatial Full** | Visium/MERFISH/CosMx/Stereo-seq | Squidpy, RCTD |
| 14 | **scTCR/BCR-seq** | Immune repertoire | Scirpy, IgBlast |
| 15 | **sc-Proteomics Full** | CITE-seq + SCoPE-MS | Seurat, limma |

---

## Quick Start
```bash
git clone https://github.com/madhubioinformatics/OmicsAgent
cd OmicsAgent
pip install -r requirements.txt
export ANTHROPIC_API_KEY="sk-ant-..."
python3 omics_agent.py --demo
```

## Usage
```bash
python3 omics_agent.py --demo          # run all 15 skills
python3 omics_agent.py --chat          # interactive chat mode
python3 omics_agent.py --skill scrna   # run one skill
python3 omics_agent.py --list          # list all skills
```

## Documentation

📖 **Website:** https://madhubioinformatics.github.io/OmicsAgent/
🎮 **Live Demo:** https://madhubioinformatics.github.io/OmicsAgent/demo.html

## Author

**Dr. Madhu Sudhana Saddala**
Bioinformatics Specialist, University of California, USA
🔗 https://www.researchgate.net/profile/Dr_Madhu_Sudhana_Saddala

## License

MIT — open source, free, reproducible.

---

## 🔁 Provenance & Reproducibility

Every OmicsAgent.ai analysis ships with a **reproducibility bundle** — not as an afterthought, but as a core output:
```
output/scrna_report/
├── report.md              # Full analysis with figures and interpretation
├── figures/               # Publication-quality PNGs (120 DPI)
├── tables/                # CSV data tables (markers, DE results, etc.)
├── commands.sh            # Exact commands to reproduce the analysis
├── environment.yml        # Conda environment snapshot (all versions pinned)
└── checksums.sha256       # SHA-256 hash of every input and output file
```

**Why this matters:**
- A **reviewer** can re-run your analysis in 30 seconds
- A **collaborator** can reproduce your Figure 3 without emailing you
- **Future-you** can regenerate results two years later from the same bundle
- A **journal** can verify your analysis was not modified after submission

### Verify any result instantly
```bash
# Re-run exact analysis
bash output/scrna_report/commands.sh

# Restore exact conda environment
conda env create -f output/scrna_report/environment.yml

# Verify all outputs are bit-identical
sha256sum -c output/scrna_report/checksums.sha256

# Expected:
# figures/umap.png: OK
# figures/scrna_dotplot.png: OK
# tables/markers.csv: OK
# report.md: OK
```

### All random seeds are fixed

Every skill fixes all random seeds before execution:
```python
np.random.seed(42)      # NumPy
random.seed(42)          # Python random
# Scanpy/Seurat: random_state=42 passed to every stochastic function
```

This guarantees **deterministic results** across machines, operating systems, and time — as long as the same conda environment is used.

### Bundle contents by skill

| Skill | Figures | Tables | Report |
|---|---|---|---|
| scRNA-seq | UMAP, QC, dot plot, composition | markers.csv | Full cell type analysis |
| scATAC-seq | UMAP, ChromVAR heatmap, TSS profile, volcano | da_peaks.csv | TF deviation analysis |
| Spatial Full | Platform QC, SVG maps, deconvolution | svg_genes.csv | 4-platform spatial report |
| scTCR/BCR | Clonal expansion, V-gene usage, CDR3 | clonotypes.csv | Repertoire diversity report |
| Proteomics | Volcano, heatmap, STRING network | de_proteins.csv | DE protein analysis |
| Metabolomics | PCA, volcano, pathway | de_metabolites.csv | Metabolic signature report |
| Integration | MOFA+ factors, cross-omics corr | mofa_factors.csv | Multi-omics factor report |
| + 8 more | 50+ total figures | 27+ total tables | 15 reports |

> OmicsAgent.ai reproducibility design is inspired by [ClawBio](https://github.com/ClawBio/ClawBio) — the open bioinformatics AI agent skill library.
