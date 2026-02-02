# Contributing to MPR Viewer

Thank you for your interest in contributing! 🎉

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/ebrahimnas577/mpr-viewer/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version, etc.)
   - Screenshots if applicable

### Suggesting Features

1. Open an issue with the `enhancement` label
2. Describe the feature and its benefits
3. Provide examples or mockups if possible

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest tests/`)
5. Format code (`black src/`)
6. Commit changes (`git commit -m 'Add amazing feature'`)
7. Push to branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Code Style

- Follow PEP 8
- Use Black for formatting
- Add docstrings to functions and classes
- Write tests for new features

### Development Setup

```bash
git clone https://github.com/ebrahimnas577/mpr-viewer.git
cd mpr-viewer
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src/mpr_viewer

# Run specific test file
pytest tests/test_volume_loader.py
```

### Code Formatting

```bash
# Format all code
black src/

# Check code style
flake8 src/

# Type checking
mypy src/
```

## Code of Conduct

Be respectful, inclusive, and professional in all interactions.

## Questions?

Feel free to open an issue or contact the maintainers.

---

Thank you for contributing to MPR Viewer! 🚀