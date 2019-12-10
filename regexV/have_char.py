import requests
import re

get_all_course_regex = re.compile("<tbody>(.+?)</tbody>")

get_course_url_regex = re.compile('<a href="(.+?)">')

get_title_regex = re.compile('<h1 id="page-title">(.+?)</h1>')

get_num_regex = re.compile('<div class="label-inline">Number:&nbsp;</div>(.+?)</div>')

get_level_regex = re.compile('<div class="field field-name-field-course-level"><div class="label-inline">Level:&nbsp;</div>(.+?)</div>')

get_unit_regex = re.compile('<div class="field field-name-field-units"><div class="label-inline">Units:&nbsp;</div>(.+?)</div>')

get_desc_regex = re.compile('<h2 class="label-above">Description</h2><p>(.+?)</p>')

home_html = requests.get("https://cs.ucsb.edu/education/courses/descriptions").content.replace("\n", "")

courses_html = get_all_course_regex.findall(home_html)
urls = get_course_url_regex.findall(courses_html[0])
result = []
for url in urls:
    course_html = requests.get("https://cs.ucsb.edu" +url)).content.replace("\n", "")
    title = get_title_regex.findall(course_html)[0]
    num = get_num_regex.findall(course_html)[0]
    try:
        level = get_level_regex.findall(course_html)[0]
    except IndexError:
        print(url)
        level = "error"
    try:
        unit = get_unit_regex.findall(course_html)[0]
    except IndexError:
        print(url)
        unit = "0"
    try:
        desc = get_desc_regex.findall(course_html)[0]
    except IndexError:
        print(url)
        desc = "none"
    result.append({
        "title": title.replace("                  ", "").replace("                 ", ""),
        "description": {
            "num": num,
            "level": level,
            "unit": unit,
            "desc": desc
        }
    })

print((result))