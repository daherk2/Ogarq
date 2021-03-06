# coding: utf-8
__author__ = 'João Marcos Silva e Araújo'
# Organizador em pastas de acordo com os seus respectivos tipos.
# .jpg, .png, .bmp para a pasta fotos; .flv, .wmv, .mp4 para a pasta vídeos e etc.

from tkinter import messagebox
import shutil, glob, os

class Ogar:

    def __init__(self):
        pass

    """
    A principal tarefa desta função {leituraArq()} é a de criar listas com os nomes dos arquivos da pasta para qual o
    programa foi apontado. Por exemplo, ele gerará a lista self.listFoto com o nome do diretório completo das imagens
    que estão na pasta. Ex: Na pasta "/home/usuario/Downloads", existe um arquivo chamado "foto.jpg", logo, gerará uma
    trupla na lista chamada "/home/usuario/Downloads/foto.jpg". Os parâmetros 'esc' e 'dir' são referentes à outra
    classe, 'esc' referente a ESCOLHA de COPIAR ou MOVER or arquivos; 'dir' referente ao DIRETÓRIO onde estarão os
    arquivos, que será capturado na área de texto da interface TK, presente no arquivo InterfaceOgarq.py.
    Para entender algumas funções, olhe-as lá em baixo antes de ver o código principal.
    """
    def leituraArq(self, esc, dir):

        #Verificação de existência do diretório.
        self.procDir(dir)

        #Verificação de existência de pastas com o mesmo nome, se não, faz a criação das pastas.
        self.criarPastas()

        #Dá permissões de super usuário à pasta diretório.
        os.system("sudo chmod -R 777 "+self.dir)

        #Criação das listas com o nome do diretório completo mais o nome do arquivo. Ex: /home/usr/Downloads/foto.jpg.
        self.listFoto = [glob.glob(self.dir+"*.jpg"), glob.glob(self.dir+"*.png"), glob.glob(self.dir+"*.bmp"),
                         glob.glob(self.dir+"*.jpeg"), glob.glob(self.dir+"*.gif")]

        self.listVid = [glob.glob(self.dir+"*.wmv"), glob.glob(self.dir+"*.mp4"), glob.glob(self.dir+"*.mkv"),
                        glob.glob(self.dir+"*.rmvb"), glob.glob(self.dir+"*.flv"), glob.glob(self.dir+"*.3gp"),
                        glob.glob(self.dir+"*.avi"), glob.glob(self.dir+"*.mov")]

        self.listMus = [glob.glob(self.dir+"*.mp3"), glob.glob(self.dir+"*.wav"), glob.glob(self.dir+"*.flac"),
                        glob.glob(self.dir+"*.aac")]

        self.listScr = [glob.glob(self.dir+"*.sh"), glob.glob(self.dir+"*.py"), glob.glob(self.dir+"*.java"),
                        glob.glob(self.dir+"*.bat")]

        self.listDoc = [glob.glob(self.dir+"*.doc"), glob.glob(self.dir+"*.docx"), glob.glob(self.dir+"*.txt"),
                        glob.glob(self.dir+"*.odt")]

        self.listComp = [glob.glob(self.dir+"*.rar"), glob.glob(self.dir+"*.zip"), glob.glob(self.dir+"*.7zip"),
                         glob.glob(self.dir+"*.tar.gz"), glob.glob(self.dir+"*.tar.xz")]

        self.listExe = [glob.glob(self.dir+"*.exe"), glob.glob(self.dir+"*.run"), glob.glob(self.dir+"*.msi")]
        #Fim da criação.

        #Alguns testes para debbuger.
        print("após as listas.")
        print(self.listFoto)
        print(esc)
        #Fim testes.

        #Verificação da escolha (COPIAR ou MOVER) e execução da função escolhida pelo usuário.
        try:
            messagebox.showinfo("INFORMAÇÃO","AGUARDE...")
            if esc == "1":
                print("1")
                self.moverArq()
            elif esc == "2":
                print("2")
                self.copiarArq()

            ##Dá permissões de super usuário à pasta diretório, para retirar a proteção de arquivos.
            os.system("sudo chmod -R 777 "+self.dir)

            #Uma pequena janela com informações.
            messagebox.showinfo("INFORMAÇÃO","TUDO PRONTO E ORGANIZADO!")
        except:
            #Uma pequena janela com informações.
            messagebox.showinfo("INFORMAÇÃO","OPSS... ALGO DEU ERRADO.")

    """
    A função {criarPastas()} faz o que o próprio nome diz: Ceia as pastas necessárias para a execução das outras
    funções, são elas COPIAR ou MOVER. Cria pastas dentro do diretório apontado.
    """
    def criarPastas(self):
        #Se está pasta padrão do programa, posterior com dois undercores, ainda não existir na pasta, quer dizer que
        #é a primeira que o programa é executado alí.
        if ("Scripts__") not in os.listdir("."):
            os.mkdir(self.dir+"Fotos"), os.mkdir(self.dir+"Vídeos"), os.mkdir(self.dir+"Documentos"), \
            os.mkdir(self.dir+"Músicas"), os.mkdir(self.dir+"Compactados"), os.mkdir(self.dir+"Executáveis"), \
            os.mkdir(self.dir+"Scripts__")

        else:
            print("Pastas já existentes.")

    """
    As funções {moverArq()} e {copiarArq()} fazem e tem quase a/o mesma coisa/código. Mudam-se apenas algumas linhas,
    tais elas são nos comandos shutill.move e shutill.copy2, o primeiro para mover, o segundo para copiar.
    Ainda há também uma pequena lógica no código, que serve para separar apenas o nome do arquivo para fazer a sua
    cópia ou para movê-lo. Primeiro separo uma lista que está dentro da "lista pai", a qual é self.listFoto.
    self.listFoto é composto de listas dentro de listas. Logo após, separo os nomes dos arquivos que há em cada lista
    (ainda com o nome do diretório inteiro).
    Em (arq.split("/"))[-1] separo apenas o nome do arquivo. Ex: "/home/usr/Downloads/foto.jpg" -> "foto.jpg".
    Logo após, o programa entra na pasta, verifica se já existe um arquivo com o nome igual. Se não, COPIA ou MOVE
    o arquivo para dentro da basta. Após cada função de COPIAR ou MOVER, o programa sai da pasta, voltando a pasta
    raiz dada ao programa. Ex: "/home/usr/Downloads/Fotos/foto.jpg" -> "/home/usr/Downloads".
    Faz-se isto com todos os arquivos, em todas as pastas.
    """
    def moverArq(self):
        try:
            print(self.listFoto)
            for lista in self.listFoto:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    #Alguns testes para debbuger.
                    print(arq)
                    #Fim testes.
                    os.chdir(self.dir+"Fotos")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.move(arq, self.dir+"Fotos")

            for lista in self.listVid:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Vídeos")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.move(arq, self.dir+"Vídeos")

            for lista in self.listMus:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Músicas")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.move(arq, self.dir+"Músicas")

            for lista in self.listDoc:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Documentos")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.move(arq, self.dir+"Documentos")

            for lista in self.listComp:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Compactados")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.move(arq, self.dir+"Compactados")

            for lista in self.listExe:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Executáveis")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.move(arq, self.dir+"Executáveis")

            for lista in self.listScr:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Scripts__")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.move(arq, self.dir+"Scripts__")
        except:
            messagebox.showinfo("ERRO","OPS, ALGO DEU ERRADO...")

    def copiarArq(self):
        try:
            for lista in self.listFoto:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Fotos")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.copy2(arq, self.dir+"Fotos")

            for lista in self.listVid:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Vídeos")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.copy2(arq, self.dir+"Vídeos")

            for lista in self.listMus:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Músicas")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.copy2(arq, self.dir+"Músicas")

            for lista in self.listDoc:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Documentos")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.copy2(arq, self.dir+"Documentos")

            for lista in self.listComp:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Compactados")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.copy2(arq, self.dir+"Compactados")

            for lista in self.listExe:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Executáveis")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.move(arq, self.dir+"Executáveis")

            for lista in self.listScr:
                for arq in lista:
                    arq = (arq.split("/"))[-1]
                    os.chdir(self.dir+"Scripts__")
                    if os.path.exists(arq):
                        print("Arquivo já existente.")
                        os.chdir("..")
                    else:
                        os.chdir("..")
                        shutill.copy2(arq, self.dir+"Scripts__")
        except:
            messagebox.showinfo("ERRO","OPS, ALGO DEU ERRADO...")

    """
    Verifica a consistência do diretório dado ao programa. Além de fornecer ou não uma barra {"/"}, caso o usuário não
    forneça, como no primeiro caso.
    """
    def procDir(self, dir):
        if dir[-1] != "/":
            dir = dir+"/"

        if os.path.isdir(dir):
            self.dir = dir
            messagebox.showinfo("INFORMAÇÃO","DIRETÓRIO ENCONTRADO!")
            return True
        else:
            messagebox.showinfo("INFORMAÇÃO","OPSS... DIRETÓRIO NÃO ENCONTRADO!")
            return False


shutill = shutil
message = messagebox
