# Search-Engine

## 📌 Overview
Search-Engine is a lightweight and efficient search engine that leverages an **inverted index** to provide fast and accurate search results. Built with Python, it processes web documents, tokenizes content, and enables powerful query operations with Boolean search capabilities.

## 🎯 Objective
The goal of this project is to develop a **high-performance** search engine that automatically processes, tokenizes, and indexes webpages, allowing users to perform **fast and intelligent queries**.

### Key Features:
- **Token Normalization**: Cleans and standardizes search terms.
- **Inverted Indexing**: Optimizes document retrieval for efficient searches.
- **Boolean Search**: Supports operations like `AND`, `OR`, and `NOT` for refined queries.
- **Fast Query Matching**: Finds and ranks relevant webpages quickly.
- **Scalability**: Designed to handle large datasets with ease.

## 🚀 How It Works
1. **Read Documents**: Extracts and tokenizes text from webpages.
2. **Build Inverted Index**: Maps words to the documents they appear in.
3. **Query Processing**: Matches search terms with indexed pages using Boolean logic.
4. **Return Results**: Displays ranked matching pages to the user.

## 🏗️ Project Structure
```
|-- search.py  # Main search engine script
|-- sampleWebsiteData.txt  # Sample dataset
|-- searchEngine-Report.pdf  # Report
|-- README.md  # Documentation
```

## 🛠️ Technologies Used
- **Python** for core processing.
- **String Manipulation & Tokenization** for data cleaning.
- **Inverted Index** for efficient searches.
- **Boolean Logic** for advanced query matching.

## 📖 Getting Started
### Prerequisites
- Python 3.8+

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/HareenaChowdary/Search-Engine.git
   cd Search-Engine
   ```
2. Run the search engine:
   ```bash
   python search.py
   ```

## 🔍 Running Queries
- **Simple Search**: Enter keywords to find matching pages.
- **Boolean Search**: Use `+` (AND) and `-` (NOT) for advanced queries:
  ```bash
  Enter query: machine +learning -deep
  ```

## 🤝 Contributing
Pull requests are welcome! Feel free to improve the indexing logic or add new features.

## 📧 Contact
Looking for collaboration? Reach out on [LinkedIn](https://www.linkedin.com/in/hareena-chowdary-polavaram/).

---
🚀 **SearchEngine – Smart, Scalable, and Lightning-Fast Search!**

