import subprocess
import os

# Set the current working directory to the repository root
repo_root = "/path/to/repo"
os.chdir(repo_root)

# Run the git pull command
result = subprocess.run(['git', 'pull'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=repo_root)

# Check if the pull was successful
if result.returncode == 0:
    with open("file.txt", "a") as file:
        file.write("Update: " + str(result.stdout))
        print("File updated successfully")
else:
    print("Error during git pull: " + str(result.stderr))
