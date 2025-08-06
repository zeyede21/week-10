import pymc3 as pm
import numpy as np

try:
    from distutils.msvccompiler import get_build_version
    print(f"MSVC Compiler Version: {get_build_version()}")
except ImportError:
    print("distutils.msvccompiler module not found. Ensure you have the necessary build tools installed.")

def build_change_point_model(data):
    """Builds a basic Bayesian change point model with PyMC3."""
    n = len(data)
    with pm.Model() as model:
        # Prior for switch point
        tau = pm.DiscreteUniform('tau', lower=0, upper=n)

        # Priors for means before and after change
        mu_1 = pm.Normal('mu_1', mu=np.mean(data), sd=np.std(data))
        mu_2 = pm.Normal('mu_2', mu=np.mean(data), sd=np.std(data))

        # Shared std deviation
        sigma = pm.HalfNormal('sigma', sd=1.0)

        # Define the means using switch logic
        mu = pm.math.switch(tau >= np.arange(n), mu_1, mu_2)

        # Likelihood
        obs = pm.Normal('obs', mu=mu, sd=sigma, observed=data)

    return model