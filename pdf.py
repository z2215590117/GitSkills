import pdfplumber
import os
import pyperclip

'''将全部pdf文件转换成1个txt文件'''
def transform(output):
    path = str(input('输入路径:'))
    dir = os.listdir(path)

    f = open('%s.txt' % (output), 'w+', encoding='utf-8')
    for file in dir:
        try:
            if file.find('.pdf') > 0:

                pdf = pdfplumber.open('%s\%s'%(path,file))

                for page in pdf.pages:


                    f.write(file +'\n'+'-'*30 + '\n' + page.extract_text() + '\n' + '-'*30 + '\n')

                else:
                    pass
        except Exception:
            print('内容为空，跳过')



'''将pdf转换成txt'''
def transform_txt():

    dir = os.listdir('D:\\1')

    for file in dir:

        try:
            if file.find('.pdf') > 0:

                index = file.find('.pdf')
                filename = file[0:index]
                f = open('%s.txt' % filename, 'w+', encoding='utf-8')

                pdf = pdfplumber.open('D:\\1\%s' % file)

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
    transform(4)
    copy(4)