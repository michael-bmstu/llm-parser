# LLM IFRS financial statements parser
The annual IFRS financial statements of issuers differs from each other in format, therefore, for the convenience of extracting key indicators, a special parser is required.

## Project struct
- `research.ipynb` : testing pdf parsing functional
- `main.py` : FastAPI application run file
- **`app`** : Application's modules
    - `utils.py` : Parsing functions
    - `models.py` : Pydantic models for PydanticOutputParser
    - `logger.py` :
    - `interface.py` : Gradio interface
- `requirements.txt`

<details>
<summary style="font-size: 20px;"><b>Key Indicators of IFRS financial reporting that will be parsed</b></summary>

Financial reporting under International Financial Reporting Standards (IFRS) includes several key indicators that help assess a company's financial position and performance. Here are the main ones:

### 1. Revenue (Выручка)
Revenue represents the total income generated from the sale of goods or services before any expenses are deducted. Under IFRS, revenue recognition is based on the transfer of control of goods or services to customers, which can occur at a point in time or over time.

### 2. Profit Before Tax (Прибыль до налогообложения)
Profit before tax (PBT) is the income earned by a company before deducting income tax expenses. It is calculated by subtracting all operating expenses, interest, and other non-operating expenses from total revenue. PBT provides insight into a company's operational efficiency and profitability.

### 3. Net Profit (Чистая прибыль)
Net profit, also known as net income or net earnings, is the amount of money that remains after all expenses, including taxes, have been deducted from total revenue. It is a key indicator of a company's profitability and is often used to assess overall financial health.

### 4. Assets (Активы)
Assets are resources owned by a company that are expected to provide future economic benefits. Under IFRS, assets are classified into current (expected to be converted into cash or used within one year) and non-current (long-term assets). Examples include cash, inventory, property, and equipment.

### 5. Liabilities (Обязательства)
Liabilities are obligations that a company owes to external parties, which are expected to be settled in the future. Similar to assets, liabilities are classified as current (due within one year) and non-current (long-term). Examples include loans, accounts payable, and accrued expenses.

### 6. Equity (Капитал)
Equity represents the residual interest in the assets of a company after deducting liabilities. It reflects the ownership interest of shareholders and includes items such as common stock, retained earnings, and additional paid-in capital. Equity is a crucial measure of a company's financial stability.

### 7. Current Liquidity Ratio (Текущий ликвидный коэффициент)
The current liquidity ratio, or current ratio, is a financial metric that measures a company's ability to pay its short-term obligations with its short-term assets. It is calculated by dividing current assets by current liabilities. A ratio above 1 indicates that the company has more current assets than current liabilities.

### 8. Debt to Assets Ratio (Коэффициент задолженности к активам)
The debt to assets ratio is a financial leverage ratio that indicates the proportion of a company's assets that are financed by debt. It is calculated by dividing total liabilities by total assets. A higher ratio suggests greater financial risk, as it indicates a higher reliance on borrowed funds.

### 9. Return on Assets (ROA) (Рентабельность активов)
Return on assets is a profitability ratio that measures how effectively a company uses its assets to generate profit. It is calculated by dividing net profit by total assets. A higher ROA indicates more efficient use of assets in generating earnings.

### 10. Return on Equity (ROE) (Рентабельность собственного капитала)
Return on equity is a measure of a company's profitability relative to shareholders' equity. It is calculated by dividing net profit by average shareholders' equity. A higher ROE indicates that the company is effectively using equity financing to generate profits.

### 11. Cash Flows (Денежные потоки)
Cash flows refer to the movement of cash into and out of a business. Under IFRS, cash flows are categorized into three activities: operating, investing, and financing. Analyzing cash flows helps assess a company's liquidity, solvency, and overall financial health.

### Conclusion
These IFRS indicators provide valuable insights into a company's financial performance and position. They are essential for investors, analysts, and stakeholders to make informed decisions regarding the company's operations and future prospects. Understanding these metrics can help in evaluating a company's profitability, liquidity, and financial stability.


These indicators help investors, analysts, and other stakeholders make informed decisions based on the company's financial reporting.
</details>