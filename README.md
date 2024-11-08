# Auto-Article: Convert YouTube Transcripts into SEO-Friendly Content with Gradio UI

Welcome to **Auto-Article**, a project that automates the conversion of YouTube video transcripts into well-structured, SEO-friendly articles using Gradio. This tool leverages NLP techniques and integrates LangChain and the Gemini API to format and optimize transcripts, making it easier to generate high-quality articles for blogs or websites.

## 🚀 Features

- **Automated SEO Optimization**: Converts YouTube transcripts into SEO-friendly articles with headings, keywords, and formatting.
- **User-Friendly Interface**: Built with Gradio for a simple and interactive web interface.
- **NLP-Powered Enhancements**: Integrates LangChain and the Gemini API to perform advanced text analysis and contextual understanding.
- **Customizable**: Allows you to set the tone.
- **Downloadable**: Easily downloadable.
- **Real-time Preview**: Preview changes and formatting in real-time.

## 🛠️ Tech Stack

- **Gradio**: For building the interactive interface.
- **LangChain**: Facilitates the chaining of NLP models for enhanced analysis and structuring of content.
- **Gemini API**: For advanced AI-driven text optimizations and contextual understanding.
- **Python**: Main programming language for text processing and SEO optimizations.
- **NLP Libraries**: Utilizes NLP for structuring the article and extracting key information.
- **YouTube Data API**: Fetches YouTube video transcripts based on input URLs.

## 📋 Prerequisites

- Python 3.8 or higher
- Gradio
- LangChain 
- Gemini API key

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone <github link>
   cd Auto-Article
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your YouTube Data API and Gemini API keys:
* Create a file named `.env` and add your API keys in the following format:
   ```python
    GOOGLE_API_KEY = <your_gemini_api_key>
   ```

## 🚀 Usage
1. Start the Gradio interface:

```bash
  python app.py
```
2. Open your browser and go to `http://localhost:7860`.

3. Enter a YouTube video URL, Set a tone and press Generate Article. You will see the SEO-friendly article preview.

## 📂 Project Structure

```graphql
    Auto-Article/
    │
    ├── app.py                  # Main file to run the Gradio5 app
    ├── requirements.txt        # Required Python packages
    ├── README.md               # Project documentation
    ├── .env                    # Environment variables (add your API keys here)
    └── utils/                  # Utility functions for transcript parsing and SEO formatting
        ├── get_transcript.py   # Functions to clean and structure transcripts
        ├── model.py            # Integration of LangChain for NLP chaining
        └── main.py             # Init file
```

## 🤖 Future Enhancements
* Multi-language Support: Extend the tool to work with multiple languages.
* AI-powered SEO Suggestions: Use LangChain and the Gemini API to provide additional SEO suggestions for better ranking.
* CMS Integration: Directly publish generated articles to popular CMS platforms like WordPress.
