

println("Installing necessary packages")

Pkg.add("Combinatorics")
Pkg.add("Iterators")
Pkg.add("DataFrames")

println("Packages Installed")

using Combinatorics
using Iterators
using DataFrames

function powerset(a, min::Integer = 0, max::Integer = length(a))
    iterators = [combinations(a,k) for k=min:max]
    if min < 1 append!(iterators, []) end
    chain(iterators...)
end

tic();

println("Reading from file")
df = readtable("data")
println("Read dataframe from file")

# Column Names of the data
header = names(df)

# All possible combinations of the column Names
power_set_list = collect(powerset(header, 1))

# Dictionary to store the unique tuples
# Key: Column Name
# Value: Array of unique tuples for each key
unique_tuple_dict = Dict()

# Iterating over each column combination and finding unique
# tuples in them
for column_comb in power_set_list

    combs = convert(Array, df[column_comb])

    dict_store = Dict()

    for i = 1: size(combs)[1]
        val = tuple(combs[i,:]...)

        #Computing the frequency of each tuple
        if haskey(dict_store, val)
            dict_store[val] += 1
        else
            dict_store[val] = 1
        end
    end

    # Finding the tuples with frequency of 1 and
    # storing them in our dictionary
    for (key, value) in dict_store
        if value == 1
            if haskey(unique_tuple_dict, column_comb)
                push!(unique_tuple_dict[column_comb], key)
            else
                unique_tuple_dict[column_comb] = [key]
            end
        end
    end
end

time = toq();

println(time)

for (key, value) in unique_tuple_dict
    println(key, " ==> ", value)
end