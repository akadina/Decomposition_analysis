# Decomposition_analysis
Decomposing inequality in health care utilization.

Note: for now, only calculation of the concentration index is available.

Concentration index is a measure of inequality. Procedure for evaluation is described in

Kakwani et al. Socioeconomic inequalities in health: Measurement, computation, and statistical inference.
http://www.sciencedirect.com/science/article/pii/S0304407696018076

Function expects a dataset in a form of pandas DataFrame or something that can be converted to DataFrame, as well as names of the columns that correspond to wealth rank of a household/individual and variable for which concentration index is to be calculated.

Returns: concentration index calculated using Kakwani method.
