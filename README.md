# Electric Vehicle Market Performance & Insights

A beginner-friendly data analytics project using Python, SQLite/SQL, Tableau Desktop and Flask.

## Project objectives
- Explore EV vehicle specifications and market attributes in the supplied dataset.
- Query and summarize data using SQL.
- Build interactive Tableau worksheets, a dashboard and a story.
- Present published Tableau views inside a responsive Flask website.

## Dataset
The source file used during development is `ev_market_train.csv` (expected fields include manufacturer, model_year, market_region, category, price_usd, range_km, annual_sales_units and customer_rating).

**Data privacy and licensing:** do not commit the full source dataset unless you have permission to redistribute it. The `.gitignore` excludes the CSV and database by default. For a public demo, publish only data you are allowed to share.

## Project structure
- `app.py` — Flask application.
- `templates/index.html` — responsive page with Tableau embed slots.
- `static/style.css` — page styling and mobile layout.
- `load_data.py` — loads the CSV into SQLite and checks the imported row count.
- `sql/queries.sql` — sample analytical SQL.
- `requirements.txt` — dependencies.
- `render.yaml` — optional Render deployment blueprint.

## Run the database loader
Put `ev_market_train.csv` in this folder (it is intentionally not tracked by Git), then run:
```bash
python -m pip install -r requirements.txt
python load_data.py
```
This creates `ev_market.db`. SQLite is used for the SQL demonstration; Tableau may continue using its already-connected CSV.

## Run Flask locally
```bash
python -m pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000`. The website will show setup instructions until published Tableau URLs are configured.

## Add Tableau views
1. Finish and save your dashboard and story in Tableau Desktop.
2. Publish them to Tableau Public only if the data is appropriate for public release.
3. Open each published view and copy its embed code or embed URL.
4. Set these environment variables in your deployment provider:
   - `TABLEAU_DASHBOARD_URL` — dashboard embed URL.
   - `TABLEAU_STORY_URL` — story embed URL.
5. Redeploy/restart the Flask app and test the page on desktop and mobile.

Use the embed URL, not a local file path such as `C:\\...` and not the GitHub URL. For Tableau Public, the URL typically references a published view on `public.tableau.com`; use the actual URL provided by Tableau.

## Deploy to Render
1. Push this project to GitHub.
2. Sign in to Render and create a new **Web Service** connected to the repository.
3. Render can use `render.yaml`, or set:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
4. Add `TABLEAU_DASHBOARD_URL` and `TABLEAU_STORY_URL` under Environment.
5. Deploy and open the generated `onrender.com` URL. Test `/health` to confirm the service is running.

A free hosting service may sleep when inactive or have other limits. A deployment is not complete until the public URL opens successfully.

## Interpretation caution
Aggregated `annual_sales_units` values describe the supplied dataset. Do not label them verified real-world market totals unless the dataset source validates that interpretation.
