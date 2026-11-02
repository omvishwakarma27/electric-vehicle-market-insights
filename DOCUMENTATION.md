# Project Documentation — Electric Vehicle Market Performance & Insights

## 1. Problem understanding
The project explores EV attributes such as manufacturers, model years, regions, vehicle category, price, range, battery characteristics and annual sales values to summarize patterns in the supplied data.

## 2. Tools
- Python and Pandas for data loading and inspection
- SQLite for database storage
- SQL for aggregation and filtering
- Tableau Desktop for visual analysis
- Flask for the web interface
- Git and GitHub for version control and project sharing

## 3. Data collection and storage
The supplied `ev_market_train.csv` file is the source dataset. `load_data.py` loads it into the SQLite table `ev_market`. The script reports row/column counts and missing-value summaries. The source CSV and generated database are excluded from Git by default.

## 4. SQL operations
Queries in `sql/queries.sql` demonstrate record counts, distinct counts, grouping, sorting, aggregate measures, and missing-value checks. Capture screenshots of the actual query results before submission.

## 5. Tableau data preparation
The CSV is connected directly in Tableau Desktop. Confirm data types, inspect null values, verify dimensions and measures, and document any exclusions or transformations actually applied.

## 6. Planned visualizations
Complete and describe the charts you actually build:
1. KPI summary — record count, average price, average range, and/or sales total.
2. Manufacturer comparison — records by manufacturer.
3. Regional sales comparison — sum of annual_sales_units by market_region.
4. Category distribution — records by category.
5. Price vs range — scatter plot using price_usd and range_km.
6. Model year distribution — record count by model_year.

## 7. Dashboard and filters
Combine completed worksheets into one dashboard. Add relevant filters such as manufacturer, market_region, category and model_year where useful. Test each filter and record screenshots.

## 8. Tableau story
Suggested scenes:
1. Overall dataset overview.
2. Manufacturer and category comparisons.
3. Regional and model-year patterns.
4. Price, range and environmental attributes.
Describe only findings supported by your charts.

## 9. Flask integration
The Flask page embeds published Tableau dashboard and story views using environment variables. The local app can run without these URLs, but a complete online demonstration requires real published Tableau embed URLs.

## 10. Performance testing
Record the source row count, load time, filter responsiveness and behavior at desktop/mobile widths. Report measured values, not estimates. The `/health` route checks whether the Flask service responds.

## 11. GitHub and demo
- GitHub repository: [Paste your real repository URL here]
- Live demo: [Paste your deployed URL here]
- Tableau dashboard: [Paste the published dashboard URL here]
- Tableau story: [Paste the published story URL here]

## 12. Conclusion
Summarize the major patterns actually observed in the dashboard, data-quality limitations, and potential improvements. Do not claim the project is deployed or tested until you have verified it.
