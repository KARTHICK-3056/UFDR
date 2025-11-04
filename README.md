# FORENSIS-AI - Universal Forensic Data Report Analysis Platform

An advanced digital forensics platform for comprehensive analysis of Universal Forensic Data Reports (UFDR), featuring behavioral intelligence, pattern recognition, and automated triage capabilities.

## Overview

FORENSIS-AI is a sophisticated forensic investigation tool designed to streamline the triage and analysis of communication data extracted from UFDR JSON files. The platform integrates vector-based semantic search, behavioral pattern analysis, and AI-driven intelligence to identify potentially suspicious activities, financial transactions, and communication anomalies within digital evidence.

## Core Capabilities

### Forensic Investigation Features
- **Automated Triage System**: AI-powered analysis of UFDR datasets to identify suspicious communications, financial activities, and irregular patterns
- **Natural Language Query Interface**: Semantic search functionality across message content with automated entity recognition
- **Entity Detection and Highlighting**: Automatic identification of cryptocurrency addresses, telephone numbers, banking information, and monetary values
- **Multi-language Processing**: Automatic language detection and translation support for Tamil, Hindi, Bengali, Telugu, and Marathi communications

### Behavioral Intelligence Analysis
- **Temporal Pattern Detection**: Identification of irregular messaging patterns, including nocturnal activity (01:00-04:00 hours) and communication volume anomalies
- **Contact Network Analysis**: Monitoring of contact establishment, relationship discontinuities, and communication frequency variations
- **Data Visualization Suite**: Interactive temporal analysis charts and network relationship graphs
- **Investigative Recommendations**: Context-aware suggestions for subsequent investigative actions

### Documentation and Export
- **Comprehensive Report Generation**: Production of professional forensic reports including findings, metadata analysis, and behavioral assessments
- **Chain of Custody Documentation**: Complete audit trail of all investigative actions with integrity verification
- **Data Export Functionality**: Export of analysis results in multiple formats for further investigation

## Installation and Configuration

### System Requirements

```bash
Python 3.8 or higher
pip package manager
```

### Installation Procedure

1. **Repository Cloning**
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
# Create environment configuration file
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

4. **Application Launch**
```bash
streamlit run frontend/app.py
```

The application will be accessible at `http://localhost:8501`

## System Architecture

```
forensis-ai/
├── frontend/
│   ├── app.py                 # Primary application interface
│   └── chroma_db/            # Vector database repository
├── backend/
│   ├── ingest.py             # Data ingestion module
│   └── search_engine.py      # Hybrid search implementation
├── utils/
│   ├── highlighter.py        # Entity recognition and text processing
│   ├── pdf_generator.py      # Report generation module
│   ├── chain_of_custody.py   # Audit logging system
│   ├── anomaly_detection.py  # Behavioral analysis engine
│   ├── gemini_client.py      # AI integration client
│   └── translation.py        # Language processing module
├── data/
│   └── sample_ufdr.json      # Sample dataset
└── requirements.txt          # Dependency specifications
```

## Operational Workflow

### 1. Data Ingestion
- Select **"Upload UFDR Data"** to import your JSON dataset
- Alternatively, select **"Load Sample Data"** for demonstration purposes

### 2. Behavioral Analysis Execution
- Initiate **"Run Behavioral Analysis"** to detect:
  - Irregular communication timestamps (01:00-04:00 hours)
  - Statistical anomalies in message volume
  - Recently established contacts (within 24-hour window)
  - Disruptions in established communication patterns
  - Network relationship mapping

### 3. Forensic Investigation
- **Automated Analysis**: Execute **"Run Automated Forensic Analysis"** for comprehensive AI-driven triage
- **Manual Investigation**: Conduct targeted searches using natural language queries:
  - "Identify cryptocurrency wallet addresses"
  - "Locate indicators of suspicious activity"
  - "Extract messages containing financial transactions"

### 4. Results Analysis
- Review automatically highlighted entities (cryptocurrency wallets, contact numbers, financial amounts)
- Examine temporal patterns and contact network relationships
- Evaluate AI-generated investigative recommendations

### 5. Report Generation
- Select **"Export to PDF"** to generate comprehensive forensic documentation

## Technical Specifications

### UFDR Data Format

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

### Language Support
- English (en)
- Tamil (ta)
- Hindi (hi)
- Bengali (bn)
- Telugu (te)
- Marathi (mr)
- Automatic language detection enabled

## Technology Infrastructure

- **User Interface**: Streamlit Framework
- **Vector Database**: ChromaDB
- **Artificial Intelligence**: Google Gemini API
- **Natural Language Processing**: spaCy, langdetect
- **Data Visualization**: Plotly, NetworkX
- **Document Generation**: ReportLab

## Security and Compliance

- Local data processing architecture
- External API communication limited to translation services only
- Comprehensive chain of custody logging for audit compliance
- Evidence integrity verification protocols

## Detection Capabilities

- **Financial Indicators**: Cryptocurrency addresses, banking information, transaction values
- **Contact Behavior**: Relationship establishment, contact discontinuity, frequency variations
- **Temporal Anomalies**: Irregular activity hours (01:00-04:00), communication volume spikes
- **Behavioral Indicators**: Suspicious terminology, coordination patterns, urgency markers

## Development Team

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

## Acknowledgments

Developed to enhance digital forensics investigation workflows and improve evidence analysis efficiency for law enforcement and investigative professionals.

---

**Legal Notice**: This platform is designed exclusively for legitimate forensic investigation purposes. Users bear sole responsibility for ensuring compliance with all applicable laws, regulations, and jurisdictional requirements.