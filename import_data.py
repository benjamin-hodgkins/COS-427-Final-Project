from Bio import Entrez, Medline
from io import StringIO
import time

#Uses esearch to search the PubMed database for the relevant term
def search(query, retsize):
    Entrez.email = 'benjamin.a.hodgkins@maine.edu'
    handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax=retsize,
                            retmode='xml',
                            mindate='2010',
                            term=query,
                            usehistory='y',
                            api_key='9595a4004cd58ea5862bf26c92a65b374e08')
    results = Entrez.read(handle)
    return results

#Uses efetch to parse the data and extract only the abstract
def get_abstracts(pmid_list, search_term):
    ids = ','.join(pmid_list)
    handle = Entrez.efetch(db='pubmed', id=ids, rettype="medline", retmode='text', api_key='9595a4004cd58ea5862bf26c92a65b374e08' )
    
    file = StringIO(handle.read())
    parsed = Medline.parse(file)
    
    abstracts = []
    found = 0
    for abstract in parsed:
        try:
            abstracts.append("\"" + abstract['AB'] + "\"" + "," + search_term)
            found += 1
        except:
            pass
    return abstracts, found

#Searches for 12,000 abstracts of each disease class
def main():
    program_start = time.perf_counter()
    for x in range(4):
        start = time.perf_counter()

        retmax = 12000
        search_terms = ['Heart Disease', 'Influenza', 'Lung Cancer', 'HIV']
        search_results = search(search_terms[x], retmax) 
        id_list = search_results['IdList']
        
        found = 0
        abstracts = []
        chunk_size = 100
        try:
            for chunk_i in range(0, len(id_list), chunk_size):
                chunk = id_list[chunk_i:chunk_i + chunk_size]
                data = get_abstracts(chunk, search_terms[x])
                abstracts.extend(data[0])
                found += data[1]
        except:
            pass
        with open("abstracts.txt", "a", encoding="utf-8") as file:
            for abstract in abstracts:
                file.write(abstract + "\n")
        end = time.perf_counter()
        
        print(f"Searched for {retmax} abstracts about {search_terms[x]}")
        print(f"Downloaded and parsed {found} abstracts about {search_terms[x]} in {end - start:0.2f} seconds")
    program_end = time.perf_counter()
    print(f"Total time: {program_end - program_start:0.2f} seconds")
main()
