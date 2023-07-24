#!/usr/bin/env bash

# Show output
set -x

# Exit on error.
set -e

# Check python tests
cd python
python3 -m unittest discover
cd ..

# Build cpp code
git submodule update --init
mkdir -p build
cd build
cmake ..
make -j4
cp cpp/*.so ../python/tests
cd ..

# Test pybind module against python tests
cd python/tests
python3 -m unittest discover
rm *.so
cd ../..

# Invoke the cli:
cp build/cpp/*.so python/bin
cd python/bin
python3 make_ellipse.py -X 35 -Y 20 -A 30 -x 0.5 -y 0.5
rm *.so
cd ../..
