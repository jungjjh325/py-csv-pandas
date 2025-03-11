import re
import os
import csv
import pandas as pd
from prettytable import PrettyTable

def valid_input(prompt, valid_input = None, isint = False):
    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print('오류: 공백이 입력되었습니다.')
            print()

            continue

        if valid_input and user_input not in valid_input:
            print(f'오류: {valid_input} 외에는 입력될 수 없습니다.')
            print()


            continue

        if isint:
            if user_input.isdigit():
                return int(user_input)

            else:
                print('오류: 숫자만 입력할 수 있습니다.')
                print()

                continue

        return user_input

def found_file(file, header = None):
    if not os.path.exists(file):
        with open('file', 'w', newline='') as file_:
            writer = csv.writer(file_)
            if header:
                writer.writerow(header)

found_file('students.csv', ['학번', '이름', '수학', '영어', '과학', '국어'])
header_exists = False

class student_infomations():
    def __init__(self):
        self.student = []
        self.ensure_file()

    def ensure_file(self):
        if not os.path.exists('students.csv'):
            print('if')
            self.create_header()
        elif os.path.getsize('students.csv') == 0:
            print('elif')
            self.create_header()
        else:
            print('else')
            with open('students.csv', 'r', encoding='utf-8') as student_csv_files:
                first_line = student_csv_files.readline()

                if first_line != 'student_id,student_name,math_score,english_score,science_score,korean_score':
                    with open('students.csv', 'a', encoding='utf-8', newline='') as student_file:
                        student_datas = csv.writer(student_file)

                else:
                    print('헤더가 이미 존재함')
                    print()

    def create_header(self):
        with open('students.csv', 'w', encoding='utf-8', newline='') as student_file:
            student_datas = csv.writer(student_file)
            student_datas.writerow(['student_id', 'student_name', 'math_score', 'english_score', 'science_score', 'korean_score'])

    def add_student(self):
        student_name = valid_input('이름: ')

        if not re.fullmatch(r'[a-zA-Z기-힣]+', student_name):
            print('오류: 이름에는 한글, 영어만 입력할 수 있습니다.')
            print()

            return

        student_number = valid_input('학번: ', isint=True)

        if not isinstance(student_number, int):
            print('오류: 학생의 학번은 숫자만 입력할 수 있습니다.')
            print()

            return

        scores_input = valid_input('점수 입력(수학,영어,과학,국어 순): ')
        scores = scores_input.split()

        if len(scores) != 4:
            print('오류: 점수 4개를 다 기입하지 않으셨습니다.')
            print()

            return

        try:
            math_score, english_score, science_score, korean_score = map(int, scores)

            if not 0 <= math_score <= 100 and 0 <= english_score <= 100 and 0 <= science_score <= 100 and 0 <= korean_score <= 100:
                print("오류: 점수는 0-100점 사이여야 합니다.")
                print()

                return

            with open('students.csv', 'a', encoding='utf-8', newline='') as students_file:
                students_csv_datas = csv.writer(students_file)

                students_csv_datas.writerow([student_number, student_name, math_score, english_score, science_score,korean_score])

                print('학생을 성공적으로 추가하였습니다.')
                print()


        except Exception as error:
            print(f'오류: 파일을 열거나 저장하는 중 오류 발생: {file_error}')
            print()

        except ValueError as error:
            print(f'오류: 숫자만 입력할 수 있습니다. [{error}]')
            print()

    def remove_student(self):
        student_number = valid_input('학생의 학번을 입력해주세요: ', isint=True)

        if not isinstance(student_number, int):
            print('오류: 학생의 학번에는 숫자만 입력할 수 있습니다.')
            print()

            return

        student_name = valid_input('학생의 이름을 입력해주세요: ')

        if not re.fullmatch(r'[a-zA-Z기-힣]+', student_name):
            print('오류: 학생의 이름에는 영문, 한글만 입력할 수 있습니다.')
            print()

            return

        try:
            pandas_csv = pd.read_csv('students.csv', encoding='utf-8', header=0)


            student_found = pandas_csv[(pandas_csv['student_id'] == student_number) & (pandas_csv['student_name'] == student_name)]

            if not student_found.empty:
                pandas_csv = pandas_csv[(pandas_csv['student_id'] != student_number) | (pandas_csv['student_name'] != student_name)]
                pandas_csv.to_csv('students.csv', index=False)

                print(f'[{student_number}] - [{student_name}] 학생을 삭제하였습니다.')
                print()

            else:
                print(f'[{student_number}] - [{student_name}]의 학생은 존재하지 않습니다.')
                print()

        except FileNotFoundError:
            print('오류: 학생 데이터 파일이 존재하지 않습니다.')
            print()

class students_grade_manager():
    def students_avg(self):
        sum_subject = add()

def main_menu():
    student_info = student_infomations()

    while True:
        print("1. 학생 추가")
        print("2. 학생 삭제")
        print("3. 학생 목록")
        print("4. 학생 정보")
        print("5. 학생 평균")
        print("6. 학생 등급")
        print("7. 전체 학생 평균")
        print("8. 프로그램 종료")
        print()

        user_choice = valid_input('입력(1-8): ', ['1', '2', '3', '4', '5', '6', '7', '8'], isint=True)

        if user_choice == 1:
            student_info.add_student()
        elif user_choice == 2:
            student_info.remove_student()
        #elif user_choice == 3:

        #elif user_choice == 4:

        #elif user_choice == 5:

        #elif user_choice == 6:

        #elif user_choice == 7:

        elif user_choice == 8:
            print('[ 프로그램을 종료합니다. ]')
            exit()

        else:
            print('오류: 1-8의 숫자를 제외한 다른 것은 입력할 수 없습니다.')
            print()

if __name__ == "__main__":
    main_menu()
