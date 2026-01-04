# 🔬 Gemma 3 Vision Agent - Multimodal Research Interface

An adaptive AI system for multimodal image analysis and decision-making in computational and experimental research, leveraging the Gemma 3 vision-language model through Ollama.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ollama-llm-image-describer.streamlit.app/)

**🚀 Live Demo**: https://ollama-llm-image-describer.streamlit.app/

---

## 📋 Overview

This application offers a research-grade interface for conducting in-depth technical analysis on scientific visualizations, experimental plots, and computational physics imagery, utilizing the Gemma 3 vision-language model. The system employs a client-side JavaScript architecture embedded within Streamlit for seamless multimodal inference workflows.

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

```
┌─────────────────────────────────────────────┐
│         Streamlit Frontend (Port 8501)      │
│  ┌───────────────────────────────────────┐  │
│  │  Embedded HTML/JavaScript Interface   │  │
│  │  - Image Upload & Base64 Encoding     │  │
│  │  - User Query Processing              │  │
│  │  - Response Rendering                 │  │
│  └─────────────┬─────────────────────────┘  │
└────────────────┼────────────────────────────┘
                 │ HTTP POST
                 ▼
┌─────────────────────────────────────────────┐
│      Ollama API Server (Port 11434)         │
│  ┌───────────────────────────────────────┐  │
│  │   Gemma 3 Vision Model (gemma3:latest)│  │
│  │   - Multimodal Processing             │  │
│  │   - Vision-Language Inference         │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

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
```

**macOS/Linux**:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verify installation:
```bash
ollama --version
```

### Step 2: Pull the Gemma 3 Vision Model

```bash
ollama pull gemma3:latest
```

This downloads the vision-language model (~4-8GB depending on variant).

### Step 3: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### Step 4: Install Python Dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt`**:
```
streamlit>=1.31.0
```

---

## 💻 Local Usage

### Running the Application

**Terminal 1** - Start Ollama with CORS enabled:
```bash
OLLAMA_ORIGINS=* ollama serve
```

**Terminal 2** - Launch Streamlit application:
```bash
streamlit run streamlit_app.py
```

The interface will be available at: `http://localhost:8501`

### Using the Interface

1. **Upload Image**: Click the upload area or drag-and-drop a research image (PNG, JPG, JPEG)
2. **Enter Query** (Optional): Provide a specific analytical question, e.g.:
   - "Identify anomalies in this experimental plot"
   - "Describe the key features of this particle collision visualization"
   - "Suggest next experimental parameter adjustments based on this data"
3. **Execute Analysis**: Click "🔬 Execute Analysis" to send the request to Gemma 3
4. **Review Output**: The model response appears in the right panel with analytical documentation
5. **Reset**: Clear the interface and upload new images as needed

---

## 📁 Project Structure

```
ollama-vision-agent/
├── app.py              # Main Streamlit application entry point
├── gemma3_vision_agent.html      # Embedded HTML/JS interface with API logic
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── .gitignore                    # Git ignore patterns
```

### File Descriptions

- **`app.py`**: Orchestrates Streamlit page configuration and embeds the HTML interface using `st.components.v1.html()`
- **`gemma3_vision_agent.html`**: Contains the complete frontend logic including image processing, base64 encoding, Ollama API communication, and response rendering

---

## ⚙️ Configuration

### Model Configuration

To use a different Ollama model, modify **line 159** in `gemma3_vision_agent.html`:

```javascript
const MODEL_NAME = 'gemma3:latest';  // Change to your preferred model
```

Available vision models via Ollama:
- `gemma3:latest` (recommended)
- `llava:latest`
- `bakllava:latest`

### API Endpoint Configuration

For deployment with remote Ollama servers, update **line 156** in `gemma3_vision_agent.html`:

```javascript
const OLLAMA_API_ENDPOINT = 'http://your-server-ip:11434/api/chat';
```

### Streamlit Interface Settings

Adjust the embedded HTML height in `app.py`:

```python
components.html(html_content, height=1000, scrolling=True)  # Modify height as needed
```

---

## 🌐 Cloud Deployment

### Deployed Application

The live version is hosted at: [**https://ollama-llm-image-describer.streamlit.app/**](https://ollama-llm-image-describer.streamlit.app/)

### Deployment to Streamlit Community Cloud

**Important**: Streamlit Community Cloud cannot run Ollama servers directly. The deployed version requires Ollama to be accessible via a public endpoint.

#### Deployment Steps:

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your GitHub repository
   - Set main file: `streamlit_app.py`
   - Click "Deploy"

3. **Configure Ollama Endpoint**:
   
   Since localhost won't work in the cloud, choose one option:

   **Option A: Remote Ollama VPS (Recommended)**
   - Deploy Ollama on a cloud VPS with GPU (DigitalOcean, AWS EC2, Hostinger)
   - Install via Docker:
     ```bash
     docker run -d -p 11434:11434 --gpus all ollama/ollama
     docker exec -it <container> ollama pull gemma3:latest
     ```
   - Update `OLLAMA_API_ENDPOINT` in HTML to point to public IP
   - Configure firewall and authentication

   **Option B: Ngrok Tunneling (Development Only)**
   - Keep Ollama on local machine
   - Expose via ngrok:
     ```bash
     OLLAMA_HOST=0.0.0.0 ollama serve
     ngrok http 11434
     ```
   - Update HTML with ngrok URL (URL changes on restart)

---

## 🛠️ Troubleshooting

### Common Issues

**Issue 1**: "Could not connect to the local service"

**Solution**: Ensure Ollama is running with CORS enabled:
```bash
OLLAMA_ORIGINS=* ollama serve
```

**Issue 2**: Model not responding

**Solution**: Verify the model is installed:
```bash
ollama list | grep gemma3
```

If not present:
```bash
ollama pull gemma3:latest
```

**Issue 3**: Interface not displaying in Streamlit

**Solution**: Check that `gemma3_vision_agent.html` is in the same directory as `streamlit_app.py`

**Issue 4**: Browser CORS errors

**Solution**: Check browser console (F12). Ensure Ollama was started with `OLLAMA_ORIGINS=*`

**Issue 5**: Cloud deployment not connecting to Ollama

**Solution**: Localhost references don't work in cloud environments. Deploy Ollama on a VPS or use ngrok tunneling

---


### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make changes and test locally
4. Commit with descriptive messages: `git commit -m "Add feature X"`
5. Push to your fork: `git push origin feature/your-feature`
6. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.



## 📧 Contact

**Author**: Yahia  
**Affiliation**: Institute of High Energy Physics, University of Chinese Academy of Sciences  
**Research Focus**: Deep Learning, Reinforcement Learning, LLMs, Intelligent Agents for Scientific Discovery

For questions or collaboration inquiries, please open an issue on this repository.

---

## 🔗 Links

- **Live Demo**: https://ollama-llm-image-describer.streamlit.app/
- **Ollama Documentation**: https://ollama.com/docs
- **Streamlit Docs**: https://docs.streamlit.io
- **Gemma Model Card**: https://ai.google.dev/gemma

---

**Last Updated**: January 5, 2026
