from setuptools import setup, find_packages
setup(
    name="omics-agent",
    version="0.2.0",
    description="OmicsAgent.ai — The complete multi-omics AI agent for bioinformatics",
    author="Madhu Sudhana Saddala",
    url="https://github.com/madhubioinformatics/OmicsAgent",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "anthropic>=0.40.0",
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "scipy>=1.11.0",
        "scikit-learn>=1.3.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "pyyaml>=6.0",
        "python-dotenv>=1.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
)
