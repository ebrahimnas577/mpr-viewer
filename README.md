# ⚡ MPR Viewer ⚡

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**Advanced Multi-Planar Reconstruction System for Medical Imaging**

[Features](#features) • [Installation](#installation) • [Quick Start](#quick-start) • [Documentation](#documentation) • [Contributing](#contributing)

</div>

---

## 🎯 Overview

MPR Viewer is a powerful, open-source medical imaging application that provides advanced multi-planar reconstruction (MPR) capabilities with AI-powered organ detection. Built with PyQt5 and modern deep learning frameworks, it offers an intuitive interface for visualizing and analyzing 3D medical volumes.

## ✨ Features

### 🔬 Core Capabilities
- **Multi-Format Support**: Load DICOM series, NIfTI files, and NumPy arrays
- **Multi-Planar Reconstruction**: Interactive Axial, Sagittal, Coronal, and Oblique views
- **AI-Powered Analysis**:
  - Automatic organ detection using TotalSegmentator
  - Volume orientation classification
- **Interactive Oblique Slicing**: Rotate planes using intuitive crosshair handles
- **Segmentation Visualization**: Contour mode with multi-label support

### 🎨 Visualization
- Synchronized crosshair navigation across all views
- Real-time zoom and pan controls
- Cine playback mode for all views
- Cyberpunk-inspired dark theme UI
- Plane intersection visualization

### 🛠️ Analysis Tools
- ROI (Region of Interest) selection and extraction
- Volume export (.npy, .nii.gz)
- Slice saving (PNG, NumPy)
- Bounding box computation for segmentations

### ⚡ Performance
- Efficient trilinear interpolation for oblique slicing
- Optimized rendering for large volumes
- Multi-threaded AI inference

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Option 1: Install from PyPI (Coming Soon)
```bash
pip install mpr-viewer
```

### Option 2: Install from Source

1. **Clone the repository**
```bash
git clone https://github.com/ebrahimnas577/mpr-viewer.git
cd mpr-viewer
```

2. **Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install the package**
```bash
pip install -e .
```

---

## 🚀 Quick Start

### Basic Usage

```python
from mpr_viewer import MPRApp
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
viewer = MPRApp()
viewer.show()
sys.exit(app.exec_())
```

### Or run directly:
```bash
python -m mpr_viewer
```

### Loading Data

1. **Load DICOM**: Click "Load DICOM" → Select folder containing DICOM series
2. **Load NIfTI**: Click "Load NIfTI/NumPy" → Select .nii/.nii.gz/.npy file
3. **Navigate**: Click on any view to set crosshair, scroll to change slices
4. **Zoom**: Ctrl + Scroll or use zoom buttons

### AI Features

#### Organ Detection
```bash
# Requires TotalSegmentator
pip install totalsegmentator

# In the app:
# 1. Load a CT volume
# 2. Click "Detect Organ (AI)"
# 3. Wait for analysis (uses fast mode)
```

#### Orientation Detection
```bash
# Place model.keras in the application directory
# Click "Run AI (orientation)" to detect volume orientation
```

---

## 📚 Documentation

- [Installation Guide](docs/installation.md)
- [User Guide](docs/user_guide.md)
- [API Reference](docs/api_reference.md)
- [Examples](examples/)

---

## 🎮 Usage Examples

### Example 1: Load and Visualize a NIfTI Volume

```python
import numpy as np
from mpr_viewer import MPRApp
from PyQt5.QtWidgets import QApplication

# Create sample volume
volume = np.random.rand(100, 100, 100)
np.save('sample_volume.npy', volume)

# Launch viewer
app = QApplication([])
viewer = MPRApp()
# Use File menu to load sample_volume.npy
viewer.show()
app.exec_()
```

### Example 2: Extract ROI Programmatically

```python
# See examples/example_usage.py for complete examples
```

---

## 🧪 Dependencies

### Core Dependencies
- **PyQt5**: UI framework
- **NumPy**: Numerical computing
- **Matplotlib**: Visualization backend
- **SciPy**: Scientific computing

### Optional Dependencies
- **nibabel**: NIfTI file support
- **pydicom**: DICOM file support
- **scikit-image**: Contour detection
- **TotalSegmentator**: AI organ segmentation
- **Keras/TensorFlow/PyTorch**: AI orientation detection

See [requirements.txt](requirements.txt) for full list.

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Clone repo
git clone https://github.com/ebrahimnas577/mpr-viewer.git
cd mpr-viewer

# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Run with development mode
python -m mpr_viewer
```

---

## 🐛 Known Issues

- Oblique slicing performance may be slow on very large volumes (>512³)
- TotalSegmentator requires significant RAM for full-body CT scans
- PyTorch backend for Keras may require disabling TorchDynamo on some systems

See [Issues](https://github.com/ebrahimnas577/mpr-viewer/issues) for more.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **TotalSegmentator**: AI organ segmentation framework
- **PyQt5**: Cross-platform UI framework
- **Medical imaging community**: For invaluable feedback and testing

---

## 📧 Contact

- **GitHub**: [@ebrahimnas577](https://github.com/ebrahimnas577)

---

<div align="center">

**⚡ Built with passion for medical imaging ⚡**

[⬆ Back to Top](#-mpr-viewer-)

</div>