import requests
import bs4
import pandas as pd

def request_url(website_url: str) -> str:
    return requests.get(website_url).text


def html_parse(unparsed_html: str) -> bs4.BeautifulSoup:
    soup = bs4.BeautifulSoup(unparsed_html , 'html.parser')
    return soup

def get_details_of_product(soup: bs4.BeautifulSoup):
    product_name = []
    product_price = []
    product_details={
        "product_name"+" "*20: product_name,
        ' '*10+"product_price": product_price
    }
    
    product_name_container = soup.find_all('a',class_= 'product-item-link')
    product_price_container = soup.find_all('span', {"data-price-type" : 'finalPrice'})

    for ele_name , ele_price in zip(product_name_container,product_price_container):
        product_name.append(ele_name.text.strip())
        product_price.append(ele_price.text.strip())

    data_frame = pd.DataFrame(product_details)
    print(data_frame)


def get_details_of_news(soup):
    news_headlines = []
    news_links= []

    top_news = {
        "News-Headline"+' '*20: news_headlines,
        "News-Link" +' '*20: news_links
    }

    container = soup.find_all('a',class_='el-item uk-panel uk-link-toggle uk-display-block')
    for ind,ele in enumerate(container):
        news_link = ele.get('href')
        news_headline = ele.find('span', class_= 'uk-link-heading').text
        # print(ind, news_link)
        news_headlines.append(news_headline)
        news_links.append(news_link)
        
    pd.set_option('display.max_rows', None)
    df = pd.DataFrame(top_news)
    print(df)


def scrape_to_get_info(option: int, website_url: str):
    html_string = request_url(website_url)
    soup = html_parse(html_string)
    if option == 1 or option == 2 or option == 3:
        get_details_of_product(soup)
    else:
        get_details_of_news(soup)

def track_record(filename, username: str, email:str):
    #1. on the basis of option choosen update the usename and email 
        record = ','.join((username,email))
        with open(filename,'a') as file:
            file.write(record)
            file.write("\n")

def main():
    while True:
        print('\n******************---------WELCOME TO SCRAPPER--------**********************\n')
        print('\n******************Choose your option***********************')
        print('1. MEN Fashion\n2. WOMEN Fashion \n3. Health Care Products \n4.Top News\n5. Exit\n')

        option = int(input('Enter your option: '))

        if option == 5:
            break
        elif  option not in [1,2,3,4]:
              print('Sorry! Please,Choose your option correctly')
              continue

        print("Please, Enter you username and email to proceed!!!!")
        username = input('Enter your username: ')
        email = input('Enter your email: ')

        if username and email:

            if option == 1:
                print('-'*100)
                print('-----------------------Here is your shopping options-----------------------------')
                website_url = 'https://www.sastodeal.com/mens-fashion/clothing.html'
                scrape_to_get_info(1,website_url)
                track_record('Men_Fashion_user_record.txt',username,email)
                print('-'*100)
            elif option == 2:
                print('-'*100)
                print('-----------------------Here is your shopping options-----------------------------')
                website_url = 'https://www.sastodeal.com/womens-fashion/clothing.html'
                scrape_to_get_info(2,website_url)
                track_record('Women_Fashion_user_record.txt',username,email)
                print('-'*100)
            elif option == 3:
                print('-'*100)
                print('-----------------------Here is your shopping options-----------------------------')
                website_url = 'https://www.sastodeal.com/sd-fast/health-care.html'
                scrape_to_get_info(3,website_url)
                track_record('Health_product_user_record.txt',username,email)
                print('-'*100)
            elif option == 4:
                print('-'*100)
                print('-----------------------Here is you news options-----------------------------')
                website_url = 'https://www.nepalnews.com/'
                scrape_to_get_info(4, website_url)
                track_record('news_reader_record.txt',username,email)
                print('-'*100)
        else:
            print('Sorry!!! Something went wrong! Enter your username and email to proceed')

if __name__ == '__main__':
    main()