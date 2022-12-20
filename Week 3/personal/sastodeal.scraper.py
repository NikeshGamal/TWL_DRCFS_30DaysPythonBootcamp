#1 Got odaraz site for a specific product
#Fetch it's current price
#Write that price to a file every  60   seconds


#Request the daraz product  page  using request module
#parse the html string using bs4
#find the element that contains the  price
#convert the price into integer 
#write the price in a file
import bs4
import requests

def request_site(url: str ) -> str:
    return requests.get(url).text
    #raw text return garxa as we need the raw text


def parse_html(unparsed_html:str) -> bs4.BeautifulSoup:
    soup = bs4.BeautifulSoup(unparsed_html,'html.parser')
    return soup



def get_price_from_soup(soup: bs4.BeautifulSoup) -> str:
    price_element = soup.find('span', class_='price-wrapper')
    nepali_price = price_element.span.string
    return nepali_price



def write_price_to_file(price:str , filename:str) -> None:
    with open(filename, mode='w', encoding = 'utf-8') as file:
        file.write(price)



def main():
    website_url="https://www.sastodeal.com/baltra-sensible-plus-electric-2-burner-infrared-cooker-bic-126-supply-baltra-09.html"
    filepath = "test_file.txt"

    html_str = request_site(website_url)
    # print("-"*60)
    # print("Raw text")
    # print(html_str)
    # print("-"*60)
    soup = parse_html(html_str)
    # print("Soup")
    # print(soup)
    # print("-"*60)
    product_price = get_price_from_soup(soup)
    print("product_price")
    print(product_price)
    print("-"*60)
    write_price_to_file(product_price,filepath)


if __name__ =='__main__':
    main()