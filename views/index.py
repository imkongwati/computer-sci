import flet as ft

def IndexView(page:ft.Page, params):
    def CreateAppBar():
        app_bar = ft.AppBar(
            leading=ft.Image("images/csc_logo_100.png"),
            leading_width=40,
            title=ft.Text("Flet Template"),
            #center_title=False,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            actions=[
                ft.IconButton(ft.Icons.RESTART_ALT, on_click=restart_clicked),
                ft.IconButton(ft.Icons.FILTER_3),

            ],
        )
        return app_bar

    def restart_clicked(e):
         dlg = ft.AlertDialog(title=ft.Text("You clicked restart"))
         page.open(dlg)
    def btn_question1_clicked(e):
        page.go("/question/1")

    def btn_question2_clicked(e):
        page.go("/question/2")

    def btn_simple_clicked(e):
        page.go("/simple_view")


    appbar = CreateAppBar()
    question_data={"questions" :" Name 5 largest country",
            "answers" : ["Russia","china","india","USA","canada","brazil"]}
    question_tb= ft.Text(value=question_data["questions"],size=54)
    answers_column=ft.Column()
    i=1
    for answer in question_data["answers"]:
        number=ft.Container(content=ft.Text(value=i,bgcolor=ft.Colors.SECONDARY_CONTAINER,width=18,height=20,
                                            alignment= ft.alignment.center,
                                            border_radius= 16))

        a=ft.Text(value=answer,size=20)
        row=ft.Row(controls=number)
        answers_column.controls.append(row)

        i+=1


    user_answer_tf= ft.TextField(value="type here")
    page.views.append(ft.View(
        "/",
        [appbar,question_tb,answers_column],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

    )
    )
    page.update()
