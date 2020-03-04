"""The idea is to get the tiles of the jobs form various sources and applay to all of thoses sources at onec"""

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver

__author__ = 'Marios Keri'
__date__ = '27-02-2020'


class ScrapPortal():
    def __init__(self, job: str, where: str):
        self.job_portal_list = {'reed': f'https://www.reed.co.uk/jobs/{job.replace(" ", "-").lower()}-in-{where.lower()}'
                                ,'monster': f'https://www.monster.co.uk/jobs/search/?q={job.replace(" ", "-").lower()}'
                                            f'&where={where.lower()}&client=power&cy=uk&rad=20&intcid=swoop_Hero_Search'
                                ,'indeed': f'https://www.indeed.co.uk/jobs?q={job.replace(" ", "+").lower()}&l={where.lower()}+'
                                ,'trovit': f'https://jobs.trovit.co.uk/index.php/cod.search_jobs/what_d.{job.replace(" ", "%20").lower()}'
                                           f'/where_d.{where.lower()}sug.0/isUserSearch.1'
                                ,'adzuma': f'https://www.adzuna.co.uk/jobs/search?q={job.replace(" ", "%20").lower()}&w={where.lower()}'
                                ,'careerbulder': f'https://www.careerbuilder.co.uk/jobsearch?utf8=%E2%9C%93&q={job.replace(" ", "%20").lower()}'
                                                 f'&loc={where.lower()}'}

    def get_requests(self, key):
        if key not in self.job_portal_list.keys():
            exit(f'Valid key names are {self.job_portal_list.keys()}')
        return requests.get(self.job_portal_list[key])

    def scrap(self, response, tag, class_name=None):
        """Scrap the title, links from h3 bs elements"""
        job_links = {}

        # scrap
        bs_object = bs(response.content, 'html.parser')
        if class_name is not None:
            element = bs_object.find_all(tag, {'class': class_name})
        else:
            element = bs_object.find_all(tag)
        # get the links and titles
        for item in element:
            try:
                job_links[item.text] = item.a['href']
            except TypeError:
                pass

        # return dict[tile: link]
        return job_links

    def get_jobs(self, key, tag, class_name=None):
        response = self.get_requests(key)
        output = self.scrap(response, tag, class_name)
        if len(output) == 0:
            exit(f'No jobs found')
        else:
            return output


      
# FORM HERE YUO CAN SCRAP THE DESCRIPTION, SPECIFICATIONS OF JOB BY USING THE LINKS RETURNED BY THE 'Red' class

# NEXT STEP: built similar class for all the links above
