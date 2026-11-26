# Looker Studio Dashboard · Duka Electronics H1 2026

**Public link:** TODO: paste your Looker Studio link here (Share → Manage access → "Anyone with the link can view").

## Screenshots

TODO: add at least two screenshots to a `screenshots/` folder and reference them here, for example:

![Dashboard overview: scorecards and trend](screenshots/dashboard_overview.png)

![Dashboard breakdowns and filter controls](screenshots/dashboard_filters.png)

## Data source

`duka_dashboard_data.csv` (created by `board_report.ipynb`, 1,000 rows): `order_id`, `order_date` (ISO `YYYY-MM-DD`), `branch`, `product`, `channel`, `quantity`, `unit_price`, `revenue`. Import it into Google Sheets (File → Import), then add the sheet as the Looker Studio data source and confirm that `order_date` is typed **Date** and `revenue` **Number**.

## What the dashboard contains

- **Scorecards:** total revenue (sum of `revenue`), number of orders (Count Distinct of `order_id`) and average order value (calculated field `SUM(revenue) / COUNT_DISTINCT(order_id)`).
- **Trend:** time series of revenue by `order_date`, date granularity set to Month.
- **Breakdowns:** sorted bar chart of revenue by branch and a second bar chart of revenue by product.
- **Controls:** a date-range control and a drop-down control for channel; test that every chart responds to both.
- **Design:** PLP colours (#8E0000 highlight, #0BA184 accent), an insight title on each chart and a source text box ("Source: Duka POS system, Jan-Jun 2026").
