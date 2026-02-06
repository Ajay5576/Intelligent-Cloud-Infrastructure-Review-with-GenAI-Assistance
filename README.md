# GenAI Cloud Security Analyzer 🔐☁️

## Overview
The GenAI Cloud Security Analyzer is a Python-based tool designed to review cloud infrastructure configurations and identify potential security risks.

This project uses Generative AI to provide advisory recommendations for detected vulnerabilities, helping organizations improve their cloud security posture.

---

## Features
- Reviews EC2, S3, and IAM configurations
- Detects risky cloud patterns
- Uses GenAI to explain risks
- Suggests remediation steps
- Generates a security review report

---

## Project Structure

```
genai-cloud-security-analyzer/
│
├── analyzer.py
├── requirements.txt
└── configs/
     ├── ec2.json
     ├── s3.json
     └── iam.json
```

---

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/your-username/genai-cloud-security-analyzer.git
cd genai-cloud-security-analyzer
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Set OpenAI API Key

Linux / Mac:
```
export OPENAI_API_KEY="your-api-key"
```

Windows:
```
setx OPENAI_API_KEY "your-api-key"
```

---

### 4. Run the Analyzer

```
python analyzer.py
```

---

## Sample Output
The tool scans configuration files and generates a cloud security review report with AI-driven recommendations.

---

## Technologies Used
- Python
- Amazon EC2 (Deployment)
- Generative AI
- JSON Configuration Analysis

---

## Learning Outcomes
- Cloud security fundamentals
- Infrastructure risk analysis
- Generative AI integration
- AWS environment setup
- Python automation

---

## Disclaimer
This project is for educational purposes only.  
Do not use real production credentials or sensitive data.

---
"# Intelligent-Cloud-Infrastructure-Review-with-GenAI-Assistance" 
