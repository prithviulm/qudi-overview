[![Ruff](https://github.com/prithviulm/qudi-overview/actions/workflows/ruff.yml/badge.svg)](https://github.com/prithviulm/qudi-overview/actions/workflows/ruff.yml)
[![Testing](https://github.com/prithviulm/qudi-overview/actions/workflows/test.yml/badge.svg)](https://github.com/prithviulm/qudi-overview/actions/workflows/test.yml)


# Getting Started

We assume you already have `git` installed on your machine. If not, you can download it [here](https://git-scm.com/downloads) or ask your friendly neighborhood developer for help.

## Step 1: Clone the Repository

To clone the repository, open your terminal and run the following command:

```git
git clone https://github.com/prithviulm/qudi-overview.git
```

## Step 2: Install Dependencies

**If you have Qudi installed, then you already would have all the dependencies for this project and can skip this step.**

You must have Python 3.10 installed on your machine. We assume that you have an anaconda environment set up for Qudi already. If not, ask your friendly neighborhood developer for help.

<details>
  <summary>Click here you have not installed Qudi already</summary>

Run the following command if you are not using a virtual environment or have no idea what a virtual environment is:
```bash
pip install -r requirements.txt
```

or if you are using a virtual environment:

```bash
conda install --file requirements_conda.txt
```
</details>


## Step 3: Open the project

You're probably using PyCharm, so open the project in PyCharm. If you're not using PyCharm, then you either know what you're doing or you should be using PyCharm.

You probably cannot edit Jupyter Notebooks in PyCharm (but can read them), so you can open the notebooks in Jupyter Lab or Jupyter Notebook. Run either of the following commands in the project directory:

```bash
jupyter lab
```

or

```bash
jupyter notebook
```

This will open a new tab in your browser with the Jupyter interface. Now you can open the `experiment.ipynb` where you will complete most of your tasks.

## Step 4: Start Solving the Tasks!

This project mimics the basic structure of Qudi, mainly the modular structure of Qudi and some of the fundamentals e.g. `AbstractBaseClasses`, inheritance, getters, setters, etc. It also demonstrates some of the basic coding standards that we want to following in Qudi e.g. docstrings, type hints, PEP8, etc.

We first have the `hardware.py` that contains the `AbstractBaseClass` for the hardware. An `AbstractBaseClass` is a class that cannot be instantiated directly. It is used to define the methods that must be implemented by the subclasses (i.e. the actual hardware modules). In this case, the `Hardware` class is an `AbstractBaseClass` that has 4 abstract methods that all hardware modules must implement. Python will raise an error if you try to instantiate a class that does not implement all the abstract methods. You may encounter this when trying to use the `APD`.

Then we have the `acquisition.py` that emulates a logic module in Qudi. It gets data from any hardware i.e. it is hardware-agnostic.

Lastly, there is the `test_hardware.py` file which currently does not exist in Qudi but we are working on this. It contains unit tests for the hardware modules. Unit tests are used to test small units of code to ensure that they work as expected. This is important because it allows us to catch bugs early and can also help ensure that new code does not break existing code.

Remember to save the `.py` files after making changes (in PyCharm or whatever editor you're using). Then, you need to reload the modules in the Jupyter Notebook. You can do this by running the cell that literally says "Run this cell to reload...".

If you have any questions, feel free to ask your friendly neighborhood developer for help.

## Step 5: Submit Your Code as a Pull Request

TODO.
