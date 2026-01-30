A Django-based web application that allows users to upload PDF and DOCX documents, extract text from them, and perform basic text analysis. The system also supports generating downloadable PDF outputs.
🚀Features
- Upload PDF and DOCX files
- Extract text from documents
- Perform basic text cleaning and processing
- Generate PDF output using extracted text
- Simple and user-friendly web interface
- Built using Django framework
  
🛠️ Tech Stack
- Backend: Python, Django
- Document Processing:
    PyPDF2 (PDF text extraction)
    python-docx (DOCX text extraction)
    PDF Generation: ReportLab
    Frontend: HTML, CSS (Django Templates)

INSTALLATIONS & SETUP
1. Clone the repository
git clone https://github.com/your-username/document-text-analysis.git
cd document-text-analysis

2.Create & activate virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3.Install dependencies
pip install -r requirements.txt

4.Run migrations
python manage.py migrate

5.Start the development server
python manage.py runserver

👨‍💻 Author
Deepesh Patil
Aspiring Python & Django Developer 🚀
Hope it will help!!

