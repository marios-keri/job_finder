import job_portals

webiste = job_portals.ScrapPortal('python developer', 'manchester')



# the 2d paramet and the 3d are the html elementa correspondint to job tiles in the original webpage
# Note: the webpage may change those element therfore they mus be update here as well, for the program to work
reed_jobs = webiste.get_jobs('reed', 'h3')
monster_jobs = webiste.get_jobs('monster', 'h2', 'title')
indeed = webiste.get_jobs('indeed', 'div', 'title')
trovit = webiste.get_jobs('trovit', 'h4')
adzuma = webiste.get_jobs('adzuma', 'h2')



for k, v in reed_jobs.items():
    print(k, v)
