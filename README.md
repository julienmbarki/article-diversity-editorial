# Article Diversity Editorial

This project is a research project to determine the diversity of the editorial supply (human-curated playlists managed by the platform) on Spotify. A preprint version of the paper is available here: [Metadata_MBARKI.pdf](https://drive.google.com/file/d/17GTNHUWvcrBlrSDQ_HhUpA9ClPL6QtX0/view?usp=sharing)

## Installation

This code is done using Jupyter Notebooks with Python 3.9 and R. You can download both of these languages here: [python.org](https://www.python.org/downloads/release/python-3919/), [R Cran](https://cran.r-project.org/).

## Python dependencies

You can download the dependencies for Python using the following commands:

```bash
pip install numpy
pip install matplotlib
pip install pandas
pip install scipy
pip install selenium
pip install sklearn
pip install spotipy
```

## Clone this repository

```bash
git clone https://github.com/article-diversity-editorial.git
```

## Data Request

The data request is done using Spotify's API (see the documentation [here](https://developer.spotify.com/documentation/web-api)) you need to create a developer account and a new app ([here](https://developer.spotify.com/dashboard)) to get client_id and client_secret tokens.

## Data management

The indicators of diversity are computed for each playlist. To perform the full analysis, you need to run the code for every playlist before merging the dataframes into a single one, and then perform the statistical analysis.

