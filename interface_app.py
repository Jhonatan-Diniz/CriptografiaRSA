from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Button, Label
from rsa import gerando_chaves, criptografar_mensagem, descriptografar_mensagem


class RsaCriptograph(App):
    # input
    def compose(self) -> ComposeResult:
        yield Button("Criptografar", id='cript')
        yield Button("Descriptografas", id='descrip')
        yield Button("Gerar chaves", id='gerar_chaves')
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed):
        if (event.button.id == 'gerar_chaves'):
            chaves = gerando_chaves()
            self.mount(Label(f"{chaves[0]} {chaves[1]}"))

        elif (event.button.id == 'cript'):
            self.text = Input(placeholder='Text', id='text')
            self.keys = Input(placeholder='Keys', id="keys")
            criptografar = Button("Confirm", id='criptografar')
            self.mount(self.text)
            self.mount(self.keys)
            self.mount(criptografar)

        elif (event.button.id == 'descrip'):
            self.d_text = Input(placeholder='Text', id='d_text')
            self.d_keys = Input(placeholder='Keys', id='d_keys')
            descriptografar = Button('Confirm', id="descriptografar")

            self.mount(self.d_text)
            self.mount(self.d_keys)
            self.mount(descriptografar)

        elif (event.button.id == "descriptografar"):
            chave = tuple(str(self.d_keys.value).split())
            self.mount(Label(f"{chave}"))
            msg = descriptografar_mensagem(self.d_text.value, chave)

            self.mount(Label("Texto Descriptografado"))
            self.mount(Label(msg))

        elif (event.button.id == "criptografar"):
            chave = tuple(str(self.keys.value).split())
            msg_cript = criptografar_mensagem(self.text.value, chave)

            self.mount(Label('Texto Criptografado:'))
            self.mount(Label(msg_cript))


app = RsaCriptograph()
app.run()
