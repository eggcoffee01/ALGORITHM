#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void makeTable(char *pattern, int table[]){
    int j = 0;
    for(int i = 1; i < strlen(pattern); i++){
        while ( j > 0  && pattern[i] != pattern[j])
        {
            j = table[j-1];
        }
        if(pattern[i] == pattern[j]){
            table[i] = ++j;
        }
    }
}

void KMP(char *pattern, char *string, int table[]){

    int n = strlen(string);
    int m = strlen(pattern);
    int i = 0; // string의 인덱스
    int j = 0; // pattern의 인덱스
    
    while (i < n) {
        if (pattern[j] == string[i]) {
            i++;
            j++;
        }
        if (j == m) {
            printf("Found pattern at index %d\n", i - j);
            j = table[j - 1];
        } else if (i < n && pattern[j] != string[i]) {
            if (j != 0) {
                j = table[j - 1];
            } else {
                i++;
            }
        }
    }

}

int main(void){
    char* pattern = "ABABCABAB";
    char* string = "ABABDABACDABABCABAB";
    const int patternSize = strlen(pattern);
    int *table = calloc(strlen(pattern), sizeof(int));

    makeTable(pattern, table);

    KMP(pattern, string, table);
    free(table);
}