import heapq

class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(frequencies):
    # Create a priority queue (min heap) to store Huffman nodes
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    # Build the Huffman tree
    while len(heap) > 1:
        # Extract the two nodes with the lowest frequencies
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        # Create a new internal node with the combined frequency
        internal_node = HuffmanNode(None, node1.frequency + node2.frequency)
        internal_node.left = node1
        internal_node.right = node2

        # Add the new internal node back to the heap
   
