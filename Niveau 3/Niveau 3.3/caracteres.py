#-------------------------------------------------------------------------------
# Name:        Afficher la liste des caractères
# Purpose:     France-IOI niveau 3.3
#
# Author:      Sébastien
#
# Created:     11/09/2022
#-------------------------------------------------------------------------------

def main():
    # Caractères 0 à 1023
    for bloc in range(8):
       for lig in range(16):
          for col in range(8):
             code = 128 * bloc + 16 * col + lig
             caractere = chr(code)
             if code < 32:
                caractere = " "
             print("{:04d} {}  ".format(code, caractere), end = "")
          print()
       print()

if __name__ == '__main__':
    main()
