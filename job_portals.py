"""The idea is to get the tiles of the jobs form various sources and applay to all of thoses sources at onec"""

import requests
from bs4 import BeautifulSoup as bs


job_portal_list = {'https://www.reed.co.uk/'
                  ,'https://www.monster.co.uk/'
                  ,'https://www.jobsite.co.uk/'
                  ,'https://www.indeed.co.uk/'
                  ,'http://jobs.telegraph.co.uk/'
                  ,'https://www.agencycentral.co.uk/'
                  ,'https://jobs.trovit.co.uk/'
                  ,'https://www.cwjobs.co.uk/'
                  ,'https://www.adzuna.co.uk/'
                  ,'https://www.careerbuilder.co.uk/'}

class Red:
"""Get the job titles from red.co.uk"""
    def query_constructor(job: str, where: str) -> str:
        """query constructor"""
        base = 'https://www.reed.co.uk/jobs/'
        title = f'{job.replace(" ", "-").lower()}'
        cyti = f'-in-{where.lower()}'
        query = base + title + cyti
        return query

    def get_requests(url: str) -> requests.Response:
        """Gets a url and returns a response"""
        return requests.get(url)

    def scrap_h3(response: requests.Response) -> dict:
        """Scrap the title, links from h3 bs elements"""
        job_links = {}

        # scrap
        bs_object = bs(response.content, 'html.parser')
        h3 = bs_object.find_all('h3')

        print(type(h3))
        # get the links and titles
        for item in h3:
            try:
                job_links[item.text] = item.a['href']
            except TypeError:
                pass

        # return dict[tile: link]
        return job_links

    # CONSTRUCTUR PATTERN
    def get_jobs(title: str, location: str) -> dict:
        query = Red.query_constructor(title, location)
        response = Red.get_requests(query)
        jobs = Red.scrap_h3(response)
        return jobs


