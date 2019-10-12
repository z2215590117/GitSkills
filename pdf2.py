import os
import pdfplumber
import pyperclip

'''将全部pdf文件转换成1个txt文件'''
def transform(output):
    f = open('%s.txt' % (output), 'w+', encoding='utf-8')
    dir_name = input('请输入桌面上要转换的文件名子：')
    '''拿到文件的路径'''
    name = os.walk(r'C:\Users\RX_TIAN\Desktop\%s' % dir_name)
    for root, dir, files in name:
        for file in files:
            path = (root + '\\' + file)

            try:
                if file.find('.pdf') > 0:

                    pdf = pdfplumber.open('%s' % path)
                    for page in pdf.pages:
                        f.write(file +'\n'+'-'*30 + '\n' + page.extract_text() + '\n' + '-'*30 + '\n')

                else:
                    pass
            except Exception:
                print('内容为空,跳过')

            f.close()

'''将pdf转换成txt'''
def transform_txt():

    dir_name = input('请输入桌面上要转换的文件名子：')
    '''拿到文件的路径'''
    name = os.walk(r'C:\Users\RX_TIAN\Desktop\%s' % dir_name)

    for root, dir, files in name:
        for file in files:
            path = (root + '\\' + file)

            try:
                if file.find('.pdf') > 0:

                    index = file.find('.pdf')
                    filename = file[0:index]
                    f = open('%s.txt' % filename, 'w+', encoding='utf-8')

                    pdf = pdfplumber.open(path)

                    for page in pdf.pages:
                        f.write(filename + '\n'+'-'*30 +'\n' + page.extract_text() + '\n'+'-'*30)
                        f.close()
                else:
                    pass

            except Exception:
                print('内容为空，跳过')

'''复制到剪贴板'''
def copy(output):
    f = open('D:\PyProject\PDF文件\\%s.txt'%(output), 'r', encoding='utf-8')
    content = f.read()
    pyperclip.copy(content)
    f.close()

if __name__ == '__main__':
    transform_txt()
