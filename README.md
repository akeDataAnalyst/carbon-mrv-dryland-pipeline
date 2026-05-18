# Dryland Carbon MRV Pipeline & Biomass Accounting Engine
[![Live Demo](https://img.shields.io/badge/Streamlit-Live%20Demo-brightgreen)](https://carbon-mrv-dryland-pipeline-ezeohkspcdrkeugzfhpbh9.streamlit.app/)


A professional MRV tool developed for high-integrity community carbon projects under Verra VM0047 ARR methodology

### Project Overview
This project demonstrates a complete, production-ready Carbon Measurement, Reporting, and Verification (MRV) pipeline tailored for dryland restoration projects in Ethiopia. 

---

### Problem
Community-led forest monitoring in drylands often suffers from:
- Inconsistent and error-prone field data (missing values, outliers, coordinate errors)
- Lack of standardized QA/QC processes
- Non-reproducible biomass and carbon calculations
- Weak integration between field data and MRV requirements
- Difficulty generating credible reports for Verra VM0047 verification

### Solution
An end-to-end automated pipeline that:
- Ingests raw community forest inventory data
- Performs rigorous, auditable QA/QC with clear flagging
- Applies dryland-appropriate allometric equations (Acacia-Commiphora group)
- Calculates Above Ground Biomass (AGB), Carbon stock, and CO2e
- Generates professional MRV-ready reports and visualizations
- Provides an interactive Streamlit dashboard for project teams

### Key Features
- Realistic field data with injected errors (real-world simulation)
- Comprehensive QA/QC system with detailed reporting
- Transparent biomass & carbon calculations
- Plot-level and project-level summaries
- Professional Excel + CSV exports
- Interactive Streamlit Dashboard
- Full audit trail and metadata

### Tech Stack
- **Python** 3.10+
- **Pandas** & NumPy – Data processing
- **Plotly** – Interactive visualizations
- **Streamlit** – Interactive dashboard
- **OpenPyXL** – Excel reporting
- **python-dotenv** – Configuration management
- **Pathlib** – Clean file handling
