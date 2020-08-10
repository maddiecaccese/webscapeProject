#import Flask and other necessary packages
from flask import Flask, request, render_template

#import beautifulsoup package
from bs4 import BeautifulSoup

#import requests to get html code
import requests

#flask constructor
app = Flask(__name__)

#process the form
@app.route('/', methods = ["GET", "POST"])
def processForm():
    try:
        if request.method == "POST":
            #get the input
            info = request.form.get("website")
            #return "The website is " + info //THIS IS TEST CODE
            #use requests to get html code from info variable
            r = requests.get(info)
            soup = BeautifulSoup(r.text, 'html.parser')
            links = []
            for link in soup.find_all('a'):
                links.append(link.get('href'))
                #test - print links in terminal
                #print(link.get('href'))
            content = soup.find(attrs={'class':'col-sm-12 col-md-gutter clearfix'}).get_text()
            # test - print contents in terminal
            #print(soup.get_text())
            return render_template("results.html", links = links, content = content, info = info)
        return render_template("webscraping.html")
    except Exception:
        print("Link is broken")
        return render_template("error.html")


#run the program
if __name__ == '__main__':
    app.run(port=4000, debug=True)