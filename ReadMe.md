
# Google Book Search (Python)

This is a command line application created with Python that works in 
conjunction with the Google Books API.

https://user-images.githubusercontent.com/105952966/208792537-1c29c8f4-9cb3-4c1e-a63e-a5840eefafcf.mp4
## Environment Variables

To run this project, you will need to add the following environment variable to your .env file:

`API_key` from the Google Books API



## API Reference

#### Get all items where the text from `search` is found in the title

```
  GET https://www.googleapis.com/books/v1/volumes?q=<search>+<terms>&key=<API_key>
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `API_key` | `string` | **Required**. Your API key |
| `search` | `string` | **Required**. The title, or part of the title, of the book  |
| `intitle` | `string` | **Required**. Specifies that `search` should be in the title of the book |




## Run Locally

Clone the project

```bash
  git clone https://github.com/fravila08/google_book_search.git
```

Go to the project google_book_search parent directory

```bash
  cd google_book_search
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the program!

```bash
  python3 runner.py
```


## Running Tests

To run tests, run the following command in the parent directory:

```bash
  pytest
```

## Resources for the Google Books APIs

 - [Getting Started](https://developers.google.com/books/docs/v1/getting_started)
 - [Using the API](https://developers.google.com/books/docs/v1/using)
 - [Developer's Guide](https://developers.google.com/books/docs/viewer/developers_guide)

## Feedback

If you have any feedback, please reach out to me at fr4v1l4@gmail.com. I'm 
always striving to improve, so any input would be greatly appreciated. Thank you!


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://favilas-portfolio.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/francisco-r-avila)
[![Youtube](https://img.shields.io/badge/youtube-C4302B?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@code_7887)
