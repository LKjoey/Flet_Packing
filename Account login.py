import flet as ft
#
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet.core.control_event import ControlEvent



def main(page: ft.Page) :

    page.title = "登录界面"
    # 垂直对其方式
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # 主题模式
    page.theme_mode = ft.ThemeMode.LIGHT
    # 无框窗口显示
    # page.window.title_bar_hidden = True
    # 隐藏标题栏
    # page.window.title_bar_hidden = False
    # 居中位置显示
    page.window.center()

    page.window.width = 400             # 窗口宽
    page.window.height = 400            # 窗口高
    page.window_resizable = False

    text_username   = TextField(label="用户名", text_align= ft.TextAlign.LEFT, width=200)
    text_password   = TextField(label="密码", text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_signup = Checkbox(label="我同意此应用的用户条款", value=False)
    button_submit   = ElevatedButton(text="sign up", width=200, disabled=True)

    # 验证
    def validate(e: ControlEvent) :
        # 只有用户名 密码 单选框 才显示登录
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
        # 更新
        page.update()

    def submit(e: ControlEvent) :
        print(f"Username: {text_username.value}")
        print(f"Password: {text_password.value}")
        # 清除画面内容
        page.clean()
        # 重新添加文本内容
        page.add(
            Row(
                controls=[Text(value=f'欢迎登录: {text_username.value}', size=20)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    # 将UI和函数关联
    text_username.on_change = validate
    text_password.on_change = validate
    checkbox_signup.on_change = validate
    button_submit.on_click = submit

    # 渲染登录界面
    page.add(
        # 行
        Row(
            controls=[
                # 列
                Column(controls=
                    [text_username,
                     text_password,
                     checkbox_signup,
                     button_submit]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER   # 行居中对其
        )
    )


if __name__ == '__main__':
    ft.app(target=main)