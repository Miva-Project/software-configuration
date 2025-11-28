# 🛠️ Software Configuration Management & Maintenance (SCMM) Lab

## 📌 Overview
> This repository contains the full lab assessment package for the **401-Level Software Configuration Management & Maintenance (SCMM)** course.  
> The project demonstrates real-world SCM and software maintenance practices using modern tools such as **Git, GitHub, VS Code, Docker, and GitHub Projects**.


**Course Title:** Software Configuration Management & Maintenance (SCMM)

**Course Code:** SEN 401


Lab involves managing a complete software lifecycle including:
- Version control
- Branching and baselines
- Maintenance activities
- Status accounting
- Auditing
- System re-engineering
- Software migration & upgrades

---

## 📂 Project Structure

```
software-configuration/
├── README.md
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml
├── .vscode/
│   └── settings.json
├── Dockerfile
├── docker-compose.yml
├── src/
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── test_main.py
│   └── test_utils.py
└── .gitattributes
```

---

## 🚀 Labs & Tasks

### Lab 1 – SCM Setup & Baseline Creation
- Create GitHub repository (private, with group members added).
- Branch setup: `main`, `dev`, `feature/*`, `main/*`.
- Upload starter code and tag release `v1.0`.
- Deliverables: GitHub repo link, PDF report with screenshots, functional Python files.

### Lab 2 – Software Maintenance Tasks
- **Corrective:** Fix bugs in `students.py` (e.g., empty list handling).
- **Adaptive:** Update for Python 3.12 compatibility, add new feature (e.g., Pydantic validation).
- **Perfective:** Improve readability, usability, and add statistics (median score).
- **Preventive:** Refactor for modularity, add comments/docstrings.
- **Deliverables:** Updated `students.py`, commit history screenshots, PDF report, repo link.

### Lab 3 – Status Accounting & Auditing
- Track and document all changes using Git.
- Create `inventory.py` and update `app.py` accordingly.
- Generate Git change logs and perform configuration status accounting.
- Deliverables: Updated repo, changelog.txt, PDF report with screenshots.

### Lab 4 – Re-engineering & Migration
- Reverse engineer existing codebase, refactor into modular components.
- Migrate data/API (e.g., SQLite or FastAPI).
- Deploy with Docker Compose.
- Deliverables: Refactored codebase, UML diagrams, Docker setup, PDF report.

---

## 🛠️ Tools Required
- Git & GitHub
- VS Code
- Docker Desktop
- GitHub Projects / Issue Tracker
- Markdown (.md)
- PDF Export Tool
- (Optional tool) GitHub Actions CI/CD

---

## 📖 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Miva-Project/software-configuration.git
   cd software-configuration
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```


## 👥 Contributors

1. Praises Tula (praises,musa@miva.edu.ng)
2. 
