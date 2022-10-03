# pLUTo - In-House Performance and Energy Simulator

## Steps to Reproduce

You may reproduce our results in one of two ways:

### Option #1 (Recommended): Follow the Step-by-Step Instructions in the Provided Jupyter Notebook

1. Ensure that Python 3.x is available on your system
2. Install the required dependencies (NumPy and pandas) using `pip install -r requirements.txt`
3. Launch the simulation walkthrough file by opening `sim_walkthrough.ipynb` as a Jupyter notebook and execute all cells

### Option #2: Manually Execute the In-House Simulator

1. Ensure you have Python 3.x available on your system
2. Install the required dependencies (NumPy and pandas) using `pip install -r requirements.txt`
3. `cd` into the `pluto_sim` directory
4. Run the simulator with `python pluto_sim.py`
5. A directory named `pysim` should be created under `pluto_sim`; this directory should contain three files identical to the ones provided in the folder `pysim_reference`
