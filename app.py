import streamlit as st

from src.black_scholes import (
    black_scholes_price,
)
from src.greeks import (
    calculate_greeks,
)
from src.monte_carlo import (
    monte_carlo_option_price,
)

st.title(
    "Quant Options Pricing Engine"
)

S = st.number_input(
    "Stock Price",
    value=100.0,
)

K = st.number_input(
    "Strike Price",
    value=100.0,
)

T = st.number_input(
    "Time to Maturity (Years)",
    value=1.0,
)

r = st.number_input(
    "Risk-Free Rate",
    value=0.05,
)

sigma = st.number_input(
    "Volatility",
    value=0.20,
)

if st.button("Calculate"):

    bs_price = black_scholes_price(
        S, K, T, r, sigma
    )

    mc_price = monte_carlo_option_price(
        S, K, T, r, sigma
    )

    greeks = calculate_greeks(
        S, K, T, r, sigma
    )

    st.subheader("Results")

    st.write(
        f"Black-Scholes Price: ${bs_price}"
    )

    st.write(
        f"Monte Carlo Price: ${mc_price}"
    )

    st.write("Greeks")

    st.json(greeks)
