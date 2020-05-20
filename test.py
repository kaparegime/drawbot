from PIL import Image
import pyautogui

def image_to_text():
    image = Image.open('zebra.jpg')
    print(image.size)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    h = 0
    with open('text.txt', 'w') as f:
        while h != height-1:
            h += 1
            f.write('\n')
            for i in range(width):
                if sum(pix[i, h]) > 300:
                    f.write('1')
                else:
                    f.write('0')

img = Image.open('zebra.jpg')
width = img.size[0]
height = img.size[1]
pix = img.load()
distance = 0
pos = pyautogui.position()
while distance != height:
    distance += 1
    pyautogui.moveTo(pos[0], pos[1]+distance)
    coordinates = []
    with open('text.txt', 'r') as f:
        g = list(f.readlines()[distance])  #Line counter
        if set(g) == {'1', '\n'}:
            continue
        elif '\n' in g:
            g.remove('\n')
            list_of_black = [i for i, val in enumerate(g) if val == '0']
        list_of_list = []
        for ind, i in enumerate(list_of_black[:-1]):
            if i + 1 == list_of_black[ind + 1]:
                continue
            else:
                list_of_list.append(list_of_black[:list_of_black.index(i)+1])
        list_of_list.append(list_of_black)
        k = 0  #Counter for collect all items from list of list and sort them
        clear_list = [list_of_list[0]]
        while k != len(list_of_list)-1:
            k += 1
            j = set(list_of_list[k]) - set(list_of_list[k-1])
            clear_list.append(list(j))
        print(clear_list)
        for i in clear_list:
            i.sort()
            i.append(i[-1])
            coordinates.append((i[0], i[-1]))
    j = 0  #Counter for wirth movement
    while j != len(coordinates):
        for y in coordinates:
            j += 1
            pyautogui.moveTo(pos[0] + y[0], pos[1] + distance)
            pyautogui.dragTo(pos[0] + y[1], pos[1] + distance)
