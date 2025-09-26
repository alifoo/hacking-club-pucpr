/*
    Rafael Longhi
    Curso: BCC
    Problema: https://leetcode.com/problems/min-stack/
*/

class MinStack {

    /// Para aumentar a performance, nós guardamos
    /// pares de valores, sendo stackMem o valor atual da stack, 
    /// e sorted sendo o valor do menor elemento da stack nessa posição.

    private var stackMem: [Int] = []
    private var sorted: [Int] = []
    
    func push(_ val: Int) {
        stackMem.append(val)
        
        /// Nota: Em Swift, ao pegar um elemento de uma lista
        /// usando .last, .first, entre outros, nós conseguimos 
        /// um Optional<Int>, ou seja, Int ou Nil. O operador `??`
        /// faz com que se o valor a esquerda, nesse caso sorted.last,
        /// seja nil, ele retorna o valor a direita, nesse caso Int.max.
        if val < (sorted.last ?? Int.max) {
            sorted.append(val)
        } else {
            sorted.append(sorted.last ?? Int.max)
        }
    }

    func pop() {
        stackMem.removeLast()
        sorted.removeLast()
    }
    
    func top() -> Int {
        return stackMem.last ?? 0
    }
    
    func getMin() -> Int {
        return sorted.last ?? 0
    }
}