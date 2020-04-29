index_text = """
#include <iostream>

void print_hello_index(){
	std::cout << "Hello, i'm index file" << std::endl;
}
"""

with open("index.h", "w") as f:
	f.write(index_text)	
