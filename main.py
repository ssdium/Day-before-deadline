import os
from dialog import Dialog
import pygame


pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
# Цвета
red = (255, 0, 0)
gray = (192, 192, 192)
black = (0, 0, 0)
white = (255, 255, 255)
# Экран
ico = pygame.image.load(("icon.png"))
icon = pygame.transform.scale(ico, (32, 32))
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('День до дедлайна')
# Фоны
menu_png = pygame.image.load(os.path.join("image", "menu.png"))
black_png = pygame.image.load(os.path.join("image", "black.png"))

count_choice = []
# Шрифт
menu_font = pygame.font.Font("font\DejaVuSans.ttf", 30)
# Музыка
pygame.mixer.music.load(os.path.join('audio', 'theme.mp3'))
click = pygame.mixer.Sound(os.path.join('audio','click.wav'))
# Вывод текста справки и помощи
def printText(txtText, Textfont, Textsize , Textx, Texty, Textcolor):
    myfont = pygame.font.SysFont(Textfont, Textsize)
    label = myfont.render(txtText, 0, Textcolor)
    screen.blit(label, (Textx, Texty))


# Вывод спрайтов персонажей
class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(os.path.join("image\persons", filename))
    def pers(self):
        screen.blit(self.bitmap, (self.x, self.y))


class Fon:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(os.path.join("image", "backgrounds", filename))
    def back(self):
        screen.blit(self.bitmap, (self.x, self.y))
# Персонажи
k1 = Sprite(320, 30, "k1.png")
k2 = Sprite(320, 30, "k2.png")
k3 = Sprite(320, 30, "k3.png")
eugene = Sprite(320, 30, "eugene.png")
# Фоны
bg1 = Fon(0, 0, "1.png")
bg2 = Fon(0, 0, "2.png")
bg3 = Fon(0, 0, "3.png")
bg4 = Fon(0, 0, "4.png")
bg5 = Fon(0, 0, "5.png")
bg6 = Fon(0, 0, "6.png")
bg7 = Fon(0, 0, "7.png")
bg8 = Fon(0, 0, "8.png")
bg9 = Fon(0, 0, "9.png")
bg10 = Fon(0, 0, "10.png")
bg11 = Fon(0, 0, "11.png")
bg12 = Fon(0, 0, "12.png")
bg13 = Fon(0, 0, "13.png")
bg14 = Fon(0, 0, "14.png")
bg15 = Fon(0, 0, "15.png")
bg16 = Fon(0, 0, "16.png")
bg17 = Fon(0, 0, "17.png")
bg18 = Fon(0, 0, "18.png")
bg19 = Fon(0, 0, "19.png")
bg20 = Fon(0, 0, "20.png")
bg21 = Fon(0, 0, "21.png")
bg22 = Fon(0, 0, "22.png")
bg23 = Fon(0, 0, "23.png")
bg24 = Fon(0, 0, "24.png")
bg25 = Fon(0, 0, "25.png")
bg26 = Fon(0, 0, "26.png")
bg27 = Fon(0, 0, "27.png")
bg28 = Fon(0, 0, "28.png")
bg29 = Fon(0, 0, "29.png")
bg30 = Fon(0, 0, "30.png")
bg31 = Fon(0, 0, "31.png")
bg32 = Fon(0, 0, "32.png")
bg33 = Fon(0, 0, "33.png")
bg_black = Fon(0, 0, "bg_black.png")


class Menu:
    hovered = False
    dark = False

    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()

    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
    #  рендер
    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())
    #  (Покрытый\ Не покрытый)
    def get_color(self):
        if self.hovered:
            return (red)
        else:
            if self.dark:
                return (gray)
            else:
                return (black)
    #  Рендер углов
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

# Главное Меню
def mmenu():
    menus = [Menu("НОВАЯ ИГРА", (300, 205)),
             Menu("ПОМОЩЬ", (325, 255)),
             Menu("АВТОРЫ", (335, 305)),
             Menu("ВЫХОД", (340, 355))]
    begin = True
    screen.blit(menu_png, (0, 0))

    while begin:
        pygame.event.pump()
        # Проверка пунктов меню
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
                menu.dark = True
            menu.draw()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "НОВАЯ ИГРА":
                        click.play()
                        floor1()
                    elif menu.hovered and menu.text == "ПОМОЩЬ":
                        click.play()
                        helps()
                    elif menu.hovered and menu.text == "АВТОРЫ":
                        click.play()
                        authors()
                    elif menu.hovered and menu.text == "ВЫХОД":
                        begin = False
                        click.play()
    pygame.quit()

def helps():
    screen.blit(black_png, (0, 0))
    hlp = True
    while hlp:
        printText("Управление Игрой", "DejaVuSans.ttf", 35, 280, 10, white)
        printText("Для продвижения вперед, нажмите пробел или клавишу \"Enter\".", "DejaVuSans.ttf", 30, 20, 60, white)
        printText("Для выбора, воспользуйтесь мышью.", "DejaVuSans.ttf", 30, 20, 90, white)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click.play()
                hlp = False
                mmenu()
            elif event.type == pygame.KEYDOWN:
                click.play()
                hlp = False
                mmenu()

def authors():
    screen.blit(black_png, (0, 0))
    aut = True
    while aut:
        printText("Над проектом работали:", "DejaVuSans.ttf", 35, 250, 10, white)

        printText("Авторы сценария:", "DejaVuSans.ttf", 25, 300, 60, white)
        printText("Дарья Рогожина и Мария Степанова", "DejaVuSans.ttf", 30, 210, 90, white)

        printText("Программирование:", "DejaVuSans.ttf", 25, 300, 120, white)
        printText("Дарья Рогожина и Мария Степанова", "DejaVuSans.ttf", 30, 210, 150, white)

        printText("Фоновые Изображения и Персонажи:", "DejaVuSans.ttf", 25, 240, 180, white)
        printText("Мария Степанова", "DejaVuSans.ttf", 30, 320, 210, white)
        printText("Музыка:", "DejaVuSans.ttf", 25, 350, 240, white)
        printText("Atrium Carceri \"End Titles\" ", "DejaVuSans.ttf", 25, 280, 260, white)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                aut = False
                click.play()
                mmenu()
            elif event.type == pygame.KEYDOWN:
                aut = False
                click.play()
                mmenu()


def floor1():
    bg1.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Вы зашли в it-куб. Вы в спешке поднялись по лестнице и направились к гардеробу. ",
                          "Дойдя до него вы остановились. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg2.back()
    unNoDialog.message = ("Хотите сдать верхнюю одежду? ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    menus = [Menu("Да", (235, 255)),
             Menu("Нет", (235, 305))]
    while True:
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Да":
                        count_choice.append(0)
                        click.play()
                        bg3.back()
                        unNoDialog = Dialog(screen)
                        unNoDialog.message = ("Вы сдали верхнюю одежду. ",)
                        unNoDialog.show = True
                        unNoDialog.sndNext()
                        go()
                    elif menu.hovered and menu.text == "Нет":
                        count_choice.append(1)
                        click.play()
                        bg2.back()
                        unNoDialog = Dialog(screen)
                        unNoDialog.message = ("Вы не сдали верхнюю одежду. ",)
                        unNoDialog.show = True
                        unNoDialog.sndNext()
                        go()

def go():
    print(count_choice)
    bg2.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Отойдя от гардероба вы ощущаете прикосновение к плечу ",
                          "и слышите фразу, произнесенную знакомым голосом. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("???: Добрый вечер, что ты здесь делаешь сегодня? ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg4.back()
    k1.pers()
    unNoDialog.message = ("Оборачиваясь на голос, вы видите ассистента айти-куба, ",
                          "It-К-9MXC86Q7+VP или Кэй, как его все называют. ")
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Кэй: Для чего ты пришел сегодня? ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Вы: Привет, Кэй, мне нужно встретиться с Евгением, ",
                          "передать ему флешку с проектом. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Вы немного удивлены его вопросу, ведь обычно Кэй сам ждет ",
                          "инструкции к действиям. Списав это на обновление, ",
                          "вы решаете узнать местоположение учителя. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Вы: Кэй, где сейчас Евгений? ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg4.back()
    k3.pers()
    unNoDialog.message = ("После небольшой паузы, вы получаете ответ. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg4.back()
    k1.pers()
    unNoDialog.message = ("Кэй: Не могу распознать его местоположение. Пойдемте поищем? ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Вы: Ты со мной? Пошли. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg5.back()
    unNoDialog.message = ("Вы направились к лестнице ведущей на верхние этажи. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg6.back()
    unNoDialog.message = ("Вы поднялись на второй этаж. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg7.back()
    unNoDialog.message = ("Наконец поднявшись на третий этаж, первое, что вы видите — окно. ",
                          "Приблизившись к нему, у вас невольно возникает мысль о надобности ",
                          "сегодняшнего визита, учитывая штормовое предупреждение. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Выдохнув, вы поворачиваетесь к ассистенту и задаете вопрос. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg8.back()
    k1.pers()
    unNoDialog.message = ("Вы: Откуда начнем? Где ты последний раз его видел? ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg8.back()
    k2.pers()
    unNoDialog.message = ("Кэй: Мы не пересекались с ним сегодня. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg8.back()
    k1.pers()
    unNoDialog.message = ("Вы поражено смотрите на Кэйа, потому что не ожидали такого ответа. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Вы: Ладно, просто начнем его искать. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg9.back()
    unNoDialog.message = ("Зайдя на третий этаж, вы удивляетесь отсутствию кого-либо за стойкой в холле. ",
                          "Тут никогда не было пусто, но, наверное, стафф ушел на перерыв пить кофе? ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Полностью уверенные в своей догадке, вы успокаиваетесь ",
                          "и продолжаете осматриваться. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Отсутсвие учеников не удивительно для подобной ситуации с погодой на улице. ",
                          "Удивительно, что вы сами пришли. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg10.back()
    unNoDialog.message = ("Погруженный в свои раздумья, вы не замечаете как подходите к служебному ",
                          "помещению. Оно так же совершенно пустое, не смотря на очевидное ",
                          "присутствие людей в нем ранее. Вы видите небольшой беспорядок, ",
                          "который присущ рабочему процессу. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg11.back()
    unNoDialog.message = ("Пройдя далее по коридору третьего этажа, вы наконец-то доходите до ",
                          "“Coffee Point”, как гласит надпись на двери. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("В нем, как и во всех предыдущих помещениях, вы не видите ни единой души. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Вдруг вы слышите голос Кэйа, выводящий вас из раздумий. ",
                          "Вы уже практически забыли, что ассистент шел с вами все это время, ",
                          "он непривычно молчаливый сегодня. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg11.back()
    k3.pers()
    unNoDialog.message = ("Кэй: Будем заходить внутрь? ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg11.back()
    menus = [Menu("Да, давай зайдем", (30, 255)),
             Menu("Не стоит тратить время", (30, 305))]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Да, давай зайдем":
                        click.play()
                        bg12.back()
                        unNoDialog.message = ("... ",)
                        unNoDialog.show = True
                        unNoDialog.sndNext()
                        click.play()
                        coffee()
                    elif menu.hovered and menu.text == "Не стоит тратить время":
                        click.play()
                        go2()

def coffee():
    bg13.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Вы: … ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Вы замираете от неожиданности, не понимая, что произошло. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("«Что это было?» ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg13.back()
    k1.pers()
    unNoDialog.message = ("Вы без слов поворачиваете голову к ассистенту. ",
                          "Кэй стоит, как ни в чем не бывало, смотрит на вас с нейтральной улыбкой. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Возможно сон все таки важен для нормального функционирования организма. ",
                          "Да и с энергетиками пора завязывать. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    go2()

def go2():
    bg14.back()
    k1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Вы: Кэй, пошли, скорее всего Евгений на другом этаже. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Кэй: Маршрут перестроен. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Гением был человек, добавивший в программу Кэйа фразы Яндекс Алисы. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Кэй интересуется вашим самочувствием сегодня. ",
                          "Слово за слово вы разговорились.  ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg15.back()
    unNoDialog.message = ("Вы поднимаетесь по лестнице. ",
                          "На пролете между этажами как всегда стоят различные вещи. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Хотите подойти ближе? ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    menus = [Menu("Подойти ближе", (400, 255)),
             Menu("Не тратить время", (400, 305))]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Подойти ближе":
                        click.play()
                        floor3_5()
                    elif menu.hovered and menu.text == "Не тратить время":
                        click.play()
                        floor4_choice()


def floor3_5():
    bg16.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("... ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg17.back()
    unNoDialog.message = ("Вы отшатнулись назад. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("«Что это??» ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Теперь вы точно будете больше спать. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg17.back()
    k1.pers()
    unNoDialog.message = ("Ассистент молча стоит сзади вас, вы в спешке оборачиваетесь на него. ",
                          "Кэй непонимающе интересуется: ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg17.back()
    k3.pers()
    unNoDialog.message = ("Кэй: Все в порядке? Ты уверен, что хочешь продолжить поиски? ",
                          "Выглядишь уставшим. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    menus = [Menu("Продолжить", (150, 255)),
             Menu("Хочу домой", (150, 305))]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Продолжить":
                        click.play()
                        floor4_choice()
                    elif menu.hovered and menu.text == "Хочу домой":
                        click.play()
                        ending1()

def ending1():
    bg17.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Вы решили уйти домой. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    k1.pers()
    unNoDialog.message = ("Вы: Кэй, я лучше пойду домой, пока. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Кэй: До скорой встречи! ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg_black.back()
    unNoDialog.message = ("Попрощавшись с ассистентом, вы спускаетесь по лестнице и думаете, ",
                          "что написать Евгению по поводу дедлайна. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Вы вышли из здания айти-куба и направились домой. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    screen.fill((0, 0, 0))
    while True:
        printText(".:.Плохая концовка 1.:.", "DejaVuSans.ttf", 40, 250, 200, red)
        printText("Вы ушли домой спать, так и не сдав проект", "DejaVuSans.ttf", 35, 160, 270, red)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click.play()
                mmenu()
            elif event.type == pygame.KEYDOWN:
                click.play()
                mmenu()

def floor4_choice():
    bg18.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Вы поднялись на четвертый этаж. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg19.back()
    unNoDialog.message = ("Хотите подняться на пятый этаж или сначала пойдете на четвертый? ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    menus = [Menu("На пятый", (450, 255)),
             Menu("На четвертый", (450, 305))]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "На пятый":
                        click.play()
                        floor5()
                    elif menu.hovered and menu.text == "На четвертый":
                        click.play()
                        floor4()

def floor5():
    bg20.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Вы решили подняться на пятый этаж. Перед вами обшарпанная дверь. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg21.back()
    unNoDialog.message = ("Вы тянетесь к ручке двери. В тот же момент вы чувствуете как Кэй одергивает вас ",
                          "за локоть. Вы недоуменно смотрите на него. " ,)
    unNoDialog.show = True
    unNoDialog.sndNext()
    k1.pers()
    unNoDialog.message = ("Вы: Что случилось? Я не могу туда войти? ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg21.back()
    k2.pers()
    unNoDialog.message = ("Кэй: … ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Вы: Сколько тут учусь все интересно: что же на пятом этаже? ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Кэй: Вы не можете туда зайти. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Вы сбиты с толку уважительным обращением от ассистента. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    menus = [Menu("Открыть дверь", (150, 255)),
             Menu("Спуститься на четвертый", (150, 305))]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Открыть дверь":
                        click.play()
                        ending2()
                    elif menu.hovered and menu.text == "Спуститься на четвертый":
                        click.play()
                        floor4()

def ending2():
    bg21.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Вы беретесь за ручку и тянете дверь на себя. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg_black.back()
    unNoDialog.message = ("Вы чувствуете сильную боль во всем теле, у вас темнеет в глазах. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    if count_choice[0] == 1:
        bg19.back()
        unNoDialog.message = ("Вы поднимаетесь на ноги. Вам повезло, вы упали на куртку, она смягчила удар об пол. ",)
        unNoDialog.show = True
        unNoDialog.sndNext()
        unNoDialog.message = ("Как странно, ощущение будто вы упали и проехались по ступенькам. ",
                              "Ваше чувство самосохранения подсказывает вам бежать отсюда. ",)
        unNoDialog.show = True
        unNoDialog.sndNext()
        bg_black.back()
        unNoDialog.message = ("Вы быстро спускаетесь на первый этаж, хоть и немного пошатываясь.",
                              "Накидываете на себя куртку и выходите из здания. ",)
        unNoDialog.show = True
        unNoDialog.sndNext()
        unNoDialog.message = ("Кажется у Кэйа сбой в программе, и он может быть опасен. Куда делись все работники? ",
                              "Почему у вас все время было ощущение кого-то еще, кроме вас с Кэйем, в помещениях? ",)
        unNoDialog.show = True
        unNoDialog.sndNext()
        unNoDialog.message = ("Ваша голова начинает болеть сильнее, поэтому вы решаете оставить свои мысли ",
                              "на потом. ",)
        unNoDialog.show = True
        unNoDialog.sndNext()
        screen.fill((0, 0, 0))
        while True:
           printText(".:.Плохая концовка 3.:.", "DejaVuSans.ttf", 40, 250, 200, red)
           printText("Вы чуть не погибли и не смогли ", "DejaVuSans.ttf", 35, 210, 270, red)
           printText("сдать проект до дедлайна :(", "DejaVuSans.ttf", 35, 225, 310, red)
           pygame.display.flip()
           for event in pygame.event.get():
               if event.type == pygame.MOUSEBUTTONDOWN:
                   click.play()
                   mmenu()
               elif event.type == pygame.KEYDOWN:
                   click.play()
                   mmenu()
    else:
        screen.fill((0, 0, 0))
        while True:
            printText(".:.Плохая концовка 2.:.", "DejaVuSans.ttf", 40, 250, 200, red)
            printText("Вы погибли, упав с лестницы", "DejaVuSans.ttf", 35, 230, 270, red)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click.play()
                    mmenu()
                elif event.type == pygame.KEYDOWN:
                    click.play()
                    mmenu()

def floor4():
    bg22.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Зайдя на четвертый этаж, вы осматриваетесь. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    k1.pers()
    unNoDialog.message = ("Отсутствие людей в помещении начинает настораживать. ",
                          "Тем не менее, Кэй выглядит как обычно. Наверное, сегодня занятия отменили? ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg23.back()
    unNoDialog.message = ("Вы одно за другим проходите пустые помещения. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg24.back()
    unNoDialog.message = ("Дойдя до конца коридора, вы видите включенный свет в вашем классе. ",
                          "Странно, может быть кто-то здесь был? ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    k1.pers()
    unNoDialog.message = ("Вы: Кэй, ты не знаешь, кто был в этом классе сегодня? ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg24.back()
    k2.pers()
    unNoDialog.message = ("Кэй: Нет, у меня нет этой информации. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg25.back()
    unNoDialog.message = ("Слева от вас, в зоне отдыха, небольшой беспорядок на столе. ",
                          "Ощущение, будто здесь только что кто-то был! ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    k3.pers()
    unNoDialog.message = ("Вы: Кэй, кто за сегодня приходил сюда? ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg25.back()
    k2.pers()
    unNoDialog.message = ("Кэй: Я не знаю. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg25.back()
    k1.pers()
    unNoDialog.message = ("Вы: Но ведь ты синхронизирован с камерами! Ты знаешь кто здесь был. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg25.back()
    k2.pers()
    unNoDialog.message = ("Кэй: Нет. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg25.back()
    k1.pers()
    unNoDialog.message = ("Почему Кэй вам не говорит? ",
                          "Странно, зачем ему скрывать эту информацию. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg25.back()
    unNoDialog.message = ("Хотите осмотреть зону отдыха? ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    menus = [Menu("Да", (330, 255)),
             Menu("Нет", (330, 305))]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Да":
                        click.play()
                        rest_zone()
                    elif menu.hovered and menu.text == "Нет":
                        click.play()
                        count_choice.append(0)
                        go3()

def rest_zone():
    bg26.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("В зоне отдыха стоит множество книг, вы заинтересованно рассматриваете их названия, ",
                          "пытаясь найти что-то знакомое. Вскоре ваше внимание привлекает одна книга. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg27.back()
    unNoDialog.message = ("Вы берете ее в руки и открываете. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Как оказалось в книге что-то лежало. Вы поднимаете объект и рассматриваете его. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Выглядит как ключ с брелком. Интересно от чего он? ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    menus = [Menu("Забрать ключ", (150, 150)),
             Menu("Положить на место", (150, 200))]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Забрать ключ":
                        click.play()
                        count_choice.append(1)
                        go3()
                    elif menu.hovered and menu.text == "Положить на место":
                        click.play()
                        count_choice.append(0)
                        go3()

def go3():
    bg28.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Вы проходите немного дальше по коридору. ",
                          "Справа от вас служебное помещение, также пустующее. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg29.back()
    unNoDialog.message = ("Слева дверь без указателя. ",
                          "Странно, вы вроде должны помнить что в том кабинете, ведь вы там были. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Это же кабинет Евгения! ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Кабинет закрыт. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    if count_choice[1] == 1:
        menus = [Menu("Использовать ключ", (30, 255)),
                 Menu("Уйти", (30, 305))]
        while True:
            pygame.event.pump()
            for menu in menus:
                if menu.rect.collidepoint(pygame.mouse.get_pos()):
                    menu.hovered = True
                else:
                    menu.hovered = False
                menu.draw()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for menu in menus:
                        if menu.hovered and menu.text == "Использовать ключ":
                            click.play()
                            count_choice.append(1)
                            ending4()
                        elif menu.hovered and menu.text == "Уйти":
                            click.play()
                            count_choice.append(0)
                            ending3()
    else:
        ending3()

def ending3():
    bg29.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Никого не отыскав, вы решаете пойти домой. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    k3.pers()
    unNoDialog.message = ("Вы: Кэй, видимо, никого нет. Я пойду домой, пока. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg29.back()
    k1.pers()
    unNoDialog.message = ("Кэй: До встречи! ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg_black.back()
    unNoDialog.message = ("Вы спустились на первый этаж, неспеша надели верхную одежду ",
                          "и затем вышли из здания. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Надеясь, что Евгений отсрочить дедлайн, вы поплелись в сторону ",
                          "автобусной остановки. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    screen.fill((0, 0, 0))
    while True:
        printText(".:.Плохая концовка4.:.", "DejaVuSans.ttf", 40, 250, 180, red)
        printText("Вы не успели до дедлайна", "DejaVuSans.ttf", 35, 240 , 250, red)
        printText("Не тяните больше до последнего", "DejaVuSans.ttf", 35, 200, 290, red)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mmenu()
            elif event.type == pygame.KEYDOWN:
                mmenu()

def ending4():
    bg30.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Вы открываете кабинет Евгения ключом, который нашли в книге. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg31.back()
    unNoDialog.message = ("Аккуратно заходя в кабинет, вы, в полумраке, ",
                          "подходите к столу и кладете на него флешку. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg32.back()
    unNoDialog.message = ("Оборачиваясь к двери, вы слышите снаружи кабинета неясный ответ Кэйа ",
                          "на чей-то вопрос. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg33.back()
    unNoDialog.message = ("Вы видите силуэт на стене. ",
                          "Кто-то заходит в кабинет. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg31.back()
    eugene.pers()
    unNoDialog.message = ("Это же Евгений! ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Вы: Здравствуйте, Евгений! ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Евгений: Здравствуй. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Вы объясняете ему что вы тут делаете в такую погоду, говорите о флешке и ",
                          "о странном поведении Кэйа. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Куратор слушает вас, кивает, шутит про черезмерную целеустремлённость. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Вы: До свидания! ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Евгений: До свидания. Удачно долететь до дома. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    bg_black.back()
    unNoDialog.message = ("Вы спускаетесь и выходите из здания, включаете музыку в наушниках ",
                          "и идете на остановку. ",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    screen.fill((0, 0, 0))
    while True:
        printText(".:.Хорошая концовка.:.", "DejaVuSans.ttf", 40, 250, 180, red)
        printText("Вы смогли! ", "DejaVuSans.ttf", 35, 320, 250, red)
        printText("Вы успели до дедлайна!", "DejaVuSans.ttf", 35, 250, 290, red)
        printText("Держите конфетку.", "DejaVuSans.ttf", 35, 280, 330, red)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mmenu()
            elif event.type == pygame.KEYDOWN:
                mmenu()


def main():
    pygame.mixer.music.play(-1)
    mmenu()
    begin = True
    while begin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                begin = False
    pygame.quit()


if __name__ == "__main__":
    main()