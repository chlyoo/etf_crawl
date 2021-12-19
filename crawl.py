from enum import Enum
from datetime import datetime
import pandas as pd
from bs4 import BeautifulSoup
from ETF import ETF
import lxml
import xlsxwriter
from selenium import webdriver
import chromedriver_autoinstaller


def basic_options():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])  #
    options.add_experimental_option('useAutomationExtension', False)  #
    #     options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    options.add_argument("lang=ko_KR")
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("--no-sandbox")
    return options


def crawl_naver_etf():
    driver = webdriver.Chrome(options=basic_options())
    frames = []
    for item in ETF:
        search_url = f"https://finance.naver.com/item/coinfo.naver?code={item.value}&target=cu_more"
        driver.get(search_url)
        driver.switch_to.frame('coinfo_cp')
        source = driver.page_source
        soup = BeautifulSoup(source, "lxml")
        table = soup.find('table', id='CU_grid')
        df = pd.read_html(table.prettify())
        frames.extend(df)
    driver.quit()
    return frames


def write_as_excel(filename, sheet_name):
    writer = pd.ExcelWriter(filename, engine='xlsxwriter', engine_kwargs={'options': {'strings_to_numbers': True}})
    result.to_excel(writer, sheet_name=sheet_name)
    max_row, max_col = result.shape
    wb = writer.book
    ws = writer.sheets[sheet_name]
    header_format = wb.add_format({
        'bold': True,
        'valign': 'top',
        'align': 'center'
    })
    name_format = wb.add_format({
        'bold': True,
        'valign': 'center',
        'align': 'center'
    })
    ws.set_column('E:E', 15, None)
    ws.set_column('D:D', 15, None)
    ws.set_column('C:C', 25, None)
    ws.set_column('B:B', 0, None)
    ws.set_column('A:A', 40, name_format)
    ws.write(0, 0, "ETF명", header_format)
    ws.autofilter(0, 0, max_row, 2)
    ws.freeze_panes(1, 3)
    writer.save()


if __name__ == '__main__':
    chromedriver_autoinstaller.install()
    etf_datas = crawl_naver_etf()
    result = pd.concat(etf_datas, keys=[etf.name for etf in ETF])
    write_as_excel(filename=f'ETF 구성 현황-{datetime.today().strftime("%y_%m_%d")}.xlsx', sheet_name="ETF 주식 구성")
