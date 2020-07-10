import dns.resolver

result = dns.resolver.query('hocla.com', 'A')

result.to_text()
for ipval in result:
    print('IP', ipval.to_text())

len(result)

