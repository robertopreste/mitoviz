FROM gitpod/workspace-full

RUN sudo apt-get update && apt-get install ffmpeg libsm6 libxext6 -y && sudo rm -rf /var/lib/apt/lists/*
