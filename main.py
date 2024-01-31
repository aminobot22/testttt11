import aminofix
c=aminofix.Client()
print(c.get_from_code("http://aminoapps.com/p/i71jer").json)
