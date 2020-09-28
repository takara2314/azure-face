import requests

BASE_URL = "https://############.cognitiveservices.azure.com/face/v1.0/detect"
KEY = "############"

# リクエストヘッダー
headers = {
    "Content-Type": "application/octet-stream",
    "Ocp-Apim-Subscription-Key": KEY
}

# 画像のパス
img_path = "./train_1.png"
# 画像をデータとして開く
img_data = open(img_path, "rb")

# FaceAPI にPOSTリクエスト
res = requests.post(
    BASE_URL,
    headers=headers,
    data=img_data
)

# 画像から検知した顔情報を出力
print(res.json())
