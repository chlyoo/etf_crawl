from setuptools import setup

setup(
    name='pythonProject',
    version='0.1',
    install_requires=[
        "selenium",
        "chromedriver-autoinstaller",
        "xlsxwriter",
        "pandas",
        "lxml",
        "BeatuifulSoup"
    ],
    packages=[''],
    url='github.com/chlyoo/etf_crawl',
    license='GPL 2.0',
    author='chlyoo',
    author_email='changhyunlyoo@gmail.com',
    description='네이버 주식 ETF 구성 크롤링'
)
