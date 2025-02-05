import streamlit as st
import colorsys
import pyperclip

# Custom CSS for styling
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            color: white;
            background: linear-gradient(90deg, #ff8c00, #ff0080);
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

# Input sliders for HSV values
hue = st.slider("Hue", 0, 360, 180)
saturation = st.slider("Saturation", 0, 100, 100)
value = st.slider("Value", 0, 100, 100)

# Convert HSV (0-360, 0-100, 0-100) to RGB (0-255)
r, g, b = colorsys.hsv_to_rgb(hue / 360, saturation / 100, value / 100)
rgb_tuple = (int(r * 255), int(g * 255), int(b * 255))
rgb_hex = '#{:02x}{:02x}{:02x}'.format(*rgb_tuple)

# Display RGB values
st.markdown(f"**RGB:** `{rgb_tuple}` | **Hex:** `{rgb_hex}`")

# Color preview box
st.markdown(f'<div class="color-box" style="background-color: {rgb_hex};">{rgb_hex}</div>', unsafe_allow_html=True)

# Copy to clipboard button
def copy_rgb():
    pyperclip.copy(f"RGB: {rgb_tuple} | HEX: {rgb_hex}")
    st.success("Copied to clipboard!")

st.button("📋 Copy RGB", on_click=copy_rgb)

st.markdown('<div class="footer">Made with ❤️ using Streamlit</div>', unsafe_allow_html=True)
