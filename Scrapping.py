import csv
from bs4 import BeautifulSoup

# importing neccessary files
with open('Amazon19.html', 'r', encoding='utf-8') as file:
    html_data = file.read()

soup = BeautifulSoup(html_data, 'html.parser')
product_divs = soup.find_all('div', class_='s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t3 puis-include-content-margin puis puis-v1aj7nq8vmj30z2oahbw0jjbcwc s-latency-cf-section s-card-border')

product_link_list = []
product_name_list = []
product_price_list = []
product_rating_list = []
product_ratings_list = []

# Scrapping data from website

for div in product_divs:
    
    product_link_tag = div.find('a', class_='a-link-normal s-no-outline')
    product_link = product_link_tag['href'] if product_link_tag else ""
    product_link_list.append("amazon.in" + product_link)

    product_name_tag = div.find('span', class_='a-size-medium a-color-base a-text-normal')
    product_name = product_name_tag.get_text(strip=True) if product_name_tag else ""
    product_name_list.append(product_name)

    product_price_tag = div.find('span', class_='a-price-whole')
    product_price = product_price_tag.get_text(strip=True) if product_price_tag else ""
    product_price_list.append(product_price)

    product_rating_tag = div.find('span', class_='a-size-base s-underline-text')
    product_rating = product_rating_tag.get_text(strip=True) if product_rating_tag else ""
    product_rating_list.append(product_rating)

    product_ratings_tag = div.find('span', class_='a-icon-alt')
    product_ratings = product_ratings_tag.get_text(strip=True) if product_ratings_tag else ""
    product_ratings_list.append(product_ratings)

# putting data in the file

print(len(product_link_list))
rows = zip(product_link_list, product_name_list, product_price_list, product_rating_list, product_ratings_list)

with open('amazon_products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Product Link', 'Product Name', 'Product Price', 'Product Rating', 'Product Ratings'])
    writer.writerows(rows)

