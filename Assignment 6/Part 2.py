#Jason Guan
#U9893-2926
#Program intended to encrypt a text file using encrypted code

def main():    
    fileNameIn = input('Please enter the name of the file you would like to encrypt: ')

    messageRead = open(fileNameIn + '.txt', 'r')
    contents = []
    contents = messageRead.readlines()
    messageRead.close()
    
    encrypt(contents)
    
def encrypt(content):
    Encrypt_Code =  {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',
        'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',
        'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2', 
        'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y', 
        'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v', 
        'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',
        'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p', 
        'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m', 
        'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j', 
        '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g', 
        '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d', 
        '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a', 
        ':':',',',':':','?':'.','.':'?','<':'>','>':'<', 
        "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=', 
        '{':'[','[':'{','}':']',']':'}'}
    
    fileNameOut = input('Please name the encrypted file: ')
    messageEncrypted = open(fileNameOut + '.txt', 'w')
    
    originalChara = list(Encrypt_Code.keys())
    convertedChara = list(Encrypt_Code.values())

    for line in content:
        messageEncrypted.write('\n')
        for chara in line:
            if chara.isspace():
                messageEncrypted.write(' ')
            for count in range(len(originalChara)):
                if chara == originalChara[count]:
                    messageEncrypted.write(convertedChara[count])
    messageEncrypted.close()

main()
