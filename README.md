# Web Scraping with BeautifulSoup

A collection of web scraping examples built with **Python**, **BeautifulSoup**, and **Streamlit**. The project demonstrates how to extract data from websites, process HTML content, download images, and display scraped information in a simple web interface.

## Features

- Scrape course information from Maktabkhooneh
- Scrape mobile phone data from Technolife
- Extract product titles
- Extract prices
- Download product images
- Display scraped data with Streamlit
- Practice CSS selectors and HTML parsing

## Technologies

- Python
- BeautifulSoup4
- Requests
- Streamlit

## Project Structure

```
web-scraping-examples/
├── maktabkhooneh_scraper.py
├── technolife_scraper.py
├── streamlit_app.py
├── images/
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/web-scraping-examples.git
```

Navigate to the project folder:

```bash
cd web-scraping-examples
```

Install the required packages:

```bash
pip install requests beautifulsoup4 streamlit
```

## Running the Project

Run any scraper:

```bash
python maktabkhooneh_scraper.py
```

or

```bash
python technolife_scraper.py
```

To launch the Streamlit application:

```bash
streamlit run streamlit_app.py
```

## What This Project Demonstrates

- Sending HTTP requests
- Parsing HTML documents
- CSS Selectors
- Finding HTML elements
- Downloading images
- Displaying scraped data
- Building a simple Streamlit dashboard

## Preview

Add screenshots of:

- Streamlit application
- Downloaded product images
- Scraped results

## Future Improvements

- Export data to CSV or Excel
- Save data into SQLite
- Product search and filtering
- Pagination support
- Asynchronous scraping
- Better error handling
- Price change tracking

## Contributing

Contributions, suggestions, and improvements are welcome. Feel free to open an issue or submit a pull request.

---

If you found this project useful, consider giving it a ⭐ on GitHub.
