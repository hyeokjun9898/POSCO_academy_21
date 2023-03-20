#!/usr/bin/env python
# coding: utf-8

# In[26]:


import sys

# 메뉴 출력
def menu():
    print("%8s" % ('Student') ,'\tName','\t     Midterm','  Final',' Average','Grade')
    print('--------------------------------------------------------------')

# 평균 학점 출력
def upgrade_avg_grade(stu_dict,nums):    
    stu_dict[nums][3] = (stu_dict[nums][1] + stu_dict[nums][2]) / 2
    if stu_dict[nums][3] >= 90: 
        stu_dict[nums][4] = 'A'     
    elif stu_dict[nums][3] >=80:
        stu_dict[nums][4]='B'
    elif stu_dict[nums][3] >=70:
        stu_dict[nums][4]='C'
    elif stu_dict[nums][3] >=60:
        stu_dict[nums][4]='D'
    else:
        stu_dict[nums][4]='F'
    return stu_dict

def show_function(stu_dict):
    menu()
    for key,value in stu_dict.items():
        print(key ,*value,sep='\t')
        
def search_function():
    nums = input("Student ID: ")
    if nums in stu_dict.keys():
        menu()
        print(nums, *stu_dict[nums])
    else:
        print('NO SUCH PERSON.')
        
def changescore():
    nums = input("Student ID: ")
    #학번이 있다면
    if nums in stu_dict.keys():
        # mid,final값받기
        mf = input("mid/final? ")
        
        # mid
        if mf == "mid":
            score = int(input("Input new score: "))
            menu()
            print(nums, *stu_dict[nums])
            print('Score changed.')
            #mid값, 총점, 학점 수정하기
            stu_dict[nums][1] = score
            upgrade_avg_grade(stu_dict,nums)
            
            #출력하기
            print(nums, *stu_dict[nums])
            
        # final
        elif mf == "final":
            score = int(input("Input new score: "))
            menu()
            print(nums, *stu_dict[nums])
            print('Score changed.')
            #final값, 총점, 학점 수정하기
            stu_dict[nums][2] = score
            upgrade_avg_grade(stu_dict,nums)
            
            #출력하기
            print(nums, *stu_dict[nums])
            
        # mid,final이 아닐 경우 실행
        else:
            pass
    
    #학번이 없으면
    else:
        print('NO SUCH PERSON.')

def add():
    nums = input("Student ID: ")
    
    #학번이 없으면 추가
    if nums not in stu_dict.keys():
        name = input("Name: ")
        mid = int(input("Midterm Score: "))
        final = int(input("Final Score: "))
        temp = 0
        stu_dict[nums] = [name,mid,final,temp,temp]
        upgrade_avg_grade(stu_dict,nums)
        print('Student added.')
    
    #학번이 있으면 에러 메시지
    else:
        print('ALREADY EXISTS.')

def searchgrade():
    # 학생 있는지 없는지 확인
    stu_in = False
    grade = input("Grade to search: ")
    
    # A,B,C,D,F값인지 확인
    if grade == "A" or grade == "B" or grade == "C" or grade == "D" or grade == "F":
        #학점에 있는지 확인
        for key,value in stu_dict.items():
            if grade in value:
                stu_in = True
        
        if stu_in:
            menu()
            for key,value in stu_dict.items():
                if grade in value:
                    print(key ,*value) 
                
        #아무도 없을때
        else:
            print('NO RESULTS')
    
    # A,B,C,D,F가 아님
    else:
        pass

def remove():
    #목록이 있을경우
    if len(stu_dict) >0:
        
        nums = input("Student ID: ")
    
        #학번이 있다면 삭제
        if nums in stu_dict.keys():
            del stu_dict[nums]
            print("Student removed.")

        #학번이 없다면
        else:
            print('NO SUCH PERSON.')
    
    #목록이 없을경우
    else:
        print("List is empty.")
    
    
def quit_function():
    save = input("Save data?[yes/no]")
    
    #yes일 경우 저장
    if save =="yes":
        filename = input("File name: ")
        fw = open(filename,'w')
        
        #내용작성
        for key,value in stu_dict.items():
            fw.write(key)
            for i in value:
                data = f'\t{i}'
                fw.write(data)
            fw.write('\n')
            
        fw.close()
    #no와 그 외일 경우
    else:
        pass
    

# 파일명 받기, 없으면 studens.txt
if len(sys.argv) != 2:
    filename = 'students.txt'
    fr = open(filename,'r')
# 파일명이 있을경우
else:
    fr = open(sys.argv[1],'r')

stu={}

# 목록 정리하기
for i in fr:
    line = i.rstrip()
    line = line.split('\t')
    
    # 중간, 기말고사 int로 바꿔주기
    line[2:] = map(int,line[2:])
    
    # 총점 구하고 값넣기
    line4 = (line[2]+line[3])/2
    line.append(line4)
    
    
    # 총점대로 Grade 넣기
    if line4 >= 90:
        grade = 'A'
    elif line4 >=80:
        grade='B'
    elif line4 >=70:
        grade='C'
    elif line4 >=60:
        grade='D'
    else:
        grade='F'
    line.append(grade)
    
    #전부 저장
    stu[line[0]]=line[1:]
    
    #딕셔너리 총점대로 정렬
    stu_dict = dict(sorted(stu.items(),key=lambda x:x[1][3],reverse=True))

while True:
    command = input("# ")
    if command == "show":
        show_function(stu_dict)
    elif command == "search":
        search_function()
    elif command == "changescore":
        changescore()
    elif command == "add":
        add()
    elif command == "searchgrade":
        searchgrade()
    elif command == "remove":
        remove()
    elif command == "quit":
        quit_function()
        break
    else:
        print("wrong input!")


# In[ ]:




