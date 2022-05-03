class Source:

    def __init__(self,id,name):
        self.id = id
        self.name = name

class Newsarticles:
    
    def __init__(self,title,description,urlToImage,publishedAt,url):
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.url = url