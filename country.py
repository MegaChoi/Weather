import pycountry

test = pycountry.countries.get(name='United Kingdom').alpha_2

test1 = pycountry.countries.search_fuzzy('United Kingdom')



print(test)
# for x in range (len(pycountry.countries)):
#     print (list(pycountry.countries)[x])
