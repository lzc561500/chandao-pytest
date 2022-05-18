import os
import time


class Excuse:

    def run_main(self):
        os.system(r"cd E:\pycharm 2019\项目列表\chandao-pytest")
        os.system("pytest")
        time.sleep(10)
        os.system("allure generate report -o report/html --clean")
        # path = r"E:\pycharm 2019\项目列表\chandao-pytest\report"
        # files = os.listdir(path)
        # for i in files:
        #     new_path = r"E:\pycharm 2019\项目列表\chandao-pytest\report"+"\\"+i
        #     if (os.path.isfile(new_path)):
        #         os.remove(new_path)
        #     else:
        #         continue


if __name__ == '__main__':
    Excuse().run_main()
