import rsa
import os

class RSACipher:
    def __init__(self, key_path="keys"):
        self.key_path = key_path
        if not os.path.exists(key_path):
            os.makedirs(key_path)
        self.private_key = None
        self.public_key = None

    def generate_keys(self, key_size=2048):
        """Generate RSA key pair and save to files"""
        (pubkey, privkey) = rsa.newkeys(key_size)
        self.private_key = privkey
        self.public_key = pubkey
        
        # Save private key
        with open(os.path.join(self.key_path, "private_key.pem"), "wb") as f:
            f.write(self.private_key.save_pkcs1())
        
        # Save public key
        with open(os.path.join(self.key_path, "public_key.pem"), "wb") as f:
            f.write(self.public_key.save_pkcs1())

    def load_keys(self):
        """Load keys from files"""
        private_key_path = os.path.join(self.key_path, "private_key.pem")
        public_key_path = os.path.join(self.key_path, "public_key.pem")
        
        try:
            with open(private_key_path, "rb") as f:
                private_key = rsa.PrivateKey.load_pkcs1(f.read())
            with open(public_key_path, "rb") as f:
                public_key = rsa.PublicKey.load_pkcs1(f.read())
            return private_key, public_key
        except FileNotFoundError:
            return None, None

    def encrypt(self, message, public_key=None):
        """Encrypt message using public key"""
        if public_key is None:
            _, public_key = self.load_keys()
        
        if public_key is None:
            raise ValueError("Public key not found")
        
        encrypted = rsa.encrypt(message.encode(), public_key)
        return encrypted.hex()

    def decrypt(self, ciphertext, private_key=None):
        """Decrypt message using private key"""
        if private_key is None:
            private_key, _ = self.load_keys()
        
        if private_key is None:
            raise ValueError("Private key not found")
        
        decrypted = rsa.decrypt(bytes.fromhex(ciphertext), private_key)
        return decrypted.decode()

    def sign(self, message, private_key=None):
        """Sign message using private key"""
        if private_key is None:
            private_key, _ = self.load_keys()
        
        if private_key is None:
            raise ValueError("Private key not found")
        
        signature = rsa.sign(message.encode(), private_key, 'SHA-256')
        return signature.hex()

    def verify(self, message, signature, public_key=None):
        """Verify signature using public key"""
        if public_key is None:
            _, public_key = self.load_keys()
        
        if public_key is None:
            raise ValueError("Public key not found")
        
        try:
            rsa.verify(message.encode(), bytes.fromhex(signature), public_key)
            return True
        except rsa.pkcs1.VerificationError:
            return False