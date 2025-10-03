# Gurugram Property Analysis

This project scrapes property data from an online property listing, cleans it, and prepares it for analysis in Power BI.

## Project Structure

- `web scraping.py`: Scrapes property data from an online property listing and saves the raw HTML files.
- `property data extraction.ipynb`: Extracts relevant information from the scraped HTML files and saves it to `gurugram_property.xlsx`.
- `data filtering.ipynb`: Cleans and preprocesses the data from `gurugram_property.xlsx` and saves the cleaned data to `gurugram_property_clean.xlsx`.
- `gurugram property dashbord.pbix`: A Power BI dashboard for visualizing the property data visually using interactive graphs and KPIs.
- `scrape html/`: A directory containing the raw HTML files scraped from the online property listing.
- `gurugram_property.xlsx`: The raw, extracted property data.
- `gurugram_property_clean.xlsx`: The cleaned and preprocessed property data.
- `requirements.txt`: A list of the Python dependencies for this project.

## How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Scrape data:**
   ```bash
   python "web scraping.py"
   ```
3. **Extract and clean data:**
   - Run the Jupyter Notebooks `property data extraction.ipynb` and `data filtering.ipynb`.
4. **View the dashboard:**
   - Open `gurugram property dashbord.pbix` in Power BI.

## Dependencies

The Python dependencies for this project are listed in the `requirements.txt` file.
