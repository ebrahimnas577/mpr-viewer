from setuptools import setup, find_packages
import os

# Read long description from README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="mpr-viewer",
    version="2.0.0",
    author="Ebrahim Nasser",
    author_email="ebrahimnas577@gmail.com",
    description="Advanced Multi-Planar Reconstruction System for Medical Imaging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ebrahimnas577/mpr-viewer",
    project_urls={
        "Bug Tracker": "https://github.com/ebrahimnas577/mpr-viewer/issues",
        "Documentation": "https://github.com/ebrahimnas577/mpr-viewer/docs",
        "Source Code": "https://github.com/ebrahimnas577/mpr-viewer",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: X11 Applications :: Qt",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
        "torch": ["torch>=2.0.0"],
        "tensorflow": ["tensorflow>=2.10.0"],
        "onnx": ["onnxruntime>=1.14.0"],
    },
    entry_points={
        "console_scripts": [
            "mpr-viewer=mpr_viewer.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "mpr_viewer": ["models/*.keras", "models/*.onnx"],
    },
)