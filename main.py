# -*- Coding: utf-8 -*-

from HTTPClient import HTTPClient

httpClient = HTTPClient()
soup = httpClient.connect("https://hogehoge.com")

#### Parserクラスは各リポジトリで作成 ####