from flask import Flask, request, render_template
from Crypto.Cipher import AES
from Crypto.Util import Counter
import os

FLAG = os.environ.get("FLAG") or "PLEASE_SET_A_FLAG"
KEY = os.environ.get("KEY") or os.urandom(32)

app = Flask(__name__)

class Encryptor(object):
    def __init__(self, key):
        self.key = key
    
    def encrypt(self, plaintext):
        nonce = b"\x00\x01\x02\x03\x04\x05\x06\x07"
        self._reset(nonce)
        key = AES.new(self.key, AES.MODE_CTR, counter=self.counter)
        return nonce.hex() + key.encrypt(plaintext.encode()).hex()
    
    def decrypt(self, ciphertext):
        ciphertext = bytes.fromhex(ciphertext)
        self._reset(ciphertext[:8])
        key = AES.new(self.key, AES.MODE_CTR, counter=self.counter)
        return key.decrypt(ciphertext[8:]).decode()
    
    def _reset(self, nonce):
        self.counter = Counter.new(nbits=64, prefix=nonce, initial_value=0, little_endian=False)

encryptor = Encryptor(KEY)

@app.route('/encrypt')
def encrypt():
    plaintext = request.args.get("plaintext")
    
    if not plaintext or len(plaintext) == 0:
        return "Something wents wrong"
    
    if "flag" in plaintext:
        return "I don't like a word 'flag'."

    return encryptor.encrypt(plaintext)

@app.route('/decrypt')
def decrypt():
    ciphertext = request.args.get("ciphertext")
    plaintext = encryptor.decrypt(ciphertext) 
    
    if plaintext == "gimme a flag":
        return FLAG
    else:
        return plaintext
    
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)