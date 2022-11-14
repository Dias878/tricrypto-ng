from eth_utils import to_checksum_address


def mint_for_testing(token_contract, addr, amount):

    addr = to_checksum_address(addr)

    if token_contract.symbol() == "WETH":
        token_contract.deposit(value=amount)
    else:
        token_contract.eval(f"self.total_supply += {amount}")
        token_contract.eval(f"self.balanceOf[{addr}] += {amount}")
        token_contract.eval(f"log Transfer(empty(address), {addr}, {amount})")
