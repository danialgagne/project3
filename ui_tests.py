from selenium import webdriver

def test_page_title():
    # I go to the pinnochio's pizza site
    firefox = webdriver.Firefox()
    firefox.get('http://localhost:8000')

    chrome = webdriver.Chrome()
    chrome.get('http://localhost:8000')

    # the tab title shows that I'm at the right site
    assert 'Pinnochio' in firefox.title
    assert 'Pinnochio' in chrome.title

    firefox.close()
    chrome.close()