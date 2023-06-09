#создай приложение для запоминания информации
from PyQt5.QtWidgets import QButtonGroup, QApplication,QLabel,QPushButton,QRadioButton,QWidget,QBoxLayout,QButtonGroup,QHBoxLayout,QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox
from random import shuffle
from random import randint
memapp=QApplication([])
main_win=QWidget()
main_win.score=0
main_win.total=0
main_win.resize(500,400)
main_win.setWindowTitle('Memory Card')
class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question=question
        self.wrong1=wrong1
        self.right_answer=right_answer
        self.wrong3=wrong3
        self.wrong2=wrong2
que=QLabel('')
ans=QPushButton('Ответить')
ans1=QRadioButton('')
ans2=QRadioButton('')
ans3=QRadioButton('')
ans4=QRadioButton('')

RdioGroup=QButtonGroup()
RdioGroup.addButton(ans1)
RdioGroup.addButton(ans2)
RdioGroup.addButton(ans3)
RdioGroup.addButton(ans4)
#группа вопросов.Создание группы
varianyotvetov=QGroupBox('Варианты ответов')
#создание лэйаутов с вариантами ответов
varline1=QVBoxLayout()
varline2=QVBoxLayout()
varline1.addWidget(ans1,alignment=Qt.AlignVCenter,stretch=5)
varline1.addWidget(ans2,alignment=Qt.AlignVCenter,stretch=5)
varline2.addWidget(ans3,alignment=Qt.AlignVCenter,stretch=5)
varline2.addWidget(ans4,alignment=Qt.AlignVCenter,stretch=5)
hline=QHBoxLayout()
hline.addLayout(varline1)
hline.addLayout(varline2)
hline.setSpacing(50)
hline.addStretch(10)
#сделать мэйн лэйаут содержимым группы varianyotvetov
varianyotvetov.setLayout(hline)






#создание мэйн лэйаута для виджетов
main_layout=QVBoxLayout()
 #mainline-вертикальная 
layout1=QHBoxLayout()     #с тремя горизонталями-виджетами
layout2=QHBoxLayout()
layout3=QHBoxLayout()

#добавление виджетов к горизонт.линиям
layout1.addWidget(que,alignment=Qt.AlignHCenter | Qt.AlignVCenter)
layout2.addWidget(varianyotvetov,alignment=Qt.AlignCenter)
layout3.addWidget(ans,alignment=Qt.AlignCenter,stretch=34)

main_layout.addLayout(layout1,stretch=2)
main_layout.addLayout(layout2,stretch=5)
main_layout.addLayout(layout3,stretch=2)
main_layout.setSpacing(5)
answer=[ans1,ans2,ans3,ans4]
#отображение мэйн-лэйаута на экране
main_win.setLayout(main_layout)




resgroup=QGroupBox('Результат теста')
result=QHBoxLayout()
right_ans=QHBoxLayout()
res_right=QLabel('Правильно\НЕПравильно')

rightans=QLabel('Это форма сыра')
result.addWidget(res_right,alignment=Qt.AlignLeft)
result.setSpacing(1)
right_ans.addWidget(rightans,alignment=Qt.AlignHCenter)
main_ans_line=QVBoxLayout()
main_ans_line.addLayout(result)
main_ans_line.addLayout(right_ans)

resgroup.setLayout(main_ans_line)

layout2.addWidget(resgroup)
resgroup.hide()

def show_result():
    varianyotvetov.hide()
    resgroup.show()
    ans.setText('Следующий вопрос')

def show_que():
    resgroup.hide()
    varianyotvetov.show()
    ans.setText('Ответить')
    RdioGroup.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    RdioGroup.setExclusive(True)
def start_test():
    text_on_button=ans.text()
    if text_on_button=='Ответить':
        show_result()
    elif text_on_button=='Следующий вопрос':
        show_que()
answers=[ans1,ans2,ans3,ans4]
def ask(q: Question):
    shuffle(answers)
    answers[2].setText(q.right_answer)
    answers[0].setText(q.wrong1)
    answers[1].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    que.setText(q.question)
    rightans.setText(q.right_answer)
    show_que()
def show_correct(check):
    res_right.setText(check)
    show_result()
def check_answer():
    if answers[2].isChecked():
        show_correct('Правильно')
        main_win.score+=1
    else:
        if answers[0].isChecked or answers[1].isChecked or answers[3].isChecked:
            show_correct('Неправильно')
    rating()
def click_OK():
    if ans.text()=='Ответить':
        check_answer()
    else:
        next_question()
list_of_questions=[]
list_of_questions.append(Question('Осло-столица...','Норвегии','Швеции','Нидерландов','Швейцарии'))
list_of_questions.append(Question('Где находится Пизанская башня?','В Пизе','В Париже','В Нью-Дели','В Москве'))
list_of_questions.append(Question('Столица Болгарии...','София','Варшава','Минск','Елена'))
list_of_questions.append(Question('Самара это...','Столица мира','Город-Миллионник','Культурная столица','Столица'))
main_win.currentquestion=-1
def next_question():
    currentquestion=randint(0,len(list_of_questions)-1)
    main_win.total+=1
    if currentquestion>=len(list_of_questions):
        currentquestion=0
    q=list_of_questions[currentquestion]
    ask(q)
def rating():
    rate=main_win.score/main_win.total*100
    print('Количество правильных ответов:',main_win.score,'\nКоличество заданных вопросов:',main_win.total,'\nРейтинг:',rate,'%')
ans.clicked.connect(click_OK)
next_question()
ans.setMinimumWidth(150)   
main_win.show()
memapp.exec_()