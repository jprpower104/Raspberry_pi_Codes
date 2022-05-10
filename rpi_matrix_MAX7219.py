import spidev
import time

spi = spidev.SpiDev(0,0)
spi.max_speed_hz = 10000

def letters(letra):
    if letra=='A':
        charlist = [0b00011110,#col 8
                    0b00100001,#col 7
                    0b00100001,#col 6
                    0b00100001,#col 5
                    0b00111111,#col 4
                    0b00100001,#col 3
                    0b00100001,#col 2
                    0b00100001]#col 1
    elif letra=='B':
        charlist = [0b00011111,
                    0b00100001,
                    0b00100001,
                    0b00011111,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00011111]
    elif letra=='C':
        charlist = [0b00111110,
                    0b00000001,
                    0b00000001,
                    0b00000001,
                    0b00000001,
                    0b00000001,
                    0b00000001,
                    0b00111110]
    elif letra=='D':
        charlist = [0b00011111,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00011111]
    elif letra=='E':
        charlist = [0b00111111,
                    0b00000001,
                    0b00000001,
                    0b00001111,
                    0b00000001,
                    0b00000001,
                    0b00000001,
                    0b00111111]
    elif letra=='F':
        charlist = [0b00111111,
                    0b00000001,
                    0b00000001,
                    0b00001111,
                    0b00000001,
                    0b00000001,
                    0b00000001,
                    0b00000001]
    elif letra=='G':
        charlist = [0b00111110,
                    0b00000001,
                    0b00000001,
                    0b00011111,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00011110]
    elif letra=='H':
        charlist = [0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00111111,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001]
    elif letra=='I':
        charlist = [0b00011111,
                    0b00000100,
                    0b00000100,
                    0b00000100,
                    0b00000100,
                    0b00000100,
                    0b00000100,
                    0b00011111]
    elif letra=='J':
        charlist = [0b00111111,
                    0b00100000,
                    0b00100000,
                    0b00100000,
                    0b00100000,
                    0b00100001,
                    0b00100001,
                    0b00011110]
    elif letra=='K':
        charlist = [0b00010001,
                    0b00001001,
                    0b00000101,
                    0b00000011,
                    0b00000101,
                    0b00001001,
                    0b00010001,
                    0b00100001]
    elif letra=='L':
        charlist = [0b00000001,
                    0b00000001,
                    0b00000001,
                    0b00000001,
                    0b00000001,
                    0b00000001,
                    0b00000001,
                    0b00111111]
    elif letra=='M':
        charlist = [0b00100001,
                    0b00110011,
                    0b00101101,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001]
    elif letra=='N':
        charlist = [0b00100001,
                    0b00100011,
                    0b00100101,
                    0b00101001,
                    0b00110001,
                    0b00100001,
                    0b00100001,
                    0b00100001]
    elif letra=='Ñ':
        charlist = [0b0101101,
                    0b0100011,
                    0b0100101,
                    0b0101001,
                    0b0110001,
                    0b0100001,
                    0b0100001,
                    0b0100001]
    elif letra=='O':
        charlist = [0b00011110,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00011110]
    elif letra=='P':
        charlist = [0b00011111,
                    0b00100001,
                    0b00100001,
                    0b00011111,
                    0b00000001,
                    0b00000001,
                    0b00000001,
                    0b00000001]
    elif letra=='Q':
        charlist = [0b00011110,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00110001,
                    0b00100001,
                    0b01011110]
    elif letra=='R':
        charlist = [0b00011111,
                    0b00100001,
                    0b00100001,
                    0b00011111,
                    0b00000101,
                    0b00001001,
                    0b00010001,
                    0b00100001]
    elif letra=='S':
        charlist = [0b00111110,
                    0b00000001,
                    0b00000001,
                    0b00011110,
                    0b00100000,
                    0b00100000,
                    0b00100000,
                    0b00011111]
    elif letra=='T':
        charlist = [0b00011111,
                    0b00000100,
                    0b00000100,
                    0b00000100,
                    0b00000100,
                    0b00000100,
                    0b00000100,
                    0b00000100]
    elif letra=='U':
        charlist = [0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00011110]
    elif letra=='V':
        charlist = [0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00010010,
                    0b00001100]
    elif letra=='W':
        charlist = [0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00101101,
                    0b00110011,
                    0b00100001]
    elif letra=='X':
        charlist = [0b00100001,
                    0b00100001,
                    0b00010010,
                    0b00001100,
                    0b00001100,
                    0b00010010,
                    0b00100001,
                    0b00100001]
    elif letra=='Y':
        charlist = [0b00100001,
                    0b00100001,
                    0b00100001,
                    0b00010010,
                    0b00001100,
                    0b00000100,
                    0b00000010,
                    0b00000001]
    elif letra=='Z':
        charlist = [0b00111111,
                    0b00100000,
                    0b00010000,
                    0b00001000,
                    0b00000100,
                    0b00000010,
                    0b00000001,
                    0b00111111]
    elif letra=='a':
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000111,
                    0b00001000,
                    0b00001110,
                    0b00001001,
                    0b00001110]
    elif letra=='b':
        charlist = [0b0000000,
                    0b0000001,
                    0b0000001,
                    0b0000001,
                    0b0000111,
                    0b0001001,
                    0b0001001,
                    0b0000111]
    elif letra=='c':
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00001110,
                    0b00000001,
                    0b00000001,
                    0b00000001,
                    0b00001110]
    elif letra=='d':
        charlist = [0b00000000,
                    0b00001000,
                    0b00001000,
                    0b00001000,
                    0b00001110,
                    0b00001001,
                    0b00001001,
                    0b00001110]
    elif letra=='e':
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000110,
                    0b00001001,
                    0b00000111,
                    0b00000001,
                    0b00001110]
    elif letra=='f':
        charlist = [0b00000000,
                    0b00001100,
                    0b00000010,
                    0b00000010,
                    0b00000111,
                    0b00000010,
                    0b00000010,
                    0b00000010]
    elif letra=='g':
        charlist = [0b00000000,
                    0b00000110,
                    0b00001001,
                    0b00001001,
                    0b00001110,
                    0b00001000,
                    0b00001000,
                    0b00000111]
    elif letra=='h':
        charlist = [0b00000000,
                    0b00000001,
                    0b00000001,
                    0b00000111,
                    0b00001001,
                    0b00001001,
                    0b00001001,
                    0b00001001]
    elif letra=='i':
        charlist = [0b00000000,
                    0b00000010,
                    0b00000000,
                    0b00000011,
                    0b00000010,
                    0b00000010,
                    0b00000010,
                    0b00000111]
    elif letra=='j':
        charlist = [0b00000000,
                    0b00001000,
                    0b00000000,
                    0b00001000,
                    0b00001000,
                    0b00001000,
                    0b00001001,
                    0b00000110]
    elif letra=='k':
        charlist = [0b00000000,
                    0b00000001,
                    0b00000001,
                    0b00001001,
                    0b00000101,
                    0b00000011,
                    0b00000101,
                    0b00001001]
    elif letra=='l':
        charlist = [0b00000000,
                    0b00000011,
                    0b00000010,
                    0b00000010,
                    0b00000010,
                    0b00000010,
                    0b00000010,
                    0b00000111]
    elif letra=='m':
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00001010,
                    0b00010101,
                    0b00010101,
                    0b00010101,
                    0b00010101]
    elif letra=='n':
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000110,
                    0b00001001,
                    0b00001001,
                    0b00001001,
                    0b00001001]
    elif letra=='ñ':
        charlist = [0b00000000,
                    0b00000110,
                    0b00000000,
                    0b00000110,
                    0b00001001,
                    0b00001001,
                    0b00001001,
                    0b00001001]
    elif letra=='o':
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000110,
                    0b00001001,
                    0b00001001,
                    0b00001001,
                    0b00000110]
    elif letra=='p':
        charlist = [0b00000000,
                    0b00000110,
                    0b00001001,
                    0b00001001,
                    0b00000111,
                    0b00000001,
                    0b00000001,
                    0b00000001]
    elif letra=='q':
        charlist = [0b00000000,
                    0b00000110,
                    0b00001001,
                    0b00001001,
                    0b00001110,
                    0b00001000,
                    0b00001000,
                    0b00001000]
    elif letra=='r':
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000110,
                    0b00001001,
                    0b00000001,
                    0b00000001,
                    0b00000001]
    elif letra=='s':
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00001110,
                    0b00000001,
                    0b00000110,
                    0b00001000,
                    0b00000111]
    elif letra=='t':
        charlist = [0b00000000,
                    0b00000010,
                    0b00000010,
                    0b00000111,
                    0b00000010,
                    0b00000010,
                    0b00001010,
                    0b00000100]
    elif letra=='u':
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00001001,
                    0b00001001,
                    0b00001001,
                    0b00001001,
                    0b00000110]
    elif letra=='v':
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00010001,
                    0b00010001,
                    0b00010001,
                    0b00001010,
                    0b00000100]
    elif letra=='w':
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00010101,
                    0b00010101,
                    0b00010101,
                    0b00010101,
                    0b00001010]
    elif letra=='x':
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00010001,
                    0b00001010,
                    0b00000100,
                    0b00001010,
                    0b00010001]
    elif letra=='y':
        charlist = [0b00000000,
                    0b00001001,
                    0b00001001,
                    0b00001001,
                    0b00001110,
                    0b00001000,
                    0b00001001,
                    0b00000110]
    elif letra=='z':
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00011111,
                    0b00001000,
                    0b00000100,
                    0b00000010,
                    0b00011111]
    elif letra=='á':
        charlist = [0b00000100,
                    0b00000010,
                    0b00000000,
                    0b00000111,
                    0b00001000,
                    0b00001110,
                    0b00001001,
                    0b00001110]
    elif letra=='é':
        charlist = [0b00000100,
                    0b00000010,
                    0b00000000,
                    0b00000110,
                    0b00001001,
                    0b00000111,
                    0b00000001,
                    0b00001110]
    elif letra=='í':
        charlist = [0b00000100,
                    0b00000010,
                    0b00000000,
                    0b00000011,
                    0b00000010,
                    0b00000010,
                    0b00000010,
                    0b00000111]
    elif letra=='ó':
        charlist = [0b00000100,
                    0b00000010,
                    0b00000000,
                    0b00000110,
                    0b00001001,
                    0b00001001,
                    0b00001001,
                    0b00000110]
    elif letra=='ú':
        charlist = [0b00000100,
                    0b00000010,
                    0b00000000,
                    0b00001001,
                    0b00001001,
                    0b00001001,
                    0b00001001,
                    0b00000110]
    elif letra=='ü':
        charlist = [0b00000000,
                    0b00001001,
                    0b00000000,
                    0b00001001,
                    0b00001001,
                    0b00001001,
                    0b00001001,
                    0b00000110]
    elif letra==':':
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000100,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000100]
    elif letra=='.':
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000100]
    elif letra=='.':
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000100]
    elif letra==',':
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00001000,
                    0b00000100]
    elif letra=='!':
        charlist = [0b00001000,
                    0b00001000,
                    0b00001000,
                    0b00001000,
                    0b00001000,
                    0b00001000,
                    0b00000000,
                    0b00001000]
    elif letra=='0':
        charlist = [0b00011110,
                    0b00110001,
                    0b00101001,
                    0b00101001,
                    0b00100101,
                    0b00100101,
                    0b00100011,
                    0b00011110]
    elif letra=='1':
        charlist = [0b00000100,
                    0b00000110,
                    0b00000101,
                    0b00000100,
                    0b00000100,
                    0b00000100,
                    0b00000100,
                    0b00011111]
    elif letra=='2':
        charlist = [0b00001110,
                    0b00010001,
                    0b00010000,
                    0b00010000,
                    0b00001110,
                    0b00000001,
                    0b00000001,
                    0b00011111]    
    elif letra=='3':
        charlist = [0b00011111,
                    0b00001000,
                    0b00000100,
                    0b00001110,
                    0b00010000,
                    0b00010000,
                    0b00010001,
                    0b00001110]
    elif letra=='4':
        charlist = [0b00010001,
                    0b00010001,
                    0b00010001,
                    0b00011111,
                    0b00010000,
                    0b00010000,
                    0b00010000,
                    0b00010000]
    elif letra=='5':
        charlist = [0b00011111,
                    0b00000001,
                    0b00000001,
                    0b00001111,
                    0b00010000,
                    0b00010000,
                    0b00010000,
                    0b00001111]
    elif letra=='6':
        charlist = [0b00001110,
                    0b00010001,
                    0b00000001,
                    0b00001111,
                    0b00010001,
                    0b00010001,
                    0b00010001,
                    0b00001110]
    elif letra=='7':
        charlist = [0b00011111,
                    0b00010000,
                    0b00010000,
                    0b00001000,
                    0b00000100,
                    0b00000100,
                    0b00000100,
                    0b00000100]
    elif letra=='8':
        charlist = [0b00001110,
                    0b00010001,
                    0b00010001,
                    0b00001110,
                    0b00010001,
                    0b00010001,
                    0b00010001,
                    0b00001110]
    elif letra=='9':
        charlist = [0b00001110,
                    0b00010001,
                    0b00010001,
                    0b00001110,
                    0b00010000,
                    0b00010000,
                    0b00010001,
                    0b00001110]
    elif letra=='':
        charlist = [0b01111110,
                    0b10000001,
                    0b10100101,
                    0b10000001,
                    0b10100101,
                    0b10011001,
                    0b10000001,
                    0b01111110]
    elif letra=='@':
        charlist = [0b00111110,
                    0b01000001,
                    0b01001001,
                    0b01010101,
                    0b01010101,
                    0b01111001,
                    0b00000001,
                    0b00111110]
    elif letra==' ':
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000]
    else:
        charlist = [0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000,
                    0b00000000]
    return charlist

def write_char(input):
    msb = input >> 8
    lsb = input & 0xFF
    spi.xfer([msb,lsb])
    
def write_display(input,col):
    n=len(input)
    msb = []
    lsb = []
    list = []
    for i in range(n):
        msb.append(col)
        lsb.append(input[i])
    for i in range(n):
        list.append(msb[i])
        list.append(lsb[i])
    spi.xfer(list)
    
def config_display():
    write_char(0x0C01) # shutdown mode operacion normal
    write_char(0x0900) # modo no decodificado
    write_char(0x0A0F) # Mmedia intensidad
    write_char(0x0B07) # Columnas 1-8
    write_char(0x0F00) # Prueba display
    
def mostrar(listCh,j):
    n = len(listCh)
    col=0x0000
    for i in range(n):
        col=(8-i)<<8
        write_display(col+(listCh[i]<<j))

def print_display(text,num_mat):
    listD=[]
    listDF=[]
    n=len(text)
    for i in range(4-n):
        text =text+" "
    for i in range(num_mat):
        char_letter = text[i]
        listD.append(letters(char_letter))
        
    for i in range(8):
        listTemp=[]
        for j in range(num_mat):
            listTemp.append(listD[num_mat-1-j][i])
        listDF.append(listTemp)

    for i in range(8):
        write_display(listDF[i],8-i)

def print_string(text,num_mat):
    n=len(text)
    if n>4:
        for i in range(n-4+5):
            print_display(text[i:num_mat+i],num_mat)
            time.sleep(0.2)
    else:
        print_string(text,num_mat)
        
        
def clean_display():
    text ="    "
    print_display(text,4)
    
def main():
    config_display()
    text = "Felíz Navidad Y Prospero Año 2023! "
    num_displays = 4
    clean_display()
    print_string(text,num_displays)
    text = """
    Autor: Mario Benedetti
    Obra : Corazón Coraza
    Porque te tengo y no
    Porque te pienso,
    Porque la noche está de ojos abiertos
    Porque la noche pasa y digo amor
    Porque has venido a recoger tu imagen
    Y eres mejor que todas tus imágenes
    Porque eres linda desde el pie hasta el alma
    Porque eres buena desde el alma a mí
    Porque te escondes dulce en el orgullo
    Pequeña y dulce
    Corazón coraza
    Porque eres mía
    Porque no eres mía
    Porque te miro y muero
    Y peor que muero
    Si no te miro amor
    Si no te miro
    Porque tú siempre existes dondequiera
    Pero existes mejor donde te quiero
    Porque tu boca es sangre
    Y tienes frío
    Tengo que amarte amor
    Tengo que amarte
    Aunque esta herida duela como dos
    Aunque te busque y no te encuentre
    Y aunque la noche pase
    y yo te tenga y no"""
    clean_display()
    print_string(text,num_displays)
    
if __name__=="__main__":
    main()



