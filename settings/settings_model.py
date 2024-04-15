from pydantic import BaseModel
from pydantic import Field


class UniswapContractAbis(BaseModel):
    factory: str = Field(
        ...,
        example='pooler/modules/uniswapv3/static/abis/IUniswapV3Factory.json',
    )
    router: str = Field(
        ...,
        example='pooler/modules/uniswapv3/static/abis/UniswapV3Router.json',
    )
    quoter: str = Field(
        ...,
        example='pooler/modules/uniswapv3/static/abis/Quoter.json',
    )
    multicall: str = Field(
        ...,
        example='pooler/modules/uniswapv3/static/abis/UniswapV3Multicall.json',
    )
    pair_contract: str = Field(
        ...,
        example='pooler/modules/uniswapv3/static/abis/UniswapV3Pool.json',
    )
    erc20: str = Field(
        ...,
        example='pooler/modules/uniswapv3/static/abis/IERC20.json',
    )
    trade_events: str = Field(
        ...,
        example='pooler/modules/uniswapv3/static/abis/UniswapTradeEvents.json',
    )
    quoter_1inch: str = Field(
        ...,
        example='pooler/modules/uniswapv3/static/abis/OneInchQuoter.json',
    )


class ContractAddresses(BaseModel):
    uniswap_v3_factory: str = Field(
        ...,
        example='0x1F98431c8aD98523631AE4a59f267346ea31F984',
    )
    uniswap_v3_router: str = Field(
        ...,
        example='0xE592427A0AEce92De3Edee1F18E0157C05861564',
    )
    uniswap_v3_quoter: str = Field(
        ...,
        example='0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6',
    )
    uniswap_v3_multicall: str = Field(
        ...,
        example='0x5BA1e12693Dc8F9c48aAD8770482f4739bEeD696',
    )
    DAI_WETH_PAIR: str = Field(
        ...,
        example='0xC2eFb029Ed7EeCd775C21b53Fa594D5dA2D3febb',
    )
    USDC_WETH_PAIR: str = Field(
        ...,
        example='0x8ad599c3A0ff1De082011EFDDc58f1908eb6e6D8',
    )
    USDT_WETH_PAIR: str = Field(
        ...,
        example='0x0d4a11d5EEaaC28EC3F61d100daF4d40471f1852',
    )
    WETH: str = Field(
        ...,
        example='0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
    )
    MAKER: str = Field(
        ...,
        example='0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2',
    )
    QUOTER_1INCH: str = Field(
        ...,
        example='0x07D91f5fb9Bf7798734C3f606dB065549F6893bb',
    )
    USDC: str = Field(
        ...,
        example='0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
    )
    USDT: str = Field(
        ...,
        example='0xdAC17F958D2ee523a2206206994597C13D831ec7',
    )
    DAI: str = Field(
        ...,
        example='0x6B175474E89094C44Da98b954EedeAC495271d0F',
    )


class Settings(BaseModel):
    uniswap_contract_abis: UniswapContractAbis
    contract_addresses: ContractAddresses


class Settings(BaseModel):
    uniswap_contract_abis: UniswapContractAbis
    contract_addresses: ContractAddresses
