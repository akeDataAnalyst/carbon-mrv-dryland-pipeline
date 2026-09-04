# Dryland Carbon MRV Pipeline & Biomass Accounting Engine

A data pipeline for biomass and carbon accounting in community-led dryland restoration projects, aligned with the Verra VM0047 ARR methodology.

[![Live Demo](https://img.shields.io/badge/Streamlit-Live%20Demo-brightgreen)](https://carbon-mrv-dryland-pipeline-ezeohkspcdrkeugzfhpbh9.streamlit.app/)

### Project Overview

This project demonstrates an end-to-end Measurement, Reporting, and Verification (MRV) pipeline for dryland restoration projects in Ethiopia, covering field-data quality control, biomass estimation, carbon accounting, and reporting.

---

### Problem

Community-led forest monitoring in drylands can face challenges such as:

* Inconsistent field data, including missing values, outliers, and coordinate errors
* Lack of standardized QA/QC processes
* Non-reproducible biomass and carbon calculations
* Weak integration between field data and MRV requirements
* Difficulty preparing consistent documentation for carbon project verification

### Solution

An automated pipeline that:

* Ingests community forest inventory data
* Performs QA/QC with clear data-quality flags
* Applies dryland-appropriate allometric equations for the Acacia-Commiphora group
* Calculates Above-Ground Biomass (AGB), carbon stocks, and CO₂e
* Generates reports and visualizations
* Provides an interactive Streamlit dashboard for project teams

### Key Features

* Simulated field data with intentionally introduced errors
* Automated QA/QC and data-quality reporting
* Transparent biomass and carbon calculations
* Plot-level and project-level summaries
* Excel and CSV exports
* Interactive Streamlit dashboard
* Audit trail and metadata tracking

### Tech Stack

* **Python 3.10+** – Pipeline development
* **Pandas & NumPy** – Data processing and calculations
* **Plotly** – Interactive visualizations
* **Streamlit** – Dashboard development
* **OpenPyXL** – Excel reporting
* **python-dotenv** – Configuration management
* **Pathlib** – File and directory handling

---

## Developed by

**Aklilu Abera** | **Data Analyst**
