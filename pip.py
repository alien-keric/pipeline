#!/bin/python3

#initilization

import os
import shutil

def separate_frontend_backend(src_dir, frontend_dir, backend_dir):
    """
    Separate frontend and backend files into their respective directories.
    """
    frontend_extensions = ['.html', '.css', '.js', '.jsx', '.vue', '.ts', '.tsx', '.scss', '.sass', '.less', '.styl', '.svg', '.png', '.jpg', '.gif']
    backend_extensions = ['.py', '.java', '.rb', '.php', '.cs', '.cpp', '.h', '.m', '.swift', '.go', '.ts', '.js', '.sql', '.pl']

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(tuple(frontend_extensions)):
                shutil.move(os.path.join(root, file), os.path.join(frontend_dir, file))
            elif file.endswith(tuple(backend_extensions)):
                shutil.move(os.path.join(root, file), os.path.join(backend_dir, file))

def main():
    # specifing the source dir
    src_dir = '/var/www/html/'  # Change this to your source directory
    frontend_dir = 'frontend'
    backend_dir = 'backend'

    os.makedirs(frontend_dir, exist_ok=True)
    os.makedirs(backend_dir, exist_ok=True)

    # Separate frontend and backend files
    separate_frontend_backend(src_dir, frontend_dir, backend_dir)

    # Continue with your pipeline stages
    print("Files separated successfully. Continuing with pipeline stages...")

if __name__ == "__main__":
    main()


