orgString = "10/15/2020"

print()
print(f'The original string: {orgString}')

splitOrgString=orgString.split("/")
print(splitOrgString) # Returns ['10', '15', '2020']
print(f'day: {splitOrgString[0]}, month: {splitOrgString[1]}, year: {splitOrgString[2]}')


print('\n\n\n')

orgString = "The big red fox is me."
splitOrgString=orgString.split("b")
print(splitOrgString) # Returns ['The ', 'ig red fox is me.']