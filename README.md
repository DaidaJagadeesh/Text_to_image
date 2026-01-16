Text-to-Image Generation using Stable Diffusion & Streamlit
# Project Overview

This project demonstrates Text-to-Image Generation using Stable Diffusion and an interactive Streamlit UI. Users can enter a text prompt, adjust parameters, and generate an AI-created image using the Stable Diffusion model.


![Screenshot 2025-03-19 193420](https://github.com/user-attachments/assets/ba93c81d-4ae6-4dc8-9519-6eceaeaf67a0)


![Screenshot 2025-03-19 193838](https://github.com/user-attachments/assets/a863166e-012b-47eb-a277-06bdcd26cf7d)

# Features

User-friendly Web Interface: Built using Streamlit.

Stable Diffusion v1.5: Generates high-quality images.

Parameter Customization: Adjust inference steps and guidance scale.

Image Download: Save generated images directly from the app.

GPU Support: Runs efficiently on CUDA-enabled devices.



🔧 Installation & Setup

1. Clone the Repository

git clone https://github.com/DaidaJagadeesh/Text_to_image.git
cd Text_to_image

2. Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

3. Install Dependencies

pip install -r requirement.txt

4. Run the Application

streamlit run app.py

🖼️ How It Works

User inputs a text prompt (e.g., "A futuristic cyberpunk city at night").

Adjustable Parameters:

Inference Steps: Defines the quality of the generated image.

Guidance Scale: Controls adherence to the text prompt.

Stable Diffusion Model Generates an Image.

Image is displayed and available for download.
