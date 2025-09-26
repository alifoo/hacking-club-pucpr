/*
    Rafael Longhi
    Curso: BCC
    Problema: https://leetcode.com/problems/contains-duplicate/
    
    Obs: Diferente dos meus outros códigos, esse foi feito em C++ devido
    a performance necessária para passar nos testes.
*/

#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:

    // Para mantermos nossa solução O(n) e evitarmos
    // o uso de dois loops for, um dentro do outro, 
    // usamos esse algorítimo que lê todos os valores
    // do vetor de entrada e checa com um outro vetor
    // de valores já lidos se o valor atual está repetido.
    //
    // Se o valor for repetido, podemos retornar verdadeiro
    // antes mesmo de checar o vetor inteiro.

    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> viewed; 
        for (int i = 0; i < nums.size(); i++) {
            if (viewed.count(nums[i])) {
                return true;
            }
            viewed.insert(nums[i]);
        }
        return false;
    }
};
