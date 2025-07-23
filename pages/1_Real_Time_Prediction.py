import streamlit as st
import time
from streamlit_webrtc import webrtc_streamer
import av
import face_rec

st.set_page_config(page_title='Real-Time Predictions', layout='wide')

# Define video_frame_callback before using it
waitTime = 3
setTime = time.time()
realtimepred = face_rec.RealTimePred()

def video_frame_callback(frame):
    global setTime
    img = frame.to_ndarray(format="bgr24")
    pred_img = realtimepred.face_prediction(img, redis_face_db,
                                            'facial_features', ['Name', 'Role'], thresh=0.4)
    timenow = time.time()
    if timenow - setTime >= waitTime:
        realtimepred.saveLogs_redis()
        setTime = time.time()
        print("Saved logs to Redis DB")
    return av.VideoFrame.from_ndarray(pred_img, format="bgr24")


st.markdown("""
    <style>
        h1, h2, h3 {
            font-family: 'Segoe UI', sans-serif;
            color: #000000;
        }
        .stButton>button {
            background-color: #636efa;
            color: white;
            border-radius: 8px;
            padding: 10px 24px;
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
    <div class="footer">🔒 Attendance System • </div>
""", unsafe_allow_html=True)

st.header("🎥 Real-Time Face Recognition System")

with st.spinner('Retrieving Data from Redis DB...'):
    redis_face_db = face_rec.retrive_data(name='academy:register')
    st.success("✅ Data successfully retrieved!")
    with st.expander("🔍 View Registered Data"):
        st.dataframe(redis_face_db)

st.markdown("---")
st.subheader("📡 Webcam Stream")
# Single webrtc_streamer with configuration and callback

webrtc_streamer(
    key="realtime_prediction",
    video_frame_callback=video_frame_callback,
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
