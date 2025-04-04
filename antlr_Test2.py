import sys
import time
from antlr4 import *
import psutil
import os


from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from GrammarListener import GrammarListener

sys.path.append(r"C:\Users\camil\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0"
                r"\LocalCache\local-packages\Python311\site-packages")


def get_memory_usage():
    # Get the current process ID
    process = psutil.Process(os.getpid())
    # Get memory usage in MB
    memory_info = process.memory_info()
    return memory_info.rss / 1024  # Convert bytes to MB


def print_tree(parse_tree, parser, level=0):
    if parse_tree.getChildCount() == 0:
        print(" " * level + parse_tree.getText())  # Print leaf node
    else:
        node_name = parser.ruleNames[parse_tree.getRuleIndex()]
        # Print the current rule with more meaningful labels
        if node_name == "expr":
            if len(parse_tree.children) == 3 and parse_tree.children[1].getText() in ['+', '-', '*', '/']:
                operator = parse_tree.children[1].getText()
                print(" " * level + f"Operation: {operator}")
            else:
                print(" " * level + f"Expression")
                # If the rule is something like addition, multiplication, etc., show it explicitly
        elif node_name == "NEWLINE":
            print(" " * level + "Newline")

        else:
            print(" " * level + f"Rule: {node_name}")

        for child in parse_tree.children:
            print_tree(child, parser, level + 2)  # Recurse for children


def parse_input(input_text):
    start_time = time.perf_counter()  # More accurate than time.time()
    start_memory = get_memory_usage()  # Get memory usage before parsing

    # Create an input stream from the provided text
    input_stream = InputStream(input_text)

    # Create a lexer
    lexer = GrammarLexer(input_stream)

    # Create a token stream from the lexer
    token_stream = CommonTokenStream(lexer)

    # Create a parser
    parser = GrammarParser(token_stream)

    # Parse the input starting from the 'start' rule
    tree = parser.start()

    # Print the parse tree in text format
    print(f"Parse Tree for input '{input_text}':")
    print(tree.toStringTree(recog=parser))  # Show parse tree as a string

    # Print the hierarchical tree format
    print(f"\nParse Tree for input '{input_text}' (Visual):")
    print_tree(tree, parser)


    end_time = time.perf_counter()
    end_memory = get_memory_usage()  # Get memory usage after parsing
    # Calculate and print the running time
    print(f"Running time: {end_time - start_time:.6f} seconds")
    print(f"Memory usage: {end_memory - start_memory:.6f} KB")


# Example usage
inputs = ["45 * 7 - 678 + 90 / 55 "]
for text in inputs:
    print(f"Processing input: {text}")
    try:
        parse_input(text)
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 50)

