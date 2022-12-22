#https://www.sastodeal.com/electronic/laptops.html
#scrape device name and price of the each item of the link
import bs4
import requests

#1. requesting raw text from the link 
def request_url(url: str)-> str:
    return requests.get(url).text

#2. get the parsed_html to unparsed_html text
#3. return soup from the parsed_html 
def parsed_html(unparsed_html: str) -> bs4.BeautifulSoup:
    soup = bs4.BeautifulSoup(unparsed_html,'html.parser')
    return soup

#4. extract or scrap the desired information from the requesting site
def get_details(soup:bs4.BeautifulSoup)->list:

    product_details=[]
    product_name_container = soup.find_all('a',class_= 'product-item-link')

    #to select on the basis of other html attribute present in the element(tag) we can use as {"tag_name":"value"}
    product_price_container = soup.find_all('span', {"data-price-type" : 'finalPrice'})

    for ele_name , ele_price in zip(product_name_container,product_price_container):
        '''
           (got it) nest the items well, you may not get the desired output sometimes
        '''
        # container = ele.div
        '''
           (done) yesari dherai nai nest garnu vanda aauta element agadi ko class/id lera garda kasto hunthyo hola...
        '''
        product_details.append({
            "product_name":ele_name.text.strip(),
            "product_price":ele_price.text.strip()
        })
    # print(product_details)

    # #return list of product details i.e. list of dictionary
    return product_details

def main():
    website_url = "https://www.sastodeal.com/electronic/laptops.html"
    html_string = request_url(website_url)
    
    soup = parsed_html(html_string)
    product_details=get_details(soup)
    # get_details(soup)
    for ele in product_details:
        res='\t\t ----- \t\t'.join((ele["product_name"],ele["product_price"]))

        with open("scrapped_data.txt","a") as file:
            file.write(res)
            file.write("\n\n")


if __name__ == '__main__':
    main()
    
    
'''
    project complete vaye paxi chai make sure you remove those unnecessary lines of code hai
'''

'''
    halka operators bich chai space dida clean dekhinxa like "html_string = request_url(website_url)" or even "def request_url(url: str)-> str:...."
'''

'''
    output chai hakla messed up jasto lagyo. try to present it clearly.
'''

'''
    otherwise, looks nice. well done.
'''
