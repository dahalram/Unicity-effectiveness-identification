dat <- read.csv('./PIC_MATH/unicity_practice.csv')
#print(dat)
#ind <- dat$index
#print(ind)
a <- dat$a
b <- dat$b
c <- dat$c
d <- dat$d

## creates the tables for a, b, c, and d##
combos <- c('a', 'b', 'c', 'd')
for (val in combos) {
  # creates and assigns the frequencies of a,b,c and d
  name <- paste("freq_", as.name(val), sep = "")
  freqs <- as.numeric(as.matrix(table(eval(as.name(paste(val))))))
  assign(name, freqs)
  # creates percentages for a, b, c and d
  frequencies <- c('freq_a', 'freq_b', 'freq_c', 'freq_d') 
  for (freq in frequencies) {
    #print(freq)
    name <- paste("percent_", as.name(val), sep = "")
    percents <- freqs/length(eval(as.name(paste(val)))) * 100
    assign(name, percents)
    name <- paste("cum_freq_", as.name(val), sep = "")
    cum_frequencies <- cumsum(freqs)
    assign(name, cum_frequencies)
    name <- paste("cum_percent_", as.name(val), sep = "")
    cum_percentages <- cumsum(percents)
    assign(name, cum_percentages)
    name <- paste("table_", as.name(val), sep = "")
    tables <- cbind(unique(eval(as.name(paste(val)))), freqs, percents, cum_frequencies, cum_percentages)
    assign(name, tables)
  }
}

## for table of a and b##
freq_ab <- as.numeric(as.matrix(table(b,a)))
percent_ab <- freq_ab/length(a) * 100
cum_freq_ab <- cumsum(freq_ab)
cum_percent_ab <- cumsum(percent_ab)
table_ab <- cbind(a, b, freq_ab, percent_ab, cum_freq_ab, cum_percent_ab)
table_ab <- table_ab[! (freq_ab == 0),]
print(table_ab)

## for table of a and c##
freq_ac <- as.numeric(as.matrix(table(c,a)))
percent_ac <- freq_ac/length(a) * 100
cum_freq_ac <- cumsum(freq_ac)
cum_percent_ac <- cumsum(percent_ac)
table_ac <- cbind(a, c, freq_ac, percent_ac, cum_freq_ac, cum_percent_ac)
table_ac <- table_ac[! (freq_ac == 0),]
print(table_ac)

## for table of a and d##
freq_ad <- as.numeric(as.matrix(table(d,a)))
percent_ad <- freq_ad/length(a) * 100
cum_freq_ad <- cumsum(freq_ad)
cum_percent_ad <- cumsum(percent_ad)
table_ad <- cbind(a, d, freq_ad, percent_ad, cum_freq_ad, cum_percent_ad)
table_ad <- table_ad[! (freq_ad == 0),]
print(table_ad)

## for the table of b and c##
freq_bc <- as.numeric(as.matrix(table(c,b)))
percent_bc <- freq_bc/length(a) * 100
cum_freq_bc <- cumsum(freq_bc)
cum_percent_bc <- cumsum(percent_bc)
table_bc <- cbind(b, c, freq_bc, percent_bc, cum_freq_bc, cum_percent_bc)
table_bc <- table_bc[! (freq_bc == 0),]
print(table_bc)

## for the table of b and d##
freq_bd <- as.numeric(as.matrix(table(d,b)))
percent_bd <- freq_bd/length(a) * 100
cum_freq_bd <- cumsum(freq_bd)
cum_percent_bd <- cumsum(percent_bd)
table_bd <- cbind(b, d, freq_bd, percent_bd, cum_freq_bd, cum_percent_bd)
table_bd <- table_bd[! (freq_bd == 0),]
print(table_bd)

## for the table of c and d##
freq_cd <- as.numeric(as.matrix(table(d,c)))
percent_cd <- freq_cd/length(a) * 100
cum_freq_cd <- cumsum(freq_cd)
cum_percent_cd <- cumsum(percent_cd)
table_cd <- cbind(c, d, freq_cd, percent_cd, cum_freq_cd, cum_percent_cd)
table_cd <- table_cd[! (freq_cd == 0),]
print(table_cd)

## for the table of a,b and c ##
freq_abc <- as.numeric(as.matrix(table(c,b,a)))
percent_abc <- freq_abc/length(a) * 100
cum_freq_abc <- cumsum(freq_abc)
cum_percent_abc <- cumsum(percent_abc)
table_abc <- cbind(a, b, c, freq_abc, percent_abc, cum_freq_abc, cum_percent_abc)
table_abc <- table_abc[! (freq_abc == 0),]
print(table_abc)

## for the table of a,b and d ##
freq_abd <- as.numeric(as.matrix(table(d,b,a)))
percent_abd <- freq_abd/length(a) * 100
cum_freq_abd <- cumsum(freq_abd)
cum_percent_abd <- cumsum(percent_abd)
table_abd <- cbind(a, b, d, freq_abd, percent_abd, cum_freq_abd, cum_percent_abd)
table_abd <- table_abd[! (freq_abd == 0),]
print(table_abd)

## for the table of a,c and d ##
freq_acd <- as.numeric(as.matrix(table(d,c,a)))
percent_acd <- freq_acd/length(a) * 100
cum_freq_acd <- cumsum(freq_acd)
cum_percent_acd <- cumsum(percent_acd)
table_acd <- cbind(a, c, d, freq_acd, percent_acd, cum_freq_acd, cum_percent_acd)
table_acd <- table_acd[! (freq_acd == 0),]
print(table_acd)

## for the table of b,c and d ##
freq_bcd <- as.numeric(as.matrix(table(d,c,b)))
percent_bcd <- freq_bcd/length(a) * 100
cum_freq_bcd <- cumsum(freq_bcd)
cum_percent_bcd <- cumsum(percent_bcd)
table_bcd <- cbind(b, c, d, freq_bcd, percent_bcd, cum_freq_bcd, cum_percent_bcd)
table_bcd <- table_bcd[! (freq_bcd == 0),]
print(table_bcd)

## for the table of a,b,c and d ##
freq_abcd <- as.numeric(as.matrix(table(d,c,b,a)))
percent_abcd <- freq_abcd/length(a) * 100
cum_freq_abcd <- cumsum(freq_abcd)
cum_percent_abcd <- cumsum(percent_abcd)
table_abcd <- cbind(a, b, c, d, freq_abcd, percent_abcd, cum_freq_abcd, cum_percent_abcd)
table_abcd <- table_abcd[! (freq_abcd == 0),]
print(table_abcd)

print(proc.time())
