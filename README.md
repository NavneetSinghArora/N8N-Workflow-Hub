# n8n Automation Stack

A streamlined, self-hosted n8n automation environment with PostgreSQL.

## Structure

```text
.
├── docker-compose.yml    # Single stack for n8n + Postgres
├── Taskfile.yml          # Easy management commands
├── .env.template         # Environment variable template
├── workflows/            # Version-controlled, sanitized workflows (JSON)
├── local-files/          # Files accessible to n8n workflows
├── scripts/              # Internal maintenance scripts
└── README.md
```

## Quick Start

1. **Setup**: Initialize your environment file.
   ```bash
   task setup
   ```
2. **Start**: Launch the stack.
   ```bash
   task up
   ```
3. **Access**: Open [http://localhost:5678](http://localhost:5678) to set up your owner account.

## Management Commands

| Command | Description |
| :--- | :--- |
| `task up` | Start n8n and Postgres |
| `task down` | Stop all services |
| `task logs` | Follow container logs |
| `task status` | Check service health |
| `task export` | Export and sanitize workflows (for Git sharing) |
| `task import` | Import workflows from `/workflows` |

## Sharing & Version Control

This repository is designed to be shared. Workflows in the `workflows/` directory are automatically:
*   **Named by Title**: Files use the workflow name (e.g., `My_Project.json`) instead of random IDs.
*   **Sanitized**: Personal names (like "Navneet") are replaced with "User" to keep them anonymous.
*   **Portable**: Workflow IDs are removed so they can be cleanly imported into any other n8n instance.

### To share your work:
1. Run `task export`.
2. Commit the new `.json` files in `workflows/` to your repository.

### To use shared workflows:
1. Add `.json` files to the `workflows/` folder.
2. Run `task import`.
