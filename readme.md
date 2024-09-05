
# 🕷️ Python Web Crawler

Welcome to **Python Web Crawler**! This project is a sophisticated web crawler built with Python, designed to crawl entire websites, extract meaningful content, and store the data in either SQLite or CSV format. Perfect for training AI models or data scraping enthusiasts! 🚀

## 📜 About the Project

This crawler is capable of:
- **Recursive Crawling**: It doesn't just stop at one page; it dives deep into all subpages within a domain.
- **Dynamic Progress Bar**: Shows real-time progress as it crawls through pages.
- **Customizable Storage**: Choose between SQLite or CSV for storing your data.
- **Polite Crawling**: Respects rate limits and handles errors gracefully.
- **Content Filtering**: Extracts useful content like text, code blocks, and important sections while ignoring unnecessary HTML, CSS, and JS.

## 🔧 Getting Started

### Prerequisites

Make sure you have Python 3.x installed and the required packages:

```bash
pip install -r requirements.txt
```

### Usage

1. Clone the repository:

```bash
git clone https://github.com/harshitkumar9030/python-web-crawler.git
cd python-web-crawler
```

2. Edit the configuration file (`config/config.yaml`) or use the provided example:

```yaml
websites:
  - "https://example.com"
output:
  type: "sqlite"  # or "csv"
  path: "data/output.db" # or "data/{name}.csv"
rate_limit:
  requests_per_minute: 30
```

3. Run the crawler:

```bash
python main.py --config config/config.yaml
```

### 🗂️ Example Configuration

An example configuration file is available [here](config/example_config.yaml). Customize it according to your needs! 🎨

## 📬 Connect with Me

Hey, I'm Harshit! 👋

- 🌐 [Website](https://leoncyriac.me)
- 📸 [Instagram](https://instagram.com/_harshit.xd)

Feel free to reach out or follow along with my projects!

## 🌟 Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or features you'd like to add. 😊

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Happy Crawling! 🕵️‍♂️🕸️

