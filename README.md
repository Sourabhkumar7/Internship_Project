Here is the  approach explaination of the solution


I completed entire project at one place in VS Code 

Step 1:-
create a conda enviroment where i install all the important python library and packages at one place needed for this task.
and then activate it .

code is :-
conda create -p python=3.8 -y
source activate ./env





step 2:-
install all the packages needed for it .

BeautifulSoup4: A library used for parsing HTML and XML documents, helping to extract data from web pages.
requests: A simple and elegant HTTP library for making HTTP requests in Python.
pandas: A powerful data manipulation and analysis library, providing data structures like DataFrame for handling structured data.
nltk: The Natural Language Toolkit, a library for working with human language data (text) in Python, providing tools for text processing and analysis.
textblob: A library for processing textual data, providing simple APIs for diving into common natural language processing (NLP) tasks such as part-of-speech tagging and sentiment analysis.
openpyxl: A library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files in Python.




step 3:-
craeted two file 
Data_Extraction :- Extract the text and title from each url and save it to article folder .
using beautifulsoup it fetch the specific text from the page.
To run this file we will use Python Data_Analysis.py which will suddenly create the folder name articles and text ,title inside of each url.

Data_Analysis:- using nltk library which natural language toolkit where i clean the text remove spaces and extra word also use stopword.
create two text file outside of name postitve and negative-words-txt which contain text realted to the positive sentiments and negative sentiments so that when i run this code it should check word by word it is present inside it or not to calculate postive and negative score.
Tokenize words and sentences to perform calculation as per your instruction . use Textblob for ploarity and python packages to complete this task and append details to the results and make a dataframe of results and save it in the Excel file.


to run this file :-
python Data_Extraction.py




