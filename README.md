# N8N Workflow Hub

[![n8n](https://img.shields.io/badge/n8n-Workflow_Automation-FF6D5A?logo=n8n&logoColor=white)](https://n8n.io/)
[![Docker](https://img.shields.io/badge/Docker-Orchestrated-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Task](https://img.shields.io/badge/Task-Managed-2CFB6D?logo=task&logoColor=white)](https://taskfile.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A professional-grade, self-hosted n8n automation infrastructure designed for reliability, portability, and version control. This stack moves beyond simple automation by implementing a "Git-First" workflow management system, allowing you to track, sanitize, and share your automation logic like code.

---

## 🚀 Key Features

- **Production-Ready Persistence**: Powered by PostgreSQL 16 for robust data integrity and performance compared to default SQLite setups.
- **Git-First Workflow Sync**: Automated pipelines to export workflows from the database into human-readable, version-controlled JSON files.
- **Automated Sanitization**: Built-in scripts to strip sensitive personal data and unique IDs, making your workflows instantly portable.
- **Simplified DevOps**: A comprehensive CLI interface via `Taskfile` that manages everything from infrastructure health to complex workflow migrations.
- **Persistent Local Storage**: Dedicated volume mapping for files accessible to n8n workflows, ensuring data persistence across container restarts.

---

## 🧩 Available Workflows

This hub comes pre-configured with professional automation logic:

- **Job Search & Analysis**: Automated pipeline that finds jobs via RapidAPI and uses AI to analyze them against your resume before saving to Notion.
- **Resume Analyser**: A modular helper for extracting entities and insights from PDF resumes.

👉 **View the full [Workflows Catalog](workflows/README.md) for detailed logic, setup, and requirements.**

---

## 🛠 Project Structure

```text
├── local-files/          # Files accessible to n8n workflows (PDFs, CSVs, etc.)
├── workflows/            # Version-controlled, human-readable workflow JSONs
├── agents/               # Gemini CLI agent definitions for autonomous tasks
├── scripts/              # Internal maintenance and sanitization scripts
├── docker-compose.yml    # Unified infrastructure (n8n + Postgres)
├── Taskfile.yml          # DevOps management entry point
├── .env.template         # Standardized environment configuration
└── README.md
```

---

## ⚙️ Installation

### Prerequisites

- [Docker](https://www.docker.com/) & Docker Compose
- [Go Task](https://taskfile.dev/installation/) (recommended for ease of use)

### Required Keys & Credentials

For these workflows to function, you need to configure access to external services directly within the n8n UI:

- **Google Gemini(PaLM) API**: Configure in the **Credentials** tab for AI-powered analysis.
- **Notion API**: Configure in the **Credentials** tab to connect to your workspace.
- **Notion Database ID**: Paste your specific Database ID directly into the Notion node settings.
- **RapidAPI Key**: Provide your `JSearch` API key in the HTTP Request node headers.

### Setup Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/NavneetSinghArora/N8N-Workflow-Hub.git
   cd N8N-Workflow-Hub
   ```

2. **Initialize configuration**:
   ```bash
   task setup
   ```
   *Note: Edit the newly created `.env` file with your specific credentials, API keys, and database IDs.*

3. **Launch the stack**:
   ```bash
   task up
   ```

4. **Access n8n**:
   Navigate to [http://localhost:5678](http://localhost:5678) to complete the owner account setup.

---

## 🎮 Management Commands

The project uses `task` to simplify complex operations. Here are the most common commands:

| Command | Action |
| :--- | :--- |
| `task up` | Start n8n and Postgres services|
| `task down` | Stop and remove containers |
| `task logs` | Follow aggregate logs in real-time |
| `task status` | Check the health of all services |
| `task export` | **Sync DB → Git**: Exports and humanizes all workflows |
| `task sanitise`| **Sanitize for Git**: Strips personal data (target all or `NAME=Name`) |
| `task import` | **Sync Git → DB**: Imports versioned workflows (target all or `NAME=Name`) |

---

## 🔄 Sharing & Version Control

To share your workflows without leaking sensitive info:

1.  **Export**: Run `task export`. This pulls all work from the DB and creates readable files in `workflows/`.
2.  **Sanitize**: Run `task sanitise` (or `task sanitise NAME=Workflow-Name`). This strips personal IDs and emails. **Always run this before committing.**
3.  **Commit**: Add the updated files in the `workflows/` directory to your Git repo.
4.  **Import**: Deploy back to n8n using `task import` (or `task import NAME=Workflow-Name`). Loading version-controlled logic is now a single command.

---

## 👤 Author

**Navneet Singh Arora**
- Email: [aroranavneetsingh.de@gmail.com](mailto:aroranavneetsingh.de@gmail.com)
- Portfolio: [navneetsingharora.com](https://www.navneetsingharora.com/)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


