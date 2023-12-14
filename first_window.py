import sqlite3
import sys

import second_window

from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget

from form_competitions import Ui_Form


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyForm(QWidget, Ui_Form):
    def __init__(self):
        """
        Конструктор класса - инициализация всех свойств класса
        """
        # наследование свойств родителей - классов QMainWindow и Ui_MainWindow
        super().__init__()
        # вызов метода загрузки интерфейса из класса Ui_MainWindow - все наши компоненты из дизайнера
        self.setupUi(self)
        # ввод классовых переменных, которые доступны из любого метода класса
        # дата соревнований
        self.date_comp = None
        # место соревнований
        self.address = None
        # название соревнований
        self.comp_name = None

        # всплывающие окна обработчика действий и текст сообщения о системных ошибках
        self.msgBox = QMessageBox()
        self.mess = 'Error!'

        # вызов обработчика событий - в нем храним связи сигналы - слоты
        self._connectAction()

        # подключение к БД
        self.db_connection()
        # инициализация результата запроса к БД
        self.res = None

    def _connectAction(self):
        # блок реакций на события
        # вызов функции обработчика нажатия кнопки формы 1
        self.pushButton_3.clicked.connect(self.ok)

    def err(self):
        # всплывающее окно-сообщение об ошибке
        self.msgBox.setIcon(QMessageBox.Warning)
        self.msgBox.setWindowTitle("Ошибка!")
        self.msgBox.setText(f'{self.mess}')
        self.msgBox.exec()

    def message(self):
        # всплывающее окно - информация для пользователя
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setWindowTitle("Ввод данных")
        self.msgBox.setText(f'{self.mess}')
        self.msgBox.exec()

    def ok(self):
        # обработчик нажатия кнопки в форме 1

        # ввод даты соревнований
        self.date_comp = self.calendarWidget_2.selectedDate().toPyDate()
        # ввод места проведения соревнований
        self.address = self.lineEdit_6.text()
        # ввод названия соревнований
        self.comp_name = self.lineEdit.text()
        # проверка на введение данных в строковых полях
        try:
            if not self.address:
                self.mess = 'Не введено место проведения соревнования!'
                raise ValueError(self.mess)
            elif not self.comp_name:
                self.mess = 'Не введено название соревнования!'
                raise ValueError(self.mess)
            else:
                self.mess = 'Предупреждение: если вы ранее не выбрали дату, запишется текущая дата!'
                self.message()
                # проверка - введено ли соревнование ранее
                self.res = self.cur.execute(
                    """SELECT ID_comp FROM Comp_date WHERE date_comp = ? and address = ? and comp_name = ?""",
                    (self.date_comp, self.address, self.comp_name)).fetchone()
                if not self.res:
                    # внесение соревнования в БД по дате, месту и названию
                    self.con.execute(
                        """INSERT INTO Comp_date(date_comp, address, comp_name) VALUES (?, ?, ?)""",
                        (self.date_comp, self.address, self.comp_name))
                    # обновление БД для получения ID внесенного соревнования
                    self.con.commit()
                    self.mess = 'Дата и место проведения соревнований успешно внесены в базу данных!'
                    self.message()
                    # перезапрос ID соревнования для передачи во второе окно формы
                    self.res = self.cur.execute(
                        """SELECT ID_comp FROM Comp_date WHERE date_comp = ? and address = ? and comp_name = ?""",
                        (self.date_comp, self.address, self.comp_name)).fetchone()
                    print(self.res)
                else:
                    self.mess = 'Cоревнование есть в базе данных. Вносите личные данные!'
                    self.message()
                # инициализация второго окна формы
                self.wind_2 = second_window.MyWidget(self.res[0])
                # закрытие первого окна формы
                self.hide()
                # открытие второго окна формы
                self.wind_2.show()
        except ValueError:
            self.err()

    def db_connection(self):
        # соединение с БД
        self.con = sqlite3.connect('dist\\db\\new_db.db')
        self.cur = self.con.cursor()


def main():
    # скрипт для запуска
    app = QApplication(sys.argv)
    ex = MyForm()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
