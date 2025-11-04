# 🕵️ FORENSIS-AI - UFDR Triage MVP

An advanced digital forensics solution leveraging artificial intelligence to analyze Universal Forensic Data Reports (UFDR) through behavioral intelligence, pattern recognition, and automated investigative triage.

## 🎯 Executive Summary

FORENSIS-AI is a sophisticated forensic analysis platform engineered to enable investigators to efficiently triage and examine communication data extracted from UFDR JSON formats. The system integrates vector-based semantic retrieval, behavioral pattern recognition, and AI-driven analytical insights to identify anomalous activities, financial transactions, and communication irregularities.

## ✨ Core Capabilities

### 🔍 Forensic Investigation Tools
- **Intelligent Triage System**: AI-driven examination of UFDR datasets to detect suspicious communications, financial indicators, and atypical behavioral patterns
- **Interactive Query Interface**: Natural language-based search functionality across message corpuses with automated entity recognition
- **Advanced Entity Detection**: Automated identification and annotation of cryptocurrency addresses, telephone numbers, banking information, and monetary values
- **Multilingual Processing**: Automatic language detection and translation services supporting Tamil, Hindi, Bengali, Telugu, and Marathi

### 🧠 Behavioral Analytics Engine
- **Temporal Pattern Recognition**: Detection of irregular messaging behaviors including nocturnal activity (01:00-04:00 hours) and communication volume anomalies
- **Contact Relationship Mapping**: Analysis of contact establishment, relationship deterioration, and interaction frequency variations
- **Dynamic Visualizations**: Temporal timeline representations and network topology graphs for communication pattern analysis
- **AI-Powered Investigation Guidance**: Context-sensitive recommendations for subsequent investigative procedures

### 📊 Documentation & Data Export
- **Professional Report Generation**: Comprehensive PDF forensic reports incorporating findings, metadata analysis, and behavioral assessments
- **Chain of Custody Management**: Complete action tracking with integrity verification protocols
- **Data Exportability**: Formatted result extraction for extended investigation workflows

## 🚀 Implementation Guide

### System Requirements

```bash
Python 3.8 or higher
pip package management system
```

### Deployment Instructions

1. **Repository Acquisition**
```bash
git clone <repository-url>
cd forensis-ai
```

2. **Dependency Installation**
```bash
pip install -r requirements.txt
```

3. **Environment Configuration**
```bash
# Initialize environment configuration file
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

4. **Application Launch**
```bash
streamlit run frontend/app.py
```

Access the application interface at http://localhost:8501

## 📁 Architecture Overview

```
forensis-ai/
├── frontend/
│   ├── app.py                 # Primary Streamlit interface
│   └── chroma_db/            # Vector database persistence
├── backend/
│   ├── ingest.py             # UFDR data processing pipeline
│   └── search_engine.py      # Hybrid retrieval implementation
├── utils/
│   ├── highlighter.py        # Entity annotation & content sanitization
│   ├── pdf_generator.py      # Report compilation module
│   ├── chain_of_custody.py   # Forensic audit logging
│   ├── anomaly_detection.py  # Behavioral analysis algorithms
│   ├── gemini_client.py      # AI integration layer
│   └── translation.py        # Language processing services
├── data/
│   └── sample_ufdr.json      # Demonstration dataset
└── requirements.txt          # Package dependencies
```

## 📖 Operational Workflow

### 1. Data Ingestion
- Select **"Upload UFDR Data"** to import your JSON dataset, or
- Choose **"Load Sample Data"** to explore demonstration capabilities

### 2. Behavioral Analysis Execution
- Initiate **"🔊 Run Behavioral Analysis"** to identify:
  - Nocturnal communication patterns (01:00-04:00 hours)
  - Statistical anomalies in message frequency
  - Contact establishment within 24-hour windows
  - Disruptions in communication patterns
  - Network relationship visualizations

### 3. Forensic Examination
- **Automated Workflow**: Execute **"🔎 Run Automated Forensic Analysis"** for AI-assisted triage
- **Manual Investigation**: Submit natural language queries such as:
  - "Identify cryptocurrency wallet addresses"
  - "Locate anomalous behavioral indicators"
  - "Extract financial transaction references"

### 4. Analysis Review
- Examine annotated entities (cryptocurrency wallets, contact information, monetary values)
- Analyze temporal patterns and relationship networks
- Review AI-generated investigative recommendations

### 5. Report Generation
- Select **"📥 Export to PDF"** to produce comprehensive forensic documentation

## 🔧 Technical Specifications

### UFDR Data Schema

```json
{
  "messages": [
    {
      "message_id": "msg_001",
      "timestamp": "2025-01-15T14:30:00Z",
      "sender": "user@example.com",
      "recipient": "contact@example.com",
      "content": "Message text here",
      "media_path": "optional/path/to/media.jpg"
    }
  ],
  "chain_of_custody": [],
  "media_analysis": [],
  "evidence_highlights": [],
  "manifest": {}
}
```

### Language Support Matrix
- English (en)
- Tamil (ta)
- Hindi (hi)
- Bengali (bn)
- Telugu (te)
- Marathi (mr)
- Automatic language detection enabled

## 🛠 Technology Infrastructure

- **User Interface**: Streamlit framework
- **Vector Storage**: ChromaDB vector database
- **AI Processing**: Google Gemini API
- **Natural Language Processing**: spaCy, langdetect
- **Data Visualization**: Plotly, NetworkX
- **Document Generation**: ReportLab

## 🔒 Security & Compliance

- Local data processing infrastructure
- Minimal external service dependencies (limited to Google Translate API)
- Comprehensive chain of custody documentation
- Forensic integrity verification mechanisms

## 📊 Detection Capabilities

- **Financial Intelligence**: Cryptocurrency addresses, banking credentials, transaction amounts
- **Relationship Analysis**: Contact establishment, communication cessation, interaction frequency shifts
- **Temporal Anomalies**: Irregular activity hours (01:00-04:00), message volume deviations
- **Behavioral Indicators**: Suspicious terminology, coordination patterns, urgency markers

## 👥 Development Team

**VIJAYA KARTHICK RAJA U M**  
📧 vkr3056@gmail.com  
🔗 [github.com/KARTHICK-3056](https://github.com/KARTHICK-3056)

**DIVYESH HARI G**  
📧 divyesh02208@gmail.com  
🔗 [github.com/DIVYESH-HARI](https://github.com/DIVYESH-HARI)

**G.K.AKASHGAUTHAM**  
📧 gkakash2006@gmail.com  
🔗 [github.com/Akashgautham](https://github.com/Akashgautham)

**K.RAKSHITHASRI**  
📧 rakshiekt@gmail.com  
🔗 [github.com/rakshithasri06](https://github.com/rakshithasri06)

**S.S.MADHAVAN**  
📧 ssmadhavan006@gmail.com  
🔗 [github.com/ssmadhavan006](https://github.com/ssmadhavan006)

**M.N.RAKSHA**  
📧 rakshanathan006@gmail.com  
🔗 [github.com/raksha006](https://github.com/raksha006)

## 🙏 Acknowledgements

Developed to empower digital forensics professionals with accelerated investigation workflows and enhanced evidence analysis capabilities.

---

**⚠️ Legal Notice**: This platform is intended exclusively for authorized forensic investigation purposes. End users bear full responsibility for ensuring compliance with applicable legal frameworks and jurisdictional regulations.
