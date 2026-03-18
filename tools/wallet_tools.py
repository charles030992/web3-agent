def get_wallet_balance(address: str, *, simulate: bool = True) -> str:
    """
    Si simulate=True, devuelve un balance simulado.
    Más adelante, simulate=False hará llamada real a API on-chain.
    """
    if simulate:
        print(f"[SIM] Consultando balance de la wallet: {address}")
        return "2.35 ETH"

    # Placeholder para el futuro (modo real)
    # Aquí conectaremos a una API tipo Alchemy/Etherscan/Infura.
    raise NotImplementedError("Modo real no implementado todavía")