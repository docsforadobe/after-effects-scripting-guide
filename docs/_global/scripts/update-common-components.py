import os
import shutil
import tarfile
import tempfile
import urllib.request

org_name = "docsforadobe"
repo_name = "docsforadobe-mkdocs-config"
destination_dir = "./docs/_global"

def download_github_repo(org_name, repo_name, destination_dir):
    tar_url = f"https://api.github.com/repos/{org_name}/{repo_name}/tarball/main"

    response = urllib.request.urlopen(tar_url)

    if (response):
        with tempfile.TemporaryDirectory() as temp_dir:
            tar = tarfile.open(fileobj=response, mode="r|gz")
            tar_extraction_path = os.path.join(temp_dir, tar.firstmember.name)

            tar.extractall(path=temp_dir)

            # If already exist, remove first
            if (os.path.isdir(destination_dir)):
                shutil.rmtree(destination_dir)

            # Move from temp folder to destination folder
            shutil.move(tar_extraction_path, destination_dir)

download_github_repo(org_name, repo_name, destination_dir)
