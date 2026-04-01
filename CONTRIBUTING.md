# Contributing to OmicsAgent.ai

## Adding a New Skill

1. Create `skills/<your_skill>/`
2. Add `SKILL.md` with: Purpose, Input Formats, Pipeline Steps, Key Thresholds, Tools, Output
3. Add `run.py` with a `run(output_dir, demo=True)` function
4. Add `__init__.py` (empty file)
5. Register in `omics_agent.py` (SKILL_NAMES and SKILL_LABELS)
6. Register routing keywords in `core/orchestrator.py`
7. Run tests and submit PR

## Code Style
- Python 3.10+
- matplotlib.use("Agg") at top of every skill
- All random seeds fixed for reproducibility
- Every skill must run with demo=True and no internet access

## Contact
Dr. Madhu Sudhana Saddala
madhubioinformatics@gmail.com
