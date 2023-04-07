
# Movie Recommendation System

A Recommendation based ML model by Avishkar. This is model is designed for , but not restricted to a collection of movies, which returns your preferred movie, along with a few more suggestions similar to it.

It is a content-based model, which suggests similar movies based on the content of their tags. These tags are collectively generated using the overview, description, cast,crew, genre, etc associated with a particular movie.

The model vectorizes the tags and then generates a sparse matrix , in which the non zero values determine the similarity score of each movie with each other movie present in the dataset.

This app is converted into a website using Streamlit - which is a kind of module that makes you doubt how relevant it really is to learn Web Development in depth.

Now it is not the most industry applicable level model because sometimes you may get varied or unrelated results for a selected movie, but still it is a great example of how you need to work with datasets in order to manipulate them, in a way convert textual data to numeric values, and get some meaning out of it
## Technologies used

 - [Python](https://www.python.org/)
 - [Streamlit](https://streamlit.io/) - definitely check this out
 - Pandas
 - Numpy
 - Jupyter Notebook
 


## Run the app
Clone the project

```bash
  git clone https://github.com/AvishkarArjan/movie-recommender-model.git
```
Install the dependencies using the following the command 
```bash
  pip install -r requirements.txt
```

To host this project locally run 
```bash
  streamlit run app.py
```

