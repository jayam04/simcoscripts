# Author: ChatGPT 3.5
# Instructor: Jayam
# Setup file that creates virtual environment and install dependencies based on user type

import os
import subprocess
import venv


def create_virtualenv(venv_dir):
    venv.create(venv_dir, with_pip=True)


def install_dependencies(venv_dir, requirements_file, is_developer):
    pip_path = os.path.join(venv_dir, 'bin', 'pip')
    subprocess.run([pip_path, 'install', '-r', requirements_file])

    if is_developer:
        dev_requirements_file = 'dev_requirements.txt'
        if os.path.exists(dev_requirements_file):
            subprocess.run([pip_path, 'install', '-r', dev_requirements_file])
        else:
            print("dev_requirements.txt not found. Skipping developer dependencies.")


def main():
    venv_dir = '.venv'  # Change this to your desired virtual environment directory
    requirements_file = 'requirements.txt'  # Change this to your requirements file

    is_developer = input("Do you want to install developer dependencies? (y/n): ").strip().lower() == 'y'

    create_virtualenv(venv_dir)
    install_dependencies(venv_dir, requirements_file, is_developer)


if __name__ == "__main__":
    main()
