import wikipediaapi
import time

user_agent = "p3_wiki (onlyian4981@gmail.com)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

start_page = wiki.page("Gentoo Linux")
target_page = wiki.page("Gentoo penguin")
#target_page = wiki.page("Ferdinand III of Castile")

def get_titles(page):
    links = page.links
    titles = []
    for title in links:
        titles.append(title)
    return titles

def find_path(start_page, target_page):
    visited = set()
    queue = [[start_page.title]]
    while queue:
        path = queue.pop(0)
        page = wiki.page(path[-1])
        if page.title == target_page.title:
            return path
        if page.title in visited:
            continue
        visited.add(page.title)
        for title in get_titles(page):
            new_path = list(path)
            new_path.append(title)
            queue.append(new_path)
    return None


