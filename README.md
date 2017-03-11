# Unicity-effectiveness-identification
Here, the code for unicity effectiveness calculation are written in several languages. 

Go to each language specific folder to see the code. 

### The sample data used is as below: 
11111 1 1 1 1
12222 1 2 2 2 
13333 2 1 3 3
14444 2 2 1 4
15555 3 1 2 1
16666 3 2 3 2
17777 1 3 1 3
18888 2 3 2 4
19999 3 3 3 1
20000 1 1 1 2
21111 2 2 2 3
22222 3 3 3 4
22223 4 1 1 1
22224 4 2 2 2
22225 4 3 3 3
22226 4 4 4 4

The runtimes for each specific languages are as follows: 

### Python :  Average Runtime (System): (0.063 + 0.074 + 0.042)/3 = 0.059 s.

### R: Average Runtime (system): (0.078 + 0.084 + 0.066)/3 = 0.076 s.

### Matlab: Average Runtime: (0.0218 + 0.0225 + 0.0220)/3 = 0.0221 s. 

### Julia: Average Runtime (excluding installing packages for the first time and printing the result):
(2.73 + 2.71 + 2.78)/3 = 2.74 s
Note: Julia seems to be pretty bad in reading input from file because even just such a small file takes me around 2 sec to load as a dataframe in the script, which pushes the runtime of the code to 2.8 s.

### C: The work hasn't been completed yet. This is taking longer than expected time to debug. Work still in progress. Will update this after we are done. 

### C++: The work hasn't been completed yet. This is taking longer than expected time to debug. Work still in progress. Will update this after we are done. 