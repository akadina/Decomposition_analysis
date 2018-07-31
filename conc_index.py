import numpy as np
import pandas as pd

def conc_index(data, wealth_group, var):
    '''data frame should contain column representing the wealth group of each household
    Args: data (pandas DataFrame or something that can make a DataFrame) - data set,
        wealth_group (str) - column name corresponding to wealth percentile,
        var (str) - column corresponding to a variable for which CI is to be calculated,
    Returns: conc_index(float) - concentration index*
    
    *as per Kakwani et al. Socioeconomic inequalities in health: Measurement, computation, and statistical inference.
    http://www.sciencedirect.com/science/article/pii/S0304407696018076'''
    
    if not isinstance(data, pd.DataFrame):
        df = pd.DataFrame(data)
    
    df = data[[wealth_group, var]]
    df.dropna(inplace=True)
    var_overall_mean = df[var].mean()
    summary = df.groupby(wealth_group).agg(['mean', 'count']).reset_index()
    summary.columns = summary.columns.droplevel(0)
    total_var = summary['count'].sum()
    summary['Rel % of {}'.format(var)] = summary['count'] / total_var
    summary['Cumul % of {}'.format(var)] = summary['Rel % of {}'.format(var)].cumsum()
    summary['Rank'] = np.nan_to_num(summary['Cumul % of {}'.format(var)].shift(1)) + 0.5 * summary['Rel % of {}'.format(var)]
    summary['fmuR'] = summary['mean'] * summary['Rel % of {}'.format(var)] * summary['Rank']
    conc_index = 2.0 / var_overall_mean * summary['fmuR'].sum() - 1
    return conc_index