import os

kaggle_username = os.environ['KAGGLE_USERNAME']
notebook_slug = f"{kaggle_username}/kaggle-git"

os.system(f"kaggle kernels output {notebook_slug} -p kaggle_outputs")
