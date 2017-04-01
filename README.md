# Unicity-effectiveness-identification
Here, the code for unicity effectiveness calculation are written in several languages.

Go to each language specific folder to see the code.

### The runtime for bigger data (available in Data Generator), is as follows:

### SAS:
Average runtime (system):
No data yet!

### Python :  
Average Runtime (System):

For dataset 1: (0.068 + 0.066 + 0.070 + 0.058 + 0.062)/5 = 0.065s

For dataset 2: (0.072 + 0.070 + 0.078 + 0.080 + 0.078)/5 = 0.076s

### R:
Average Runtime (system):

For dataset 1: (0.080 + 0.084 + 0.066 + 0.076 + 0.080)/5 = 0.078 s.

For dataset 2: (0.10 + 0.12 + 0.10 + 0.11 + 0.11)/5 = 0.11 s.

### Matlab:
Average Runtime:

For dataset 1:

For dataset 2:

### Julia:
Average Runtime (excluding installing packages for the first time and printing the result):

For dataset 1: (2.669322515 + 2.587425153 + 2.587662671 + 2.714858562 + 2.725893324)/5 = 2.657032445

For dataset 2: (2.805421131 + 2.762209794 + 2.721966287 + 2.808386271 + 2.840796785)/5 = 2.7877560536

### C:
Average runtime (system):

For dataset 1: (0.015 + 0.011 + 0.013 + 0.017 + 0.017) = 0.015s

For dataset 2:

### C++:
Average runtime (system):

For dataset 1: (0.035 + 0.033 + 0.033 + 0.036 + 0.035) = 0.035s

For dataset 2: (0.072 + 0.070 + 0.076 + 0.072 + 0.076) = 0.073s

-----
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

### SAS:
Average runtime (system): (1.74 + 2.4 + 2.8 + 2.85 + 2.93 + 2.84)/6 = 2.59 s.

### Python :  
Average Runtime (System): (0.063 + 0.074 + 0.042)/3 = 0.059 s.

### R:
Average Runtime (system): (0.078 + 0.084 + 0.066)/3 = 0.076 s.

### Matlab:
Average Runtime: (0.0218 + 0.0225 + 0.0220)/3 = 0.0221 s.

### Julia:
Average Runtime (excluding installing packages for the first time and printing the result):
(2.73 + 2.71 + 2.78)/3 = 2.74 s.

Note: Julia seems to be pretty bad in reading input from file because even just such a small file takes around 2 sec to load as a dataframe in the script, which pushes the runtime of the code to 2.8 s.

### C:
The work hasn't been completed yet. This is taking longer than expected time to debug. Work still in progress. Will update this after we are done.

### C++:
Average runtime (system): (0.001 + 0.0009 + 0.001)/3 = 0.00096666666 s.

As we can see, these codes (except Julia for some reason) runs way faster than SAS.
