import streamlit as st
import serial
from serial.tools import list_ports
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh
from check_auth import require_login

require_login()

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ======= CSS Styling =======
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://w.wallhaven.cc/full/5w/wallhaven-5w79w5.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }

    .block-container {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Inisialisasi session_state ---
if "serial_conn" not in st.session_state:
    st.session_state.serial_conn = None
if "serial_status" not in st.session_state:
    st.session_state.serial_status = "❌ Disconnected"
if "com_port" not in st.session_state:
    st.session_state.com_port = None
if "baudrate" not in st.session_state:
    st.session_state.baudrate = None
if "monitoring" not in st.session_state:
    st.session_state.monitoring = False
if "history" not in st.session_state:
    st.session_state.history = []

st.title("Realtime Monitoring Kelembapan Tanah")

def get_serial_ports():
    ports = list_ports.comports()
    return [port.device for port in ports]

def read_moisture():
    try:
        conn = st.session_state.serial_conn
        if conn and conn.is_open:
            line = conn.readline().decode('utf-8').strip()
            if line.isdigit():
                return int(line)
        return None
    except:
        return None

# --- Panel Pengaturan Serial ---
with st.expander("Pengaturan Serial", expanded=True):
    ports = get_serial_ports()
    selected_port = st.selectbox("Pilih Port COM", ports, index=ports.index(st.session_state.com_port) if st.session_state.com_port in ports else 0)
    selected_baud = st.selectbox("Pilih Baudrate", [9600, 115200, 4800, 19200], index=[9600, 115200, 4800, 19200].index(st.session_state.baudrate) if st.session_state.baudrate else 0)
    timeout = st.slider("Timeout (detik)", min_value=0.1, max_value=1.0, value=0.1, step=0.1)


    col1, col2 = st.columns(2)
    with col1:
        if st.button("Connect"):
            try:
                if st.session_state.serial_conn:
                    st.session_state.serial_conn.close()
                conn = serial.Serial(selected_port, selected_baud, timeout=timeout)
                st.session_state.serial_conn = conn
                st.session_state.serial_status = "Connected"
                st.session_state.com_port = selected_port
                st.session_state.baudrate = selected_baud
                st.success(f"Terhubung ke {selected_port} @ {selected_baud} bps")
            except Exception as e:
                st.session_state.serial_conn = None
                st.session_state.serial_status = "Disconnected"
                st.error(f"Gagal connect: {e}")

    with col2:
        if st.button("Disconnect"):
            if st.session_state.serial_conn:
                st.session_state.serial_conn.close()
                st.session_state.serial_conn = None
                st.session_state.serial_status = "Disconnected"
                st.success("Disconnected")

    st.markdown("---")
    st.markdown(f"**Port:** `{st.session_state.com_port}`")
    st.markdown(f"**Baudrate:** `{st.session_state.baudrate}`")
    st.markdown(f"**Status:** {st.session_state.serial_status}")

# --- Monitoring Controls ---
start_stop_col1, start_stop_col2 = st.columns(2)
with start_stop_col1:
    if st.button("Start Monitoring"):
        if st.session_state.serial_status == "Connected":
            st.session_state.monitoring = True
            st.session_state.history = []
        else:
            st.warning("Hubungkan dulu ke serial sebelum mulai monitoring!")

with start_stop_col2:
    if st.button("Stop Monitoring"):
        st.session_state.monitoring = False

# --- Autorefresh hanya jika monitoring aktif ---
if st.session_state.monitoring:
    count = st_autorefresh(interval=1000, limit=None, key="autorefresh_counter")
    moisture = read_moisture()
    if moisture is not None:
        st.session_state.history.append(moisture)
    else:
        moisture = st.session_state.history[-1] if st.session_state.history else 0

    # Tampilkan gauge
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=moisture,
        delta={'reference': 50, 'increasing': {'color': "lime"}, 'decreasing': {'color': "red"}},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#00c7ff"},
            'steps': [
                {'range': [0, 20], 'color': "#ff6666"},
                {'range': [20, 40], 'color': "#ffe066"},
                {'range': [40, 60], 'color': "#66ff99"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 35
            }
        },
        title={'text': "Soil Moisture (%)", 'font': {'size': 24}}
    ))
    st.plotly_chart(fig, use_container_width=True)


    def emoji_large(emoji_char):
        return f"<p style='font-size:48px; margin:0'>{emoji_char}</p>"

    if moisture < 20:
        st.error("Tanah terlalu kering! Segera sirami tanaman.")
        st.markdown(emoji_large("😟"), unsafe_allow_html=True)
    elif 20 <= moisture <= 40:
        st.warning("Kelembapan cukup. Periksa secara berkala.")
        st.markdown(emoji_large("😐"), unsafe_allow_html=True)
    else:
        st.success("Tanah lembab dan sehat.")
        st.markdown(emoji_large("😊"), unsafe_allow_html=True)



else:
    st.info("Tekan Start Monitoring untuk mulai membaca data dari Arduino.")
