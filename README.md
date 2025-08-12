# CompliMate Lite
**CompliMate Lite helps you quickly find relevant rules, sections, and guidelines within petroleum compliance documents — making regulatory navigation simpler and faster.**

<p align="center">
  <a href="assets/CompliMate_Lite-Screen Recording.mp4">
    <img src="assets/CompliMate_Lite interface.png" alt="Demo Preview" width="600"/>
  </a>
</p>

---

## 🚀 About the Project

- Your smart companion for quick lookups and clear insights from dense regulatory files.
- This project was created as part of an internship program for **Reliance BP Mobility Limited (d/b/a Jio-bp)**.
- This project processes DOCX and PDF regulatory documents using python-docx and pdf2docx, converts their content into searchable embeddings with sentence-transformers, and uses FAISS for fast similarity search to help users quickly find relevant sections. It efficiently manages document metadata and caching to ensure smooth performance.

## ✨ Features

- Uploaded petroleum regulatory files (docx/pdf) are searched through and relevant information as per user queries are retrieved.
- Chatbot style responses
- Cloud-hosted: Runs on Streamlit Community Cloud for easy access without complex setup.
- Has AI powered version **CompliMate** 

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.8+ (preferably 3.11)
- Streamlit (`pip install streamlit`)
- Other dependencies the app uses (`pip install -r requirements.txt`)

### Installation

1. Clone the repo  
```bash
git clone https://github.com/SaranyaSarangi/CompliMate_Lite
cd your-repo-name
```

2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run the app locally
```bash
streamlit run app.py
```
---

## 📦 Usage
- How users can use the app:
Users can enter words or phrases for their concerned topic and click 'Submit'.

- What output or feedback to expect
CompliMate Lite will return relevant sections from the files uploaded in RAG folder.

---

## 🛠️ Deployment
- This app is deployed via Streamlit Community Cloud.
- For live app visit : [CompliMate Lite](https://complimatelite-ccfsz8qvsmmjfqvrjkkbqq.streamlit.app/)
- App auto-updates whenever code is pushed to the main branch on GitHub.

You can also deploy locally or on your preferred cloud platform.

---

## 🤝 Contributing
Contributions are welcome! Please fork the repo, create a new branch for your feature/fix, and submit a pull request.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact
- Email – sharanya.sarangi@gmail.com
- LinkedIn - linkedin.com/in/saranya-sarangi-5b3745374
- Source Code : https://github.com/SaranyaSarangi/CompliMate_Lite

## 🎉 Acknowledgments
I would like to sincerely thank **Reliance BP Mobility Limited (d/b/a Jio-bp)** for providing me the valuable opportunity to work on this project as part of their internship program. Their support and guidance were instrumental in bringing this project to life.
