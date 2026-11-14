# Programming for AI — Coursework (2026)

**Student:** Shan (SAP 72387)  
**Program:** BS Artificial Intelligence — Section AI/3-1  
**University:** Riphah International University, Islamabad  
**Course:** Programming for AI (Python)

This repository contains the original Python lab tasks, notebooks, supporting data, reports and two assignments from the supplied coursework folder. Environment packages, IDE settings and generated Python bytecode are intentionally excluded.

## Lab index

| Week | Included material |
| --- | --- |
| [01](week01/) | Python introduction, inputs, calculations and Jupyter notebook |
| [02](week02/) | Conditional statements, loops and debugging |
| [03](week03/) | Functions, modules, exceptions and testing |
| [04](week04/) | Python OOP, student storage and experiment tracking |
| [05](week05/) | NumPy arrays and vectorization |
| [06](week06/) | Pandas cleaning, raw/processed CSVs and notebook |
| [07](week07/) | Matplotlib charts, figures and notebook |
| [09](week09/) | Introductory machine learning (decision tree) |
| [10](week10/) | Spambase classification comparison and evaluation |
| [11](week11/) | Concrete-strength regression, diagnostics and reports |

**Not present in the uploaded ZIP:** Week 08 and Week 12. These have **not** been invented or replaced with content from other sources.

## Assignments

- [Assignment 01 — Student Support Rule Engine](assignments/assignment-01/)
- [Assignment 02 — Patient Dataset Audit Toolkit](assignments/assignment-02/)

## Python setup

Use a compatible Python 3 installation and create a new virtual environment locally:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use notebooks with the selected environment in VS Code or Jupyter. For some labs the **working directory matters**: Week 06 notebook uses relative paths and should be opened/run with `week06/` as its working directory; Week 11 notebook expects the repository root as its working directory.

Example commands from repository root:

```powershell
python week01/01_hello.py
python week09/ml_pipeline.py
python week10/compare_classifiers.py
python assignments/assignment-01/test_support_engine.py
python assignments/assignment-02/test_patient_dataset.py
```

The saved model files (`.joblib`) are educational artifacts. **Do not load untrusted serialized models.** The outputs were preserved from the original coursework, not freshly re-trained during this organization.

## Semester project

**AcadInsight — Smart Student Performance Analyzer** is intentionally kept **outside the labs repository**. The original complete project is packaged separately with its Python code, HTML/CSS/JS, test files, proposal, report, viva guide and presentation. Intended project repository: `ShanShahidAI/acadinsight-pfai` (create separately).

## Preservation

This repository-ready structure was produced from `72387_PFAI.zip`. All original coursework source bytes are preserved except where a small documentation link was updated to reflect the new assignment folder path. The Week 11 nested folder was flattened so the existing notebook paths match `week11/data` and `week11/reports`. A full source-to-target SHA256 inventory is supplied in `SOURCE_MANIFEST.csv`.

[GitHub profile](https://github.com/ShanShahidAI)
