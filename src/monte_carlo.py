import numpy as np


def monte_carlo_option_price(
    S,
    K,
    T,
    r,
    sigma,
    simulations=10000,
):

    z = np.random.standard_normal(
        simulations
    )

    ST = S * np.exp(
        (r - 0.5 * sigma**2) * T
        + sigma * np.sqrt(T) * z
    )

    payoffs = np.maximum(ST - K, 0)

    option_price = np.exp(
        -r * T
    ) * np.mean(payoffs)

    return round(option_price, 4)
