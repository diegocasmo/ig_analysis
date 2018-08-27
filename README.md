# WIP: ig_analysis (Instagram Analysis)

### Installation
  - [Install Anaconda or Miniconda](https://conda.io/docs/user-guide/install/macos.html)
  - Run ``conda env create -f environment.yml`` to install dependencies
  - Run ``source activate ig_analysis`` to activate environment
  - Copy ``.env.example`` file to ``.env`` and set up the environment variables accordingly

### Usage
  - Run ``python scripts/main.py`` in your terminal to get IG user data (this will create a number of ``.csv`` files in the ``/data`` directory)
  - Open ``analysis/ig_analysis.ipynb`` with Jupyter and run the cells to see the analysis of the IG user data
    - The folder name (where the data is saved inside the ``./data` directory) is retrieved from an environment variable. Make sure it's correctly set in ``.env`` (``'{}-{}'.format(api.username, api.username_id)``).
