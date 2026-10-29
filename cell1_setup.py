# Cell 1: Setup Packages
!pip install -q -U scipy
!pip install -q insightface onnxruntime-gpu flask flask-cors opencv-python-headless pillow
!wget -q -O /content/inswapper_128.onnx https://huggingface.co/ezioruan/inswapper_128.onnx/resolve/main/inswapper_128.onnx
!wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O /content/cloudflared
!chmod +x /content/cloudflared

print("✅ Setup Ready!")
