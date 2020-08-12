from googlesearch import search


# External package to search Google using python
class GoogleSearch:
    def __init__(self, name_search):
        self.name = name_search
        self.result = ""

    def Gsearch(self):
        for i in search(query=self.name, tld='co.in', lang='en', num=5, stop=5, pause=1):
            self.result += i + "\n"
        if self.result != "":
            return self.result
        else:
            return None
