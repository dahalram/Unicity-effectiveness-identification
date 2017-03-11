# Test
# install.packages("rvest")
# install.packages("magrittr")
# install.packages("dplyr")
# install.packages("RCurl")
# install.packages("XML")
# install.packages("readr")

library(rvest)
library(magrittr)
library(dplyr)
library(RCurl)
library(XML)
library(readr)

powerSet <- function() {
	s <- list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

}

unicityCalculator <- function() {
	power_set <- list(powerset([1,2,3,4]))
    
    final_ans <- {}
    for i in power_set:
        alphabet <- [code[j] for j in i]
        freq_tracker <- {}
        for values in a:
            key_val <- ''
            for indexes in i:
                key_val <- key_val + values[indexes]
            if key_val not in freq_tracker:
                freq_tracker[key_val] <- 1
            else:
                freq_tracker[key_val] <- freq_tracker[key_val] + 1
        
        for k in freq_tracker:
            if freq_tracker[k] == 1:
                index_key <- ''.join(alphabet)
                if index_key not in final_ans:
                    final_ans[index_key] <- [k]
                else:
                    final_ans[index_key].append(k)

    for j in final_ans:
        print j
        for val in final_ans[j]:
            print val
}

unicityCalculator(data)