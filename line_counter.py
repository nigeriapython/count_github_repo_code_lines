import os
import subprocess
import tempfile
import shutil
from collections import defaultdict

def run_git_command(cmd, cwd):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Git command failed: {' '.join(cmd)}\n{result.stderr}")
    return result.stdout.strip()

def count_lines_by_extension(path):
    result = subprocess.run(['git', 'ls-files'], cwd=path, capture_output=True, text=True)
    files = result.stdout.splitlines()

    ext_counts = defaultdict(int)
    total_lines = 0

    for file in files:
        file_path = os.path.join(path, file)
        _, ext = os.path.splitext(file_path)
        ext = ext.lower() or 'NO_EXTENSION'

        try:
            with open(file_path, 'r', errors='ignore') as f:
                lines = sum(1 for _ in f)
                ext_counts[ext] += lines
                total_lines += lines
        except Exception as e:
            print(f"Could not read {file}: {e}")

    return total_lines, dict(ext_counts)

def count_lines_per_branch(repo_url):
    temp_dir = tempfile.mkdtemp()
    try:
        print(f"Cloning {repo_url} into {temp_dir}")
        run_git_command(['git', 'clone', '--quiet', repo_url, temp_dir], cwd='.')

        branches_output = run_git_command(['git', 'branch', '-r'], cwd=temp_dir)
        remote_branches = [line.strip().replace('origin/', '') for line in branches_output.splitlines()
                           if '->' not in line]

        branch_stats = {}

        for branch in remote_branches:
            print(f"\nChecking out branch: {branch}")
            run_git_command(['git', 'checkout', '--quiet', branch], cwd=temp_dir)

            total_lines, ext_stats = count_lines_by_extension(temp_dir)

            branch_stats[branch] = {
                'total_lines': total_lines,
                'by_extension': ext_stats
            }

            print(f"Branch '{branch}': {total_lines} total lines")
            for ext, count in ext_stats.items():
                print(f"  {ext}: {count} lines")

        return branch_stats

    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    repo_url = input("Enter the GitHub repository URL: ").strip()
    try:
        stats = count_lines_per_branch(repo_url)
        print("\nSummary:")
        for branch, data in stats.items():
            print(f"\nBranch: {branch}")
            print(f"  Total lines: {data['total_lines']}")
            print("  Lines by file type:")
            for ext, lines in sorted(data['by_extension'].items()):
                print(f"    {ext}: {lines}")
    except Exception as e:
        print(f"Error: {e}")
