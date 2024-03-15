# Discord 聊天統計機器人

一個基於 `Discord.py` 開發的聊天統計機器人，可以查詢指定時間區間內所有成員的聊天訊息(目前只有這個功能)，有需要的請自取。

使用channel.history來實現，不像一般只能統計機器人加入後的訊息，但是因為discord API的設計單一指令只能執行15分鐘，所以訊息總數大約6萬就到極限。

## Getting Started

```shell
git clone https://github.com/balaOuO/DiscordBot.git
cd discord-statistics-bot
pip install -r requirements.txt
```
接下來在此目錄下加入一個檔案`.env`，並在裡面加上你的discord 機器人的token () : 
```env
TOKEN='{Your Discord Bot Token}'
```
接下來執行`main.py`
```shell
python main.py
```
當出現下列訊息代表啟動成功
```shell
目前登入身份 --> {Your Discord Bot Name}
載入 2 個斜線指令
```

## 指令介紹
### `/阿巴阿巴`
機器人使用說明

### `/聊天統計`
計算聊天室、討論串、語音文字聊天室和貼文的聊天句數
(發送斜線指令不記入聊天句數)  
參數 :  
`start`開始時間  
`end`結束時間  
`member`成員  
`limit`單一頻道最大統計訊息數量  