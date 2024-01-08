# Import package
import wikipedia
# Specify the title of the Wikipedia page
wiki = wikipedia.page('Sam_Altman')
# Extract the plain text content of the page
text = wiki.content
print(text)