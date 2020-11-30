from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time

lines = []
fp = open("testfile.txt", "r", encoding="utf-8")
text2 = fp.readlines()
for line in text2:
    lines.append(line)

#text = fp.read()
fp.close()

line_st = ''
lines_list = []
index = 0
size = 0

while index != len(lines):
    size += len(lines[index])
    if size < 500:
        line_st += lines[index]
        line_st += ';'
        index += 1
    else:
        lines_list.append(line_st)
        size = 0
        line_st = ''

#ready_list = []

# while (len(text) > 500):
#     temp_str = text[:500]
#     last_space = temp_str.rfind(' ')
#     temp_str = text[0:last_space]
#     ready_list.append(temp_str)

#     text = text[last_space:]

# ready_list.append(text)

dv = webdriver.Chrome(
    executable_path=r'C:/Users/chromedriver_win32/chromedriver.exe')
dv.get("http://www.naver.com")

elem = dv.find_element_by_name("query")
elem.send_keys("맞춤법 검사기")
elem.send_keys(Keys.RETURN)

time.sleep(2)

textarea = dv.find_element_by_class_name("txt_gray")

new_str = ''
for ready in lines_list:
    textarea.send_keys(Keys.CONTROL, "a")
    textarea.send_keys(ready)

    elem = dv.find_element_by_class_name("btn_check")
    elem.click()

    time.sleep(1)

    soup = BeautifulSoup(dv.page_source, 'html.parser')

    st = soup.select("p._result_text.stand_txt")[0].text
    new_str += st.replace(';', '\n')

fp = open("modify_result.txt", 'w', encoding='utf-8')
fp.write(new_str)
