# coding=utf-8
"""
    作者：s.xiao
    时间：2018年12月16日00点02分
    功能：实现一个cmd下简单的学生信息管理系统
    版本：V1.0
    # 学生信息管理项目，要求带操作界面，并完成每项操作：
    #  ＋－－－－－－－－－－－－－－－－－－－－－－＋
    # ｜　１）添加学生信息　　　　　　　　　　　　　　　　　　　　　　｜
    # ｜　２）显示所有学生的信息　　　　　　　　　　　　　　　　　｜
    # ｜　３）删除学生信息　　　　　　　　　　　　　　　　　　　　　　｜
    #  ｜　４）修改学生信息　　　　　　　　　　　　　　　　　　　　　　｜
    # ｜　５）按学生成绩高－低显示学生信息　　　　　　　　　｜
    # ｜　６）按学生成绩低－高显示学生信息　　　　　　　　　｜
    # ｜　７）按学生年龄高－低显示学生信息　　　　　　　　　｜
    # ｜　８）按学生年龄低－高显示学生信息　　　　　　　　　｜
    # ｜ ９）保存学生信息到文件（students.txt)      ｜
    # ｜ １０）从文件中读取数据（students.txt)      ｜
    # ｜ 退出：其他任意按键＜回车＞                 ｜
    # ＋－－－－－－－－－－－－－－－－－－－－－－＋               　　　　　　　　　｜

"""


def menu():
    menu_info = """
                #  ＋－－－－－学生信息管理信息系统－－－－－－－－＋
                # ｜　１）添加学生信息　　　　　　　　　　　　 　｜
                # ｜　２）显示所有学生的信息　　　　　　　　　　 ｜
                # ｜　３）删除学生信息　　　　　　　　　　　　 　｜
                # ｜　４）修改学生信息　　　　　　　　　　　　　｜
                # ｜　５）按学生成绩高－低显示学生信息　　　　　 ｜
                # ｜　６）按学生成绩低－高显示学生信息　　　　 　｜
                # ｜　７）按学生年龄高－低显示学生信息　　 　　　｜
                # ｜　８）按学生年龄低－高显示学生信息　　 　　　｜
                # ｜  ９）保存学生信息到文件（students.txt)      ｜
                # ｜  １０）从文件中读取数据（students.txt)      ｜
                # ｜  退出：其他任意按键＜回车＞                 ｜
                # ＋－－－－－－－－－－－－－－－－－－－－－－＋ 
    
    """
    print(menu_info)


def add_student_info():
    """
        1)添加学生信息
    :return: L
    """
    L = []
    while True:
        stu_info_name = input('请输入学生姓名信息：')
        if not stu_info_name:
            break
        try:
            stu_info_age = input('请输入学生年龄信息：')
            stu_info_score = input('请输入学生成绩：')
        except:
            print('输入无效，请重新输入')
            continue

        stu_info = {"name": stu_info_name, "age": stu_info_age, "score": stu_info_score}
        L.append(stu_info)
    print("学生信息输入完毕！")
    return L


def del_student_info(student_info, del_name=""):
    """
        删除学生信息
    :param student_info: 学生信息
    :param del_name: 删除学生姓名
    :return: 被学生的信息
    """
    if not del_name:
        del_name = input('请输入删除学生的姓名：')
    for info in student_info:
        if del_name == info.get('name'):
            return info
    raise IndexError('学生信息不匹配，没有找到%s' % del_name)


def mod_student_info(student_info):
    if not student_info:
        mod_name = input('请输入需要修改学生的姓名：')
    for info in student_info:
        if mod_name == info.get('name'):
            mode_age = input('请输入需要修改的学生年龄：')
            mode_score = input('请输入需要修改的学生的成绩：')
            info = {'name': mod_name, 'age': mode_age, 'score': mode_score}


def show_student_info(student_info):
    if not student_info:
        print('无效的学生信息。。。')
        return
    print("名字".center(8), "年龄".center(4), "成绩".center(4))

    for info in student_info:
        print(info.get("name").center(10), info.get("age").center(4), info.get("score").center(4))


def main():
    menu()

    l1 = add_student_info()
    show_student_info(l1)
    del_student_info(l1)


if __name__ == '__main__':
    main()
