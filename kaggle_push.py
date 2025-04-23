import os

notebook_path = "dummy_notebook.ipynb"
kaggle_username = os.environ['KAGGLE_USERNAME']
# kernel_slug = f"{kaggle_username}/kaggle-git.ipynb"
kernel_slug = "kavindu210588u/kaggle-and-git.ipynb"


# prepare kernel-metadata.json
kernel_meta = f"""
{{
  "id": "{kernel_slug}",
  "title": "Kaggle and Git",
  "code_file": "{notebook_path}",
  "language": "python",
  "kernel_type": "notebook",
  "is_private": true
}}
"""

with open("notebooks/kernel-metadata.json", "w") as f:
    f.write(kernel_meta)

os.system(f"kaggle kernels push -p notebooks")
