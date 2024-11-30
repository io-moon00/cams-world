from django import template
from bs4 import BeautifulSoup

register = template.Library()

@register.filter
def first_paragraph(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    paragraph = soup.find('p')
    return str(paragraph) if paragraph else ''

@register.filter
def exclude_first_paragraph(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    first_paragraph = soup.find('p')
    if first_paragraph:
        first_paragraph.extract()  # Remove the first paragraph
    return str(soup)