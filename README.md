# Book API

## System Overview

Book-API is a rest API to list book collection

## Resources

Resources available in this API:

* Books

List of book collection. It provides information about title and author of the book, as well as the reading status of the book, read it or unread it.

* Book

Information of a specific book referenced by its id

## Setup Instructions

### Prerequisite

1. Install Python3.8

### Environment Setup

Get the project running in just 3 quick steps.

1. For this repository and clone to your local machine. Then  **cd** into the project

   ```bash
   git clone https://github.com/alucardthefish/bookapi.git

   cd bookapi
   ```

2. Create your virtual environment, and activate it.

   ```bash
   python -m venv env

   source env/bin/activate  # Linux/Mac
   env\Scripts\activate  # Windows
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

## Run

You just need to run the server by executing the script main.py

```bash
   python main.py
```

## Usage

Go the api url to call the available endpoints

```bash
    http://localhost:5000/api/
```