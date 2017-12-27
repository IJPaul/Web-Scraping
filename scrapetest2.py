from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def getTitle(url):
    """
    Returns the title object of the html page as a Tag object.
    If page or server is not found or cannot be connected to, returns None
    
    Parameter url: the url address of the page
    Precondition: url is a str
    """
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError:
        return None
    return title


def getChildren(url, tag, attributes):
    """
    Returns NavigableString object list of all children of the first tag passed
    with the passed attributes for the webpage given by the passed url. If page
    or server is not found or cannot be connected to, returns None.
    
    Parameter url: the url address of the page
    Precondition: url is a str
    
    Parameter tag: the html element to find children of
    Precondition: tag is a str
    
    Parameter attributes: the attributes that the tag should have
    Preconditon: attributes is a dictionary
    """
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        children = bsObj.find(tag, attributes).children
    except AttributeError:
        return None
    return children

def getLinks(url):
    """
    Returns all the links to other pages located on a static page.
    
    Parameter url: the url address of the page
    Precondition: url is a str
    """
    import re
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a"):
        if 'href' in link.attrs:
            print(link.attrs['href'])

getLinks("https://en.wikipedia.org/wiki/Calculus")

    
