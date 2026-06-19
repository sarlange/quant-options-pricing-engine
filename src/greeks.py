import numpy as np
from scipy.stats import norm


def calculate_greeks(S, K, T, r, sigma):

    d1 = (
        np.log(S / K)
        + (r + 0.5 * sigma**2) * T
    ) / (sigma * np.sqrt(T))

    d2 = d1 - sigma * np.sqrt(T)

    delta = norm.cdf(d1)
    gamma = norm.pdf(d1) / (
        S * sigma * np.sqrt(T)
    )
    vega = (
        S * norm.pdf(d1) * np.sqrt(T)
    ) / 100

    theta = (
        -S
        * norm.pdf(d1)
        * sigma
        / (2 * np.sqrt(T))
    ) / 365

    rho = (
        K
        * T
        * np.exp(-r * T)
        * norm.cdf(d2)
    ) / 100

    return {
        "Delta": round(delta, 4),
        "Gamma": round(gamma, 4),
        "Vega": round(vega, 4),
        "Theta": round(theta, 4),
        "Rho": round(rho, 4),
    }
