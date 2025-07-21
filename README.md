# Face Recognition Attendance System

This project is a **complete Attendance System using Face Recognition** built with Python. It detects, recognizes, and records student or employee attendance in real time using deep learning models and a Streamlit-based web interface.

## 📌 Project Highlights

- Real-time face detection and recognition using [InsightFace](https://github.com/deepinsight/insightface)
- Facial embeddings generated with pre-trained ONNX models
- Redis for fast in-memory data handling and session management
- Streamlit UI for:
  - 🧍 Registration Form
  - 👁️ Real-Time Face Recognition
  - 📊 Attendance Report
- Modular and scalable architecture

---

## 🗂️ Folder Structure

```
ATTENDANCE-SYSTEM-APP/
├── face_attendance_env/               # Python virtual environment
├── insightface_model/
│   └── models/buffalo_sc/
│       ├── det_500m.onnx              # Face detection model
│       └── w600k_mbf.onnx             # Face recognition model
├── pages/
│   ├── 1_Real_Time_Prediction.py      # Streamlit page for real-time face recognition
│   ├── 2_Registration_form.py         # Page for new user registration
│   └── 3_Report.py                    # Page to view attendance reports
├── check_redis.py                     # Script to verify Redis connection
├── configure.sh                       # Setup script
├── face_rec.py                        # Core face recognition logic
├── Home.py                            # Main Streamlit homepage
├── main.sh                            # Shell script to launch app
├── requirements.txt                   # Project dependencies
```

---

## 🚀 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/face-attendance-app.git
cd face-attendance-app

# Create virtual environment & activate it (optional but recommended)
python -m venv face_attendance_env
source face_attendance_env/bin/activate  # On Windows: face_attendance_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🧠 Technologies Used

- Python 3.10
- Streamlit
- OpenCV
- NumPy, Pandas
- InsightFace (ONNX models)
- Redis

---

## 💡 Features

- Add new users with live webcam or image
- Detect and recognize faces in real-time
- Mark attendance with timestamps
- View and download reports
- Works offline once set up

---

## 🛠️ Run the App

Make sure Redis is installed and running.

```bash
# Optional: Check Redis connection
python check_redis.py

# Run the app
streamlit run Home.py
```

---

## 📄 License

This project is open-source and free to use under the MIT License.