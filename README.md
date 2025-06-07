# GitHub Repository Line Counter by Branch and File Type

This Python script analyzes a GitHub repository to report:

- ✅ Total number of lines of code per **Git branch**
- ✅ A breakdown of lines of code by **file type** (extension) within each branch

It clones the specified repository, checks out each remote branch, and counts all lines (including comments and blank lines) for all tracked files.

---

## 📦 Features

- 🧠 Automatically clones a public GitHub repo into a temporary directory
- 🔀 Iterates over all **remote branches**
- 📁 Lists all Git-tracked files per branch
- 🧮 Counts:
  - Total lines of code
  - Lines of code per file extension (e.g., `.py`, `.js`, `.html`)
- 🧹 Cleans up all temporary files after analysis

---

## 📌 Requirements

- Python 3.6+
- `git` must be installed and accessible via the command line
- Internet connection (to clone the repo)

---

## 🚀 Usage

### 1. Save the script

Save the script in a file called `line_counter.py`.

### 2. Run the script

```bash
python line_counter.py
