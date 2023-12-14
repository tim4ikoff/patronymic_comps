import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog

from form_registration import Ui_MainWindow


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self, id_comp, parent=None):
        """
        Конструктор класса - инициализация всех свойств класса
        """
        # прием данных - ID соревнования
        self.id_comp = id_comp
        # наследование свойств родителей - классов QMainWindow и Ui_MainWindow
        super().__init__()
        # вызов метода загрузки интерфейса из класса Ui_MainWindow - все наши компоненты из дизайнера
        self.setupUi(self)

        # имя участника
        self.name = None
        # отчество участника
        self.dad_name = None
        # фамилия участника
        self.fam = None
        # пол участника
        self.gend = None
        # дата рождения участника
        self.birthday = None
        # вес участника
        self.pweight = None
        # пояс участника
        self.ku = None
        # тип соревнований - инд или командный
        self.type_comp = None
        # соревновательная категория
        self.cat_comp = None
        # результат участника - место, которое он занял
        self.result = None

        # всплывающие окна
        self.msgBox = QMessageBox()
        self.msgBoxOK1 = QMessageBox()
        self.msgBoxOK2 = QMessageBox()
        self.mess = 'Error!'

        # диалоговое окно с возможностью ввода информации пользователем
        self.msgDialog = QInputDialog()

        # вызов обработчика событий - в нем храним связи сигналы - слоты
        self._connectAction()

        # подключение к БД
        self.db_connection()
        # инициализация результата запроса к БД
        self.res = None
        self.res1 = None
        self.ress = None
        self.ud = None

        # сбор списка имен участников из БД
        self.names = [x[0] for x in self.cur.execute("""SELECT DISTINCT name 
                                          FROM TraineeMembers ORDER BY name""").fetchall()]
        self.comboBox_5.addItems(['Новое имя'] + sorted(self.names))
        # сбор списка отчеств участников из БД
        self.dads = [x[0] for x in self.cur.execute("""SELECT DISTINCT dad_name 
                                        FROM TraineeMembers ORDER BY dad_name""").fetchall()]
        self.comboBox_6.addItems(['Новое отчество'] + sorted(self.dads))
        # сбор списка фамилий участников из БД
        self.fams = [x[0] for x in self.cur.execute("""SELECT DISTINCT fam
                                         FROM TraineeMembers ORDER BY fam""").fetchall()]
        self.comboBox_7.addItems(['Новая фамилия'] + sorted(self.fams))
        # ku - пояс - в готовом списке от 1 до 9
        self.cat_ku = [str(x) for x in range(1, 10)]
        self.comboBox.addItems(self.cat_ku)
        # вес участника - ввод в строку
        self.lineEdit_4.setText(None)
        # пол участника - в готовом списке
        self.gender = ['male - мужской', 'female - женский']
        self.comboBox_2.addItems(self.gender)
        # тип соревнования - в готовом списке
        self.form_comp = ['solo - индивидуальное', 'team - командное']
        self.comboBox_3.addItems(self.form_comp)
        # категория выступления - в готовом списке
        self.cat = ['sanbon', 'ippon', 'kata']
        self.comboBox_4.addItems(self.cat)
        # результат конкретного участника - место в протоколе - ввод в строку
        self.lineEdit_5.setText(None)

    def _connectAction(self):
        # блок обработчиков событий - нажатий кнопок, выборов из выпадающих списков

        # вызов функции обработчика нажатия кнопки Ввести данные формы 2
        self.pushButton.clicked.connect(self.ok1)
        # вызов функции обработчика нажатия кнопки Подтвердить данные формы 2
        self.pushButton_2.clicked.connect(self.ok2)
        # вызов обработчика выбора имени из выпадающего списка
        self.comboBox_5.activated.connect(self.input_name)
        # вызов обработчика выбора отчества из выпадающего списка
        self.comboBox_6.activated.connect(self.input_dad_name)
        # вызов обработчика выбора фамилии из выпадающего списка
        self.comboBox_7.activated.connect(self.input_fam)

    def message(self):
        # всплывающее окно - информация для пользователя
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setWindowTitle("Ввод данных")
        self.msgBox.setText(f'{self.mess}')
        self.msgBox.exec()

    def dialog(self, arg):
        # диалоговое окно с возможностью пользовательского ввода
        self.msgDialog.setWindowTitle('Ввод данных')
        self.msgDialog.setLabelText(self.mess)
        self.msgDialog.setTextValue('')
        self.msgDialog.setInputMode(0)
        result = self.msgDialog.exec()
        self.data = self.msgDialog.textValue()
        # нажата кнопка OK
        if result == self.msgDialog.Accepted:
            # проверка корректности ввода имени, отчества, фамилии и корректировка неполных данных
            if not self.data:
                self.mess = 'Данные не введены! Исправьте!'
                self.err()
                self.data = arg
            elif not self.data.isalpha():
                self.mess = 'Данные содержат недопустимые символы! Исправьте!'
                self.err()
                self.data = arg
            return self.data
        else:
            self.mess = 'Возврат в форму без изменений!'
            self.message()
            self.msgBox.close()

    def input_name(self):
        # ввод имени участника
        self.name = self.comboBox_5.currentText()
        if self.name == 'Новое имя':
            self.mess = 'Введите имя участника:'
            self.name = str(self.dialog(self.name))
        self.comboBox_5.clear()
        self.comboBox_5.addItems([self.name] + sorted(self.names))
        if self.name not in self.names:
            self.names = self.names + [self.name]

    def input_dad_name(self):
        # ввод отчества участника
        self.dad_name = self.comboBox_6.currentText()
        if self.dad_name == 'Новое отчество':
            self.mess = 'Введите отчество участника:'
            self.dad_name = str(self.dialog(self.dad_name))
        self.comboBox_6.clear()
        self.comboBox_6.addItems([self.dad_name] + sorted(self.dads))
        if self.dad_name not in self.dads:
            self.dads = self.dads + [self.dad_name]

    def input_fam(self):
        # ввод фамилии участника
        self.fam = self.comboBox_7.currentText()
        if self.fam == 'Новая фамилия':
            self.mess = 'Введите фамилию участника:'
            self.fam = str(self.dialog(self.fam))
        self.comboBox_7.clear()
        self.comboBox_7.addItems([self.fam] + sorted(self.fams))
        if self.fam not in self.fams:
            self.fams = self.fams + [self.fam]

    def err(self):
        # окно сообщений об ошибках
        self.msgBox.setIcon(QMessageBox.Warning)
        self.msgBox.setWindowTitle("Ошибка!")
        self.msgBox.setText(f'{self.mess}')
        self.msgBox.exec()

    def new_record(self, name=None, dad_name=None, fam=None, gend=None, birthday=None,
                   ku=None, pweight=None, type_comp=None, cat_comp=None, result=None, n_table=1, id_comp=None, id=None):
        # метод ввода данных в БД
        # print(name, dad_name, fam, gend, birthday, ku, pweight, type_comp, cat_comp, result, n_table, id_comp, id)
        if all([name, dad_name, fam, gend, birthday]) and n_table == 1:
            self.con.execute("""INSERT INTO TraineeMembers(name, dad_name, fam, gend, birthday) 
                                VALUES (?, ?, ?, ?, ?)""",
                             (name, dad_name, fam, gend, birthday))
            self.con.commit()
            res = self.check_record(name=name, dad_name=dad_name, fam=fam, n_table=1)
        elif all([ku, pweight, type_comp, cat_comp, result]) and n_table == 2:
            self.con.execute("""INSERT INTO Competitions(ID_comp, ID_participant, ku, pweight, type_comp, cat_comp, result) 
                                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                             (id_comp, id, ku, pweight, type_comp, cat_comp, result))
            self.con.commit()
            res = self.check_record(id_comp=id_comp, id=id, type_comp=type_comp, cat_comp=cat_comp, n_table=2)
        else:
            res = None
            self.mess = 'Упс... Что-то пошло не так...'
            self.message()
            self.msgBox.close()
        return res

    def update_record(self, gend=None, birthday=None, pweight=None, ku=None, type_comp=None,
                      cat_comp=None, result=None, id_comp=None, id=None, id_record=None, n_table=1):
        # метод обновления уже имеющихся в БД данных
        # print('-up-', gend, birthday, ku, pweight, type_comp, cat_comp, result, id_comp, id, id_record, n_table)
        if n_table == 1 and all([gend, birthday, id]):
            # обновление частичных данных полной записью
            self.con.execute(
                """UPDATE TraineeMembers 
                SET gend = ?, birthday = ?
                WHERE ID_participant = ?""",
                (gend, birthday, id))
            # обновление базы данных
            self.con.commit()
            res = id
        elif n_table == 2 and all([ku, pweight, type_comp, cat_comp, result, id_comp, id, id_record]):
            # запись в базу измененных данных по ID ребенка
            self.con.execute(
                """UPDATE Competitions
                SET ku = ?, pweight = ?, type_comp = ?, cat_comp = ?, result = ? 
                WHERE ID_comp = ? AND ID_participant = ? AND ID_record = ?""",
                (ku, pweight, type_comp, cat_comp, result, id_comp, id, id_record))
            self.con.commit()
            res = id_record
        return res

    def check_record(self, name=None, dad_name=None, fam=None, gend=None, birthday=None, pweight=None, ku=None,
                     type_comp=None, cat_comp=None, result=None, n_table=1, id=None, id_comp=None):
        # метод проверки наличия данных в БД
        # print(name, dad_name, fam, gend, birthday, pweight, ku, type_comp, cat_comp, result, n_table, id, id_comp)
        # поиск участника по базе - если есть, то фиксируем ID, если нет, то добавляем в базу новый ID и данные
        if all([name, dad_name, fam]) and n_table == 1:
            res = self.cur.execute("""SELECT ID_participant 
                                      FROM TraineeMembers 
                                      WHERE fam = ? and name = ? and dad_name = ?""",
                                   (fam, name, dad_name)).fetchone()
        elif all([type_comp, cat_comp, id, id_comp]) and n_table == 2:
            res = self.cur.execute("""SELECT ID_record 
                                      FROM Competitions 
                                      WHERE ID_comp = ? and ID_participant = ? and type_comp = ? and cat_comp = ?""",
                                   (id_comp, id, type_comp, cat_comp)).fetchone()
        else:
            self.mess = 'Упс... Что-то пошло не так...'
            self.message()
            self.msgBox.close()
            res = None
        return res

    def renew(self):
        # обновление окна формы 2 для ввода нового участника
        self.comboBox_5.clear()
        self.comboBox_5.addItems(['Новое имя'] + sorted(self.names))
        self.comboBox_6.clear()
        self.comboBox_6.addItems(['Новое отчество'] + sorted(self.dads))
        self.comboBox_7.clear()
        self.comboBox_7.addItems(['Новая фамилия'] + sorted(self.fams))
        # ku - пояс
        self.comboBox.clear()
        self.comboBox.addItems(self.cat_ku)
        self.ku = None
        # пол участника
        self.comboBox_2.clear()
        self.comboBox_2.addItems(self.gender)
        # дата рождения участника
        self.calendarWidget.showToday()
        # тип соревнования
        self.comboBox_3.clear()
        self.comboBox_3.addItems(self.form_comp)
        # категория выступления
        self.comboBox_4.clear()
        self.comboBox_4.addItems(self.cat)
        # вес участника
        self.lineEdit_4.clear()
        self.pweight = None
        # результат конкретного участника - место в протоколе
        self.lineEdit_5.setText(None)
        self.result = None

    def ok1(self):
        # обработчик нажатия кнопки Ввести данные в форме 2
        # ввод пола участника
        self.gend = self.comboBox_2.currentText()
        # ввод даты рождения участника
        self.birthday = self.calendarWidget.selectedDate().toPyDate()
        self.id = self.check_record(name=self.name, dad_name=self.dad_name, fam=self.fam)
        if not self.id:
            # проверка показала отсутствие участника в БД, будет произведена запись его в БД
            self.id = self.new_record(name=self.name, dad_name=self.dad_name, fam=self.fam, gend=self.gend,
                                      birthday=self.birthday)
            # после записи в self.id вернется номер этого участика в БД
            if self.id:
                self.id = self.id[0]
                self.mess = 'Данные участника успешно внесены в базу данных!\nМожно продолжить ввод данных!'
            else:
                # невозможная ситуация, но если... self.id = None
                self.mess = 'Упс... Что-то пошло не так...'
            self.message()
            self.msgBox.close()
        else:
            # участник есть в БД, корректируем его self.id
            self.id = self.id[0]
            # обновляем его данные
            num = self.update_record(gend=self.gend, birthday=self.birthday, id=self.id)
            # для контроля возвращаем его self.id из БД
            if num:
                self.mess = 'Данные участника успешно обновлены!\nМожно продолжить ввод данных!'
            else:
                # невозможная ситуация, но если... self.id = None
                self.id = None
                self.mess = 'Упс... Что-то пошло не так...'
            self.message()

    def ok2(self):
        # обработчик нажатия кнопки Подтвердитдь данные в форме 2

        # ввод веса участника
        self.pweight = self.lineEdit_4.text()
        # ввод ку - вид пояса
        self.ku = self.comboBox.currentText()
        # ввод вида соревнований
        self.type_comp = self.comboBox_3.currentText()
        # ввод категории соревнований
        self.cat_comp = self.comboBox_4.currentText()
        # ввод результата участия в соревноании
        self.result = self.lineEdit_5.text()
        # внесение данных в БД
        try:
            # проверка ввода данных в пустые строки
            if not self.pweight and not self.result:
                self.mess = 'Не введены вес и результат участника!'
                raise ValueError(self.mess)
            elif not self.result:
                self.mess = 'Не введен результат участника!'
                raise ValueError(self.mess)
            elif not self.pweight:
                self.mess = 'Не введен вес участника!'
                raise ValueError(self.mess)
            else:
                # проверка данных участника на наличие в БД по номеру участника, номеру соревнования, типу и категории
                self.ress = self.check_record(id_comp=self.id_comp, id=self.id, type_comp=self.type_comp,
                                              cat_comp=self.cat_comp, n_table=2)
                if not self.ress:
                    # внесение ребенка в базу данных
                    self.ress = self.new_record(id_comp=self.id_comp, id=self.id, ku=self.ku, pweight=self.pweight,
                                                type_comp=self.type_comp, cat_comp=self.cat_comp, result=self.result,
                                                n_table=2)
                    if self.ress:
                        # теперь результаты участника уже есть в БД
                        self.mess = 'Данные участника успешно внесены в базу данных!'
                        self.ress = self.ress[0]
                        self.message()
                    else:
                        # невозможная ситуация, но если...
                        self.mess = 'Упс... Что-то пошло не так...'
                else:
                    # приветствие, ребенок уже есть в базе данных
                    self.mess = 'Данные этого участника будут обновлены!\nПроверьте корректность данных!'
                    self.message()
                    self.ud = self.update_record(ku=self.ku, pweight=self.pweight, type_comp=self.type_comp,
                                                 cat_comp=self.cat_comp,
                                                 result=self.result, id_comp=self.id_comp, id=self.id,
                                                 id_record=self.ress[0],
                                                 n_table=2)
                    if not self.ud:
                        # невозможная ситуация, но если...
                        self.mess = 'Упс... Что-то пошло не так...'
                        self.message()
                    else:
                        # проверка на успешность внесения в БД
                        self.mess = 'Результат успешно изменен!'
                        self.message()
                self.work()
        except ValueError:
            # обработка ошибок
            self.err()

    def db_connection(self):
        # соединение с БД
        self.con = sqlite3.connect('dist\\db\\new_db.db')
        self.cur = self.con.cursor()


    def work(self):
        # диалоговое окно ОК/Cansel - продолжение работы или выход
        self.mess = 'Для продолжения работы - ОК, для выхода - Cancel'
        self.msgBoxOK2.setIcon(QMessageBox.Information)
        self.msgBoxOK2.setWindowTitle("Внимание!")
        self.msgBoxOK2.setText(f'{self.mess}')
        self.msgBoxOK2.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msgBoxOK2.buttonClicked.connect(self.worker)
        self.msgBoxOK2.exec()

    def worker(self, i):
        # обработка нажатия кнопок ОК/Cancel
        if i.text() == 'OK':
            # продолжаем работу с базой - чистим поля
            self.renew()
        else:
            self.mess = 'Работа с базой данной успешно завершена!'
            self.message()
            self.msgBox.close()
            sys.exit()
        self.msgBoxOK2.close()

def main(n):
    # скрипт для запуска
    app = QApplication(sys.argv)
    ex = MyWidget(n)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
