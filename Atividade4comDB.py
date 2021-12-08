import tkinter
import mysql.connector
import math
from tkinter import END

class appimc_tk(tkinter.Tk):
 def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

 def initialize(self):
     self.grid()

     # Variáveis Texto
     nome = tkinter.Label(self, text="Nome Completo: ", font=("Times 12"),anchor="w")
     nome.grid(column=0, row=0, sticky='W')

     endereco = tkinter.Label(self, text="Endereco: ", font=("Times 12"),anchor="w")
     endereco.grid(column=0, row=1, sticky='W')

     peso=tkinter.Label(self,text="Peso (em Kg): ", font=("Times 12"),anchor="w")
     peso.grid(column=0, row=2, sticky='W')

     altura = tkinter.Label(self, text="Altura (em metros): ", font=("Times 12"),anchor="w")
     altura.grid(column=0, row=3, sticky='W')

    ##

      # Entradas
     self.nm = tkinter.StringVar()
     nome = tkinter.Entry(self, textvariable=self.nm)
     nome.grid(column=1 , columnspan=3, row=0, sticky='W')

     self.end = tkinter.StringVar()
     endereco = tkinter.Entry(self, textvariable=self.end)
     endereco.grid(column=1, row=1, sticky='W')

     self.kg = tkinter.DoubleVar()
     quilos = tkinter.Entry(self, textvariable=self.kg)
     quilos.grid(column=1, row=2, sticky='W')

     self.mt = tkinter.DoubleVar()
     metros = tkinter.Entry(self, textvariable=self.mt)
     metros.grid(column=1, row=3, sticky='W')

      # botões
     botao1 = tkinter.Button (self, text="Calcular",command=self.botaocalc)
     botao1.grid(column=1,row=5,sticky='W')

     self.botao2 = tkinter.Button(self, text="Reiniciar", command=self.clear_text)
     self.botao2.grid(column=1, row=5)

     botao3 = tkinter.Button(self, text=" Sair ", command=self.quit,height= 1,width= 6)
     botao3.grid(column=2,row=5 )

     botaoSalvar = tkinter.Button(self, text=" Salvar ",command=self.botaoSalvar,height= 1,width= 6)
     botaoSalvar.grid(column=2, row=6)


     self.rimc = tkinter.StringVar()
     resultado = tkinter.Entry(self, textvariable=self.rimc)
     resultado.grid(column=1, row=6, sticky='W')
     textoresultado = tkinter.Label(self, textvariable=self,text="Resultado:")
     textoresultado.grid(column=0, row=6, sticky='EW')

     self.geometry('500x300')
     self.grid_columnconfigure(1, weight=10)
     self.resizable(True, True)

 def botaocalc(self):
     p = self.kg.get()
     a = self.mt.get()
     e=a*a
     mpg =math.ceil(p/e)
     return self.rimc.set(mpg)


 def botaoSalvar(self):
     cnx = mysql.connector.connect(user='root', password='mysql',
                                   host='127.0.0.1',
                                   database='mysql')
     cursor = cnx.cursor()
     self.imc = float(self.rimc.get())

     cursor.execute('CREATE TABLE IF NOT EXISTS tabela_imc (nome VARCHAR(100), imc float)')

     sql = "INSERT INTO tabela_imc (nome, imc ) VALUES (%s,%s)"
     cursor.execute(sql,(str(self.nm.get()),self.imc ) )
     cursor.close()
     cnx.commit()
     cnx.close()


 def clear_text(self):
     self.rimc.set('')
     self.nm.set('')
     self.end.set('')
     self.kg.set('')
     self.mt.set('')

if __name__ == "__main__":
     app = appimc_tk(None)
     app.title('Calculo do IMC - índice de'
               ' massa corporal')

app.mainloop()
