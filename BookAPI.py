import requests

search_dict = {}
reading_list = {}

def pull_api(title_keyword):
  url = 'https://www.googleapis.com/books/v1/volumes?q='
  API_key = '&key=AIzaSyAjH0QzWJvcyokNRhFaDUko2x5BAWt8lzE'
  response = requests.get(url + title_keyword + API_key)
  results = response.json()
  return (results)

def get_search_books(title_keyword):
  index_pos = 1
  results = pull_api(title_keyword)
  for x in range(5):
    try:
      title = results['items'][x]['volumeInfo']['title']
    except:
      title = 'NA'
    try:
      author = results['items'][x]['volumeInfo']['authors']
    except:
      author = 'NA'
    try:
      publishing_company = results['items'][x]['volumeInfo']['publisher']
    except:
      publishing_company = 'NA'

    search_dict.update({index_pos: [title, author, publishing_company]})
    index_pos += 1
  return search_dict

def save_to_reading_list(title_keyword, index_pos):
  get_search_books(title_keyword)
  number = len(reading_list) + 1
  book = search_dict[int(index_pos)]
  reading_list.update({number: book})
  return reading_list

def view_reading_list():
  return reading_list

def run():
  
  while True:
    print(f"""       Welcome to my book list Application
    ____________________________________________________
          press 1: view searches for the title
          press 2: add a title to reading List
          Press 3: view Reading List
          Press 4: To exit app
    ____________________________________________________
    """)
    menu = input("select an option Please complete search before saving:")
    if menu == '1':
      keyword_search = input("What title are you looking for:")
      print(get_search_books(keyword_search))
    elif menu == '2':
      keyword_search = input("What title are you looking for:")
      index_pos = input("what number book did you want to read?")
      save_to_reading_list(keyword_search, index_pos)
    elif menu == '3':
      print(view_reading_list())
    elif menu == '4':
      quit()

start = run()









