import string

# Step 1: Cleans token
def cleanToken(token):
    """
  -->It converts input string to normalized form

  Args:
    token (str): The token to clean

  Returns:
    str: Normalized Token
  """
    token = token.strip(string.punctuation) # Remove punctuations
    if not any(char.isalpha() or char.isnumeric() for char in token):
        return ""
    return token.lower()
   
# Step 2: Creates the Inverted index
def buildInvertedIndex(docs):
    """swaps the dictionary key value pairs

  Args:
    docs: A dictionary where, 
    keys - URLs of the pages and
    values - tuple containing set of the tokens in the page and date of the page.

  Returns:
    An inverted dictionary, where the keys are the tokens and the values are sets of
    the URLs of the documents that contain the token.
  """
    inv_dic = {}
    for url, (tokens, _) in docs.items():
        for token in tokens:
            # If token not in new dictionary, it'll be added as a key
            if token not in inv_dic:
                inv_dic[token] = set()
            # Url will be added to it's respective token
            inv_dic[token].add(url)
    return inv_dic
    
# Step 3: Search Webpages
def findQueryMatches(index, query):
    """Finds the pages that matches given query.

  Args:
    index: Inverted index.
    query: Input string.

  Returns:
    A set of URLs of the documents that matches with given input.
  """
    # Concatenates operator to pair of set to evaluate them
    def apply_optr(op, set1, set2):
        if op == '+':
            return set1.intersection(set2)
        elif op == '-':
            return set1.difference(set2)
        else:
            return set1.union(set2)

    query = query.lower()
    terms = query.split()
    results = set()

    optr = '+'
    for term in terms:
        # If the token is an operator, then it sets the operator variable.
        if term in ['+', '-']:
            optr = term
        else:
            term = cleanToken(term) # normalises the token
            # If search token is in inverted dictionary, then adds it to the result
            if term:
                if term in index:
                    if not results:
                        results = index[term]
                    else:
                        results = apply_optr(optr, results, index[term])

    return results
    
# Step 4: Process Webpages
def readDocs(dbfile):
    """Reads the raw data(webpages) from a text(database) file and converts it to the required dictionary format of URLs to unique words.

  Args:
    dbfile (str): The path to test(database) file.

  Returns:
    A dictionary where, 
    keys - URLs of the pages and
    values - tuple containing set of the tokens in the page and date of the page.
  """
    docs = {}
    with open(dbfile, 'r') as file:
        lines = file.readlines()
        # Initialise variables
        url = None
        body = ""
        date = None
        for line in lines:
            line = line.strip() # Removes white space from sentence
            # If sentence starts with http, it adds url of the new page or if it already exists, then it adds it to the dictinory along with tokens
            if line.startswith("http"):
                if url:
                    tokens = [cleanToken(token) for token in body.split()]
                    uni_tokens = set(tokens)
                    docs[url] = (uni_tokens, date)
                url = line
                body = ""
                date = None
            # finds date of the page
            elif line.startswith("[") and line.endswith("]"):
                date = line[1:-1]
            # data of the page
            else:
                body += line + " "
        
        # Handles the last webpage
        if url:
            tokens = [cleanToken(token) for token in body.split()]
            uni_tokens = set(tokens)
            docs[url] = (uni_tokens, date)
            
    return docs
# Step 5: Builds the Search Engine
def mySearchEngine(dbfile):
    """A search engine.
  Args:
    dbfile: The path to the text file.
  """

    # Reads and process the database file
    print("Stand by while building index...")
    # Reads the data from text file
    docs = readDocs(dbfile)
    # creates inverted index
    inverted_index = buildInvertedIndex(docs)
    # Displays the number of indexed pages and number of unique tokens in the input file.
    num_pages = len(docs)
    num_unique_terms = sum(len(tokens) for tokens, _ in docs.values())
    print(f"Indexed {num_pages} pages containing {num_unique_terms} unique terms.")

    while True:
    
    

        # Takes input
        query = input("Enter query sentence (RETURN/ENTER to quit): ").strip()
        if not query:
            break
        
        
        # Performs the query and displays the results
        matches = findQueryMatches(inverted_index, query)
        print(f"Found {len(matches)} matching pages")
        print(matches)

if __name__ == "__main__":
    mySearchEngine("sampleWebsiteData.txt")