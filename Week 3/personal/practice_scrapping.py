#https://www.sastodeal.com/electronic/laptops.html
#scrape device name and price of the each item of the link
import bs4
import requests

#1. requesting raw text from the link 
def request_url(url: str)->str:
    return requests.get(url).text

#2. get the parsed_html to unparsed_html text
#3. return soup from the parsed_html 
def parsed_html(unparsed_html:str)->bs4.BeautifulSoup:
    soup = bs4.BeautifulSoup(unparsed_html,'html.parser')
    return soup

#4. extract or scrap the desired information from the requesting site
def get_details(soup:bs4.BeautifulSoup)->list:

    # order_list = soup.find('ol',class_='products list items product-items')
    # main_container= order_list.li.div
    # details_container = main_container
    # product_name = details_container.strong.a.string
    # product_price = details_container.div.span.span.span.span.string
    # # container = main_container.div
    # print("Reached inside container")
    # print(product_name,product_price)

    product_details=[]
    order_list = soup.find_all('li',class_='item product product-item')
    for ind,ele in enumerate(order_list):
        container = ele.div
        product_name = container.strong.a.string.strip()
        product_price = container.div.span.span.span.span.string.strip()
        # product_details["product_name"]=product_name
        # product_details["product_price"]=product_price
        product_details.append({
            "product_name":product_name,
            "product_price":product_price
        })
        # print(ind,product_name,product_price)


    #return list of product details i.e. list of dictionary
    return product_details

def main():
    website_url ="https://www.sastodeal.com/electronic/laptops.html"
    html_string= request_url(website_url)
    print("main function")
    soup = parsed_html(html_string)
    product_details=get_details(soup)

    # product_name,product_price =product_details[0]
    # print(product_details[0])
    # print(product_details[0]["product_name"],product_details[0]["product_price"])

    for ele in product_details:
        # product_name,product_price = ele
        # print(ele["product_name"],ele["product_price"])

        res='---'.join((ele["product_name"],ele["product_price"]))
        print(res)
        print()
        with open("scrapped_data.txt","a") as file:
            file.write(res)
            file.write("\n")


if __name__ == '__main__':
    main()