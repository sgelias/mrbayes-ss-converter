# MrBayes Secondary Structure Converter

Originally written by Diogo Margins de Sá (http://lattes.cnpq.br/2090058491124450)

Convert the dot-bracket format to MrBayes readable format. The dot-bracket format consists of a combination of brackets (complementary parenthesis) the Watson–Crick pairs of RNA and dots representing loops.

## Usage

It receives only a `-s` parameter containing a dot-bracket string.

```bash

python ./converter.py -s '.((((((((((((((((((((((...)))))))))))...))).))))))))....(((((....(.((.(((.((((...))))))).)))))))).'

```

The output like this:

```bash

stems = 2 52 3 51 4 50 5 49 6 48 7 47 8 46 9 45 10 43 11 42 12 41 13 37 14 36 15 35 16 34 17 33 18 32 19 31 20 30 21 29 22 28 23 27 57 97 58 96 59 95 60 94 61 93 66 92 68 91 69 90 71 88 72 87 73 86 75 85 76 84 77 83 78 82

loops = 1 24-26 38-40 44 53-56 62-65 67 70 74 79-81 89 98

pairs: 2:52,3:51,4:50,5:49,6:48,7:47,8:46,9:45,10:43,11:42,12:41,13:37,14:36,15:35,16:34,17:33,18:32,19:31,20:30,21:29,22:28,23:27,57:97,58:96,59:95,60:94,61:93,66:92,68:91,69:90,71:88,72:87,73:86,75:85,76:84,77:83,78:82

```

___

Let's code and be happy!!
