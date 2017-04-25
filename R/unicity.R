power_set_calculator <- function(set) { 
  n <- length(set)
  size <- 2^(1:n-1)
  lapply( 1:2^n-1, function(u) set[ bitwAnd(u, size) != 0 ] )
}

powerset <- c(power_set_calculator(1:4))

code <- c(1, 2, 3, 4)
names(code) <- c('a', 'b', 'c', 'd')

ab <- '11111 1 1 1 1
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
22226 4 4 4 4'

ab <- strsplit(ab, '\n')
vc <- c()
for (i in 1:16){
  vc <- c(vc, ab[[1]][i])
}

a <- c()
for (dt in vc) {
  tm <- strsplit(dt, ' ')
  tp <- c()
  for (i in 1:5){
    tp <- c(tp, tm[[1]][i])
  }
  print(tp)
  a <- c(a, tp)
}

unicity_calculator <- function(a) {
  result <- c()
  for (i in powerset) {
    alphabet <- c()
    for (j in i) {
      alphabet <- c(alphabet, j)
    }
    
    freq_tracker <- c()
    for (values in a) {
      key_val <- ''
      for (indexes in i) {
        key_val <- key_val + values[indexes]
      }
      
      if (key_val %in% names(alphabet)) {
        freq_tracker[key_val] <- freq_tracker[key_val] + 1
      } else {
        c(freq_tracker, key_val=1)
      }
    }
    
    for (k in freq_tracker) {
      if (freq_tracker[k] == 1) {
        index_key <- paste(alphabet, collapse = '')
        if (index_key %in% result){
          c(result[index_key], k) 
        } else {
          result[index_key] <- k
        }
      }
    }
  }
  
  for (j in result) {
    print(j)
    for (val in result[j]){
      print(val)
    }
    print('----------------')
  }
}
unicity_calculator(a)
