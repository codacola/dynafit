# Dynafit - Modeling Linear Dynamical Systems 
Dynafit provides methods to model **linear dynamic systems** with and without constraints and to project traces of such systems state-vectors onto planes that emphasize specific dynamic properties of interest.

One particularly interesting projection is onto the planes which maximize the rotational components of the state-vector traces along time. The methods implemented here to perform the necessary calculations termed **jPCA** are drawn from the article [Neural population dynamics during reaching](https://www.nature.com/articles/nature11129), its supplementary materials and code examples. We'd like to encourage you to cite the original research article when you apply the jPCA code of this repository in your projects.

## Setup

### Dependencies
The following packages are used to perform simulatiom, fitting, matrix and vector operations:
- numpy >= 1.17
- scipy >= 1.3

The plots in `example.py` additionally require:
- matplotlib >= 3.1

### Installation
Clone or copy the repository in a folder of your choice and use pip to install the package into your python libs, e.g.
```
git clone https://github.com/codacola/dynafit.git
cd dynafit
pip install -e .
```

### Tests
Basic functionality and sanity checks can be performed using the *unittest* framework:
```
  python test.py
```
## Examples / Usage
The basic usage can be seen in `example.py`: 
1. Toy data can be simulated using `dynafit.simulation.lds()` which takes a dynamics matrix and generates sample traces of the corresponding dynamical system. Make sure that the absolute values of your dynamics matrices are all small compared to the simulation time-step (default: 1).
2. Use `dynafit.fit.fit_full` or `dynafit.fit.fit_skew()` to fit unconstrained and skew-symmetric models respectively
3. Project time-traces onto vectors of maximal rotation (jPCA) by calling `dynafit.projection.project_rotmax()'

## Participation
You're invited to contribute to this repository, just contact me and/or send a pull request.
