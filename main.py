import sys
import os
import subprocess
from PyQt6.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt6 import QtWidgets, uic, QtGui
from pymediainfo import MediaInfo
from pypresence import Presence
import time

try:
    RPC = Presence("1074502796029743144")
    RPC.connect()

    RPC.update(
        details='convertendo para .MP4',
        large_image='onion1',
        large_text='Onion Subs',
        small_image='heart',
        start=time.time(),
        buttons=[{"label": "Onion Subs", "url": "https://site.onionsubs.repl.co"}, {"label": "Repo", "url": "https://github.com/Onion-subs/ToMP4"}])
    print('Online')
except Exception as e: 
        print(e)


global ffmpeg

if sys.platform == 'linux':
    ffmpeg = 'ffmpeg'
else:
    ffmpeg = r'"ffmpeg\ffmpeg.exe"'

# ffmpeg -i "ENTRADA" -vf scale="%videoResolution%" -i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k -c:s srt -map v:0 -map a -map 1:0 -ss 00:00:00 -to 00:00:10 "SAIDA"


class AppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('toMP4 - V1.0')
        self.setWindowIcon(QtGui.QIcon('assets/icon.png'))

        self.findVideoDir.clicked.connect(self.pyFindVideoDir)
        self.findSubDir.clicked.connect(self.pyFindSubDir)
        self.findOutputDir.clicked.connect(self.pyFindOutputDir)
        self.execute.clicked.connect(self.pyExecute)

    def pyFindVideoDir(self):
        try:
            fname=QFileDialog.getOpenFileName(self, 'Select video', '' , 'Videos (*.mp4 *.webm *.wmv *.mkv *.gif *.mov *.avi)')
            global videoDir
            global videoName
            videoDir = str(fname[0])
        
            self.videoDir.setText(videoDir)

            clip_info = MediaInfo.parse(videoDir)
            duration_ms = clip_info.tracks[0].other_duration
            self.timeEnd.setText(duration_ms[3])
            self.videoWidth.setText(str(clip_info.tracks[1].width))
            self.videoHeight.setText(str(clip_info.tracks[1].height))

            videoN = videoDir.split('/')
            videoN = videoN[len(videoN) - 1].split('.')
            videoName = videoN[0]
        except:
            print('Sem vídeo selecionado')

    def pyFindSubDir(self):
        try:
            fname=QFileDialog.getOpenFileName(self, 'Select subtitle', '' , 'Subtitles (*.ass *.srt *.vtt)')
            global subDir
            subDir = str(fname[0])
            self.subDir.setText(subDir)
        except:
            print('Sem legenda selecionado')
            

    def pyFindOutputDir(self):
        try:
            fname=QFileDialog.getExistingDirectory(self, 'Select output folder')
            global outputDir
            outputDir = fname
            self.outputDir.setText(outputDir)
            print(outputDir)
        except:
            print('Sem output selecionado')

    def pyExecute(self):
        subDir = str(self.subDir.text())
        # Validações
        print ('entrou')
        if str(self.chooseVideoFormat.currentText()) == 'MP4':
            codec_video = '-c:v libx264'
            print('1')
            

        if self.crfNum.text() is not None or self.crfNum.text() != '':
            crf = '-crf ' + self.crfNum.text()
            print('2')
        else:
            crf = ' '
            print('2')

        preset = '-preset ' + str(self.preset.currentText())
        print('3')

        if str(self.chooseAudioFormat.currentText()) == 'AAC':
            codec_audio = '-c:a aac'
            print('4')

        
        if self.withAudio.isChecked():
            bitrate_audio = '-b:a ' + self.audioQuality.text()
            print('5')
        else:
            bitrate_audio = ' '
            print('5')

        debug = '-ss ' + self.timeStart.text() +  ' -to ' + self.timeEnd.text()
        print('6')

        if self.withSub.isChecked():
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
            subDir = subDir.replace("/" , '//')
            subDir = subDir.replace(":" , "\\\:")
            print(subDir)
            print('7.1')
        else:
            print('7.2')
            subDir = ' '
            map_legenda = ' '

        if self.withAudio.isChecked():
            print('8')
        else:
            codec_audio = ' '
            print('8')

        arquivo_saida = outputDir + '/' + videoName + '.' + str(self.chooseVideoFormat.currentText())
        print('9')

        if self.withSub.isChecked():
            if str(self.chooseSubFormat.currentText()) == 'SRT':
                if self.withAudio.isChecked():
                    '''Execução'''
                    print('10')
                    print(ffmpeg)
                    print(videoDir)
                    print(outputDir)
                    print(subDir)
                    print(codec_video)
                    print(crf)
                    print(preset)
                    print(codec_audio)
                    print(bitrate_audio)
                    print(debug)
                    print(map_legenda)
                    print(arquivo_saida)
                    command = f'{ffmpeg} -i "{videoDir}" -vf "subtitles="{subDir}"" {codec_video} {crf} {preset} {codec_audio} {bitrate_audio} {debug} "{arquivo_saida}"'
                    # command = {ffmpeg} +" -i " + f'"{videoDir}" ' + '-vf ' + '"subtitles=' + f'"{subDir}"" ' + {codec_video} + " " + {crf} + " " + {preset} + " " + {codec_audio} + " " + {bitrate_audio} + " " + {debug} + " " + f'"{arquivo_saida}"'
                    print('11')
                    print("com legenda .srt com audio")
                    print(command)
                    try:
                        subprocess.call(command)
                    except:
                        print('Algo deu errado')
                else:
                    '''Execução'''
                    print('10')
                    print(ffmpeg)
                    print(videoDir)
                    print(outputDir)
                    print(subDir)
                    print(codec_video)
                    print(crf)
                    print(preset)
                    print(debug)
                    print(map_legenda)
                    print(arquivo_saida)
                    command = f'{ffmpeg} -i "{videoDir}" -vf "subtitles="{subDir}"" {codec_video} -an {crf} {preset} {debug} "{arquivo_saida}"'
                    print("com legenda .srt sem audio")
                    print('11')
                    print(command)
                    try:
                        subprocess.call(command)
                    except:
                        print('Algo deu errado')
            else:
                if self.withAudio.isChecked():
                    '''Execução'''
                    print('10')
                    print(ffmpeg)
                    print(videoDir)
                    print(outputDir)
                    print(subDir)
                    print(codec_video)
                    print(crf)
                    print(preset)
                    print(codec_audio)
                    print(bitrate_audio)
                    print(debug)
                    print(map_legenda)
                    print(arquivo_saida)
                    command = f'{ffmpeg} -i "{videoDir}" -vf "ass="{subDir}"" {codec_video} {crf} {preset} {codec_audio} {bitrate_audio} {debug} "{arquivo_saida}"'
                    # command = {ffmpeg} +" -i " + f'"{videoDir}" ' + '-vf ' + '"ass=' + f'"{subDir}"" ' + {codec_video} + " " + {crf} + " " + {preset} + " " + {codec_audio} + " " + {bitrate_audio} + " " + {debug} + " " + f'"{arquivo_saida}"'
                    print('11')
                    print("com legenda .ass com audio")
                    print(command)
                    try:
                        subprocess.call(command)
                    except:
                        print('Algo deu errado')
                else:
                    '''Execução'''
                    print('10')
                    print(ffmpeg)
                    print(videoDir)
                    print(outputDir)
                    print(subDir)
                    print(codec_video)
                    print(crf)
                    print(preset)
                    print(debug)
                    print(map_legenda)
                    print(arquivo_saida)
                    command = f'{ffmpeg} -i "{videoDir}" -vf "ass="{subDir}"" {codec_video} -an {crf} {preset} {debug} "{arquivo_saida}"'
                    print("com legenda .ass sem audio")
                    print('11')
                    try:
                        subprocess.call(command)
                    except:
                        print('Algo deu errado')
        else: 
            if self.withAudio.isChecked():
                '''Execução'''
                print('10')
                print(ffmpeg)
                print(videoDir)
                print(outputDir)
                print(subDir)
                print(codec_video)
                print(crf)
                print(preset)
                print(codec_audio)
                print(bitrate_audio)
                print(debug)
                print(map_legenda)
                print(arquivo_saida)
                command = f'{ffmpeg} -i "{videoDir}" {codec_video} {crf} {preset} {codec_audio} {bitrate_audio} {debug} "{arquivo_saida}"'
                print("sem legenda com audio")
                print('11')
                try:
                    subprocess.call(command)
                except:
                    print('Algo deu errado')
            else:
                '''Execução'''
                print('10')
                print(ffmpeg)
                print(videoDir)
                print(outputDir)
                print(codec_video)
                print(crf)
                print(preset)
                print(debug)
                print(arquivo_saida)
                command = f'{ffmpeg} -i "{videoDir}" {codec_video} -an {crf} {preset} {debug} "{arquivo_saida}"'
                print('11')
                print("sem legenda e sem audio")
                print(command)
                try:
                    subprocess.call(command)
                except Exception as e: 
                    print(str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_window = AppWindow()
    app_window.show()
    sys.exit(app.exec())