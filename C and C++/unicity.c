#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include "hashmap.h"

// reading data from data.txt

//(TODO: vijay, thapaliya) 

map_t* printPowerSet(char *set, int set_size)
{
    // initiate hashmap
    any_t power_set_hashmap;
    power_set_hashmap = hashmap_new();

    /*set_size of power set of a set with set_size
      n is (2**n -1)*/
    unsigned int pow_set_size = pow(2, set_size);
    int counter, j;
    /*Run from counter 000..0 to 111..1*/
    for(counter = 0; counter < pow_set_size; counter++)
    {
      char subset_val[4+1];

      int index = 0;
      for(j = 0; j < set_size; j++)
       {
          /* Check if jth bit in the counter is set
             If set then pront jth element from set */
          if(counter & (1<<j)){
            //printf("%c", set[j]);
            subset_val[index] = set[j];
            index ++;
            //printf("%d\n",index);
            // each index coming over here
          }
       }
       // Now based on index add values after reading from file 
       // Add null terminating character at the end
       subset_val[index] = '\0';

       any_t unicity_hashmap;
       unicity_hashmap = hashmap_new();
       

       char* x;
       x = malloc ( 5 * sizeof (char));
       strcpy(x, subset_val);
       hashmap_put(power_set_hashmap,(char *)x,unicity_hashmap);


       //printf("%s\n",subset_val);


       // for (int i=0; i< index;i++){
       //  printf("%c",subset_val[i]);
       // }

       //reset subset_val and index
       subset_val[0] = '\0';
       index = 0;
       printf("\n");
    }

    return power_set_hashmap;

}
 
int f(item, val){
    return MAP_OK;
   }

/*Driver program to test printPowerSet*/
int main()
{


 char set[] = {'1','2','3', '4'};
 

  // contains the hashmap a:unicity hashmap, ab: unicity hashmap etc...
  // iterate this and keep adding unique values by reading from file

  
 any_t power_set_hashmap;
 power_set_hashmap = printPowerSet(set, 4); 

 any_t unicity_val;
 printf("%p\n", unicity_val);
 hashmap_iterate(power_set_hashmap,f, unicity_val);
 //printf("%p\n", power_set_hashmap);





 static const char filename[] = "data.txt";

   FILE *file = fopen ( filename, "r" );

   if ( file != NULL )
   {
      char line [ 128 ]; /* or other suitable maximum line size */
      char *p = NULL;
      while ( fgets ( line, sizeof line, file ) != NULL ) /* read a line */
      {
        //fputs ( line, stdout ); /* write the line */
        p = strtok(line," ");
        // from each line now we read word by word
        while(p != NULL)
        {
          //printf("%s\n ",p); /* your word */
          p = strtok(NULL," ");
        }
        // main logic goes here get the different combinations and add to hashmap
      }
      fclose ( file );
   }
   else
   {
      perror ( filename ); /* why didn't the file open? */
   }

  
  return 0;
}

