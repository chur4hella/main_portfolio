from bs4 import BeautifulSoup
import requests

r = requests.get('https://catalog.onliner.by')
soup = BeautifulSoup(r.text, 'html.parser')

c_dict = {}
csf = soup('span', 'catalog-navigation-classifier__item-title-wrapper')[:10]
csf = [' '.join((i.get_text()).split()) for i in csf]
csf1 = soup('div', 'catalog-navigation-list__category')[:10]

ctg = []
sctg = []
ssctg = []

for i in csf1:
    ctg.append([' '.join((j.get_text()).split()) for j in i.find_all('div', 'catalog-navigation-list__aside-title')])


for i in csf1:
    for j in i.find_all('div', 'catalog-navigation-list__aside-item'):
        ssctg.append([' '.join((k.get_text()).split()) for k in j.find_all('span', 'catalog-navigation-list__dropdown-title')])


# k = 0
# l = 0
# for i in csf:
#     c_dict[i] = {}
#     for j in ctg[k]:
#         c_dict[i][j] = {}
#
#     k += 1

k = 0
l = 0
for i in csf:
    c_dict[i] = {}
    for j in ctg[k]:
        c_dict[i][j] = ssctg[l]
        l += 1

    k += 1



def main():
    # print(len(ctg))
    # print(ctg[-1])
    print(c_dict)

main()
