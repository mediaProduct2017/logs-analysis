# logs-analysis

This project is for logs analysis of a news website. The logs are produced by the website and stored in a postgresql database. We design a class that could finish the analysis of logs. We first use a script to call a method of the class for creating views in the database. Then we use a script to call several methods of the calss to finish the analysis. The analysis tries to answer the following three questions:
1. What are the page views for 3 most popular articles?
2. What are the page views for most popular authors?
3. List the days on which the error rate is more than 1%.

## Getting started
You need to have the postgresql database with the log data to run this project. You also need to install python2 and the python module - psycopg2. To get started, clone the repository to run the application locally on your computer.

    $ git clone https://github.com/mediaProduct2017/logs-analysis.git
    
## Usage
1. Open the directory "logs-analysis" and run the script "create_view.py" to create views in the database.

       $ cd logs-analysis
       $ python create_view.py
    
2. Run the script "analysis.py" to conduct the log analysis.

       $ python analysis.py
    
3. Open the text file "results.txt" in the directory and you'll see the answers for the 3 questions.    
