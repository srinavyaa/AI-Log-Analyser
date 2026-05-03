# AI Log Analyzer

## Overview
AI Log Analyzer is a real-time log monitoring system that generates logs, analyzes them using machine learning, detects anomalies, and visualizes results through a dashboard.

## Features
- Real-time log generation
- Log analysis
- Feature extraction
- AI anomaly detection
- Separate anomaly logging
- Dashboard visualization
- Pie chart analytics

## Tech Stack
- Python
- scikit-learn
- Streamlit
- Matplotlib

## Project Structure

```bash
log_generator.py
log_analyzer.py
dashboard.py
app.log
anomalies.log
README.md
```

## Workflow

```bash
Log Generator
→ app.log
→ Log Analyzer
→ AI Model
→ anomalies.log
→ Dashboard
```

## Machine Learning
Model used:
- Isolation Forest

Feature extraction:
- INFO → 1
- WARNING → 2
- ERROR → 3

## Run Project

### Start log generator
python log_generator.py

### Start analyzer
python log_analyzer.py

### Start dashboard
python -m streamlit run dashboard.py