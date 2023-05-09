from typing import Dict, List

from src.models.schemas import harvester


class SemanticScholarAPI:

    @staticmethod
    async def get_author(authorId: int | str, session) -> harvester.SemanticScholarData | None:
        URL = f"https://api.semanticscholar.org/graph/v1/author/{authorId}?fields=" + \
            "authorId,externalIds,url,name,aliases,affiliations,homepage,paperCount,citationCount,hIndex," +\
            f"papers.paperId,papers.corpusId,papers.externalIds,papers.url,papers.title,papers.abstract,papers.venue,papers.publicationVenue,papers.year,papers.referenceCount,papers.citationCount,papers.influentialCitationCount,papers.isOpenAccess,papers.openAccessPdf,papers.fieldsOfStudy,papers.s2FieldsOfStudy,papers.publicationTypes,papers.publicationDate,papers.journal,papers.citationStyles,papers.authors&limit=1000"

        # async with semaphore:
        async with session.get(URL, ssl=False) as response:
            json_response = await response.json()

            if response.status == 200:
                if len(json_response.get('papers')) == 1000:

                    # for num in range(1001, 5001):
                    async with session.get(URL + "&offset=1001", ssl=False) as response:

                        json_response_2 = await response.json()
                        json_response['papers'] += json_response_2['papers']

                return json_response

    @staticmethod
    async def get_authors(ids: Dict[str, List[str]], session) -> List[harvester.SemanticScholarData] | None:

        URL = f"https://api.semanticscholar.org/graph/v1/author/batch?fields=" + \
            "authorId,externalIds,url,name,aliases,affiliations,homepage,paperCount,citationCount,hIndex," +\
            "papers.paperId,papers.corpusId,papers.externalIds,papers.url,papers.title,papers.abstract,papers.venue,papers.publicationVenue,papers.year,papers.referenceCount,papers.citationCount,papers.influentialCitationCount,papers.isOpenAccess,papers.openAccessPdf,papers.fieldsOfStudy,papers.s2FieldsOfStudy,papers.publicationTypes,papers.publicationDate,papers.journal,papers.citationStyles,papers.authors&limit=1000"

        # NOTE: 'Cannot request more than 100 authors  with fields=papers'
        async with session.post(URL, json=ids) as response:
            json_response = await response.json()

            if response.status == 200:
                return json_response

            return None

    @staticmethod
    async def get_paper(paperId, session, semaphore) -> harvester.SemanticScholarData | None:

        URL = f"https://api.semanticscholar.org/graph/v1/paper/{paperId}?fields=" +\
            "paperId,corpusId,externalIds,url,title,abstract,venue,publicationVenue,year,referenceCount,citationCount,influentialCitationCount,isOpenAccess,openAccessPdf,fieldsOfStudy,s2FieldsOfStudy,publicationTypes,publicationDate,journal,citationStyles,authors"

        async with session.get(URL,  ssl=False) as response:
            json_response = await response.json()

            if response.status == 200:
                return json_response

        return None
