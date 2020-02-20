<p align="center">
    <img src="https://pmcvariety.files.wordpress.com/2018/01/amazon-logo.jpg?w=1000&h=562&crop=1" alt="logo" width="500" height="300"/>
</p>

<p style="text-align:left; font-size:20px;">Static webpage version of this analysis available <a href="https://ukrainian-serge.github.io/amazon_reviews.io/">HERE</a></p>
  
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ukrainian-serge/amazon_reviews.io/master)



<h1  align="center">Database creation and analysis using Amazon review data</h1>

The final goal of this project is to compare digital vs non-digital book reviews and compare whether the substrate the media is on effects the review. We'll squeeze as much insight as possible out of this and branch off into other categories for analysis and comparison.

The first objective would be starting with really understanding our data, for this I undertake the task of creating a local database with designed table formatted(PostgreSQL) for revisitation of the project. Thankfully it was a rather clean dataset as it came from a AWS server which led to the next step of EDA with SQL queries and Python pandas.

The final visualizations were done with interactive Bokeh charts on a customized Jupyter Notebook. The below link leads you to the static HTML webpage, and if you wish, from there you can also view it in the github repo which contains the notebooks themselves.


<h2 align="center">Brief work sequence overview</h2>

<h3 align="left">Acquire</h3>

 - [Amazon data](https://s3.amazonaws.com/amazon-reviews-pds/readme.html):
    - download source data using a url from [this](https://s3.amazonaws.com/amazon-reviews-pds/tsv/index.txt) link.
        This was a tough choice. Instead of later realizing I didnt have enough data, I went ahead and chose the largest set. 
    
<h3 align="left">Data wrangle and database creation</h3>

 - [Notebook_1](https://github.com/ukrainian-serge/amazon_reviews.io/blob/master/notebooks/NOTEBOOK_1.0.ipynb) initial data parsing and wrangling:
      - this [notebook](https://github.com/ukrainian-serge/amazon_reviews.io/blob/master/notebooks/NOTEBOOK_1.1_LOG_explore.ipynb) deals with `pandas.read_csv` errors.
      - creation of local PosgreSQL database `amazon_reviews`.
      - design datatype structure for columns and creation of `reviews` tables with inserted values.
    
 - [Notebook_2](https://github.com/ukrainian-serge/amazon_reviews.io/blob/master/notebooks/NOTEBOOK_2.0.ipynb) table creation automation:
      - more parse and wrangle.
      - automated the process of splitting initial `reviews` into separate tables(by `product_category`).

<h3 align="left">Analysis and visualization</h3>

 - [Notebook_3](https://github.com/ukrainian-serge/amazon_reviews.io/blob/master/notebooks/NOTEBOOK_3.0_FINAL.ipynb) **FINAL**. Contains full notebook, queries, python code and all
    - [Bokeh](https://docs.bokeh.org/en/latest/docs/gallery.html) interative charts for analysis and observation notation
    - Github will not preview the bokeh charts. Repo must be cloned to see charts in Jupyter Notebook form or visit [here](https://ukrainian-serge.github.io/amazon_reviews.io/)
 
---

My [module](https://github.com/ukrainian-serge/amazon_reviews.io/blob/master/notebooks/amazon_reviews_module.py) with functions designed for this project.

<h2 align="center">Technologies I used</h2>

 - [PostgreSQL](https://www.postgresql.org/download/) for database creation  
 - [Jupyter Notebooks/Lab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) with [nbextensions](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/) for bulk of work  
 - [Python](https://www.python.org/) with [Pandas](https://pandas.pydata.org/), [Sqalchemy](https://www.sqlalchemy.org/), [psycopg2](https://pypi.org/project/psycopg2/), [Bokeh](https://docs.bokeh.org/en/latest/docs/gallery.html), and more
 - [VsCode](https://code.visualstudio.com/) for editing html/markdown files and testing python functions outside of Jupyter Notebooks
 - [Git](https://git-scm.com/) for version control
 - [PowerShell](https://docs.microsoft.com/en-us/powershell/) for automating minor stuff
