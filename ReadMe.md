
# Google Book Search (Python)

This is a command line application created with Python that works in 
conjunction with the Google Books API.

https://user-images.githubusercontent.com/105952966/210851025-3d6d57a6-713a-4b0b-ac02-6ba9205f3e89.mp4
## Environment Variables

To run this project, you will need to add the following environment variable to your .env file:

`API_key` from the Google Books API

## Getting your API Key

As previously mentioned, to run this program you'll need to create your own API Key. Use the following resources to create your API Key.

- [Getting Started](https://developers.google.com/books/docs/v1/getting_started)
- [Create Your API Key](https://cloud.google.com/docs/authentication/api-keys?visit_id=638085398466762425-18212346&rd=1#create)


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
  #Then enter the cloned directory
  cd google_book_search
```

Go to the project google_book_search parent directory

```bash
  cd google_book_search
```

Install dependencies

```bash
  pip3 install -r requirements.txt
```

Create .env file to hold your API Key
```bash
  vim .env
  #This will open up vim
  #press the "i" key on your keyboard to -INSERT- text
  API_key="<enter your API key here>"
  #press the "ESC" key on your keyboard to exit -INSERT- mode
  #enter the following to save the file and exit vim
  :wq
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
 - [Using the API](https://developers.google.com/books/docs/v1/using#PerformingSearch)
 - [Developer's Guide](https://developers.google.com/books/docs/viewer/developers_guide)

## Feedback

If you have any feedback, please reach out to me at fr4v1l4@gmail.com. I'm 
always striving to improve, so any input would be greatly appreciated. Thank you!


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://favilas-portfolio.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/francisco-r-avila)
[![Youtube](https://img.shields.io/badge/youtube-C4302B?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@code_7887)
