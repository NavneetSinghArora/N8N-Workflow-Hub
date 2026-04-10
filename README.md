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

## 🛠 Project Structure

```text
├── local-files/          # Files accessible to n8n workflows (PDFs, CSVs, etc.)
├── workflows/            # Version-controlled, human-readable workflow JSONs
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
   *Note: Edit the newly created `.env` file with your specific credentials and encryption keys.*

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
| `task export` | **Sync DB → Git**: Exports, humanizes, and sanitizes workflows |
| `task import` | **Sync Git → DB**: Imports versioned workflows into the instance |

---

## 🔄 Sharing & Version Control

To share your workflows without leaking sensitive info:

1.  **Export & Sanitize**: Run `task export`. This will rename files from random IDs (e.g., `12.json`) to their actual names (e.g., `Email_Automator.json`) and replace personal names with placeholders.
2.  **Commit**: Add the updated files in the `workflows/` directory to your Git repo.
3.  **Collaborate**: Other users can simply pull the repo and run `task import` to load the exact same logic into their own local n8n instance.

---

## 👤 Author

**Navneet Singh Arora**
- Email: [aroranavneetsingh.de@gmail.com](mailto:aroranavneetsingh.de@gmail.com)
- Portfolio: [navneetsingharora.com](https://www.navneetsingharora.com/)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


