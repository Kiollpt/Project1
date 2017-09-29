使用BeautifulSoup取得Beauty版的title, liked, img_src 並存入資料庫</br>
設定liked數決定是否下載圖片，並將圖片存到電腦的指定位置</br>
資料庫有兩種選擇：SQLite/ Mongodb</br>
In spider.py:</br>
 1. run_sql():存入SQLite</br>
 2. run_mongo():存入Mongodb</br>
