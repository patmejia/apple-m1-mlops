import tensorflow as tf
import cv2
import numpy as np
import subprocess

def test_tensorflow_version():
    try:
        version = tf.__version__
        print(f'TensorFlow Version: {version}')
        assert version.startswith('2'), "TensorFlow version should start with '2'"
    except Exception as e:
        print(f"TensorFlow version test failed: {e}")
        raise

def test_tensorflow_operation():
    try:
        with tf.device('/GPU:0'):
            a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
            b = tf.constant([[1.0, 1.0], [0.0, 1.0]])
            result = tf.matmul(a, b)
            assert result is not None, "TensorFlow operation failed"
    except Exception as e:
        print(f"TensorFlow operation test failed: {e}")
        raise

def test_opencv_version():
    try:
        version = cv2.__version__
        print(f'OpenCV Version: {version}')
        assert version.startswith('4.5.3'), "OpenCV version should be '4.5.3'"
    except Exception as e:
        print(f"OpenCV version test failed: {e}")
        raise

def test_opencv_operation():
    try:
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        assert gray_img is not None, "OpenCV operation failed"
    except Exception as e:
        print(f"OpenCV operation test failed: {e}")
        raise

def test_environment_requirements():
    try:
        result = subprocess.run(['pip', 'check'], capture_output=True, text=True)
        if result.returncode != 0:
            raise AssertionError(f"Dependency check failed: {result.stdout}")
    except Exception as e:
        print(f"Environment requirements test failed: {e}")
        raise

if __name__ == '__main__':
    try:
        test_tensorflow_version()
        test_tensorflow_operation()
        test_opencv_version()
        test_opencv_operation()
        test_environment_requirements()
        print("All tests passed successfully.")
    except AssertionError as e:
        print(f"Test failed: {e}")
        raise
