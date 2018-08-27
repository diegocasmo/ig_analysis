# ig_analysis (Instagram Analysis)

## Installation
  - [Install Anaconda or Miniconda](https://conda.io/docs/user-guide/install/macos.html)
  - Run ``conda env create -f environment.yml`` to install dependencies
  - Run ``source activate ig_analysis`` to activate environment
  - Copy ``.env.example`` file to ``.env`` and set up the environment variables accordingly

## Usage
  - Run 'python scripts/main.py' in your terminal to get IG user data (this will create a number of .csv files in the ``/data`` directory)
  - Open ``analysis/ig_analysis.ipynb`` with Jupyter to and run cells to see the analysis of the IG user data
