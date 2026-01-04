# 🔬 Gemma 3 Vision Agent - Multimodal Research Interface

An adaptive AI system for multimodal image analysis and decision-making in computational and experimental research, leveraging the Gemma 3 vision-language model through Ollama.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ollama-llm-image-describer.streamlit.app/)

**Live Demo**: [https://ollama-llm-image-describer.streamlit.app/](https://ollama-llm-image-describer.streamlit.app/)

---

## 📋 Overview

This application provides a research-grade interface for performing deep technical analysis on scientific visualizations, experimental plots, and computational physics imagery using the Gemma 3 vision-language model. The system employs a client-side JavaScript architecture embedded within Streamlit for seamless multimodal inference workflows.

### Key Features

- **Multimodal Analysis**: Upload research images (plots, visualizations, experimental data) and receive detailed analytical descriptions
- **Vision-Language Processing**: Powered by Google's Gemma 3 architecture with vision capabilities
- **Streamlit Deployment**: Clean, web-based interface accessible via browser
- **Local LLM Integration**: Direct communication with Ollama API for privacy-preserving inference
- **Drag-and-Drop Interface**: Intuitive image upload with base64 encoding for API transmission
- **Research-Oriented Output**: Generates publishable-quality analytical paragraphs suitable for documentation

---

## 🏗️ Architecture

### System Components

┌─────────────────────────────────────────────┐
│ Streamlit Frontend (Port 8501) │
│ ┌───────────────────────────────────────┐ │
│ │ Embedded HTML/JavaScript Interface │ │
│ │ - Image Upload & Base64 Encoding │ │
│ │ - User Query Processing │ │
│ │ - Response Rendering │ │
│ └─────────────┬─────────────────────────┘ │
└────────────────┼────────────────────────────┘
│ HTTP POST
▼
┌─────────────────────────────────────────────┐
│ Ollama API Server (Port 11434) │
│ ┌───────────────────────────────────────┐ │
│ │ Gemma 3 Vision Model (gemma3:latest)│ │
│ │ - Multimodal Processing │ │
│ │ - Vision-Language Inference │ │
│ └───────────────────────────────────────┘ │
└─────────────────────────────────────────────┘

text

**Technical Stack**:
- **Frontend**: Streamlit 1.31+ with `st.components.v1.html()` for embedded rendering
- **Backend**: Ollama local inference server with CORS enabled
- **Model**: Gemma 3 Vision (`gemma3:latest`) - multimodal transformer architecture
- **Communication Protocol**: RESTful API with JSON payloads and base64 image encoding

---

## 🚀 Installation & Setup

### Prerequisites

- **Python 3.8+**
- **Ollama**: Download from [ollama.com](https://ollama.com/download)
- **Git**: For cloning the repository

### Step 1: Install Ollama

**Windows**:
```bash
# Download OllamaSetup.exe from https://ollama.com/download/windows
# Run the installer and follow the setup wizard
macOS/Linux:

bash
curl -fsSL https://ollama.com/install.sh | sh
Verify installation:

bash
ollama --version
Step 2: Pull the Gemma 3 Vision Model
bash
ollama pull gemma3:latest
This downloads the vision-language model (~4-8GB depending on variant).

Step 3: Clone the Repository
bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
Step 4: Install Python Dependencies
bash
pip install -r requirements.txt
requirements.txt:

text
streamlit>=1.31.0
💻 Local Usage
Running the Application
Terminal 1 - Start Ollama with CORS enabled:

bash
OLLAMA_ORIGINS=* ollama serve
Terminal 2 - Launch Streamlit application:

bash
streamlit run streamlit_app.py
The interface will be available at: http://localhost:8501

Using the Interface
Upload Image: Click the upload area or drag-and-drop a research image (PNG, JPG, JPEG)

Enter Query (Optional): Provide a specific analytical question, e.g.:

"Identify anomalies in this experimental plot"

"Describe the key features of this particle collision visualization"

"Suggest next experimental parameter adjustments based on this data"

Execute Analysis: Click "🔬 Execute Analysis" to send the request to Gemma 3

Review Output: The model response appears in the right panel with analytical documentation

Reset: Clear the interface and upload new images as needed

📁 Project Structure
text
ollama-vision-agent/
├── streamlit_app.py              # Main Streamlit application entry point
├── gemma3_vision_agent.html      # Embedded HTML/JS interface with API logic
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── .gitignore                    # Git ignore patterns
File Descriptions
streamlit_app.py: Orchestrates Streamlit page configuration and embeds the HTML interface using st.components.v1.html()

gemma3_vision_agent.html: Contains the complete frontend logic including image processing, base64 encoding, Ollama API communication, and response rendering

⚙️ Configuration
Model Configuration
To use a different Ollama model, modify line 159 in gemma3_vision_agent.html:

javascript
const MODEL_NAME = 'gemma3:latest';  // Change to your preferred model
Available vision models via Ollama:

gemma3:latest (recommended)

llava:latest

bakllava:latest

API Endpoint Configuration
For deployment with remote Ollama servers, update line 156 in gemma3_vision_agent.html:

javascript
const OLLAMA_API_ENDPOINT = 'http://your-server-ip:11434/api/chat';
Streamlit Interface Settings
Adjust the embedded HTML height in streamlit_app.py line 20:

python
components.html(html_content, height=1000, scrolling=True)  # Modify height as needed
🌐 Cloud Deployment
Deployed Application
The live version is hosted at: https://ollama-llm-image-describer.streamlit.app/

Deployment Architecture
Important: Streamlit Community Cloud cannot run Ollama servers directly. The deployed version requires one of these configurations:

Option 1: Remote Ollama VPS (Recommended for Production)
Deploy Ollama on a cloud VPS with GPU (DigitalOcean, AWS EC2, Hostinger)

Install via Docker:

bash
docker run -d -p 11434:11434 --gpus all ollama/ollama
docker exec -it <container> ollama pull gemma3:latest
Update API endpoint in gemma3_vision_agent.html to point to public IP

Configure firewall rules and authentication for security

Option 2: Ngrok Tunneling (Development Only)
Keep Ollama on local machine

Expose via ngrok:

bash
OLLAMA_HOST=0.0.0.0 ollama serve
ngrok http 11434
Update HTML with ngrok URL (note: URL changes on restart)

Option 3: Local Deployment Only
Run exclusively on localhost for personal research use.

🛠️ Troubleshooting
Common Issues
Issue 1: "Could not connect to the local service"

Solution: Ensure Ollama is running with CORS enabled:

bash
OLLAMA_ORIGINS=* ollama serve
Issue 2: Model not responding

Solution: Verify the model is installed:

bash
ollama list | grep gemma3
If not present:

bash
ollama pull gemma3:latest
Issue 3: Interface not displaying in Streamlit

Solution: Check that gemma3_vision_agent.html is in the same directory as streamlit_app.py

Issue 4: Browser CORS errors

Solution: Check browser console (F12). Ensure Ollama was started with OLLAMA_ORIGINS=*

Issue 5: Cloud deployment not connecting to Ollama

Solution: Localhost references don't work in cloud environments. Deploy Ollama on a VPS or use ngrok tunneling

🔬 Research Applications
This tool is designed for accelerating scientific discovery in computational physics and experimental research contexts. Potential applications include:

High Energy Physics: Analysis of particle collision visualizations and detector readouts

Experimental Data Validation: Automated anomaly detection in experimental plots

Literature Analysis: Extraction of information from scientific figures in papers

Computational Simulations: Interpretation of simulation output visualizations

Multi-Modal Scientific Reasoning: Combining visual and textual information for hypothesis generation

📊 Performance Considerations
Hardware Requirements
Minimum: 8GB RAM, 10GB disk space

Recommended: 16GB RAM, NVIDIA GPU with 8GB+ VRAM for faster inference

Model Size: Gemma 3 requires ~4-8GB storage depending on variant

Inference Speed
CPU: 2-10 seconds per image analysis (model-dependent)

GPU (CUDA): 0.5-2 seconds per image analysis

Enable GPU acceleration on Windows:

powershell
[Environment]::SetEnvironmentVariable("OLLAMA_CUDA", "1", "User")
🤝 Contributing
Contributions are welcome! Areas for enhancement:

 Support for batch image processing

 Multi-turn conversational context with image history

 Export functionality for analysis reports (PDF, Markdown)

 Integration with additional vision models (LLaVA, BakLLaVA)

 Fine-tuning capabilities for domain-specific physics tasks

Development Setup
Fork the repository

Create a feature branch: git checkout -b feature/your-feature

Make changes and test locally

Commit with descriptive messages: git commit -m "Add feature X"

Push to your fork: git push origin feature/your-feature

Open a Pull Request

📄 License
This project is licensed under the MIT License. See LICENSE file for details.

🙏 Acknowledgments
Ollama Team: For providing the local LLM inference framework

Google DeepMind: For the Gemma 3 vision-language architecture

Streamlit: For the rapid web application deployment framework

Institute of High Energy Physics (IHEP): Research institutional support

📧 Contact
Author: Yahia
Affiliation: Institute of High Energy Physics, University of Chinese Academy of Sciences
Research Focus: Deep Learning, Reinforcement Learning, LLMs, Intelligent Agents for Scientific Discovery

For questions or collaboration inquiries, please open an issue on this repository.

🔗 Links
Live Demo: https://ollama-llm-image-describer.streamlit.app/

Ollama Documentation: https://ollama.com/docs

Streamlit Docs: https://docs.streamlit.io

Gemma Model Card: https://ai.google.dev/gemma
