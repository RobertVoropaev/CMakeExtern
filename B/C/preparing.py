import argparse
import os
import sys

parser = argparse.ArgumentParser('Generate source files: A1.cpp A2.cpp')
parser.add_argument('--dir', help='Output directory', required=True)
args = parser.parse_args()

print('Generate (python script)')

outdir = args.dir
os.makedirs(outdir, exist_ok=True)

change = False

def create(filename, content):
  if os.path.exists(filename) and args.smart:
    old_content = open(filename, 'r').read()
    if old_content == content:
      return
  global change
  change = True
  open(filename, 'w').write(content)

content = """
/*!
     \file
     \brief Сгенерированный заголовочный файл
*/

#include <iostream>

/*!
     \brief Главная функция сгенерированного заголовочного файла

     Печатает в stdin "Hello, i'm index file!"
*/


void print_hello_index(){
	std::cout << "Hello, i'm index file!" << std::endl;
}

"""

create(os.path.join(outdir, 'index.h'), content)

# Check changes
if (not change) and args.check_changes:
  sys.exit('No changes!')
