'''
По данной непустой строке ss длины не более 10^4, 
состоящей из строчных букв латинского алфавита,
постройте оптимальный беспрефиксный код. 

В первой строке выведите количество различных букв k, встречающихся в строке, 
и размер получившейся закодированной строки. 

В следующих k строках запишите коды букв в формате "letter: code".
В последней строке выведите закодированную строку.
'''







from collections import Counter # счётчик частот символов в строке
from collections import namedtuple
import heapq # очередь с приоритетами





class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc+"0")
        self.right.walk(code, acc+"1")
        
    
class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"
    







def huffman_encode(s):
    
    # подсчитываем частоты символов в строке
    frequencies = []
    for char, freq in Counter(s).items():
        frequencies.append((freq, len(frequencies), Leaf(char)))
    heapq.heapify(frequencies)



    
    # подсчитываем коды Хаффмана для символов
    count = len(frequencies)
    while len(frequencies) > 1:
        # достаём первые два символа с минимальными частотами
        firstFreq, _firstCount, left = heapq.heappop(frequencies)
        secondFreq, _secondCount, right = heapq.heappop(frequencies)

        # добавляем в очередь элемент вместо двух с минимальными частотами
        heapq.heappush(frequencies, (firstFreq + secondFreq, count, Node(left, right)))
        count += 1
        
    code = {}
    if frequencies:
        [(_freq, _count, root)] = frequencies
        root.walk(code, "")
        
    return code
    
    
    
    
    

s = input() 
code = huffman_encode(s)
encoded = "".join(code[ch] for ch in s)
print(len(code), len(encoded))
for ch in sorted(code):
    print("{}: {}".format(ch, code[ch]))
print(encoded)