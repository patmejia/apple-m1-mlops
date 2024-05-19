# apple-m1-mlops

Apple M1-specific setup for machine learning engineering production systems, focusing on MLOps practices with Metal acceleration.

For detailed acknowledgments, please see the [MLOps](https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/tree/main/course1/week1-ungraded-lab). This project is part of [deeplearning.ai](https://www.deeplearning.ai/)'s Machine Learning Engineering for Production Specialization.

## Start Here

### [Clone the repository](https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public)

```bash
git clone https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public.git
```

### 1. Navigate to the directory

```bash
cd machine-learning-engineering-for-production-public/course1/week1-ungraded-lab
```

### 2.Environment Setup

```bash
conda create --name mlep-w1-lab python=3.8
conda activate mlep-w1-lab
```

#### i. General Setup - no Apple M1

```bash
pip install -r requirements.txt
```

#### ii. Apple M1 users: 

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
# Install modified requirements
pip install -r requirements-m1.txt
```


### 3. Verify Installations

```bash
python -c "import tensorflow as tf; print('TensorFlow Version:', tf.__version__)"
python -c "import cv2; print('OpenCV Version:', cv2.__version__)"
```


### 4. Launch Jupyter Lab

```bash
jupyter lab
```

### 5. Access Jupyter Lab and Run the Notebook

i. Copy the URL from the terminal and paste it into your browser to open the `server.ipynb` notebook.

```plaintext
http://localhost:8888/lab/tree/course1/week1-ungraded-lab/server.ipynb
```

ii. Run the cells by clicking on each and pressing `Shift + Enter` or using the play button.