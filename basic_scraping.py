from urllib.request import Request, urlopen
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
            
 def getPageElements(url, tag, attrs = ""):
    """
    Returns  all of the page elements that match specified page element tag and attributes.
    This function is able to by-pass the server security feature of some sites that block known
    spider/bot user agents.

    Parameter url: a valid webapge url
    Precondition: url is a string

    Parameter tag: an element tag on the page
    Precondition: tag is a string

    Parameter attrs: the specified attribut
    Precondition: attrs is a string
    """
    assert isinstance(url, str) and isinstance(tag, str)
    assert isinstance(attrs, str) or isinstance(attrs, dict)
    
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req).read()
        bsObj = BeautifulSoup(html, 'lxml')
        items = bsObj.findAll(tag, attrs)
        try:
            return items
        except AttributeError:
            print('Attribute error. Are the attributes of that tag valid?')
    except HTTPError:
        print('Http error')
        
    except ValueError:
        print('Value error. Is the url valid?')

def popupmsg(msg, title, buttonmsg):
    """
    Creates a pop-up message
    """
    import easygui
    try:
        easygui.msgbox(msg, title, ok_button=str(buttonmsg))
    except:
        print('error in creating pop-up. Are you passing in strings?')


    
