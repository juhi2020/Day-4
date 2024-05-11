import customtkinter as ctk
import pyodbc


app = ctk.CTk()
app.geometry("500x500")
app.title("INSERT INTO")


entry_table_name = ctk.CTkEntry(app, placeholder_text="TABLE NAME", width=190)
entry_table_name.place(relx=0.1, rely=0.1)

entry_column1_value = ctk.CTkEntry(app, placeholder_text="COLUMN_1 VALUE", width=190)
entry_column1_value.place(relx=0.1, rely=0.2)

entry_column2_value = ctk.CTkEntry(app, placeholder_text="COLUMN_2 VALUE", width=190)
entry_column2_value.place(relx=0.1, rely=0.3)

entry_column3_value = ctk.CTkEntry(app, placeholder_text="COLUMN_3 VALUE", width=190)
entry_column3_value.place(relx=0.1, rely=0.4)


def insert_data():
    try:

        connection = pyodbc.connect(
            "DRIVER={SQL SERVER};"
            "Server=HP\\SQLEXPRESS;"
            "Database=caldb;"
            "Trusted_Connection=True"
        )

        sql_insert = f"INSERT INTO {entry_table_name.get()} " f"VALUES (?, ?, ?)"

        connection.execute(
            sql_insert,
            (
                entry_column1_value.get(),
                entry_column2_value.get(),
                entry_column3_value.get(),
            ),
        )

        connection.commit()

        info_label.configure(text="Data Inserted")
    except pyodbc.Error as ex:
        print("Error:", ex)
        info_label.configure(text="Error: Data Insertion Failed")


insert_button = ctk.CTkButton(app, text="INSERT", command=insert_data)
insert_button.place(relx=0.1, rely=0.5)


info_label = ctk.CTkLabel(app, text="")
info_label.place(relx=0.1, rely=0.6)

# Start the GUI application
app.mainloop()
