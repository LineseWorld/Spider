from PIL import Image
import pytesseract
# 基本上失败了

def convert_img(img,threshold):
    """
    将图片灰度两极分化
    :param img: 图片
    :param threshold: 设置threshold阈值，超过阈值的为黑色
    :return: 图片
    """
    img = img.convert("L")  # 处理灰度
    # 加载图片形式
    pixels = img.load()
    # 颜色遍历处理
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return img

# 简单识别
# 打开图片
# captcha1 = Image.open("captcha_img\\pic1.png")
# # 识别成功
# result1 = pytesseract.image_to_string(captcha1)
# print(result1)
#
# # ====难度2
# captcha2 = Image.open("captcha_img\\pic2.png")
# result2 = pytesseract.image_to_string(captcha2)
# # 识别失败
# print(result2)




# ===== 需要自己调参数才有可能识别成功 。。。


captcha1 = Image.open("captcha_img\\pic1.png")
result1 = convert_img(captcha1,150) # 简单灰度优化
result1 = pytesseract.image_to_string(result1)
print(result1)


captcha2 = Image.open("captcha_img\\pic2.png")
result2 = convert_img(captcha2,120)
result2.show()
result2 = pytesseract.image_to_string(result2)
print(result2) # 成功了


captcha3 = Image.open("captcha_img\\2.png")
result3 = convert_img(captcha3,170)
result3.show()
result3 = pytesseract.image_to_string(result3)
print(result3) # 失败了

captcha4 = Image.open("captcha_img\\pic3.png")
result4 = convert_img(captcha4,125)
result4.show()
result4 = pytesseract.image_to_string(result4)
print(result4) # 成功了

