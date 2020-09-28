# 画像から顔を切り出すプログラムです

# OpenCVを読み込む
import cv2

# 正面の顔のカスケード分類器を読み込む
face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

def face_detect(file_name):
    # 画像ファイルの読み込み
    img = cv2.imread(file_name)
    # 読み込んだ画像ファイルをモノクロに
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 顔を検出
    faces = face_cascade.detectMultiScale(gray)
    # 画像に映った顔情報を返す
    return img, faces

def trimming(img, info):
    # カウンター (画像ファイルの名前に使う)
    counter = 0
    for (x,y,w,h) in info:
        counter += 1
        # 画像をトリミング
        block = img[y:y+h, x:x+w]
        # 画像ファイルの名前
        output_file_name = "image_%d.png" % counter
        # 画像を保存
        cv2.imwrite(output_file_name, block)

# 指定した画像をデータとして受け取り、顔の情報を受け取る
img, faces = face_detect("train_1.png")
# 受け取った情報を元に、トリミングを行う
trimming(img, faces)