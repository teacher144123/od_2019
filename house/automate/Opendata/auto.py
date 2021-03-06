from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://semap.moi.gov.tw/STATViewer/Web/Map/STATViewer_Map.aspx')
driver.maximize_window()
driver.find_element_by_id('Locate').click()
time.sleep(1)

driver.find_element_by_id('ui-id-12').click()
driver.find_element_by_css_selector("label[for='LocateBox_Coord_WGS84']").click()
driver.find_element_by_id('LocateBox_Coord_Work_WGS84_lng').clear()
driver.find_element_by_id('LocateBox_Coord_Work_WGS84_lat').clear()
driver.find_element_by_id('LocateBox_Coord_Work_WGS84_lng').send_keys('121.533012')
driver.find_element_by_id('LocateBox_Coord_Work_WGS84_lat').send_keys('25.042385')
driver.find_element_by_id('LocateBox_Coord_Work_WGS84_Locate').click()

time.sleep(1)
driver.find_element_by_css_selector("img[class='PointStatInfo']").click()

#element = driver.find_element_by_css_selector("img[class='PointStatInfo']").click()
#driver.execute_script("arguments[0].click();", element)


time.sleep(1)
res = driver.find_element_by_class_name('PointStatInfoBox_STUnitBts')
tds = res.find_elements_by_tag_name('td')


i = 0
while(True):
    time.sleep(1)
    print(i)
    print(tds[1].text)
    if tds[1].text != "讀取中...":
        print("Done!")
        break
    i += 1

key = ["county","town","village","code2","code1","codebase"]
result = {}

for i in range(len(key)):
    result[key[i]] = tds[i+(i+1)].text
print(result)

#print([td.text for td in tds[1::2]])
#{tds[i].text: tds[i + 1].text for i in range(0, len(tds), 2)}
