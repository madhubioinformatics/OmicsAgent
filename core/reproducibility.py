import hashlib, datetime, pathlib, os

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def generate_bundle(output_dir, skill_name, commands, conda_deps, report_md, figures, tables):
    output_dir = pathlib.Path(output_dir)
    (output_dir / "figures").mkdir(parents=True, exist_ok=True)
    (output_dir / "tables").mkdir(parents=True, exist_ok=True)
    (output_dir / "report.md").write_text(report_md)
    for fname, content in figures.items():
        fpath = output_dir / "figures" / fname
        if isinstance(content, bytes):
            fpath.write_bytes(content)
        else:
            fpath.write_text(str(content))
    for fname, content in tables.items():
        (output_dir / "tables" / fname).write_text(content)
    ts = datetime.datetime.now().isoformat()
    sh = f"#!/bin/bash\n# OmicsAgent.ai — {skill_name}\n# Generated: {ts}\nset -euo pipefail\n\n"
    sh += "\n".join(commands) + "\n"
    cmd_path = output_dir / "commands.sh"
    cmd_path.write_text(sh)
    os.chmod(cmd_path, 0o755)
    env = f"name: omicsagent-{skill_name}\nchannels:\n  - conda-forge\n  - bioconda\ndependencies:\n  - python>=3.10\n"
    env += "".join(f"  - {d}\n" for d in conda_deps)
    (output_dir / "environment.yml").write_text(env)
    checksums = []
    for fpath in sorted(output_dir.rglob("*")):
        if fpath.is_file() and fpath.name != "checksums.sha256":
            rel = fpath.relative_to(output_dir)
            checksums.append(f"{sha256_file(fpath)}  {rel}")
    (output_dir / "checksums.sha256").write_text("\n".join(checksums) + "\n")
    return output_dir
