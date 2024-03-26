import os
import pickle

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NoteManager:
    def __init__(self):
        self.notes = []

    def create_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)
        print("Заметка создана.")

    def save_notes(self):
        with open("notes.pkl", "wb") as f:
            pickle.dump(self.notes, f)
        print("Заметки сохранены.")

    def load_notes(self):
        if os.path.exists("notes.pkl"):
            with open("notes.pkl", "rb") as f:
                self.notes = pickle.load(f)
            print("Заметки загружены.")
        else:
            print("Файл с заметками не найден.")

    def list_notes(self):
        if self.notes:
            print("Список заметок:")
            for i, note in enumerate(self.notes):
                print(f"{i + 1}. {note.title}")
        else:
            print("Нет заметок.")

    def edit_note(self, index, title, content):
        if 1 <= index <= len(self.notes):
            self.notes[index - 1].title = title
            self.notes[index - 1].content = content
            print("Заметка отредактирована.")
        else:
            print("Недопустимый индекс заметки.")

    def delete_note(self, index):
        if 1 <= index <= len(self.notes):
            del self.notes[index - 1]
            print("Заметка удалена.")
        else:
            print("Недопустимый индекс заметки.")

def main():
    note_manager = NoteManager()
    note_manager.load_notes()

    while True:
        print("\n1. Создать заметку")
        print("2. Сохранить заметки")
        print("3. Показать список заметок")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержание заметки: ")
            note_manager.create_note(title, content)
        elif choice == "2":
            note_manager.save_notes()
        elif choice == "3":
            note_manager.list_notes()
        elif choice == "4":
            index = int(input("Введите индекс заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            content = input("Введите новое содержание заметки: ")
            note_manager.edit_note(index, title, content)
        elif choice == "5":
            index = int(input("Введите индекс заметки для удаления: "))
            note_manager.delete_note(index)
        elif choice == "6":
            break
        else:
            print("Недопустимый ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()