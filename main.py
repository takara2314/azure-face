import copy
import requests
import cv2

BASE_URL = "###"
KEY = "###"

# リクエストヘッダー
headers = {
    "Content-Type": "application/octet-stream",
    "Ocp-Apim-Subscription-Key": KEY
}

def get_faceid(img_path):
    # 画像をデータとして開く
    img_data = open(img_path, "rb")
    # 画像をOpenCVの形式で開く
    img_data_cv2 = cv2.imread(img_path)

    # FaceAPI にPOSTリクエスト
    res = requests.post(
        BASE_URL+"/detect",
        headers=headers,
        data=img_data
    )

    # レスポンスから顔情報を受け取る
    # 型: リスト (リストの中に辞書がある)
    faces = res.json()

    # 顔の分だけループをまわす
    for face in faces:
        # 顔IDや顔の位置や長さを取得
        face_id = face["faceId"]
        x = face["faceRectangle"]["top"]
        y = face["faceRectangle"]["left"]
        w = face["faceRectangle"]["width"]
        h = face["faceRectangle"]["height"]

        # 画像ファイルとして書き込み
        cv2.imwrite("{}.png".format(face_id), img_data_cv2[x:x+w, y:y+h])

get_faceid("train_1.png")