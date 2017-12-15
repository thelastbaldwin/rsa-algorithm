# RSA - (Rivest–Shamir–Adleman)

RSA is a public encryption/decryption scheme allowing for secure information transfer.

The premise of the algorithm relies on the "Factoring Problem"[1], a problem in mathametics that is difficult and time consuming to solve, making the keys generated with it difficult to discover.


## Setting up RSA

* Choose two prime numbers, `p` and `q`
* Set the `MOD value`, `p * q`
* Find the number of coprimes, the `totient`, using `(p -1) * (q - 1)`
* Choose `E` where `1 < E < totient`
* Choose `D` where (d * e) % `totient` == 1

`E` is the Public Key, which is handed out to all parties who need to send information securely.
`D` is the Private Key, which only you use to decrypt the securely transmitted information

## To Encrypt:
int `encrypted_message` = value_to_encrpyt ^ `E` % `MOD`

## To Decypt:
int `decrypted_message` = `encrypted_message` ^`D` % `MOD`

### Example
`python demo.py`

p = 11
q = 17
mod = 187
totient = 160
`E` = 159
`D` = 31679


## Notes: 
You can encrpyt with the private key to verify the sender, although the normal method is to use the public key to encrypt and the private to decrpyt

Big (0) depends on the operation, with encryption being cheaper than decyption.
But they are still slow operations. You need to figure out the size of the key in bits, as the value of `k`.
Then:
Encrpytion is O(k^2) 
Decyption is O(k^3)


Ref: 

1.) https://en.wikipedia.org/wiki/Integer_factorization

2.) Difficulty:
Not all numbers of a given length are equally hard to factor. The hardest instances of these problems (for currently known techniques) are semiprimes, the product of two prime numbers. When they are both large, for instance more than two thousand bits long, randomly chosen, and about the same size (but not too close, e.g., to avoid efficient factorization by Fermat's factorization method), even the fastest prime factorization algorithms on the fastest computers can take enough time to make the search impractical; that is, as the number of digits of the primes being factored increases, the number of operations required to perform the factorization on any computer increases drastically.
