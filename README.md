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


### 3. Input GitHub repository

When prompted:

```bash
Enter the GitHub repository URL: https://github.com/nigeriapython/count_github_repo_code_lines.git
```

### 4. View Output

Example output:

```
Branch 'main': 1240 total lines
  .py: 1002 lines
  .md: 88 lines
  .html: 150 lines

Branch 'dev': 1380 total lines
  .py: 1120 lines
  .yml: 60 lines
  .js: 200 lines
```

---

## 📁 Output Details

Each branch report includes:

* `total_lines`: Total number of lines across all files in that branch
* `by_extension`: A breakdown of lines by file extension (including files without extensions)

If a file has no extension, it’s grouped under `NO_EXTENSION`.

---

## ⚠️ Notes

* This script only counts **Git-tracked files** (`git ls-files`)
* It **does not** count untracked or ignored files
* All line counts include **blank lines and comments**

---

## 🧪 Example Use Cases

* Audit the size and complexity of branches
* Compare development and production branch sizes
* Understand tech stack distribution by file type

---

## 🛠 Future Enhancements (Optional)

You can modify or extend the script to:

* Filter file types (e.g., exclude `.md`, `.json`)
* Count only non-empty lines or code lines (using regex)
* Export results to JSON/CSV
* Run against private repositories (with SSH or token auth)

---

## 🧹 Cleanup

The script uses `tempfile.mkdtemp()` and deletes the clone after execution, so **no files are left behind**.

---

## 👨‍💻 Author

Built using Python and Git.

Feel free to fork, modify, or contribute!

```

Let me know if you want a version with badges, license info, or GitHub Actions setup too.
```
