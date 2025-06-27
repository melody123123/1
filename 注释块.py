"""
学生成绩管理系统
功能：添加、查询、统计、保存和加载学生成绩
"""

import json
import os

# 全局变量：存储学生数据
students = []

def display_menu():
    """显示主菜单"""
    print("\n" + "=" * 30)
    print("学生成绩管理系统")
    print("1. 添加学生信息")
    print("2. 查询学生信息")
    print("3. 统计成绩")
    print("4. 显示所有学生")
    print("5. 保存数据到文件")
    print("6. 从文件加载数据")
    print("0. 退出系统")
    print("=" * 30)

def add_student():
    """添加学生信息"""
    print("\n--- 添加学生信息 ---")
    name = input("姓名: ")
    student_id = input("学号: ")
    while True:
        try:
            math = float(input("数学成绩: "))
            english = float(input("英语成绩: "))
            break
        except ValueError:
            print("错误：请输入数字！")

    student = {
        "name": name,
        "id": student_id,
        "math": math,
        "english": english,
        "total": math + english
    }
    students.append(student)
    print(f"成功添加学生: {name}")

def query_student():
    """查询学生信息"""
    print("\n--- 查询学生信息 ---")
    keyword = input("请输入学号或姓名: ")
    found = False
    
    for student in students:
        if keyword in (student["id"], student["name"]):
            print("\n找到学生信息:")
            print(f"姓名: {student['name']}")
            print(f"学号: {student['id']}")
            print(f"数学: {student['math']}")
            print(f"英语: {student['english']}")
            print(f"总分: {student['total']}")
            found = True
    
    if not found:
        print("未找到匹配的学生！")

def show_all_students():
    """显示所有学生"""
    print("\n--- 所有学生信息 ---")
    if not students:
        print("没有学生数据！")
        return
    
    for idx, student in enumerate(students, 1):
        print(f"{idx}. {student['name']}({student['id']}): "
              f"数学{student['math']} 英语{student['english']} "
              f"总分{student['total']}")
# def show_statistics():
#     """统计成绩"""
#     if not students:
#         print("没有学生数据可统计！")
#         return
#     
#     math_scores = [s["math"] for s in students]
#     english_scores = [s["english"] for s in students]
#     
#     print("\n--- 成绩统计 ---")
#     print(f"学生总数: {len(students)}")
#     print(f"数学平均分: {sum(math_scores)/len(math_scores):.1f}")
#     print(f"英语平均分: {sum(english_scores)/len(english_scores):.1f}")
#     print(f"数学最高分: {max(math_scores)}")
#     print(f"英语最高分: {max(english_scores)}")

def main():
    """主程序循环"""
    while True:
        display_menu()
        choice = input("请选择操作(0-6): ")
        
        if choice == "0":
            print("感谢使用，再见！")
            break
        elif choice == "1":
            add_student()
        elif choice == "2":
            query_student()
        elif choice == "3":
            print("该功能已临时禁用")  # 原 show_statistics() 调用替换为提示
        # elif choice == "3":
        #     show_statistics()
        elif choice == "4":
            show_all_students()
        elif choice == "5":
            save_to_file()
        elif choice == "6":
            load_from_file()
