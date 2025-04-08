# Use: python update_urls.py /path/to/local/repo https://old-url https://new-url

# /path/to/local/repo: The local path to your cloned GitHub repository.
# https://old-url: The old Codespaces URL you want to replace.
# https://new-url: The new Codespaces URL you want to use.

import os
import sys
import git

# Function to replace the URL in a file
def replace_url_in_file(file_path, old_url, new_url):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

        # Replace the old URL with the new one
        if old_url in file_content:  # Only replace if the old URL is found
            new_content = file_content.replace(old_url, new_url)

            # Write the modified content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Replaced URL in file: {file_path}")
        else:
            print(f"No URL found to replace in: {file_path}")
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# Function to walk through the repository and replace the URL in all files
def replace_url_in_repo(repo_path, old_url, new_url):
    # Walk through the files in the repository
    for root, dirs, files in os.walk(repo_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Only process files that are text-based (e.g., markdown, yml, etc.)
            if file_path.endswith(('.md', '.yml', '.yaml', '.json', '.txt', '.html', '.js', '.css')):
                print(f"Processing file: {file_path}")
                replace_url_in_file(file_path, old_url, new_url)

# Function to commit and push the changes back to GitHub
def commit_and_push_changes(repo_path, new_url):
    try:
        repo = git.Repo(repo_path)
        repo.git.add('--all')  # Stage all changes
        repo.index.commit(f"Update Codespaces URL to {new_url}")  # Commit changes
        origin = repo.remotes.origin
        origin.push()  # Push changes to the remote repository
        print(f"Changes committed and pushed to GitHub with new URL: {new_url}")
    except Exception as e:
        print(f"Error during Git commit/push: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python update_urls.py <repo_path> <old_url> <new_url>")
        sys.exit(1)

    repo_path = sys.argv[1]
    old_url = sys.argv[2]
    new_url = sys.argv[3]

    # Replace URLs in the repository files
    replace_url_in_repo(repo_path, old_url, new_url)

    # Commit and push the changes
    commit_and_push_changes(repo_path, new_url)

    print(f"All URLs replaced from {old_url} to {new_url} and changes pushed to GitHub!")

if __name__ == "__main__":
    main()
