import requests
from bs4 import BeautifulSoup
from urllib import parse


class Job():


    def get_html(self):
        ua = {'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0)"}
        response = requests.get("https://hh.ru", headers=ua)
        self.html = response.text

    def get_div(self):
        html = BeautifulSoup(self.html, "lxml")
        self.div = html.find_all("div", {"class": "vacancies-of-the-day__item"})

if __name__ == "__main__":
    job = Job()
    job.get_html()
    #print(job.html)
    job.get_div()
    #print(job.div)
    for div_1 in job.div:
        result = div_1.find("span", {"class": "vacancy-of-the-day__title"})
        print(result.text)
    for div_2 in div_1:
        result = div_2.find("span", {"class": "vacancy-of-the-day__salary"})
        print(result.text)
    for div_3 in div_1:
        result = div_3.find("span", {"class": "vacancy-of-the-day__company"})
        print(result.text)
