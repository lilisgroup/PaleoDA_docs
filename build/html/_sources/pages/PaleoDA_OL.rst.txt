.. _Overview of PDA_OL:

Overview of PDA_OL
==================

Proxies and simulations
--------------------------------------------------
1. Proxies are from the Past Global Changes 2k Network 
(PAGES2k `Emile-Geay et al. 2017 <https://www.nature.com/articles/sdata201788>`_) 
with temporal coverage of the Common Era (0-2000 CE) The proxy system model (PSM), 
i.e., the forward operator, is constructed by a linear univariate model for each kind of proxy, 
based on annual means / seasonal averages for tree-based proxies 
and annual means for the other kinds of proxies (`Tardif et al. 2019 <https://cp.copernicus.org/articles/15/1251/2019/>`_). 
For the :math:`p^{th}` proxy, the PSM is calibrated relative to the 
NASA Goddard Institute for Space Studies surface temperature analysis (GISTEMP; `Hansen et al. 2010 <https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2010RG000345>`_), 
through the linear regression that gives the best fit to the proxy data. 
The regression residual :math:`\sigma _p^2` is used as the observation error variance, 
i.e., the diagonal element of the diagonal matrix **R**

2. The model data is from the Community Earth System Model-Last Millennium Ensemble Project 
(CESM LME; `Otto-Bliesner et al., 2016 <https://journals.ametsoc.org/doi/10.1175/BAMS-D-14-00233.1>`_). 
Ensemble simulations of the CESM LME with full forcing, 
including the transient evolution of solar intensity, volcanic activity, 
orbital parameters, changes in land use/land cover and greenhouse gases, 
give a total of 13 full-forcing simulations from 850 to 2005 CE. 
For annual mean and seasonal averages, 
the monthly output is processed by removing the climatology over the entire period.


Surrogate models
---------------------------------
The traditional online DA advances the numerical model from the posteriors, 
and provides priors with flow-dependent uncertainties for next DA cycle. 
Instead of using numerical models that are computationally expensive, 
data-driven surrogate models are used here for PDA_OL. 
Due to the different time scales of proxy records, the PSM requires different 
seasonal averages. Therefore, the integrate time of the surrogate model is usually the average 
time scale of the proxies, which is generally 12 months for PAGES2k. Based on this, 
the surrogate model is designed to take in a continuous 12 months of SAT and SST fields and 
predict for the subsequent 12 months:

.. math:: {\bf{X}}_{t{\rm{ + 1:t + 12}}}^f = M\left( {{\bf{X}}_{t - 12:t}^a} \right)

where the superscripts :math:`f` and :math:`a` denote prior and posterior, respectively.
*M* is a self-attention-based surrogate model (`Zhou and Zhang 2023 <https://www.science.org/doi/10.1126/sciadv.adf2827>`_)

.. image:: transformer.png 

The loss function *L* is defined using the mean square eroor (MSE) of the 12 predictive months and the truth:

.. math:: L = \left\| {{\bf{X}}_{t + 1:t + 12}^{} - M\left( {{\bf{X}}_{t - 12:t}^{}} \right)} \right\|_{}^2

DA methods
---------------------------------    
Different from ensemble priors of offline DA 
that are randomly sampled from a climatological simulation, 
ensemble priors :math:`{\bf{x}}_{cyc,i}^f` (:math:`i =1,…,N`) of online DA are short-term forecasts based on the surrogate models. 
The ensemble mean :math:`{\bf{\bar x}}_{cyc}^f = \left( {1/N} \right)\sum\limits_{i = 1}^N {{\bf{x}}_{cyc,i}^f}`  
and ensemble perturbations :math:`{\bf{x'}}_{cyc,i}^f` (:math:`i =1,…,N`) are updated separately, 
but through the integrated hybrid EnKF (IHEnKF, `Lei et al. 2021 <https://journals.ametsoc.org/view/journals/mwre/149/12/MWR-D-21-0002.1.xml>`_) 
that is superior to the commonly used hybrid ensemble-variational method 
but within a pure ensemble framework.