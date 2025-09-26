/*
    Rafael Longhi
    Curso: BCC
    Problema: https://leetcode.com/problems/valid-anagram/
*/

class Solution {

    /// Essa é uma solução extremamente elegante e performática
    /// desse problema. Nós convertemos as duas strings em dicionários,
    /// no qual temos os caractéres como chave e a quantidade de vezes
    /// que aparecem na string como valor.
    /// 
    /// Ao checar os dois dicionários com ==, checamos se eles tem as
    /// mesmas chaves com os mesmos valores, efetivamente checando se
    /// ambas as strings possuem o mesmo conteúdo indeferente da ordem.
    
    func isAnagram(_ s: String, _ t: String) -> Bool {
        var sDict: [Character: Int] = [:]
        var tDict: [Character: Int] = [:]
        
        for char in s {
            sDict[char, default: 0] += 1
        }
        
        for char in t {
            tDict[char, default: 0] += 1
        }
        
        return sDict == tDict
    }
}
