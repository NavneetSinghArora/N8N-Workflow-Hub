# 🧩 Workflows Catalog

This directory contains version-controlled, human-readable JSON exports of the n8n workflows managed by this stack. Below is a detailed breakdown of each workflow's purpose, logic, and configuration requirements.

---

## 1. Job Search & Analysis (`Job-Search.json`)

A high-performance automated pipeline designed to find and qualify job opportunities based on your professional profile.

### 🚀 Logic Flow
1.  **Resume Extraction**: Reads your local resume (`User-Resume.pdf`) from the mapped storage.
2.  **Search Query Generation**: Uses **Google Gemini** to analyze your resume and generate a highly targeted search query.
3.  **Live Job Search**: Queries the **JSearch API (RapidAPI)** to find the latest job postings (filtered by date and location).
4.  **Deduplication**: Checks your **Notion Database** to ensure the job hasn't already been processed.
5.  **AI Analysis**: For new jobs, Gemini performs a deep-dive comparison between the job description and your specific skills.
6.  **Scoring**: Calculates a `Relevance Score` (1-100) and `Skill Match Score` (1-100).
7.  **Delivery**: Creates a detailed entry in Notion with salary info, remote status, and a summarized "Why this matches" explanation.

### ⚙️ Requirements
- **Google Gemini API**: For document analysis.
- **RapidAPI (JSearch)**: For live job data.
- **Notion**: A database with specific properties (Job Title, Company, URL, etc.).

---

## 2. Resume Analyser (`Resume-Analyser.json`)

A modular helper workflow designed for text extraction and classification.

### 🚀 Logic Flow
1.  **Trigger**: Designed to be called as a sub-workflow or triggered with passthrough data.
2.  **Parsing**: Extracts raw text from PDF documents.
3.  **Entity Recognition**: Uses LLMs to identify key professional entities (current title, core tech stack).
4.  **Output**: Returns a structured JSON object containing the extracted text and classified metadata for use in other workflows.

### ⚙️ Requirements
- **Google Gemini API**: For semantic analysis.

---

## 🛠 How to Use These Workflows

1.  **Configuration**: Ensure your `.env` file contains the necessary API keys (`N8N_ENCRYPTION_KEY`, etc.).
2.  **Import**: Run `task import` from the project root to load these into your local n8n instance.
3.  **Credentials**: Once imported, you will need to set up your credentials for Notion, Gemini, and RapidAPI within the n8n UI.
