from os import system, name
import csv
from pandas import read_csv


class student:
    def __init__(self, filename: str) -> None:
        self.filename = filename

        self.name = input("Öğrencinin ismi:")
        self.no = int(input("Öğrencinin numarası:"))
        self.mid = float(input("Vize notu:"))
        self.final = float(input("Final notu:"))
        self.average = self.calculate_avarage(self.mid, self.final)
        self.letter = self.calculate_letter(self.average)
        self.status = True if self.average >= 50 else False

        self.add_to_csv()

    def calculate_avarage(self, mid: float, final: float) -> float:
        if 0 <= mid <= 100 and 0 <= final <= 100:
            return (mid * 0.4) + (final * 0.6)
        else:
            print("Girilen notlar hatalıdır. Uygulama kapatmak için bir tuşa basın.")
            input("..: ")
            exit(0)

    def calculate_letter(self, avarage: float) -> str:
        if 90 <= avarage:
            return "AA"
        elif 85 <= avarage:
            return "BA"
        elif 80 <= avarage:
            return "BB"
        elif 75 <= avarage:
            return "CB"
        elif 70 <= avarage:
            return "CC"
        elif 60 <= avarage:
            return "DC"
        elif 50 <= avarage:
            return "DD"
        elif 40 <= avarage:
            return "FD"
        elif 0 <= avarage:
            return "FF"

    def add_to_csv(self):
        try:
            # trying to open file in read mode to see if file exists or not
            # if exists it appends net student data
            open(self.filename, "r").close()
            with open(self.filename, "a") as file:
                writer = csv.writer(file)
                writer.writerow(
                    [
                        self.name,
                        self.no,
                        self.mid,
                        self.final,
                        self.average,
                        self.letter,
                        self.status,
                    ]
                )
                file.close()

        except FileNotFoundError:
            # if not exists opens a new file named *filename and writes the csv headers
            with open(self.filename, "w") as file:
                writer = csv.writer(file)
                writer.writerow(
                    [
                        "Name",
                        "Student No",
                        "Midterm Exam",
                        "Final Exam",
                        "Avarage",
                        "Letter",
                        "Status",
                    ]
                )
                file.close()
            # After creating a new file calls it self again to add the student data to the created file (recursive)
            self.add_to_csv()


def show_table(filename: str):
    # Reads csv file from *filename converts it to a Dataframe and prints
    dataframe = read_csv(filename)
    print(dataframe.to_string())


def clear_cmd():
    # name = os.name Checks the operating system name for runing the (clear) command)
    if name == "posix":
        system("clear")
    elif name == "nt":
        system("cls")
    else:
        system("clear")


if __name__ == "__main__":
    filename = "student.csv"

    # Command Line Interface
    while True:
        clear_cmd()
        print("1: Öğrenci ve not ekleme")
        print("2: Öğrenci tablosunu göster")
        print("3: Uygulamadan çık!!")
        choice = int(input("\n Lütfen yapmak istediğini seç:  "))
        if choice == 1:
            student(filename)
        elif choice == 2:
            show_table(filename)
        elif choice == 3:
            exit(1)
        input("Geçmek için (enter) tuşuna basın: ")
