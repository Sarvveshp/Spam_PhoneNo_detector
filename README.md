# 📞 Spam Phone Number Detector

This is a web-based application that detects whether a given phone number is **spam** by:

- Checking against a MongoDB database of known spam numbers.
- Applying simple rules (like repeated digits) to detect suspicious patterns.
- Allowing users to **report new spam numbers**, which are saved for future detections.

---

## 🚀 Features

- 🔍 Check any phone number for spam
- 🧠 Basic ML/logic-based pattern detection for unknown numbers
- 📦 MongoDB integration to store known spam numbers
- ✍️ Report a number as spam via the UI
- 📄 View all reported spam numbers
- 🖥️ Clean Bootstrap-based user interface

---

## 🛠 Tech Stack

- **Frontend**: Flask + HTML + Bootstrap
- **Backend**: Python + Flask
- **Database**: MongoDB (local or network)
- **UI Enhancements**: Bootstrap 5

---

## 💻 Local Setup

### 1. Clone the repo

### 2. Set up virtual environment (optional but recommended)
<pre> '''bash
python -m venv venv
source venv/bin/activate  
# on Windows: venv\Scripts\activate '''</pre>

### 3. Install dependencies
<pre> '''bash
pip install -r requirements.txt ''' </pre>
### 4. Run the app
<pre>'''bash
python app.py''' </pre>
Visit http://127.0.0.1:5000/ in your browser.

```bash
git clone https://github.com/yourusername/spam-number-detector.git
cd spam-number-detector


