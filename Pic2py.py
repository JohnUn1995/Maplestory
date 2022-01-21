import base64

def main():
    pics = ["money_1.png", "ojbk.png","sure.png","location.png"]      ## 需要转换的图片的名字
    for i in pics:
        pic2py(i)
    print("ok")
 
def pic2py(picture_name):
    """
    将图像文件转换为py文件
    :param picture_name:
    :return:
    """
    open_pic = open("%s" % picture_name, 'rb')
    b64str = base64.b64encode(open_pic.read())
    open_pic.close()
    # 注意这边b64str一定要加上.decode()
    write_data = 'img = "%s"' % b64str.decode()
    f = open('%s.py' % picture_name.replace('.', '_'), 'w+')
    f.write(write_data)
    f.close()
 
if __name__ == '__main__':
    main()