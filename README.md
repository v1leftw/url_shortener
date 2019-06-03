# Bitly url shortener

Script makes URL short by using [bit.ly API](https://dev.bitly.com/v4_documentation.html)
Also can be used to get count of the clicks of specific bit.ly link (If you arleady have one)


### Quickstart
To use just type link you need to make short:
```
python3 shortener.py http://any.url
bit.ly/your_short_url
```
To get clicks count input your bit.ly link:
```
python3 shortener.py http://bit.ly/your_short_url
clicks_count: 10
```
### How to install
This scripts using token authentication. To get information that script provides you need to set your token in .env file.

[How to get your token](https://dev.bitly.com/v4/#section/Authentication)


Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).