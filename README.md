# dynafit
Dynafit provides methods to fit linear dynamic models with and without contraints on the dynamics matrices and to project the state-vectors onto planes that feature specific dynamic properties of interest.  

One particularly interesing projection is onto the planes which maximize the rotational components of the state-vector traces along time. The methods implemented here to perform the neccessary calculations termed **jPCA** projection are drawn from the article [Neural population dynamics during reaching](https://www.nature.com/articles/nature11129), its supplementary materials and code examples. 

If you use this repository for academic purposes please cite the orignal article.

## Setup

1. git clone https://github.com/codacola/dynafit.git
2. cd dynafit
3. pip install -e .
