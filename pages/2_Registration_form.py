import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import numpy as np
import face_rec  # Make sure face_rec.py exists and is error-free

st.set_page_config(page_title='Registration Form', layout='wide')

# Custom CSS for styling
st.markdown("""
    <style>
        h1, h2, h3 {
            font-family: 'Segoe UI', sans-serif;
            color: #000000;
        }
        .stButton>button {
            background-color: #1ABC9C;
            color: white;
            border-radius: 10px;
            padding: 10px 22px;
            font-size: 16px;
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #111;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 14px;
        }
    </style>
    <div class="footer">🔒 Attendance System •</div>
""", unsafe_allow_html=True)

st.header("📝 Register New User")

# Load registration form logic
registration_form = face_rec.RegistrationForm()

# Get user input
person_name = st.text_input(label='Full Name', placeholder='John Doe')
role = st.selectbox(label='Role', options=('Student', 'Teacher'))

# Capture face and save embedding
def video_callback_func(frame):
    img = frame.to_ndarray(format='bgr24')
    reg_img, embedding = registration_form.get_embedding(img)

    if embedding is not None:
        with open('face_embedding.txt', mode='ab') as f:
            np.savetxt(f, embedding)

    return av.VideoFrame.from_ndarray(reg_img, format='bgr24')

# Show camera stream
st.markdown("### 📸 Capture Face")
webrtc_streamer(
    key="realtime_prediction",
    video_frame_callback=video_callback_func,
    rtc_configuration={
        "iceServers": [
            {
                "urls": ["stun:bn-turn2.xirsys.com"]
            },
            {
                "username": "tpbmCGWfojEpDlj9-d1biQlZ42CqdEtgmtIN_SK1uSdIe5Wdp47vdNCBckRoQidhAAAAAGiA71JOaXJtYWw=",
                "credential": "f92e183c-67cf-11f0-b781-0242ac140004",
                "urls": [
                    "turn:bn-turn2.xirsys.com:80?transport=udp",
                    "turn:bn-turn2.xirsys.com:3478?transport=udp",
                    "turn:bn-turn2.xirsys.com:80?transport=tcp",
                    "turn:bn-turn2.xirsys.com:3478?transport=tcp",
                    "turns:bn-turn2.xirsys.com:443?transport=tcp",
                    "turns:bn-turn2.xirsys.com:5349?transport=tcp"
                ]
            }
        ]
    }
)

# Submit button
if st.button('✅ Submit Registration'):
    if not person_name.strip():
        st.warning("Please enter a valid name before submitting.")
    else:
        return_val = registration_form.save_data_in_redis_db(person_name, role)
        if return_val is True:
            st.success(f"{person_name} registered successfully!")
        elif return_val == 'name_false':
            st.error("Please enter a valid name.")
        elif return_val == 'file_false':
            st.error("face_embedding.txt not found. Please recapture the face.")
