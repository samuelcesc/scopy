#! Scopus document retrieval
# Type, Title, Abstract, Publication Year, EID, Affliation Country, DOI
from __future__ import print_function
from scopus import ScopusSearch,ScopusAbstract
import json

def main():
    print("Starting up...")
    
    s = ScopusSearch('AFFILORG(Covenant University)', refresh=True)
    eids = s.EIDS
    
    writablefile = open("list.json", "w")
    data = []
    count = 0

    for eid in eids:
        statement = "Processing {} out of {}".format(count+1, len(eids))
        print(statement)

        ab = ScopusAbstract(eid)
        
        affils = []

        for aff in ab.affiliations:
            affils.append(aff.country)

        document = {
            'type': ab.aggregationType,
            'publication': ab.publicationName,
            'title': ab.title,
            'desc': ab.description,
            'abstract': ab.abstract,
            'year': ab.coverDate,
            'doi': ab.doi,
            'affils': affils
        }

        data.append(document)
        count += 1

    writablefile.write(json.dumps(data))

    writablefile.close()

    print("Process complete!")

if __name__ == '__main__':
    main()