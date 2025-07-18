from pydantic import BaseModel, Field
from typing import List, Optional

class IFRS(BaseModel):
    revenue_recognition: str = Field(..., description="Description of revenue recognition principles under IFRS.")
    financial_position_indicators: List[str] = Field(..., description="Key indicators related to financial position.")
    profitability_ratios: List[str] = Field(..., description="Ratios that measure profitability.")
    liquidity_ratios: List[str] = Field(..., description="Ratios that assess liquidity.")
    solvency_ratios: List[str] = Field(..., description="Ratios that evaluate solvency.")
    cash_flow_indicators: List[str] = Field(..., description="Indicators related to cash flow.")
    investment_indicators: List[str] = Field(..., description="Indicators that assess investment performance.")
    comprehensive_income: Optional[str] = Field(None, description="Description of comprehensive income components.")
    segment_reporting: Optional[str] = Field(None, description="Details on segment reporting requirements.")
    fair_value_measurement: Optional[str] = Field(None, description="Explanation of fair value measurement techniques.")

# Example usage with PydanticOutputParser
from langchain_core.output_parsers import PydanticOutputParser

ifrs_parser = PydanticOutputParser(pydantic_object=IFRS)
