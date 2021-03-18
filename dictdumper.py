import requests

from joblib import Parallel, delayed

from bs4 import BeautifulSoup


processes = []

def dictdump():

    url = "https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/"

    response = requests.get(url)

    html_icerigi = response.content

    soup = BeautifulSoup(html_icerigi,"lxml")

    icerik = soup.find_all("div", attrs={"class": "row"})
    
    for section1 in icerik:
        section2 = section1.find_all("section", attrs={"class": "col-md-12"})
        for section3 in section2:
            section4 = section3.find_all("div")
            for section5 in section4:
                q = str(section5)
                q = q.replace("</p>", "")
                q = q.replace("<p>", "")
                splitted1 = q.split(".")

                Splitted = splitted1[-1].split("<br/>")



                if __name__ == "__main__":

                    Parallel(12)(delayed(cevir)(i) for i in Splitted)


def cevir(en):

    url2 = "https://tureng.com/en/turkish-english/{}".format(en)

    result = requests.get(url2)

    url2_icerigi = result.content

    soup2 = BeautifulSoup(url2_icerigi, "lxml")

    icerik = soup2.find_all("table", attrs={"id": "englishResultsTable"})

    a = list()

    for icerik1 in icerik:

        icerik2 = icerik1.find_all("td", attrs={"class": "ts"})

        f = open("sonuc1.txt","a")
        f.write(str(en) + " : " + str(icerik2[0].text) + "\n")
        f.close()


        print(en[0])


if __name__ == "__main__":

    dictdump()











