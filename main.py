import subprocess

def trigger_github_action():
    # Create a dummy change
with open("trigger.txt", "w") as f:
        f.write("Triggering GitHub Actions")

    # Run git commands to commit and push the change
    subprocess.run(["git", "add", "trigger.txt"], check=True)
    subprocess.run(["git", "commit", "-m", "Trigger GitHub Action"], check=True)
    subprocess.run(["git", "push"], check=True)

if __name__ == "__main__":
    trigger_github_action()
