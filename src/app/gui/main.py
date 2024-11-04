import sys
import gi
from gi.repository import Gtk, Adw
from src.app.dbservice.dbservice import DbService
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, title="My ToDo")

        self.set_default_size(400, 380)
        self._entry_title = self.create_entry_title()
        self.list_box = Gtk.ListBox()

        # Main box
        v_main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=24)
        self.set_child(v_main_box)

        # form box
        form_box = self.create_form_box()
        v_main_box.append(form_box)

        # entry title
        # self.entry_title = self.create_entry_title()

        # list box
        self.list_box.props.show_separators = True
        self.list_box.props.selection_mode = Gtk.SelectionMode.NONE
        self.populate_list_box(self.list_box)
        v_main_box.append(self.list_box)

    @property
    def entry_title(self):
        return self._entry_title

    @entry_title.setter
    def entry_title(self, entry):
        self._entry_title = entry

    # actions
    def on_entry_title_changed(self, entry, button):
        button.set_sensitive(True)

    def on_button_add_clicked(self, button, entry_title):
        title_text = entry_title.get_text()
        task = self.__create_task(title_text)
        self.add_task_to_list_box(task)
        entry_title.set_text('')
        button.set_sensitive(False)

    def on_check_toggled(self, check, task):
        task.completed = check.get_active()
        self.__update_task(task)

    def on_button_delete_clicked(self, button,  task):
        self.__delete_task(task)
        row_box = button.get_parent()
        row = row_box.get_parent()
        self.list_box.remove(row)

    # widgets
    def create_form_box(self):
        form_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=24)
        # button add '+'
        button_add = self.create_button_add_task()
        form_box.append(self.entry_title)
        form_box.append(button_add)
        self.entry_title.connect('changed', self.on_entry_title_changed, button_add)
        return form_box

    def create_entry_title(self):
        entry = Gtk.Entry()
        entry.props.hexpand = True
        entry.props.placeholder_text = "Add a new task"
        return entry

    def create_button_add_task(self):
        button_add = Gtk.Button(label='+')
        button_add.props.hexpand = True
        button_add.props.halign = Gtk.Align.END
        button_add.set_sensitive(False)
        button_add.connect('clicked', self.on_button_add_clicked, self.entry_title)
        return button_add

    def create_button_delete_task(self, task):
        del_button = Gtk.Button(label='Delete')
        del_button.props.hexpand = True
        del_button.props.halign = Gtk.Align.END
        del_button.connect('clicked', self.on_button_delete_clicked, task)
        return del_button

    def populate_list_box(self, list_box):
        tasks = self.__get_tasks_from_db()
        for task in tasks:
            self.add_task_to_list_box(task)

    def add_task_to_list_box(self, task):
        row = Gtk.ListBoxRow()
        row.set_child(self.create_task_row(task))
        self.list_box.append(row)

    def create_task_row(self, task):
        row_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=24)
        check_box = self.create_task_status_checkbox(task)
        row_box.append(check_box)

        task_label = self.create_task_title_label(task)
        row_box.append(task_label)

        delete_button = self.create_button_delete_task(task)
        row_box.append(delete_button)
        return row_box

    def create_task_title_label(self, task):
        label = Gtk.Label(label=task.title)
        label.props.halign = Gtk.Align.START
        return label

    def create_task_status_checkbox(self, task):
        check = Gtk.CheckButton()
        check.set_active(task.completed)
        check.connect('toggled', self.on_check_toggled, task)
        return check

    def __get_tasks_from_db(self):
        with DbService() as db_service:
            db_service = DbService()
            tasks = db_service.get_tasks()
            return tasks

    def __update_task(self, task):
        with DbService() as db_service:
            db_service.update_task(task.id, task.title, task.completed)
            print(f"[Info] Task {task.id} updated.")

    def __delete_task(self, task):
        with DbService() as db_service:
            db_service.delete_task(task.id)
            print(f"[Info] Task {task.id} deleted.")

    def __create_task(self, title):
        with DbService() as db_service:
            task = db_service.create_task(title)
            print(f"[Info] Task {title} created.")
            return task


class MyToDoApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


def main():
    app = MyToDoApp(application_id="com.github.andrelcunha.myToDo_python_GTK4")
    app.run(sys.argv)


if __name__ == "__main__":
    main()
