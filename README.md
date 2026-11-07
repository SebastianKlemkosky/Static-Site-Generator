# Static Site Generator

A static site generator built with Python as part of the [Boot.dev](https://www.boot.dev/) backend development curriculum.

The project converts Markdown files into HTML pages, allowing a website to be generated automatically from Markdown content.

**[View Live Website](https://sebastianklemkosky.github.io/Static-Site-Generator/)**

## Features

- Converts Markdown content into HTML
- Supports headings, paragraphs, links, images, lists, and code blocks
- Recursively generates HTML pages from Markdown files
- Copies static assets such as CSS and images
- Uses HTML templates to generate pages
- Supports deployment through GitHub Pages

## Technologies

- Python 3
- HTML
- CSS
- Markdown
- Git and GitHub Pages

## Getting Started

Clone the repository:

```bash
git clone https://github.com/SebastianKlemkosky/Static-Site-Generator.git
cd Static-Site-Generator
```

Generate the website:

```bash
python3 src/main.py
```

Preview the generated website:

```bash
python3 -m http.server --directory docs
```

Visit `http://localhost:8000` in your browser.

## Project Structure

```text
Static-Site-Generator/
├── content/       # Markdown source files
├── static/        # CSS and images
├── src/           # Python generator
├── docs/          # Generated website
└── README.md
```

## What I Learned

- Recursive programming and directory traversal
- Object-oriented programming in Python
- Parsing Markdown and generating HTML
- File handling and directory management
- Working with HTML templates
- Deploying a static website using GitHub Pages

## Acknowledgments

Created as part of the [Boot.dev](https://www.boot.dev/) Static Site Generator course.
