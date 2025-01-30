## Web Scraper for Trending Table Tennis Rubbers

This project is a **web scraper** that searches various table tennis websites to track and gather data about trending rubbers. The scraper collects relevant information such as rubber brand, type, and user ratings, then compiles the data for easy analysis.

### Features:
- **Website Scraping**: Scrapes multiple table tennis websites for information on trending rubbers.
- **Data Extraction**: Extracts key details like rubber brand, type, and ratings.
- **Trending Rubbers Tracker**: Identifies and compiles data about the most popular rubbers across websites.
- **CSV Export**: Saves the collected data to a CSV file for analysis and sharing.

### How It Works:
1. The scraper visits predefined table tennis websites and loads the pages containing information about rubbers.
2. Using BeautifulSoup (or other scraping libraries), it parses the HTML and extracts relevant data.
3. The extracted information is compiled into a list and can be saved in CSV format for later use.

### Built With:
- **Python**: For web scraping and data processing.
- **BeautifulSoup**: For parsing HTML and extracting data.
- **Pandas**: For organizing and exporting data.
