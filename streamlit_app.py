import streamlit as st
import colorsys
import pyperclip

st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            color: white;
            background: linear-gradient(90deg, #0000ff, #00c0ff);
            padding: 10px;
            border-radius: 10px;
        }
        .color-box {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 150px;
            border-radius: 10px;
            color: white;
            font-size: 1.5rem;
            font-weight: bold;
            margin-top: 10px;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 0.8rem;
            color: gray;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">HSV to RGB Converter</div>', unsafe_allow_html=True)

st.sidebar.header("Adjust HSV Values")
hue = st.sidebar.slider("Hue", 0, 360, 0)
saturation = st.sidebar.slider("Saturation", 0, 100, 0)
value = st.sidebar.slider("Value", 0, 100, 0)

r, g, b = colorsys.hsv_to_rgb(hue / 360, saturation / 100, value / 100)
rgb_tuple = (int(r * 255), int(g * 255), int(b * 255))
rgb_hex = '#{:02x}{:02x}{:02x}'.format(*rgb_tuple)

st.subheader("Converted RGB Values")
st.write(f"**RGB:** `{rgb_tuple}` | **Hex:** `{rgb_hex}`")

col1, col2 = st.columns(2)
with col1:
    st.metric("Hue", hue)
    st.metric("Saturation", saturation)
    st.metric("Value", value)
with col2:
    st.markdown(f'<div class="color-box" style="background-color: {rgb_hex};">{rgb_hex}</div>', unsafe_allow_html=True)

def copy_rgb():
    pyperclip.copy(f"RGB: {rgb_tuple} | HEX: {rgb_hex}")
    st.success("Copied to clipboard!")

st.button("📋 Copy RGB", on_click=copy_rgb)

st.expander("More Info").write("HSV (Hue, Saturation, Value) is a color representation model where Hue defines the color type, Saturation defines intensity, and Value defines brightness.")

st.markdown('<div class="footer">Made with ❤️ using Streamlit </div>', unsafe_allow_html=True)
