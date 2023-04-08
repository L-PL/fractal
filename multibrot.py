from PIL import Image, ImageDraw

iterations = 100

def u_n(c,q=2):
    
    z,n = 0,0
    while (z.real)**2 + (z.imag)**2 <= 4 and n < iterations :
        z = z**q + c
        n += 1
    return n

x_min = -2
x_max =  1
y_min = -1
y_max =  1

largeur = 2000
hauteur = (largeur*(y_max-y_min)) // (x_max-x_min)

im = Image.new('RGB', (largeur, hauteur), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(0, largeur):
    for y in range(0, hauteur):
        
        c = complex(x_min + (x / largeur) * (x_max - x_min),
                    y_min + (y / hauteur) * (y_max - y_min))
        
        u = u_n(c,3)

        couleur = 255 - (u * 255)//iterations
        draw.point([x, y], (couleur, couleur, couleur))

im.save('multibrot.png', 'PNG')
print("Image enregistrée.")
