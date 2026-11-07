# Static Site Generator

A static site generator built with Python as part of the [Boot.dev](https://www.boot.dev/) backend development curriculum.

The project converts Markdown files into HTML pages, allowing a website to be generated automatically from Markdown content.

## Features

- Converts Markdown into HTML
- Supports headings, paragraphs, links, images, lists, and code blocks
- Converts Markdown into HTML nodes
- Recursively generates pages from Markdown files
- Copies static assets such as images and CSS
- Uses an HTML template to generate web pages

## Technologies

- Python 3
- HTML
- CSS
- Markdown
- Git

## Getting Started

Clone the repository and navigate to the project directory.

```bash
git clone <repository-url>
cd static-site-generator
```

Generate the website:

```bash
python3 src/main.py
```

Start a local web server:

```bash
python3 -m http.server --directory docs
```

Open `http://localhost:8000` in your browser.

## Project Structure

```text
static-site-generator/
├── content/       # Markdown content
├── static/        # CSS and images
├── src/           # Python source code
├── docs/          # Generated HTML website
└── README.md
```

## What I Learned

- Object-oriented programming in Python
- Recursive functions and directory traversal
- Parsing Markdown into structured HTML
- Working with files and directories
- Generating HTML pages programmatically
- Building a static website without external frameworks

## Acknowledgments

Built as part of the [Boot.dev](https://www.boot.dev/) Static Site Generator course.
