from PIL import Image
import os
PATH = "input_path"
# 변환할 파일이 있는 폴더 path 입력!
OUT_PATH = "out_path"
# 변환 파일을 출력할 폴더 path 입력!
odin = os.listdir(PATH)

for i in range(len(odin)):
    # 출력경로 : path + '/' 파일 이름
    node = str(PATH + '/' + odin[i])
    img = Image.open(node)
    height = 128
    width = 128
    # 조정할 이미지 사이즈 입력 ( 비율 유지 - 픽셀 )
    img = img.resize((height, width), Image.ANTIALIAS)
    OUTPUT = OUT_PATH + '/' + odin[i]
    img.save(OUTPUT)