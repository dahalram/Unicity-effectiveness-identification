tic;
%{
In the code the keys(key1) of data_result dictionary is the subset of all possible combination . instead of using "abcd" i am using "1234".  the values of the data_result  dictionary is a dictionary whose key(key2) is the unique combination of the rows and the values are its frequency. 
for example is the data = [1 2 
                                          1 3 ]
then result_data has 3 keys ( 1, 2, 12) and each key is associated with a dic.
for example result_data(1) has 1 key with value 2.
result_data(2) has 2 key with each value 1.
result_data(12) has 2 key with each value 1.
%}
Actual_data=[11111 1 1 1 1
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
];

global data;
data = [ 1 1 1 1
 1 2 2 2 
 2 1 3 3
 2 2 1 4
 3 1 2 1
 3 2 3 2
 1 3 1 3
 2 3 2 4
 3 3 3 1
 1 1 1 2
 2 2 2 3
 3 3 3 4
 4 1 1 1
 4 2 2 2
 4 3 3 3
 4 4 4 4
];
global col_num;
global row_num;
row_num = 16;
global result_data;
% Dict witnin a dict 
result_data = containers.Map('KeyType','double','ValueType','any');
col_num = 1:4;
for n = 1:4
    compbnz{n} = combnk(col_num,n);
end

subset(compbnz);

  
    



display (keys(result_data));

display((result_data(1)));
   


display(toc);

function subset(comb_set)

global data
global result_data;
global row_num;




for i = 1:4
    sub_set_inorder = transpose(comb_set{i});
    map_set = containers.Map('KeyType','double','ValueType','double');
    for j = sub_set_inorder
        
        row_name = transpose(j);
        for row_count = 1:row_num
            k =join_num(data(row_count,row_name));
            if isKey(map_set,k)  
                map_set(k) = map_set(k)+1;
            else
                map_set(k) = 1;
            end
        end  
        
        result_data(join_num(row_name)) = map_set;
    end
end

end



function result = join_num(num_array)
s = 0;
    for k = num_array
        s=s*10+k; 
 
    end

result = s ;

end





