from pydantic import BaseModel, Field

class IFRS(BaseModel):
    revenue: float = Field(
        default=0.0,
        description="Total income generated from the company's primary operations before taxes and discounts."
    )
    
    profit_before_tax: float = Field(
        default=0.0,
        description="Profit earned before accounting for tax obligations."
    )
    
    net_profit: float = Field(
        default=0.0,
        description="Profit remaining after all expenses, including taxes, have been deducted."
    )
    
    assets: float = Field(
        default=0.0,
        description="Total resources controlled by the company that have economic value."
    )
    
    liabilities: float = Field(
        default=0.0,
        description="Total debts and financial obligations of the company."
    )
    
    equity: float = Field(
        default=0.0,
        description="The difference between assets and liabilities, representing the owners' interest in the company."
    )
    
    current_liquidity_ratio: float = Field(
        default=0.0,
        description="A measure of the company's ability to cover its short-term obligations with current assets."
    )
    
    debt_to_assets_ratio: float = Field(
        default=0.0,
        description="The ratio of total liabilities to total assets, indicating the level of financial risk."
    )
    
    return_on_assets: float = Field(
        default=0.0,
        description="A measure of profitability relative to total assets, indicating how efficiently assets are used."
    )
    
    return_on_equity: float = Field(
        default=0.0,
        description="A measure of profitability relative to shareholders' equity, indicating how effectively equity is used."
    )
    
    cash_flows: float = Field(
        default=0.0,
        description="Net cash generated or used in operating, investing, and financing activities."
    )
