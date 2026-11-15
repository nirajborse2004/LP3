
import math
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def Huffman_code(text):
    freq = {}

    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    heap = [Node(ch, fr) for ch, fr in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right

        heapq.heappush(heap, new_node)

    root = heap[0]
    codes = {}

    def generate_code(node, code):
        if node.char is not None:
            codes[node.char] = code
            return

        generate_code(node.left, code + "0")
        generate_code(node.right, code + "1")

    generate_code(root, "")
    return codes


text = input("Enter the text: ")
codes = Huffman_code(text)

for ch in codes:
    print(ch, ":", codes[ch])

encoded_text = ""

for ch in text:
    encoded_text = encoded_text + codes[ch]

print("Encoded Text:", encoded_text)

original_bits = len(text)*8
encoded_bits=len(encoded_text)
saving = original_bits-encoded_bits

print("originalBits : ",original_bits)
print("encodedBits :",encoded_bits)
print("SavedSpace : ",saving)

