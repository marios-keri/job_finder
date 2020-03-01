"""The idea is to get the tiles of the jobs form various sources and applay to all of thoses sources at onec"""

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver

__author__ = 'Marios Keri'
__date__ = '27-02-2020'


class Portal():
    def __init__(self, job: str, where: str):
        self.job_portal_list = {'reed': f'https://www.reed.co.uk/jobs/{job.replace(" ", "-").lower()}-in-{where.lower()}'
                                ,'monster': f'https://www.monster.co.uk/jobs/search/?q={job.replace(" ", "-").lower()}'
                                            f'&where={where.lower()}&client=power&cy=uk&rad=20&intcid=swoop_Hero_Search'
                                ,'indeed': f'https://www.indeed.co.uk/jobs?q={job.replace(" ", "+").lower()}&l={where.lower()}+'
                                ,'torvit': f'https://jobs.trovit.co.uk/index.php/cod.search_jobs/what_d.{job.replace(" ", "%20").lower()}'
                                           f'/where_d.{where.lower()}sug.0/isUserSearch.1'
                                ,'adzuma': f'https://www.adzuna.co.uk/jobs/search?q={job.replace(" ", "%20").lower()}&w={where.lower()}'
                                ,'careerbulder': f'https://www.careerbuilder.co.uk/jobsearch?utf8=%E2%9C%93&q={job.replace(" ", "%20").lower()}'
                                                 f'&loc={where.lower()}'}


class Reed(Portal):
    """Get the job titles from red.co.uk"""
    def __init__(self, job, where):
        super().__init__(job, where)
        self.url = self.job_portal_list['reed']

    def get_requests(self, url: str) -> requests.Response:
        """Gets a url and returns a response"""
        return requests.get(url)

    def scrap_h3(self, response: requests.Response) -> dict:
        """Scrap the title, links from h3 bs elements"""
        job_links = {}

        # scrap
        bs_object = bs(response.content, 'html.parser')
        h3 = bs_object.find_all('h3')

        # get the links and titles
        for item in h3:
            try:
                job_links[item.text] = item.a['href']
            except TypeError:
                pass

        # return dict[tile: link]
        return job_links

    def get_jobs(self) -> dict:
        """CONSTRUCTUR PATTERN"""
        response = self.get_requests(self.url)
        jobs = self.scrap_h3(response)
        return jobs


class Monster(Portal):
    """Get the job titles from red.co.uk"""
    def __init__(self, job: str, where: str):
        super().__init__(job, where)
        self.url = self.job_portal_list['monster']

    def get_requests(self, url: str) -> requests.Response:
        """Gets a url and returns a response"""
        return requests.get(url)

    def scrap_title(self, response: requests.Response) -> dict:
        """Scrap the title, links from h3 bs elements"""
        job_links = {}

        # scrap
        bs_object = bs(response.content, 'html.parser')
        job_title = bs_object.find_all('h2', {'class': 'title'})

        # get the links and titles
        for item in job_title:
            try:
                job_links[item.text] = item.a['href']
            except TypeError:
                pass

        # return dict[tile: link]
        return job_links

    def get_jobs(self) -> dict:
        """CONSTRUCTUR PATTERN"""
        response = self.get_requests(self.url)
        jobs = self.scrap_title(response)
        return jobs

      
# FORM HERE YUO CAN SCRAP THE DESCRIPTION, SPECIFICATIONS OF JOB BY USING THE LINKS RETURNED BY THE 'Red' class

# NEXT STEP: built similar class for all the links above
