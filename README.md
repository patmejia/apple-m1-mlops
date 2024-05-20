# apple-m1-mlops

Apple M1-specific setup for machine learning engineering production systems, focusing on MLOps practices with Metal acceleration and [Jupyter](https://jupyter.org/)

For detailed acknowledgments, please see the [MLOps](https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/tree/main/course1/week1-ungraded-lab). This project is part of [deeplearning.ai](https://www.deeplearning.ai/)'s Machine Learning Engineering for Production Specialization.

[Clone the DeepLearning.ai repository (optional)](https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public)

```bash
git clone https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public.git
```

## Start Here

### 1. Environment Setup

```bash
conda create --name mlep-w1-lab python=3.8
conda activate mlep-w1-lab
```

General Setup - no Apple M1 (optional)

```bash
pip install -r requirements.txt
```

#### Apple M1 Users

```bash
# Add conda-forge to channels
conda config --add channels conda-forge
# Install TensorFlow dependencies
conda install -c apple tensorflow-deps
# Install TensorFlow for macOS
python -m pip install tensorflow-macos tensorflow-metal
# Install specific OpenCV version
conda install -c conda-forge opencv===4.5.3
# Modify requirements for M1 compatibility
sed -i '.bak' \
    -e 's/^tensorflow==2.7.0/# tensorflow==2.7.0  # Use tensorflow-macos and tensorflow-metal instead/' \
    -e 's/^opencv-python-headless==4.5.3.56/# opencv-python-headless==4.5.3.56  # Commented out for compatibility with M1 Mac/' \
    requirements.txt
# Rename requirements for clarity
mv requirements.txt requirements-m1.txt
# Update protobuf version for compatibility
sed -i '.bak' 's/^protobuf==.*/protobuf>=3.20.3,<4.21.0/' requirements-m1.txt
# Install modified requirements
pip install -r requirements-m1.txt
```
Compatabilit note:
- Updates protobuf for tensorflow-macos 2.13.0 requirements.
- Disables tensorflow==2.7.0 for M1 Mac compatibility.
- Replaces opencv-python-headless with opencv==4.5.3 for M1.


### 2. Verify Installations

```bash
python -c "import tensorflow as tf; print('TensorFlow Version:', tf.__version__)"
python -c "import cv2; print('OpenCV Version:', cv2.__version__)"
```

### 3. Launch Jupyter Lab

```bash
jupyter lab
```

### 4. Access Jupyter Lab and Run the Notebook

i. Copy the URL from the terminal and paste it into your browser to open the `server.ipynb` notebook.

```plaintext
http://localhost:8888/lab
```

### 5. Run Installation Verification Tests

Run the test script:

```bash
python src/test_installation.py
```

Test installtions note: 
- TensorFlow Version: Verifies TensorFlow version starts with '2'.
- TensorFlow Operation: Confirms GPU/Metal support via matrix multiplication.
- OpenCV Version: Ensures OpenCV version is '4.5.3'.
- OpenCV Operation: Validates OpenCV can process images.
- Environment Requirements: Checks for dependency conflicts.
