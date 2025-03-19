import streamlit as st
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

# Load the Stable Diffusion model
@st.cache_resource
def load_pipeline():
    model_id = "runwayml/stable-diffusion-v1-5"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipeline = StableDiffusionPipeline.from_pretrained(model_id)
    pipeline.to(device)
    return pipeline

pipeline = load_pipeline()

def generate_image(prompt, num_inference_steps=50, guidance_scale=7.5):
    """Generate an image using Stable Diffusion."""
    with torch.no_grad():
        image = pipeline(prompt, num_inference_steps=num_inference_steps, guidance_scale=guidance_scale).images[0]
    return image

# Streamlit UI
st.title("🖼️ Text-to-Image Generator with Stable Diffusion")
st.write("Enter a text prompt below and generate an AI-powered image.")

# User input fields
prompt = st.text_input("Enter your image description:", "A futuristic cyberpunk city at night")
num_inference_steps = st.slider("Inference Steps", 10, 100, 50)
guidance_scale = st.slider("Guidance Scale", 1.0, 20.0, 7.5)

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image..."):
            generated_image = generate_image(prompt, num_inference_steps, guidance_scale)
            st.image(generated_image, caption="Generated Image", use_column_width=True)
            # Option to download image
            img_path = "generated_image.png"
            generated_image.save(img_path)
            st.download_button("Download Image", data=open(img_path, "rb"), file_name="generated_image.png", mime="image/png")
    else:
        st.warning("Please enter a text prompt!")
