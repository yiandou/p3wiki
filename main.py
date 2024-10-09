import wikipediaapi
import time
from queue import Queue
user_agent = "p3_wiki (onlyian4981@gmail.com)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

start_page = wiki.page("Gentoo Linux")
target_page = wiki.page("Bird Island, South Georgia")

def get_titles(page):
    links = page.links
    titles = []
    for title in links:
        titles.append(title)
    return titles

def wikipedia_game_solver(start_page, target_title):
    print(f"Starting from {start_page.title} to {target_title}")
    start_time = time.time()
    queue = Queue() 
    visited = set()
    parent = {}

    queue.put(start_page.title)
    visited.add(start_page.title)

    while not queue.empty():
        current_page_title = queue.get()
        if current_page_title == target_title.title:
            break

        current_page = wiki.page(current_page_title)
        links = get_titles(current_page)
        
        for link in links:
            if link not in visited:
                queue.put(link)
                visited.add(link)
                parent[link] = current_page_title

    path = []
    page_title = target_page.title
    while page_title != start_page.title:
        path.append(page_title)
        page_title = parent[page_title]

    path.append(start_page.title)
    path.reverse()

    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")
    return path

path = wikipedia_game_solver(start_page, target_page)
print(path)
