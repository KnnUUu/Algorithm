#pragma once
#include <iostream>
#include <string>
#include <vector>
#include <assert.h> 
#include <algorithm>

using namespace std;

class Solution {
public:
    void xxx(const char* str) {
        
        std::string newStr(str);
        auto pch = strchr(str, '1');
        auto pchLast = strrchr(str, '1');
        //printf("%d\n", pchLast - pch);
        //printf("%d\n", pch - str);
        auto pos = newStr.find('1');
        if (pos != std::string::npos) printf("%d\n",pos);
        pos = newStr.find('2',3);
        if (pos != std::string::npos) printf("%d\n", pos);
        //printf("%c\n",&str[0]);
        /*
        auto prePch = str;
        while (pch != NULL)
        {
            printf("len %d\n", pch - prePch);
            prePch = pch;
            pch = strchr(pch + 1, '\n');
        }
        */
    }
    void test() {
        /*
        char strCopy[1024];
        auto strLen = strlen(str);
        strcpy_s(strCopy, 1024,str);
        
        char* context;
        char* pTok = strtok_s(strCopy,"\n",&context);
        if (pTok){
            while (pTok){
                printf(pTok);
                printf("\n");
                pTok = strtok_s(NULL, "\n", &context);
            }
        }
        */
        xxx("1\n22\n333\n4444");
        //xxx("55555");

        /*
        for (int i = 0; i < strlen(str); i++){
            printf("%c", str[i]);
            if (*(str+i)=='\n'){
                printf("xxx");
            }
        }
        printf("%d",strlen(str));
        */
    }
};

